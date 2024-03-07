from app.crud.base import CRUDBase
from app.models import Employee
from app.schemas.employee import EmployeeCreate


class CRUDEmployee(CRUDBase[Employee, EmployeeCreate, EmployeeCreate]):

    def __init__(self):
        super().__init__(Employee)


crud = CRUDEmployee()
