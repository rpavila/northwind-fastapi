from app.crud.base import CRUDBase
from app.models import Customer
from app.schemas.customer import CustomerCreate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerCreate]):

    def __init__(self):
        super().__init__(Customer)


crud = CRUDCustomer()
