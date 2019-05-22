from abc import ABCMeta, abstractmethod
from typing import Union, Tuple, Dict, Any, NamedTuple

from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.user import User


class UserJson(NamedTuple):
    userId: str
    userName: str
    userAge: int
    userEmail: str
    url: str

    @staticmethod
    def from_user(*, user: User) -> 'UserJson':
        return UserJson(
            userId=user.id,
            userName=user.name,
            userAge=user.age,
            userEmail=user.email,
            url=f"/users/{user.id}"
        )


Status = int
PostResponse = Union[Tuple[Error, Status], Tuple[UserJson, Status]]


class UserRestApiGateway:
    class Post(metaclass=ABCMeta):
        @abstractmethod
        def __init__(self, *, create_user_usecase: CreateUserUseCase) -> None: pass

        @abstractmethod
        def send_request(self, *, data: Dict[str, Any]) -> PostResponse: pass
