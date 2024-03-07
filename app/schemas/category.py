from typing import Optional

from pydantic import BaseModel


class CategorySchema(BaseModel):
    id: int
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]

    class Config:
        orm_mode = True


class CategoryCreate(BaseModel):
    category_name: str
    description: Optional[str]
    picture: Optional[bytes]
