from typing import List, TypeVar, Generic, Optional

from fastapi import APIRouter, HTTPException
from pydantic import create_model, BaseModel
from sqlalchemy.orm import Session

from app import schemas, models
from app.api.v1.deps import SessionDep
from app.crud import crud_customer as crud_module

router = APIRouter()

DataT = TypeVar('DataT')

class Response(BaseModel, Generic[DataT]):
    data: Optional[DataT] = None

# model = create_model()

# @router.get("", response_model=List[schemas.CustomerSchema], response_model_exclude_unset=True)
@router.get("")
async def read_all(skip: int = 0, limit: int = 100, fields=[], db: Session = SessionDep):
    fields = fields.split(',')
    items = crud_module.get_all(db, skip=skip, limit=limit, fields=fields)
    if items is None:
        raise HTTPException(status_code=404, detail="Customers not found")

    # columns = models.Customer.__table__.columns
    # print(list(map(lambda x: x.name, columns)))
    f = list(filter(lambda x: x in fields, list(models.Customer.__dict__.keys())))
    # print(fields, f)
    # print(list(models.Customer.__dict__.keys()))

    LangText = create_model(
        "Customer",
        **{lang: (Optional[str], "") for lang in f},  # dynamically created fields
    )

    response = Response[List[LangText]](data=[i._asdict() for i in items])
    return response.model_dump()


@router.get('/{pk}', response_model=schemas.CustomerSchema)
async def read_one(pk: str, db: Session = SessionDep):
    instance = crud_module.get(db, id=pk)
    if instance is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return instance