from app.crud.base import CRUDBase
from app.models import Product
from app.schemas.product import ProductCreate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductCreate]):

    def __init__(self):
        super().__init__(Product)


crud = CRUDProduct()
