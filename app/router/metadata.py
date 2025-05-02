from fastapi import APIRouter

from app.models.metadata import MetaData
from app.services.metadata import MetadataService

router = APIRouter()


@router.get("/", response_model=MetaData)
async def get_metadata():
    return MetadataService.get()
