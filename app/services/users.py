from typing import List

from app.models.user import CreateUserRequest, User
from app.database.local_storage import LocalStorageUserRepository
from app.database.mongodb import MongoDBUserRepository


class UsersService:
    @staticmethod
    async def create_user(data: CreateUserRequest):
        db = LocalStorageUserRepository()
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
    async def get_all_users() -> List[User]:
        # db = LocalStorageUserRepository()
        db = MongoDBUserRepository()
        data = await db.load()
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
    async def get_user_by_id(user_id: int) -> User:
        db = LocalStorageUserRepository()
        user = db.get_user_by_id(user_id)

        if user:
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
    async def get_user_by_mail(mail: str) -> User:
        db = LocalStorageUserRepository()
        user = db.get_user_by_email(mail)

        if user:
            return User(
                id=user["id"],
                email=user["email"],
                name=user["name"],
                age=user["age"],
                personality=user["personality"],
                interests=user["interests"],
            )
        return None
