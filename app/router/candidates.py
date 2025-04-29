from fastapi import APIRouter

from app.services.candidates import CandidatesService

router = APIRouter()


@router.get("/generate/{user_id}")
def generate_candidates_list_from_user(user_id: str):
    user_id = int(user_id)
    service = CandidatesService(user_id)
    data = service.generate()
    return data

