from typing import List

from pydantic import BaseModel

from .domain import Question


class PersonaQuestionsResponse(BaseModel):
    questions: List[Question]


class PersonaResponse(BaseModel):
    title: str
    description: str


class PersonaCountResponse(BaseModel):
    count: int
