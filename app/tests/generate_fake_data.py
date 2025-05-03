from typing import List, Dict, Tuple, Any
import random
import asyncio
import argparse

from faker import Faker

from app.services.metadata import MetadataService


class GenerateFakeUsers:
    def __init__(self, length: int, first_id: int):
        self.length = length
        self.first_id = first_id

        self.personalities: List[str] = None
        self.interests: List[str] = None

        # configurations:
        self.random_min_age = 18
        self.random_max_age = 45
        self.prcnt_diff_interval = 0.2

    async def get_metadata(self):
        service = MetadataService()
        metadata = await service.get()
        return metadata.personalities, metadata.interests

    def generate_fake_users(self) -> List[Dict[str, Any]]:
        fake = Faker()
        ids = self.first_id
        personalities_max_index = len(self.personalities) - 1

        mx_index_pers = len(self.personalities) - 1
        min_index = int(self.prcnt_diff_interval * mx_index_pers)
        max_index = mx_index_pers - int(self.prcnt_diff_interval * mx_index_pers)

        fake_users = []

        for _ in range(self.length):
            random_idx_personality = random.randint(0, personalities_max_index)
            total_possible_interests = random.randint(min_index, max_index)

            fake_user = {
                "id": ids,
                "email": fake.email(),
                "name": fake.name(),
                "age": random.randint(self.random_min_age, self.random_max_age),
                "personality": self.personalities[random_idx_personality],
                "interests": random.sample(self.interests, total_possible_interests)
            }
            fake_users.append(fake_user)
            ids += 1

        return fake_users

    async def main(self):
        personalities, interests = await self.get_metadata()
        self.personalities = personalities
        self.interests = interests

        fake_data = self.generate_fake_users()
        for user in fake_data:
            print(user)


def get_args() -> Tuple[int, int]:
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, required=True, help="Total of users")
    parser.add_argument("--first-id", type=int, required=True, help="First ID value")
    args = parser.parse_args()
    return int(args.length), int(args.first_id)


if __name__ == "__main__":
    length, first_id = get_args()
    asyncio.run(GenerateFakeUsers(length, first_id).main())
