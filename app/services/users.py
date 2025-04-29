from typing import List, Dict

from app.models.user import CreateUserRequest, User
from app.database import local_storage as db


class UsersService:
    @staticmethod
    def create_user(data: CreateUserRequest):
        db.insert_user(data.email, data.name, data.age, data.personality, data.interests)

    @staticmethod
    def get_all_users() -> List[User]:
        data = db.load()
        return [
            User(
                id=user["id"],
                email=user["email"],
                name=user["name"],
                age=user["age"],
                personality=user["personality"],
                interests=user["interests"],
            )
            for user in data
        ]

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        data = db.load()
        for user in data:
            if user["id"] == user_id:
                return User(
                    id=user["id"],
                    email=user["email"],
                    name=user["name"],
                    age=user["age"],
                    personality=user["personality"],
                    interests=user["interests"],
                )
        return None
