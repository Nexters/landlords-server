from typing import List

from pydantic import BaseModel

from .domain import CheckQuestion


class ChecklistAnswersResponse(BaseModel):
    check_ids: List[int]


class ChecklistResponse(BaseModel):
    questions: List[CheckQuestion]
