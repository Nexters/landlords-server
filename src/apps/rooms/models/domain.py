from pydantic import BaseModel, Field

from .entity import Address, Description, Uid


class RoomItem(BaseModel):
    uid: str = Field(max_length=Uid.max_length)
    deposit: int = Field(...)
    monthly_rent: int = Field(...)
    is_jeonse: bool = Field(...)
    address: str = Field(max_length=Address.max_length)
    description: str = Field(max_length=Description.max_length)

    class Config:
        orm_mode = True
