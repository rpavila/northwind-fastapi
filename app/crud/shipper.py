from app.crud.base import CRUDBase
from app.models import Shipper
from app.schemas.shipper import ShipperCreate


class CRUDShipper(CRUDBase[Shipper, ShipperCreate, ShipperCreate]):

    def __init__(self):
        super().__init__(Shipper)


crud = CRUDShipper()
