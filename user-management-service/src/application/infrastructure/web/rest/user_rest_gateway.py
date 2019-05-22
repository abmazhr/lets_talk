from abc import ABCMeta, abstractmethod
from typing import Union, Tuple

from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.user import User

Status = int
PostResponse = Union[Tuple[Error, Status], Tuple[User, Status]]


class UserRestApiGateway(metaclass=ABCMeta):
    @abstractmethod
    def post_user(self, *, create_user_usecase: CreateUserUseCase) -> PostResponse: pass
