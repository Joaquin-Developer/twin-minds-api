from typing import List, Dict, Any
import json

from app.database.repository import UserRepository, MetadataRepository
from app.logger import logger

JSON_PATH = "app/resources/users.json"


class LocalStorageUserRepository(UserRepository):
    def generate_unique_id(self, data: List[Dict[str, Any]]) -> int:
        if not data:
            return 1
        max_id = max(item.get("id", 0) for item in data)
        return max_id + 1

    def insert_user(self, email, name, age, personality, interests):
        data = self.load()

        emails = set([usr["email"] for usr in data])
        if email in emails:
            raise Exception("User already exists.")

        new_id = self.generate_unique_id(data)
        new_user = {
            "id": new_id,
            "email": email,
            "name": name,
            "age": age,
            "personality": personality,
            "interests": interests
        }
        data.append(new_user)

        with open(JSON_PATH, "w") as file:
            json.dump(data, file, indent=4)

        logger.info("User %s inserted with ID: %s", name, str(new_id))
        return new_user

    def load(self) -> List[Dict[str, str]]:
        try:
            with open(JSON_PATH, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            logger.error("'%s' file not found", JSON_PATH)
            return []
        except json.JSONDecodeError:
            logger.error("Invalid '%s' file", JSON_PATH)
            return []

    def get_user_by_id(self, user_id: int) -> Dict[str, str]:
        data = self.load()
        for user in data:
            if user["id"] == user_id:
                return user
        return None

    def get_user_by_email(self, email: str) -> Dict[str, str]:
        data = self.load()
        for user in data:
            if user["email"] == email:
                return user
        return None


class LocalStorageMetadatarepository(MetadataRepository):
    def insert_interest(self, interest: str):
        raise NotImplementedError()

    def get_all_interests(self, ) -> List[str]:
        return list({
            "videogames", "gym", "astronomy", "voley", "cars", "science", "music",
            "art", "yoga", "rock", "jazz", "anime", "cats", "dogs",
        })

    def delete_interest(self, interest: str):
        raise NotImplementedError()

    def get_all_personalities(self) -> List[str]:
        personalities_set = {
            "INTJ",
            "INTP",
            "ENTJ",
            "ENTP",
            "INFJ",
            "INFP",
            "ENFJ",
            "ENFP",
            "ISTJ",
            "ISFJ",
            "ESTJ",
            "ESFJ",
            "ISTP",
            "ISFP",
            "ESTP",
            "ESFP",
        }
        return list(personalities_set)
