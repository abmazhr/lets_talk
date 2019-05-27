from typing import Union, Dict

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence
from src.domain.gateway.online_users_persistent import OnlineUsersPersistent


class InMemoryOnlineUsersPersistent(OnlineUsersPersistent):
    def __init__(self, *, configs: Dict[str, str] = None) -> None:
        super().__init__(configs=configs)
        self.__db = {}  # in memory ;)

    def save_online_user(self, *, user_persistence: UserPersistence) -> Union[Error, Success]:
        if isinstance(self._validate_user_persistent_data(user_persistent=user_persistence), Success):
            db_user = self.__db.get(user_persistence.socket_id, None)
            if db_user is not None:
                return Error(
                    reason=f'This user with socket_id "{user_persistence.socket_id}" does exist already as an online user'
                )

            self.__db[user_persistence.socket_id] = user_persistence
            return Success(data=None)

        return Error(reason='Invalid user persistent data')

    def remove_online_user(self, *, socket_id: str) -> Union[Error, Success]:
        db_user = self.__db.get(socket_id, None)
        if db_user is not None:
            del self.__db[socket_id]
            return Success(data=None)

        return Error(reason=f"This username with socket_id '{socket_id}' does not exist as an online user")

    def _validate_user_persistent_data(self, *, user_persistent: UserPersistence) -> Union[Error, Success]:
        # simple validation of data for now
        if user_persistent:
            if user_persistent.username == '':
                return Error(reason='Invalid username')
            if user_persistent.socket_id == '':
                return Error(reason='Invalid socket_id')

            return Success(data=None)

        return Error(reason='Invalid user persistent data')
