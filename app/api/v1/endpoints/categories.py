from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api.v1.deps import SessionDep, get_db
from app.crud import crud_category as crud_module
from app.crudrouter import SQLAlchemyCRUDRouter
from app.models import Category
from app.schemas.category import CategorySchema, CategoryCreate

# router = APIRouter()
router = SQLAlchemyCRUDRouter(
    schema=CategorySchema,
    create_schema=CategoryCreate,
    update_schema=CategoryCreate,
    db_model=Category,
    db=get_db
)


# @router.get("", response_model=List[schemas.CategorySchema])
# async def read_all(skip: int = 0, limit: int = 100, db: Session = SessionDep):
#     items = crud_module.get_all(db, skip=skip, limit=limit)
#     if items is None:
#         raise HTTPException(status_code=404, detail="Categories not found")
#     return items
#
#
# @router.get('/{pk}', response_model=schemas.CategorySchema)
# async def read_one(pk: int, db: Session = SessionDep):
#     instance = crud_module.get(db, id=pk)
#     if instance is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     return instance