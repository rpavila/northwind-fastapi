from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api.v1.deps import SessionDep
from app.crud import crud_customer

router = APIRouter()


@router.get("/", response_model=List[schemas.CustomerSchema])
async def read_all(skip: int = 0, limit: int = 100, db: Session = SessionDep):
    customers = crud_customer.get_all(db, skip=skip, limit=limit)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customers not found")
    return customers


@router.get('/{pk}', response_model=schemas.CustomerSchema)
async def read_one(pk: str, db: Session = SessionDep):
    instance = crud_customer.get(db, id=pk)
    if instance is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return instance