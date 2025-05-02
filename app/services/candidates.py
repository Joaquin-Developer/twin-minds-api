from typing import List, Any

from app.models.user import User
from app.models.candidates import Candidate
from app.services.compatibilities import COMPATIBILITIES_MYERS_BRIGGS_DATA
from app.services.users import UsersService


class CandidatesService:
    def __init__(self, user_id: int = None, user: User = None):
        self.users_service = UsersService()
        self.user = user if user else self.users_service.get_user_by_id(user_id)

    def get_personality_match_by_level(self, level: str) -> List[str]:
        """
        Level: (excellent, good, neutral, bad)
        """
        return COMPATIBILITIES_MYERS_BRIGGS_DATA[level][self.user.personality]

    async def get_candidates_db(self):
        # TODO: Filter in bd by location and age range.
        data = await self.users_service.get_all_users()
        return [
            Candidate(
                score=0,
                name=user.name,
                age=user.age,
                personality=user.personality,
                interests=user.interests,
            )
            for user in data
            if user.id != self.user.id
        ]

    def calculate_mbty_personality(self, candidates: List[Candidate]) -> List[Candidate]:
        filtered_candidates: List[Candidate] = []

        excellent = self.get_personality_match_by_level("excellent")
        good = self.get_personality_match_by_level("good")
        neutral = self.get_personality_match_by_level("neutral")
        # bad = self.get_personality_match_by_level("bad")

        aceptable = excellent + good + neutral

        for candidate in candidates:
            if candidate.personality in excellent:
                candidate.score += 70

            if candidate.personality in good:
                candidate.score += 50

            if candidate.personality in neutral:
                candidate.score += 35

            if candidate.personality in aceptable:
                filtered_candidates.append(candidate)

        return filtered_candidates

    def calculate_interests_personality(self, candidates: List[Candidate]):
        """
        Si coinciden todos los intereses → 30 puntos.
        Si coinciden mitad de los intereses → 15 puntos.
        Si coinciden 1 de 5 intereses → 6 puntos, etc.
        """
        user_interests = set(self.user.interests)
        total_user_interests = len(user_interests)

        for candidate in candidates:
            score = 0
            interests = set(candidate.interests)

            common_interests = user_interests & interests
            match_ratio = len(common_interests) / total_user_interests
            score = int(match_ratio * 30)

            candidate.score += score

    async def generate(self) -> List[Candidate]:
        all_candidates = await self.get_candidates_db()
        candidates = self.calculate_mbty_personality(all_candidates)
        self.calculate_interests_personality(candidates)

        candidates.sort(key=lambda candidate: candidate.score, reverse=True)

        return candidates
