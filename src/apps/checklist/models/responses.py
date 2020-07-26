from typing import List

from pydantic import BaseModel

from .domain import CheckItem


class ChecklistAnswerResponse(BaseModel):
    checklistAnswers: List[ChecklistAnswer]


class ChecklistAnswer(BaseModel):
    room_id: int
    check_ids: List[int]
