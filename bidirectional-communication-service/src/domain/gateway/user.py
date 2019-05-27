from abc import ABCMeta, abstractmethod
from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence
from src.domain.gateway.http_client import HttpClient
from src.domain.gateway.online_users_persistent import OnlineUsersPersistent


class CheckUserCredentials(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, http_client: HttpClient) -> None: pass

    @abstractmethod
    def execute(self, *, url: str, username: str, password: str) -> Union[Error, Success]: pass


class AddOnlineUser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, online_user_persistent: OnlineUsersPersistent) -> None: pass

    @abstractmethod
    def execute(self, *, user_persistence: UserPersistence) -> Union[Error, Success]: pass


class RemoveOnlineUser(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, online_user_persistent: OnlineUsersPersistent) -> None: pass

    @abstractmethod
    def execute(self, *, username: str) -> Union[Error, Success]: pass
