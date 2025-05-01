from typing import List

from app.models.user import CreateUserRequest, User
from app.database import local_storage as db


class UsersService:
    @staticmethod
    def create_user(data: CreateUserRequest):
        new_user = db.insert_user(data.email, data.name, data.age, data.personality, data.interests)
        return User(
            id=new_user["id"],
            email=new_user["email"],
            name=new_user["name"],
            age=new_user["age"],
            personality=new_user["personality"],
            interests=new_user["interests"],
        )

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

    @staticmethod
    def get_user_by_mail(mail: str) -> User:
        data = db.load()
        for user in data:
            if user["email"] == mail:
                return User(
                    id=user["id"],
                    email=user["email"],
                    name=user["name"],
                    age=user["age"],
                    personality=user["personality"],
                    interests=user["interests"],
                )
        return None
