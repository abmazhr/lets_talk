from typing import Dict, Any

from src.domain.entity.user import User


def from_dict_to_user(*, data: Dict[str, Any]) -> User:
    return User(
        id=None,
        name=data['name'],
        password=data['password'],
        age=data['age'],
        email=data.get('email', '')
    )
