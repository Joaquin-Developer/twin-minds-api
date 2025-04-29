from typing import List, Dict, Any
import json


JSON_PATH = "app/resources/users.json"


def load() -> List[Dict[str, str]]:
    try:
        with open(JSON_PATH, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: '{JSON_PATH}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid '{JSON_PATH}' file.")
        return []


def generate_unique_id(data: List[Dict[str, Any]]) -> int:
    if not data:
        return 1
    max_id = max(item.get("id", 0) for item in data)
    return max_id + 1


def save_data(data: List[Dict[str, Any]]):
    with open(JSON_PATH, "w") as file:
        json.dump(data, file, indent=4)


def insert_user(email: str, name: str, age: int, personality: str, interests: List[str]):
    data = load()

    emails = set([usr["email"] for usr in data])
    if email in emails:
        raise Exception("User already exists.")

    new_id = generate_unique_id(data)
    new_user = {
        "id": new_id,
        "email": email,
        "name": name,
        "age": age,
        "personality": personality,
        "interests": interests
    }
    data.append(new_user)
    save_data(data)
    print(f"Usuario '{name}' insertado con ID: {new_id}")


PERSONALITIES_SET = [
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
]


INTERESTS_SET = [
    "videogames", "gym", "astronomy", "voley", "cars", "science", "music", "art", "yoga", "rock", "jazz", "anime",
    "cats", "dogs",
]
