from app.crud.base import CRUDBase
from app.models import OrderDetail
from app.schemas.order import OrderDetailsCreate


class CRUDOrderDetail(CRUDBase[OrderDetail, OrderDetailsCreate, OrderDetailsCreate]):

    def __init__(self):
        super().__init__(OrderDetail)


crud = CRUDOrderDetail()
