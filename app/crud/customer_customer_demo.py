from app.crud.base import CRUDBase
from app.models import CustomerCustomerDemo
from app.schemas import CustomerCustomerDemoCreate


class CRUDCustomerCustomerDemo(CRUDBase[CustomerCustomerDemo, CustomerCustomerDemoCreate, CustomerCustomerDemoCreate]):

    def __init__(self):
        super().__init__(CustomerCustomerDemo)


crud = CRUDCustomerCustomerDemo()
