from typing import List, Any

from app.models.user import User
from app.services.compatibilities import COMPATIBILITIES_MYERS_BRIGGS_DATA
from app.services.users import UsersService


class CandidatesService:
    def __init__(self, user_id: int = None, user: User = None):
        self.user = user if user else UsersService.get_user_by_id(user_id)

    def get_personality_match(self) -> List[str]:
        """
        Returns List of personality matches, order by level (excellent, good or neutral) 
        """
        personality = self.user.personality
        return (
            COMPATIBILITIES_MYERS_BRIGGS_DATA["excellent"][personality]
            + COMPATIBILITIES_MYERS_BRIGGS_DATA["good"][personality]
            + COMPATIBILITIES_MYERS_BRIGGS_DATA["neutral"][personality]
        )

    def calculate_mbty_personality(self):
        pass

    def calculate_interests_personality(self):
        pass

    def generate(self) -> List[Any]:
        pass
