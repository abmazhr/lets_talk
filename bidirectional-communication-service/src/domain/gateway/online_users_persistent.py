from abc import ABCMeta, abstractmethod
from typing import Dict, Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence


class OnlineUsersPersistent(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, configs: Dict[str, str] = None) -> None: pass

    @abstractmethod
    def save_online_user(self, *, user_persistence: UserPersistence) -> Union[Error, Success]: pass

    @abstractmethod
    def remove_online_user(self, *, socket_id: str) -> Union[Error, Success]: pass

    @abstractmethod
    def _validate_user_persistent_data(self, *, user_persistent: UserPersistence) -> Union[Error, Success]: pass
