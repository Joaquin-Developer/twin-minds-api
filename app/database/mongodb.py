from typing import List, Dict

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.settings import settings
from app.database.repository import UserRepository, MetadataRepository
from app.exceptions import UserAlreadyExistsException

client = AsyncIOMotorClient(settings.MONGODB_URL)
db = client["twin_minds"]


class MongoDBUserRepository(UserRepository):
    async def generate_unique_id(self, _ = None) -> int:
        doc = await db.users.find().sort("id", -1).limit(1).to_list(length=1)
        if doc:
            return doc[0]["id"] + 1
        return 1

    async def insert_user(self, email: str, name: str, age: int, personality: str, interests: List[str]) -> Dict[str, str]:
        existing_email = await db.users.find_one({"email": email})
        if existing_email:
            raise UserAlreadyExistsException(f"User with email {email} already exists")

        new_id = await self.generate_unique_id()
        user_doc = {
            "id": new_id,
            "email": email,
            "name": name,
            "age": age,
            "personality": personality,
            "interests": interests
        }
        await db.users.insert_one(user_doc)
        return user_doc

    async def load(self) -> List[Dict[str, str]]:
        return await db.users.find().to_list(None)

    async def get_user_by_email(self, email: str):
        return await db.users.find_one({"email": email})

    async def get_user_by_id(self, id: int):
        return await db.users.find_one({"id": id})


class MongoDBMetadataRepository(MetadataRepository):
    async def insert_interest(self, interest: str):
        await db.interests.insert_one({"name": interest})

    async def get_all_interests(self) -> List[str]:
        return await db.interests.find().to_list(None)

    async def delete_interest(self, interest: str):
        await db.interests.delete_one({"mame": interest})

    async def get_all_personalities(self) -> List[str]:
        return await db.personalities.find().to_list(None)
