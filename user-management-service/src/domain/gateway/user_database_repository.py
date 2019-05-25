from abc import ABCMeta, abstractmethod
from typing import Dict, Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User


class UserDatabaseRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, configs: Dict[str, str] = None) -> None: pass

    @abstractmethod
    def save_user(self, *, user: User) -> Union[Error, Success]: pass

    @abstractmethod
    def check_user_credentials(self, *, username: str, password: str) -> Union[Error, Success]: pass
