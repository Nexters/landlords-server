from typing import Optional

from pydantic import BaseModel, Extra


class Properties(BaseModel):
    nickname: str
    profile_image: str
    thumbnail_image: str

    class Config:
        extra = Extra.allow


class Profile(BaseModel):
    nickname: str
    thumbnail_image_url: str
    profile_image_url: str

    class Config:
        extra = Extra.allow


class KakaoAccount(BaseModel):
    profile_needs_agreement: bool
    profile: Profile

    has_age_range: Optional[bool]
    age_range_needs_agreement: Optional[bool]
    age_range: Optional[str]
    has_gender: Optional[bool]
    gender_needs_agreement: Optional[bool]
    gender: Optional[str]

    class Config:
        extra = Extra.allow
