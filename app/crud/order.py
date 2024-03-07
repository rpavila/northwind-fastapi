from app.crud.base import CRUDBase
from app.models import Order
from app.schemas.order import OrderCreate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderCreate]):

    def __init__(self):
        super().__init__(Order)


crud = CRUDOrder()
