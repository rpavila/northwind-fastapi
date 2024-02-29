from app.crud.base import CRUDBase
from app.models import Category
from app.schemas import CategoryCreate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryCreate]):

    def __init__(self):
        super().__init__(Category)


crud = CRUDCategory()
