from typing import List

from pydantic import BaseModel

from .domain import CheckItem, CheckQuestion


class ChecklistAnswersResponse(BaseModel):
    check_ids: List[int]
