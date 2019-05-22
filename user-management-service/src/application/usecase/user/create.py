from typing import Union, Any, Dict

from dpcontracts import ensure

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User
from src.domain.gateway.user import CreateUser
from src.domain.gateway.user_database_repository import UserDatabaseRepository


class CreateUserUseCase(CreateUser):
    def __init__(self, db_repository: UserDatabaseRepository) -> None:
        super().__init__(db_repository=db_repository)
        self.__db_repository = db_repository

    @ensure('return type should be Error or User',
            lambda args, result: isinstance(result, Error) or isinstance(result, User))
    def execute(self, *, data: Dict[str, Any]) -> Union[Error, User]:
        validated = self.__validate_data(data=data)
        if isinstance(validated, Error):
            return validated

        saved = self.__db_repository.save_user(user=User(
            id=None,
            name=data['name'],
            password=data['password'],
            age=data['age'],
            email=data.get('email', '')
        ))
        if isinstance(saved, Error):
            return saved

        return saved.data

    def __validate_data(self, *, data: Dict[str, Any]) -> Union[Error, Success]:
        # simple validation, may be replaced with json validator later :)
        if data.get('name', None) is None:
            return Error(reason="Not valid name")
        if data.get('name', '') == '':
            return Error(reason="Not valid name")
        if data.get('password', '') == '':
            return Error(reason="Not valid password")
        try:
            if int(data.get('age', -1)) == -1 or int(data.get('age', -1)) < 18:  # 18 for adult :D
                return Error(reason="Not valid age")
        except ValueError:
            return Error(reason="Not valid age type")
        # maybe later should validate email as well properly, now we will take it as it is even none

        return Success(data=None)
