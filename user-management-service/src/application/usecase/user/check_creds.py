from typing import Dict, Any, Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.user import CheckUserCredentials
from src.domain.gateway.user_database_repository import UserDatabaseRepository


class CheckUserCredentialsUseCase(CheckUserCredentials):
    def __init__(self, *, db_repository: UserDatabaseRepository) -> None:
        super().__init__(db_repository=db_repository)
        self.__db_repository = db_repository

    def execute(self, *, data: Dict[str, Any]) -> Union[Error, Success]:
        validation_result = self.__validate_data(data=data)
        if isinstance(validation_result, Error):
            return validation_result

        return self.__db_repository.check_user_credentials(
            username=data['username'],
            password=data['password']
        )

    def __validate_data(self, *, data: Dict[str, Any]) -> Union[Error, Success]:
        # simple validation, may be replaced with json validator later :)
        if data:
            if data.get('username', None) is None:
                return Error(reason="username is required")
            if data.get('username', '') == '':
                return Error(reason="Not valid username")
            if data.get('password', '') == '':
                return Error(reason="Not valid password")

            return Success(data=None)
        else:
            return Error(reason="Not valid data")
