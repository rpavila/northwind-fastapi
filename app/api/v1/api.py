from fastapi import APIRouter

from app.api.v1.endpoints import (categories, customers, employees, employees_territories, orders, orders_details,
                                  products, regions, shippers, suppliers, territories, us_states)

api_router = APIRouter()
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(employees_territories.router, prefix="/employees-territories", tags=["employees_territories"])
api_router.include_router(orders.router, prefix="/orders", tags=["orders"])
api_router.include_router(orders_details.router, prefix="/orders-details", tags=["orders_details"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(regions.router, prefix="/regions", tags=["regions"])
api_router.include_router(shippers.router, prefix="/shippers", tags=["shippers"])
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(territories.router, prefix="/territories", tags=["territories"])
api_router.include_router(us_states.router, prefix="/us-states", tags=["us_states"])