from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.database import SessionLocal
from app.routers.customers.crud import get_customers

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.get("/", response_model=List[schemas.CustomerSchema])
# async def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     customers = get_customers(db, skip=skip, limit=limit)
#     if customers is None:
#         raise HTTPException(status_code=404, detail="Customers not found")
#     return customers

# @router.get("/customer_demographics", response_model=List[CustomerDemographics])
# async def read_customer_demographics(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     customer_demographics = get_customer_demographics(db, skip=skip, limit=limit)
#     if customer_demographics is None:
#         raise HTTPException(status_code=404, detail="Customer demographics not found")
#     return customer_demographics
#
# @router.get("/customer_customer_demo", response_model=List[CustomerCustomerDemo])
# async def read_customer_customer_demo(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     customer_customer_demo = get_customer_customer_demo(db, skip=skip, limit=limit)
#     if customer_customer_demo is None:
#         raise HTTPException(status_code=404, detail="Customer customer demo not found")
#     return customer_customer_demo