from typing import List

from pydantic import BaseModel


class Candidate(BaseModel):
    score: int
    name: str
    age: int
    personality: str
    interests: List[str]
