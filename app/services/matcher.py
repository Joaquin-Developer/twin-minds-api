from typing import List


COMPATIBILITIES_MYERS_BRIGGS_DATA = {
  "excellent": {
    "INTJ": ["ENFP", "INFP"],
    "INTP": ["ENTP", "ENFP"],
    "ENTJ": ["INFP", "INTP"],
    "ENTP": ["INFJ", "INFP"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFP", "INFJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ISFJ"],
    "ISFJ": ["ESFP", "ISTJ"],
    "ESTJ": ["ISFJ", "ESFJ"],
    "ESFJ": ["ISFP", "ESFP"],
    "ISTP": ["ESFP", "ISFP"],
    "ISFP": ["ESFP", "INFP"],
    "ESTP": ["ISFP", "ISTP"],
    "ESFP": ["ISFP", "ESFJ"]
  },
  "good": {
    "INTJ": ["ENTP", "INFJ"],
    "INTP": ["INTJ", "INFJ"],
    "ENTJ": ["ENFP", "ENTP"],
    "ENTP": ["INTP", "ENFP"],
    "INFJ": ["INFP", "INTJ"],
    "INFP": ["INTJ", "ENFP"],
    "ENFJ": ["INFJ", "INFP"],
    "ENFP": ["INFP", "ENTP"],
    "ISTJ": ["ISFJ", "ESTJ"],
    "ISFJ": ["ISTJ", "ESFJ"],
    "ESTJ": ["ISTJ", "ESFJ"],
    "ESFJ": ["ISFJ", "ESTJ"],
    "ISTP": ["ESTP", "ISFP"],
    "ISFP": ["ISTP", "ESFP"],
    "ESTP": ["ISTP", "ESFP"],
    "ESFP": ["ISFP", "ESTP"]
  },
  "neutral": {
    "INTJ": ["ISTJ", "ISFJ"],
    "INTP": ["ISTP", "ISFP"],
    "ENTJ": ["ESTJ", "ENTP"],
    "ENTP": ["ENTJ", "ENFJ"],
    "INFJ": ["ISFJ", "INFP"],
    "INFP": ["INFJ", "ISFP"],
    "ENFJ": ["ESFJ", "ENFP"],
    "ENFP": ["ENFJ", "ISFP"],
    "ISTJ": ["INTJ", "ISFJ"],
    "ISFJ": ["ISTJ", "INTJ"],
    "ESTJ": ["ENTJ", "ESFJ"],
    "ESFJ": ["ENFJ", "ESTJ"],
    "ISTP": ["INTP", "ISFP"],
    "ISFP": ["ISTP", "INFP"],
    "ESTP": ["ENTP", "ESFP"],
    "ESFP": ["ENFP", "ESTP"]
  },
  "bad": {
    "INTJ": ["ESTJ", "ESFJ"],
    "INTP": ["ESTP", "ESFP"],
    "ENTJ": ["ISTJ", "ISFJ"],
    "ENTP": ["ISTP", "ISFP"],
    "INFJ": ["ESTJ", "ESFJ"],
    "INFP": ["ESTP", "ESFP"],
    "ENFJ": ["ISTJ", "ESTJ"],
    "ENFP": ["ISTP", "ESTP"],
    "ISTJ": ["ENTJ", "ENFJ"],
    "ISFJ": ["ENTJ", "ENFJ"],
    "ESTJ": ["INTJ", "INFJ"],
    "ESFJ": ["INTJ", "INFJ"],
    "ISTP": ["ENTP", "ENFP"],
    "ISFP": ["ENTP", "ENFP"],
    "ESTP": ["INTP", "INFP"],
    "ESFP": ["INTP", "INFP"]
  }
}


def get_personality_match(user_type: str, comp_type) -> List[str]:
    return COMPATIBILITIES_MYERS_BRIGGS_DATA[comp_type][user_type]


class MatchesService:
    ...
