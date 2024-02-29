from app.crud.base import CRUDBase
from app.models import USState
from app.schemas import USStateCreate


class CRUDUSState(CRUDBase[USState, USStateCreate, USStateCreate]):

    def __init__(self):
        super().__init__(USState)


crud = CRUDUSState()
