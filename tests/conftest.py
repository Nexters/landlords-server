import pytest
from fastapi.applications import FastAPI
from starlette.testclient import TestClient

from src.core.config import settings
from src.main import create_app
from src.routes import api_v1


@pytest.fixture
def app() -> FastAPI:
    """ test app """
    app = create_app(title="테스트")
    app.include_router(api_v1, prefix=f"{settings.API_VERSION_PREFIX}")
    return app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """ test client """
    return TestClient(app)
