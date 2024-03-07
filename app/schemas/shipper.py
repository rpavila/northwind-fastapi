from typing import Optional

from pydantic import BaseModel


class ShipperSchema(BaseModel):
    id: int
    company_name: str
    phone: Optional[str]

    class Config:
        orm_mode = True


class ShipperCreate(BaseModel):
    company_name: str
    phone: str
