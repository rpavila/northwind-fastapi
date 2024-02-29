from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api.v1.deps import SessionDep
from app.crud import crud_order_detail as crud_module

router = APIRouter()


@router.get("", response_model=List[schemas.OrderDetailsSchema])
async def read_all(skip: int = 0, limit: int = 100, db: Session = SessionDep):
    items = crud_module.get_all(db, skip=skip, limit=limit)
    if items is None:
        raise HTTPException(status_code=404, detail="OrderDetails not found")
    return items


@router.get('/{pk}', response_model=schemas.OrderDetailsSchema)
async def read_one(pk: str, db: Session = SessionDep):
    instance = crud_module.get(db, id=pk)
    if instance is None:
        raise HTTPException(status_code=404, detail="OrderDetail not found")
    return instance