from pydantic import BaseModel


class RegionSchema(BaseModel):
    id: int
    region_description: str

    class Config:
        orm_mode = True


class RegionCreate(BaseModel):
    region_description: str
