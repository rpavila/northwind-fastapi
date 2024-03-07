from app.crud.base import CRUDBase
from app.models import CustomerDemographics
from app.schemas.customer import CustomerDemographicsCreate


class CRUDCustomerDemographics(CRUDBase[CustomerDemographics, CustomerDemographicsCreate, CustomerDemographicsCreate]):

    def __init__(self):
        super().__init__(CustomerDemographics)


crud = CRUDCustomerDemographics()
