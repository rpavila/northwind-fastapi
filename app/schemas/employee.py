from datetime import date
from typing import Optional

from pydantic import BaseModel


class EmployeeSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    title: Optional[str]
    # title_of_courtesy: Optional[str]
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
