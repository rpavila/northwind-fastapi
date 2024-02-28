from fastapi import FastAPI

from app.routers import customers

app = FastAPI()

app.include_router(customers.router, prefix="/customer", tags=["customer"])

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}