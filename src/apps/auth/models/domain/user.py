from pydantic import BaseModel


class UserInDB(BaseModel):
    id: int
    email: str
    full_name: str
    profile: str
    disabled: bool

    class Config:
        orm_mode = True
