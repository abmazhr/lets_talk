from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence
from src.domain.gateway.online_users_persistent import OnlineUsersPersistent
from src.domain.gateway.user import AddOnlineUser


class AddOnlineUserUseCase(AddOnlineUser):
    def __init__(self, *, online_user_persistent: OnlineUsersPersistent) -> None:
        super().__init__(online_user_persistent=online_user_persistent)
        self.__online_user_persistent = online_user_persistent

    def execute(self, *, user_persistence: UserPersistence) -> Union[Error, Success]:
        return self.__online_user_persistent.save_online_user(user_persistence=user_persistence)
