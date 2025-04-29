from typing import List
import traceback

from fastapi import APIRouter, Response, status

from app.services.candidates import CandidatesService
from app.models.candidates import Candidate

router = APIRouter()


@router.get("/generate/{user_id}", response_model=List[Candidate])
def generate_candidates_list_from_user(user_id: str):
    try:
        user_id = int(user_id)
        service = CandidatesService(user_id)
        data = service.generate()
        return data
    except Exception as error:
        traceback.print_exc()
        return Response(str(error), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
