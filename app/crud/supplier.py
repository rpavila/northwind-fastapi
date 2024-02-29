from app.crud.base import CRUDBase
from app.models import Supplier
from app.schemas import SupplierCreate


class CRUDSupplier(CRUDBase[Supplier, SupplierCreate, SupplierCreate]):

    def __init__(self):
        super().__init__(Supplier)


crud = CRUDSupplier()
