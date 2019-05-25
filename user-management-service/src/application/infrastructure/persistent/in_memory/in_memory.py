from typing import Union, Dict, Optional
from uuid import uuid4

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User
from src.domain.gateway.user_database_repository import UserDatabaseRepository


class InMemoryUserDatabaseRepository(UserDatabaseRepository):
    def __init__(self, *, configs: Dict[str, str] = None) -> None:
        super().__init__(configs=configs)
        self.__configs = configs
        self.__db = {}  # in-memory right? :D

    def save_user(self, *, user: User) -> Union[Error, Success]:
        if self.__does_exist_before(user=user):
            return Error(reason=f'This username {user.name} does exist before, use different username please.')

        user = User(
            id=uuid4().hex,
            name=user.name,
            password=user.password,
            age=user.age,
            email=user.email
        )
        self.__db[user.name] = user
        return Success(data=user)

    def check_user_credentials(self, *, username: str, password: str) -> Union[Error, Success]:
        db_user: Optional[User] = self.__db.get(username, None)
        if db_user is not None:
            db_password = db_user.password
            if password == db_password:
                return Success(data=f"This user's '{username}' credentials are valid")

            return Error(reason=f"This user's '{username}' credentials are not valid")

        return Error(reason=f"User with username '{username}' does not exist")

    def __does_exist_before(self, *, user: User) -> bool:
        return self.__db.get(user.name, None) is not None
