from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    age: int
    # city: str
    personality: str  # example: "INTJ"
    interests: List[str]
