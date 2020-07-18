from src.apps.rooms.models.domain.dabang import Dabang
from src.apps.rooms.services import (
    DabangCrawlingException,
    get_dabang_room_detail,
)


def test_get_dabang() -> None:
    try:
        dabang: Dabang = get_dabang_room_detail(
            room_id="5f0681178839af708334481e"
        )
    except DabangCrawlingException as err:
        assert err
    else:
        print(dabang)
