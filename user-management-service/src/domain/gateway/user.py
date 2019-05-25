from abc import ABCMeta, abstractmethod
from typing import Union, Any, Dict

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User
from src.domain.gateway.user_database_repository import UserDatabaseRepository


class CreateUser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, db_repository: UserDatabaseRepository) -> None: pass

    @abstractmethod
    def execute(self, *, data: Dict[str, Any]) -> Union[Error, User]: pass


class CheckUserCredentials(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, db_repository: UserDatabaseRepository) -> None: pass

    @abstractmethod
    def execute(self, *, data: Dict[str, Any]) -> Union[Error, Success]: pass
