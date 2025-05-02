from app.database.local_storage import LocalStorageMetadatarepository
from app.models.metadata import MetaData


class MetadataService:
    @staticmethod
    def get() -> MetaData:
        db = LocalStorageMetadatarepository()
        return MetaData(
            personalities=db.get_all_personalities(),
            interests=db.get_all_interests(),
        )
