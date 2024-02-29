from app.crud.base import CRUDBase
from app.models import Territory
from app.schemas import TerritoryCreate


class CRUDTerritory(CRUDBase[Territory, TerritoryCreate, TerritoryCreate]):

    def __init__(self):
        super().__init__(Territory)


crud = CRUDTerritory()
