from typing import List

from app.models.user import CreateUserRequest, User
from app.database.local_storage import LocalStorageUserRepository
from app.database.mongodb import MongoDBUserRepository
from app.core.settings import settings


class UsersService:
    def __init__(self):
        if settings.USE_LOCAL_STORAGE:
            self.db = LocalStorageUserRepository()
        else:
            self.db = MongoDBUserRepository()

    async def create_user(self, data: CreateUserRequest) -> User:
        new_user = await self.db.insert_user(data.email, data.name, data.age, data.personality, data.interests)
        return User(
            id=new_user["id"],
            email=new_user["email"],
            name=new_user["name"],
            age=new_user["age"],
            personality=new_user["personality"],
            interests=new_user["interests"],
        )

    async def get_all_users(self) -> List[User]:
        data = await self.db.load()
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

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.db.get_user_by_id(user_id)

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

    async def get_user_by_mail(self, mail: str) -> User:
        user = await self.db.get_user_by_email(mail)

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
