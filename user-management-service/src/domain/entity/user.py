from typing import NamedTuple, Optional


class User(NamedTuple):
    id: str
    name: str
    password: str
    age: int
    email: Optional[str]
