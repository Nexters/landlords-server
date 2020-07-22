"""
main.py
"""
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException

from .apps.auth.exceptions import AuthError
from .apps.rooms.exceptions import RoomNotFoundException
from .core.handlers import (
    database_exception_handler,
    http_exception_handler,
    oauth_exception_handler,
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

    app.add_exception_handler(AuthError, handler=oauth_exception_handler)

    app.add_exception_handler(
        SQLAlchemyError, handler=database_exception_handler
    )
    app.add_exception_handler(
        RoomNotFoundException, handler=database_exception_handler
    )
    app.add_exception_handler(HTTPException, handler=http_exception_handler)

    return app
