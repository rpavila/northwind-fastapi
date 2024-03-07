from typing import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    product_name: str
    supplier_id: Optional[int]
    category_id: Optional[int]
    quantity_per_unit: Optional[str]
    unit_price: Optional[float]
    units_in_stock: Optional[int]
    units_on_order: Optional[int]
    reorder_level: Optional[int]
    discontinued: int

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    product_name: str
    supplier_id: int
    category_id: int
    quantity_per_unit: Optional[str]
    unit_price: Optional[float]
    units_in_stock: Optional[int]
    units_on_order: Optional[int]
    reorder_level: Optional[int]
    discontinued: int
