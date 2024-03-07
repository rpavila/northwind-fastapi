from datetime import date
from typing import Optional

from pydantic import BaseModel


class OrderSchema(BaseModel):
    id: int
    customer_id: Optional[str]
    employee_id: Optional[int]
    order_date: Optional[date]
    required_date: Optional[date]
    shipped_date: Optional[date]
    ship_via: Optional[int]
    freight: Optional[float]
    ship_name: Optional[str]
    ship_address: Optional[str]
    ship_city: Optional[str]
    ship_region: Optional[str]
    ship_postal_code: Optional[str]
    ship_country: Optional[str]

    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    customer_id: str
    employee_id: Optional[int]
    order_date: Optional[date]
    required_date: Optional[date]
    shipped_date: Optional[date]
    ship_via: Optional[int]
    freight: Optional[float]
    ship_name: Optional[str]
    ship_address: Optional[str]
    ship_city: Optional[str]
    ship_region: Optional[str]
    ship_postal_code: Optional[str]
    ship_country: Optional[str]


class OrderDetailsSchema(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int
    discount: float

    class Config:
        orm_mode = True


class OrderDetailsCreate(BaseModel):
    order_id: int
