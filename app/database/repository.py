from typing import List, Dict
from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def insert_user(self, email: str, name: str, age: int, personality: str, interests: List[str]) -> Dict[str, str]:
        ...

    @abstractmethod
    def load(self) -> List[Dict[str, str]]:
        ...

    @abstractmethod
    def get_user_by_id(self, id: int) -> Dict[str, str]:
        ...

    @abstractmethod
    def get_user_by_email(self, email: str) -> Dict[str, str]:
        ...


class CandidatesRepository(ABC):
    ...


class MetadataRepository(ABC):
    @abstractmethod
    def insert_interest(self, interest: str):
        ...

    @abstractmethod
    def get_all_interests(self, ) -> List[str]:
        ...

    @abstractmethod
    def delete_interest(self, interest: str):
        ...

    @abstractmethod
    def get_all_personalities(self) -> List[str]:
        ...