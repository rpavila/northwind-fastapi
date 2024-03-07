from typing import Any, Callable, List, Type, Generator, Optional, Union

from fastapi import Depends, HTTPException
from sqlalchemy.sql import false as FALSE

from . import CRUDGenerator, NOT_FOUND, _utils
from ._helpers import get_model, get_related_model, session_query, get_by, is_like_list
from ._search import search
from ._types import DEPENDENCIES, PAGINATION, PYDANTIC_SCHEMA as SCHEMA

try:
    from sqlalchemy.orm import Session
    from sqlalchemy.ext.declarative import DeclarativeMeta as Model
    from sqlalchemy.exc import IntegrityError
except ImportError:
    Model = None
    Session = None
    IntegrityError = None
    sqlalchemy_installed = False
else:
    sqlalchemy_installed = True
    Session = Callable[..., Generator[Session, Any, None]]

CALLABLE = Callable[..., Model]
CALLABLE_LIST = Callable[..., List[Model]]


class SQLAlchemyCRUDRouter(CRUDGenerator[SCHEMA]):
    def __init__(
        self,
        schema: Type[SCHEMA],
        db_model: Model,
        db: "Session",
        create_schema: Optional[Type[SCHEMA]] = None,
        update_schema: Optional[Type[SCHEMA]] = None,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        paginate: Optional[int] = None,
        get_all_route: Union[bool, DEPENDENCIES] = True,
        get_one_route: Union[bool, DEPENDENCIES] = True,
        create_route: Union[bool, DEPENDENCIES] = True,
        update_route: Union[bool, DEPENDENCIES] = True,
        delete_one_route: Union[bool, DEPENDENCIES] = True,
        delete_all_route: Union[bool, DEPENDENCIES] = True,
        **kwargs: Any
    ) -> None:
        assert (
            sqlalchemy_installed
        ), "SQLAlchemy must be installed to use the SQLAlchemyCRUDRouter."

        self.db_model = db_model
        self.db_func = db
        self._pk: str = db_model.__table__.primary_key.columns.keys()[0]
        self._pk_type: type = _utils.get_pk_type(schema, self._pk)

        super().__init__(
            schema=schema,
            create_schema=create_schema,
            update_schema=update_schema,
            prefix=prefix or db_model.__tablename__,
            tags=tags,
            paginate=paginate,
            get_all_route=get_all_route,
            get_one_route=get_one_route,
            create_route=create_route,
            update_route=update_route,
            delete_one_route=delete_one_route,
            delete_all_route=delete_all_route,
            **kwargs
        )

    def _get_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route(
            db: Session = Depends(self.db_func),
            pagination: PAGINATION = self.pagination,
        ) -> List[Model]:
            skip, limit = pagination.get("skip"), pagination.get("limit")

            # resource_id = None
            resource_id = self.prefix[1:]
            filters = []
            sort = []
            # Get the resource with the specified ID.
            primary_resource = get_by(db, self.db_model, resource_id, 'id')
            if primary_resource is None:
                return []
                # return error_response(404, detail=f'No resource with ID {escape(resource_id)}')
            # Get the model of the specified relation.
            related_model = get_related_model(self.model, relation_name)
            if related_model is None:
                # return error_response(404, detail=f'No such relation: {escape(relation_name)}')
                return []
            # Determine if this is a to-one or a to-many relation.
            if is_like_list(primary_resource, relation_name):
                model = get_model(self.db_model)
                # related_model = get_related_model(model, relation_name)
                related_model = get_related_model(model, self.db_model.__tablename__)
                query = session_query(db, related_model)

                # Filter by only those related values that are related to `instance`.
                relationship = getattr(self.db_model, self.db_model.__tablename__)
                primary_keys = {self.api_manager.primary_key_value(inst) for inst in relationship}
                # If the relationship is empty, we can avoid a potentially expensive
                # filtering operation by simply returning an intentionally empty
                # query.
                if not primary_keys:
                    query = query.filter(FALSE())
                    print(query)
                # else:
                #     query = query.filter(self.api_manager.primary_key_value(related_model).in_(primary_keys))

                #     return self._get_collection_helper(resource=primary_resource,
                #                                        relation_name=relation_name,
                #                                        filters=filters, sort=sort)
                # else:
                #     resource = getattr(primary_resource, relation_name)
                #     return self._get_resource_helper(resource=resource,
                #                                      primary_resource=primary_resource,
                #                                      relation_name=relation_name)

            # db_models: List[Model] = (
            #     db.query(self.db_model)
            #     .order_by(getattr(self.db_model, self._pk))
            #     .limit(limit)
            #     .offset(skip)
            #     .all()
            # )
            db_models: List[Model] = (
                search(session=db, model=self.db_model, filters=[], sort=[]).limit(limit)
                .offset(skip)
                .all()
            )
            return db_models

        return route

    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type, db: Session = Depends(self.db_func)  # type: ignore
        ) -> Model:
            model: Model = db.query(self.db_model).get(item_id)

            if model:
                return model
            else:
                raise NOT_FOUND from None

        return route

    def _create(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            model: self.create_schema,  # type: ignore
            db: Session = Depends(self.db_func),
        ) -> Model:
            try:
                db_model: Model = self.db_model(**model.dict())
                db.add(db_model)
                db.commit()
                db.refresh(db_model)
                return db_model
            except IntegrityError:
                db.rollback()
                raise HTTPException(422, "Key already exists") from None

        return route

    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type,  # type: ignore
            model: self.update_schema,  # type: ignore
            db: Session = Depends(self.db_func),
        ) -> Model:
            try:
                db_model: Model = self._get_one()(item_id, db)

                for key, value in model.dict(exclude={self._pk}).items():
                    if hasattr(db_model, key):
                        setattr(db_model, key, value)

                db.commit()
                db.refresh(db_model)

                return db_model
            except IntegrityError as e:
                db.rollback()
                self._raise(e)

        return route

    def _delete_all(self, *args: Any, **kwargs: Any) -> CALLABLE_LIST:
        def route(db: Session = Depends(self.db_func)) -> List[Model]:
            db.query(self.db_model).delete()
            db.commit()

            return self._get_all()(db=db, pagination={"skip": 0, "limit": None})

        return route

    def _delete_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        def route(
            item_id: self._pk_type, db: Session = Depends(self.db_func)  # type: ignore
        ) -> Model:
            db_model: Model = self._get_one()(item_id, db)
            db.delete(db_model)
            db.commit()

            return db_model

        return route