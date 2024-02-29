from fastapi import APIRouter

from app.api.v1.endpoints import customers, us_states

api_router = APIRouter()
api_router.include_router(customers.router, prefix="/customers", tags=["customers"])
api_router.include_router(us_states.router, prefix="/us-states", tags=["us_states"])