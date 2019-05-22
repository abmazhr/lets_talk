from typing import NamedTuple, Optional


class User(NamedTuple):
    id: Optional[str]
    name: str  # unique for now
    password: str
    age: int
    email: Optional[str]
