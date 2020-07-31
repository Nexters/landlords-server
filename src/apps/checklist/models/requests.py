from pydantic import BaseModel


class AnswerCreateRequest(BaseModel):
    """ CheckAnswer 생성 요청"""
    check_id: int
