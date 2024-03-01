from datetime import date
from pydantic import BaseModel, ConfigDict, Field, validator, field_validator, BeforeValidator
from typing import Optional, Annotated, List


class CategorySchema(BaseModel):
    id: int
    category_name: str
    description: str | None = None
    picture: Optional[bytes]

    # class Config:
    #     orm_mode = True


class CustomerCustomerDemoSchema(BaseModel):
    id: str
    customer_type_id: str

#     class Config:
#         orm_mode = True


class CustomerDemographicsSchema(BaseModel):
    customer_type_id: str
    customer_desc: str | None = None

#     class Config:
#         orm_mode = True

IdValidator = BeforeValidator(lambda id: id or '')



class EmployeeSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    title: str | None = None
    # title_of_courtesy: str | None = None
    birth_date: Optional[date]
    hire_date: Optional[date]
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    home_phone: str | None = None
    extension: str | None = None
    photo: Optional[bytes]
    notes: str | None = None
    reports_to: Optional[int]
    photo_path: str | None = None

#     class Config:
#         orm_mode = True


class EmployeeTerritoriesSchema(BaseModel):
    employee_id: int
    territory_id: str

#     class Config:
#         orm_mode = True


class OrderDetailsSchema(BaseModel):
    order_id: int
    product_id: int
    unit_price: float
    quantity: int
    discount: float

#     class Config:
#         orm_mode = True


class OrderSchema(BaseModel):
    id: int
    customer_id: str | None = None
    employee_id: Optional[int]
    order_date: Optional[date]
    required_date: Optional[date]
    shipped_date: Optional[date]
    ship_via: Optional[int]
    freight: Optional[float]
    ship_name: str | None = None
    ship_address: str | None = None
    ship_city: str | None = None
    ship_region: str | None = None
    ship_postal_code: str | None = None
    ship_country: str | None = None

    class Config:
        from_attributes = True


class ProductSchema(BaseModel):
    id: int
    product_name: str
    supplier_id: Optional[int]
    category_id: Optional[int]
    quantity_per_unit: str | None = None
    unit_price: Optional[float]
    units_in_stock: Optional[int]
    units_on_order: Optional[int]
    reorder_level: Optional[int]
    discontinued: int

#     class Config:
#         orm_mode = True


class RegionSchema(BaseModel):
    id: int
    region_description: str

#     class Config:
#         orm_mode = True


class ShipperSchema(BaseModel):
    id: int
    company_name: str
    phone: str | None = None

#     class Config:
#         orm_mode = True


class SupplierSchema(BaseModel):
    id: int
    company_name: str
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None
    homepage: str | None = None

#     class Config:
#         orm_mode = True


class TerritorySchema(BaseModel):
    id: str
    territory_description: str
    region_id: int

#     class Config:
#         orm_mode = True


class UsStateSchema(BaseModel):
    id: int
    state_name: str | None = None
    state_abbr: str | None = None
    state_region: str | None = None

#     class Config:
#         orm_mode = True


class CustomerCreate(BaseModel):
    company_name: str
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None



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
    description: str | None = None
    picture: Optional[bytes]


class SupplierCreate(BaseModel):
    company_name: str
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None
    homepage: str | None = None


class ProductCreate(BaseModel):
    product_name: str
    supplier_id: int
    category_id: int
    quantity_per_unit: str | None = None
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
    ship_name: str | None = None
    ship_address: str | None = None
    ship_city: str | None = None
    ship_region: str | None = None
    ship_postal_code: str | None = None
    ship_country: str | None = None


class OrderDetailsCreate(BaseModel):
    order_id: int


class EmployeeCreate(BaseModel):
    last_name: str
    first_name: str
    title: str | None = None
    title_of_courtesy: str | None = None
    birth_date: Optional[date]
    hire_date: Optional[date]
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    home_phone: str | None = None
    extension: str | None = None
    photo: Optional[bytes]
    notes: str | None = None
    reports_to: Optional[int]
    photo_path: str | None = None


class EmployeeTerritoriesCreate(BaseModel):
    territory_id: str


class CustomerCustomerDemoCreate(BaseModel):
    customer_id: str
    customer_type_id: str


class CustomerDemographicsCreate(BaseModel):
    customer_desc: str | None = None


class CustomerSchema(BaseModel):
    id: str
    company_name: str
    contact_name: str | None = None
    contact_title: str | None = None
    address: str | None = None
    city: str | None = None
    region: str | None = None
    postal_code: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None

    orders: list[OrderSchema] = []

    class Config:
        from_attributes = True

    # @field_validator
    # def set_fax(cls, value):
    #     return value or 'Empty'