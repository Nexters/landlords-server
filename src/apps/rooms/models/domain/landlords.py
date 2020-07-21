from typing import Optional

from pydantic import BaseModel, Field

from ..entity import Address, BuildingType, Description, Title, Uid


class RoomItem(BaseModel):
    uid: str = Field(max_length=Uid.max_length)
    deposit: int = Field(...)
    monthly_rent: int = Field(...)
    is_jeonse: bool = Field(...)
    address: Optional[str] = Field(max_length=Address.max_length)
    title: Optional[str] = Field(max_length=Title.max_length)
    description: Optional[str] = Field(max_length=Description.max_length)
    building_type: BuildingType = Field(...)

    class Config:
        orm_mode = True