"""
main.py
"""
from authlib.integrations.base_client.errors import OAuthError
from fastapi.applications import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic.error_wrappers import ValidationError
from starlette.exceptions import HTTPException

from .core.handlers import (
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
    app.add_exception_handler(OAuthError, handler=oauth_exception_handler)
    app.add_exception_handler(HTTPException, handler=http_exception_handler)

    return app
