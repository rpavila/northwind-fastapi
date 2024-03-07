from app.crud.base import CRUDBase
from app.models import EmployeeTerritories
from app.schemas.employee import EmployeeTerritoriesCreate


class CRUDEmployeeTerritories(CRUDBase[EmployeeTerritories, EmployeeTerritoriesCreate, EmployeeTerritoriesCreate]):

    def __init__(self):
        super().__init__(EmployeeTerritories)


crud = CRUDEmployeeTerritories()
