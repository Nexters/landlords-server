from enum import Enum
from http import HTTPStatus

import requests

from .models.domain.dabang import Dabang

dabang_detail_api = (
    "https://www.dabangapp.com/api/3/room/detail"
    "?api_version=3.0.1"
    "&call_type=web"
    "&room_id={room_id}"
    "&use_map={use_map}"
    "&version=1"
)


class DabangCrawlingException(Exception):
    """ 다방 크롤링 예외 """


class MapType(str, Enum):
    Kakao = "kakao"


def get_dabang_room_detail(
    room_id: str, use_map: MapType = MapType.Kakao
) -> Dabang:
    """ 다방의 방 상세정보 가져오기 (BackgroundTask) """
    response = requests.get(
        dabang_detail_api.format(room_id=room_id, use_map=use_map)
    )
    if response.status_code != HTTPStatus.OK:
        raise DabangCrawlingException(f"error: {response.reason}")
    return Dabang(**response.json())
