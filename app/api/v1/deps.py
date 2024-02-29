from fastapi import Depends, Request


def get_db(request: Request):
    return request.state.db


SessionDep = Depends(get_db)