"""
main.py
"""
from authlib.common.errors import AuthlibBaseError
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException

from .core.exceptions import RepositoryException
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
        RepositoryException, handler=database_exception_handler
    )
    app.add_exception_handler(HTTPException, handler=http_exception_handler)
    app.add_exception_handler(AuthlibBaseError, handler=auth_exception_handler)
    return app
