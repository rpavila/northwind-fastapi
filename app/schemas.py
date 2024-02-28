from datetime import date
from pydantic import BaseModel
from typing import Optional


class CategoriesSchema(BaseModel):
    category_id: int
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]

    class Config:
        orm_mode = True


class CustomerCustomerDemoSchema(BaseModel):
    customer_id: str
    customer_type_id: str

    class Config:
        orm_mode = True


class CustomerDemographicsSchema(BaseModel):
    customer_type_id: str
    customer_desc: Optional[str]

    class Config:
        orm_mode = True


class CustomerSchema(BaseModel):
    customer_id: str
    company_name: str
    contact_name: Optional[str]
    contact_title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    fax: Optional[str]

    class Config:
        orm_mode = True


class EmployeesSchema(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    title: Optional[str]
    title_of_courtesy: Optional[str]
    birth_date: Optional[date]
    hire_date: Optional[date]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    home_phone: Optional[str]
    extension: Optional[str]
    photo: Optional[bytes]
    notes: Optional[str]
    reports_to: Optional[int]
    photo_path: Optional[str]

    class Config:
        orm_mode = True


class EmployeeTerritoriesSchema(BaseModel):
    employee_id: int
    territory_id: str

    class Config:
        orm_mode = True


class OrderDetailsSchema(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int
    discount: float

    class Config:
        orm_mode = True


class OrdersSchema(BaseModel):
    order_id: int
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


class ProductsSchema(BaseModel):
    product_id: int
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


class RegionSchema(BaseModel):
    region_id: int
    region_description: str

    class Config:
        orm_mode = True


class ShippersSchema(BaseModel):
    shipper_id: int
    company_name: str
    phone: Optional[str]

    class Config:
        orm_mode = True


class SuppliersSchema(BaseModel):
    supplier_id: int
    company_name: str
    contact_name: Optional[str]
    contact_title: Optional[str]
    address: Optional[str]
    city: Optional[str]
    region: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    phone: Optional[str]
    fax: Optional[str]
    homepage: Optional[str]

    class Config:
        orm_mode = True


class TerritoriesSchema(BaseModel):
    territory_id: str
    territory_description: str
    region_id: int

    class Config:
        orm_mode = True


class UsStatesSchema(BaseModel):
    state_id: int
    state_name: Optional[str]
    state_abbr: Optional[str]
    state_region: Optional[str]

    class Config:
        orm_mode = True
