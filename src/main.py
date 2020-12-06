"""
main.py
"""
from fastapi.applications import FastAPI

from .core.handlers import set_exception_handlers


def create_app(title: str) -> FastAPI:
    """ app factory method """
    app = FastAPI(title=title)
    set_exception_handlers(app)
    return app
