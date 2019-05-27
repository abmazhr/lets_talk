from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.online_users_persistent import OnlineUsersPersistent
from src.domain.gateway.user import RemoveOnlineUser


class RemoveOnlineUserUseCase(RemoveOnlineUser):
    def __init__(self, *, online_user_persistent: OnlineUsersPersistent) -> None:
        super().__init__(online_user_persistent=online_user_persistent)
        self.__online_user_persistent = online_user_persistent

    def execute(self, *, socket_id: str) -> Union[Error, Success]:
        return self.__online_user_persistent.remove_online_user(socket_id=socket_id)
