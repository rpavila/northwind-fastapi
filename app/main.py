from fastapi import FastAPI

from app.api.v1.api import api_router
from app.routers.customers.router import router as router_customer

app = FastAPI()

app.include_router(api_router)