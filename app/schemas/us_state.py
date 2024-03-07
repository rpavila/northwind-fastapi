from typing import Optional

from pydantic import BaseModel


class UsStateSchema(BaseModel):
    id: int
    state_name: Optional[str]
    state_abbr: Optional[str]
    state_region: Optional[str]

    class Config:
        orm_mode = True


class USStateCreate(BaseModel):
    state_name: str
    state_abbr: str
    state_region: str