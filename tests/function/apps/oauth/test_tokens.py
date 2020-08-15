import pytest
from fastapi.applications import FastAPI

from src.apps.oauth.models.domain.landlords import UserInfo
from src.apps.oauth.services import create_access_token


@pytest.fixture
def mocking_user() -> UserInfo:
    return UserInfo(
        sub="jwt sub",
        email="sju02030@naver.com",
        name="Taya",
        picture="http://www.pngmart.com/files/6/Stitch-PNG-Photos.png",
    )


@pytest.fixture
def test_create_token(app: FastAPI) -> str:
    return create_access_token(user_info=mocking_user())
