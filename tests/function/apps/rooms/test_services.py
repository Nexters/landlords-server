from src.apps.rooms.models.domain.dabang import Dabang
from src.apps.rooms.models.domain.zigbang import Zigbang
from src.apps.rooms.services import (
    get_dabang_room_detail,
    get_zigbang_room_detail,
)
from src.core.exceptions import CrawlingException


def test_get_dabang() -> None:
    try:
        dabang: Dabang = get_dabang_room_detail(
            room_id="5f2ce8637601ce75301269cf"
        )
        room_item = dabang.to_room()
    except CrawlingException as err:
        assert err
    else:
        print(room_item)


def test_get_zigbang() -> None:
    try:
        zigbang: Zigbang = get_zigbang_room_detail(room_id=23126067)
        room_item = zigbang.to_room()
    except CrawlingException as err:
        assert err
    else:
        print(room_item)
