from pydantic import BaseModel, Field, validator
from typing import Optional


class Character(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    house: Optional[str]
    animal: Optional[str]
    symbol: Optional[str]
    nickname: Optional[str]
    role: str
    age: int
    death: Optional[int]
    strength: str

    @validator("age", pre=True, always=True)
    def validate_age(cls, value):
        if value is None or value < 0:
            raise ValueError("Age must be a positive integer")
        return value