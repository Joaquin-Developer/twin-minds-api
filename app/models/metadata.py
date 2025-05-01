from typing import List

from pydantic import BaseModel


class MetaData(BaseModel):
    personalities: List[str]
    interests: List[str]
