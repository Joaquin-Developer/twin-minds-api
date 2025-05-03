from app.database.mongodb import MongoDBMetadataRepository
from app.database.local_storage import LocalStorageMetadatarepository
from app.models.metadata import MetaData
from app.core.settings import settings


class MetadataService:
    def __init__(self):
        if settings.USE_LOCAL_STORAGE:
            self.db = LocalStorageMetadatarepository()
        else:
            self.db = MongoDBMetadataRepository()

    async def get(self) -> MetaData:
        personalities = await self.db.get_all_personalities()
        interests = await self.db.get_all_interests()
        return MetaData(
            personalities=personalities,
            interests=interests,
        )
