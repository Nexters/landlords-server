from enum import Enum
from http import HTTPStatus
from typing import Any, Union

import requests

from ...core.exceptions import CrawlingException
from .models.domain.dabang import Dabang
from .models.domain.landlords import CrawlingTarget
from .models.domain.zigbang import Zigbang

dabang_detail_api = (
    "https://www.dabangapp.com/api/3/room/detail"
    "?api_version=3.0.1"
    "&call_type=web"
    "&room_id={room_id}"
    "&use_map={use_map}"
    "&version=1"
)
zigbang_api = "https://apis.zigbang.com/v2/items/list"
zigbang_description_api = "https://apis.zigbang.com/v1/items/{room_id}/read"


class MapType(str, Enum):
    Kakao = "kakao"


def get_room_detail(
    room_id: str, crawling_target: CrawlingTarget
) -> Union[Zigbang, Dabang]:
    result: Union[Zigbang, Dabang]
    if crawling_target == CrawlingTarget.Dabang:
        result = get_dabang_room_detail(room_id)
    elif crawling_target == CrawlingTarget.Zigbang:
        result = get_zigbang_room_detail(room_id=int(room_id))

    return result


def get_dabang_room_detail(
    room_id: str, use_map: MapType = MapType.Kakao
) -> Dabang:
    """ 다방의 방 상세정보 가져오기 (BackgroundTask) """
    response = requests.get(
        dabang_detail_api.format(room_id=room_id, use_map=use_map)
    )
    if response.status_code != HTTPStatus.OK:
        raise CrawlingException(f"error: {response.reason}")
    return Dabang(**response.json())


def get_zigbang_room_detail(room_id: int) -> Zigbang:
    response = requests.post(zigbang_api, json={"item_ids": [room_id]})
    zigbang = Zigbang(**response.json())
    if response.status_code != HTTPStatus.OK:
        raise CrawlingException(f"error: {response.reason}")

    description_response = requests.get(
        zigbang_description_api.format(room_id=room_id)
    )
    if description_response.status_code == HTTPStatus.OK:
        description = description_response.json()
        zigbang.items[0].description = description

    return zigbang
