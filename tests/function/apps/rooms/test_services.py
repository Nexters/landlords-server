from src.apps.rooms.models.domain.dabang import Dabang
from src.apps.rooms.services import get_dabang_room_detail
from src.core.exceptions import CrawlingException


def test_get_dabang() -> None:
    try:
        dabang: Dabang = get_dabang_room_detail(
            room_id="5f0681178839af708334481e"
        )
    except CrawlingException as err:
        assert err
    else:
        print(dabang)
