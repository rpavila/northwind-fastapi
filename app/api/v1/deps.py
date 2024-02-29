from collections.abc import Generator
from typing import Annotated

from fastapi import Depends

from app.database import SessionLocal


# def get_db() -> Generator:
#     with SessionLocal() as session:
#         yield session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SessionDep = Annotated[SessionLocal, Depends(get_db)]
SessionDep = Depends(get_db)