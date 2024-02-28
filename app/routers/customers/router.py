from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import schemas
from app.routers.customers.crud import get_one, get_all

router = APIRouter()


# Dependency
def get_db(request: Request):
    return request.state.db


@router.get("/", response_model=List[schemas.CustomerSchema])
async def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = get_one(db, skip=skip, limit=limit)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customers not found")
    return customers

@router.get("/{pk}", response_model=schemas.CustomerSchema)
async def read_one(pk: str, db: Session = Depends(get_db)):
    customers = get_all(db, pk)
    if customers is None:
        raise HTTPException(status_code=404, detail="Customers not found")
    return customers