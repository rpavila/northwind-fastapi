from datetime import date
from pydantic import BaseModel
from typing import Optional


class CategoriesSchema(BaseModel):
    id: int
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]

    class Config:
        orm_mode = True


class CustomerCustomerDemoSchema(BaseModel):
    id: str
    customer_type_id: str

    class Config:
        orm_mode = True


class CustomerDemographicsSchema(BaseModel):
    customer_type_id: str
    customer_desc: Optional[str]

    class Config:
        orm_mode = True


class CustomerSchema(BaseModel):
    id: str
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


class EmployeeSchema(BaseModel):
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


class OrderDetailsModel(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int
    discount: float

    class Config:
        orm_mode = True


class OrdersSchema(BaseModel):
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


class ProductsSchema(BaseModel):
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


class RegionSchema(BaseModel):
    id: int
    region_description: str

    class Config:
        orm_mode = True


class ShippersSchema(BaseModel):
    id: int
    company_name: str
    phone: Optional[str]

    class Config:
        orm_mode = True


class SuppliersSchema(BaseModel):
    id: int
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


class TerritorySchema(BaseModel):
    id: str
    territory_description: str
    region_id: int

    class Config:
        orm_mode = True


class UsStateSchema(BaseModel):
    id: int
    state_name: Optional[str]
    state_abbr: Optional[str]
    state_region: Optional[str]

    class Config:
        orm_mode = True


class CustomerCreate(BaseModel):
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


class USStateCreate(BaseModel):
    state_name: str
    state_abbr: str
    state_region: str


class RegionCreate(BaseModel):
    region_description: str


class TerritoryCreate(BaseModel):
    region_id: int
    region_description: str


class ShipperCreate(BaseModel):
    company_name: str
    phone: str


class CategoryCreate(BaseModel):
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]


class SupplierCreate(BaseModel):
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


class OrderDetailsCreate(BaseModel):
    order_id: int


class EmployeeCreate(BaseModel):
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


class EmployeeTerritoriesCreate(BaseModel):
    territory_id: str


class CustomerCustomerDemoCreate(BaseModel):
    customer_id: str
    customer_type_id: str


class CustomerDemographicsCreate(BaseModel):
    customer_desc: Optional[str]
