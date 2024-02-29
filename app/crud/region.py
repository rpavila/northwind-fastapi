from app.crud.base import CRUDBase
from app.models import Region
from app.schemas import RegionCreate


class CRUDRegion(CRUDBase[Region, RegionCreate, RegionCreate]):

    def __init__(self):
        super().__init__(Region)


crud = CRUDRegion()
