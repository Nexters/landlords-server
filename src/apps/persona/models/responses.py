from typing import List

from pydantic import BaseModel

from .domain import Question, RecommendedPlace


class PersonaQuestionsResponse(BaseModel):
    questions: List[Question]


class PersonaResponse(BaseModel):
    type: str
    description: str
    recommended_place: List[RecommendedPlace]


class PersonaCountResponse(BaseModel):
    count: int
