from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    name: str
    age: int
    # city: str
    personality: str  # example: "INTJ"
    interests: List[str]


class CreateUserRequest(BaseModel):
    email: str
    name: str
    age: int
    personality: str
    interests: List[str]
