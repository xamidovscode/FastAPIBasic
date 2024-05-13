from enum import Enum

from pydantic import BaseModel
from pydantic import Field
from typing import List, Optional


class PositionTypes(Enum):
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'


class UserPosition(BaseModel):
    id: int
    position: PositionTypes
    experience: str


class User(BaseModel):
    id: int = Field(ge=0)
    role: str
    name: str
    position: Optional[List[UserPosition]] = []

