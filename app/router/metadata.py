from fastapi import APIRouter, Response, status

from app.models.metadata import MetaData
from app.services.metadata import MetadataService
from app.logger import logger

router = APIRouter()
metadata_service = MetadataService()


@router.get("/", response_model=MetaData)
async def get_metadata():
    try:
        return await metadata_service.get()
    except Exception as error:
        logger.warning(error)
        # return Response(content=str(error), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
