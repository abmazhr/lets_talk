from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.http_client import HttpClient
from src.domain.gateway.user import CheckUserCredentials


class CheckUserCredentialsUseCase(CheckUserCredentials):
    def __init__(self, *, http_client: HttpClient) -> None:
        super().__init__(http_client=http_client)
        self.__http_client = http_client

    def execute(self, *, url: str, username: str, password: str) -> Union[Error, Success]:
        validation_result = self.__validate_data(url=url, username=username, password=password)
        if isinstance(validation_result, Error):
            return validation_result

        check_validation_result = self.__http_client.post(
            url=url,
            data={'username': username, 'password': password}
        )
        if isinstance(check_validation_result, Error):
            return check_validation_result

        if check_validation_result.data is not None and check_validation_result.data.get('valid', False):
            return Success(data=None)

        return Error(reason=f'Invalid credentials for user "{username}"')

    def __validate_data(self, *, url: str, username: str, password: str) -> Union[Error, Success]:
        # simple validation of data and should be enhanced later ;)
        if url == '':
            return Error(reason='Invalid url')
        if username == '':
            return Error(reason='Invalid username')
        if password == '':
            return Error(reason='Invalid password')
        return Success(data=None)
