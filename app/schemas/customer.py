from typing import Optional

from pydantic import BaseModel


class CustomerSchema(BaseModel):
    id: str
    company_name: str
    contact_name: Optional[str]
    # contact_title: Optional[str]
    # address: Optional[str]
    # city: Optional[str]
    # region: Optional[str]
    # postal_code: Optional[str]
    # country: Optional[str]
    # phone: Optional[str]
    fax: Optional[str]
    # fax: Annotated[str, IdValidator] = Field(default=None, validate_default=True)

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


class CustomerCustomerDemoCreate(BaseModel):
    customer_id: str
    customer_type_id: str


class CustomerDemographicsCreate(BaseModel):
    customer_desc: Optional[str]