from typing import List, Optional

from pydantic import BaseModel, Field

from ...oauth.models.domain.landlords import OAuthType
from ...persona.models.domain import ChoiceItem


class UserInfo(BaseModel):
    sub: str = Field(..., description="구글 jwt sub")
    email: str = Field(..., description="이메일")
    name: str = Field(..., alias="full_name", description="전체 이름")
    picture: str = Field(..., alias="profile", description="프로필 이미지")
    persona_answers: Optional[List[ChoiceItem]] = Field(
        default=None, description="페르소나 선택 항목 리스트"
    )

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserInDB(UserInfo):
    uid: int
    oauth_type: OAuthType
    sub: str
    disabled: bool

    class Config:
        orm_mode = True
