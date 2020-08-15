# from typing import Dict

# import pytest
# from fastapi.applications import FastAPI
# from sqlalchemy.orm import Session
# from starlette.testclient import TestClient

# from src.apps.oauth.services import get_current_user
# from src.apps.rooms.models.domain.landlords import CrawlingTarget
# from src.apps.rooms.routes import crawling_room, router
# from src.core.database import get_database_session

# from ..oauth.test_tokens import create_access_token

# client = TestClient(router)

# # headers: Dict[str, str] = {}


# def test_crawling_room() -> None:
#     response = client.put(
#         "/{room_id}",
#         headers=create_access_token,
#         room_id="23431209",
#         crawling_room=CrawlingTarget.Zigbang,
#     )
#     assert response.status_code == 200
#     assert response.json()["uid"] == "Zigbang::23431209"


# @pytest.fixture
# def item() -> str:
#     return "item"


# def test_crawling_item_bad_request(client: TestClient) -> None:
#     # response = client.put("/{room_id}", room_id="")
#     print(client)
