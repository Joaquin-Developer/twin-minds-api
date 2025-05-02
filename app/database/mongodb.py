from typing import List, Dict

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.settings import settings
from app.database.repository import UserRepository, MetadataRepository


client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client["twin_minds"]


class MongoDBUserRepository(UserRepository):
    async def insert_user(self, email: str, name: str, age: int, personality: str, interests: List[str]) -> Dict[str, str]:
        user_doc = {
            "email": email,
            "name": name,
            "age": age,
            "personality": personality,
            "interests": interests
        }
        _ = await db.users.insert_one(user_doc)
        return user_doc

    async def load(self) -> List[Dict[str, str]]:
        return await db.users.find().to_list(None)

    async def get_user_by_email(self, email: str):
        return await db.users.find_one({"email": email})

    async def get_user_by_id(self, id: int):
        return await db.users.find_one({"id": id})


class MongoDBMetadataRepository(MetadataRepository):
    async def insert_interest(self, interest: str):
        new_interest = await db.interests.insert_one({"name": interest})
        print(new_interest)

    async def get_all_interests(self) -> List[str]:
        return await db.interests.find().to_list(None)

    async def delete_interest(self, interest: str):
        await db.interests.delete_one({"mame": interest})

    async def get_all_personalities(self) -> List[str]:
        return await db.personalities.find().to_list(None)
