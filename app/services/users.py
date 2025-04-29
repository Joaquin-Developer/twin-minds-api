from app.models.user import CreateUserRequest
from app.database import local_storage as db


class UsersService:
    @staticmethod
    def create_user(data: CreateUserRequest):
        db.insert_user(data.email, data.name, data.age, data.personality, data.interests)

    @staticmethod
    def get_all_users():
        data = db.load()
        return data