from app.database import local_storage as db
from app.models.metadata import MetaData


class MetadataService:
    @staticmethod
    def get() -> MetaData:
        return MetaData(
            personalities=list(db.PERSONALITIES_SET),
            interests=list(db.INTERESTS_SET),
        )
