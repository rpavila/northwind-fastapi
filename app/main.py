from fastapi import FastAPI

from app.routers.customers.router import router as router_customer

app = FastAPI()

app.include_router(router_customer, prefix="/customers", tags=["customer"])