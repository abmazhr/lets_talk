from abc import ABCMeta, abstractmethod
from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.user_database_repository import DatabaseRepository


class CreateUser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, db_repository: DatabaseRepository) -> None: pass

    @abstractmethod
    def execute(self) -> Union[Error, Success]: pass
