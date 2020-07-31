from typing import List

from pydantic import BaseModel

from .domain import CheckItem, CheckQuestion


class CheckItemResponse(CheckItem):
    """체크항목 정보 response"""


class CheckItemsResponse(BaseModel):
    check_items: List[CheckItem]


class ChecklistResponse(BaseModel):
    questions: List[CheckQuestion]
