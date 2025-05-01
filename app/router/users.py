from typing import List

from fastapi import APIRouter, Response, status

from app.models import user as usr_models
from app.services.users import UsersService

router = APIRouter()


@router.get("/", response_model=List[usr_models.User])
def get_all_users():
    return UsersService.get_all_users()


@router.get("/mail-exists/{mail}", response_model=usr_models.User)
def mail_exists(mail: str):
    user = UsersService.get_user_by_mail(mail)
    return user if user else Response(content="User not found", status_code=status.HTTP_404_NOT_FOUND)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=usr_models.User)
def create_user(data: usr_models.CreateUserRequest):
    try:
        return UsersService.create_user(data)
    except Exception as error:
        return Response(content=str(error), status_code=status.HTTP_400_BAD_REQUEST)


# router.post("/set_profile")
# def set_user_profile():
#     pass
