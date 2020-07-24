"""
main.py
"""
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from jwt import PyJWTError
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException

from .apps.rooms.exceptions import RoomNotFoundException
from .core.handlers import (
    auth_exception_handler,
    database_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)


def create_app() -> FastAPI:
    """ app factory method """
    app = FastAPI()

    app.add_exception_handler(
        ValidationError, handler=validation_exception_handler
    )

    app.add_exception_handler(
        RequestValidationError, handler=validation_exception_handler
    )

    app.add_exception_handler(
        SQLAlchemyError, handler=database_exception_handler
    )
    app.add_exception_handler(
        RoomNotFoundException, handler=database_exception_handler
    )
    app.add_exception_handler(HTTPException, handler=http_exception_handler)
    app.add_exception_handler(PyJWTError, handler=auth_exception_handler)
    return app
