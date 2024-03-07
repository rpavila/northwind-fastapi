from pydantic import BaseModel


class TerritorySchema(BaseModel):
    id: str
    territory_description: str
    region_id: int

    class Config:
        orm_mode = True


class TerritoryCreate(BaseModel):
    region_id: int
    region_description: str
