from typing import Dict, Any, Union

from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.http_client import HttpClient, Response


class FakeHttpClient(HttpClient):
    def __init__(self, *, configs: Dict[str, Any] = None) -> None:
        super().__init__(configs=configs)
        self.__configs = configs

    def post(self, *, url: str, data: Dict[str, Any]) -> Union[Error, Response]:
        return self.__configs['result']


def test_valid_user_credentials_check():
    url = 'fake'
    username = 'abdulrahman'
    password = 'test'

    http_client = FakeHttpClient(configs={'result': Success(data={'valid': True})})
    check_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)

    assert isinstance(check_creds_usecase.execute(
        url=url,
        username=username,
        password=password
    ), Success)


def test_invalid_user_credentials_check():
    url = 'fake'
    username = 'abdulrahman'
    password = 'invalid'

    http_client = FakeHttpClient(configs={'result': Success(data={'valid': False})})
    check_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)

    assert isinstance(check_creds_usecase.execute(
        url=url,
        username=username,
        password=password
    ), Error)

    http_client = FakeHttpClient(configs={'result': Error(reason='Network error? maybe? :D')})
    check_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)

    assert isinstance(check_creds_usecase.execute(
        url=url,
        username=username,
        password=password
    ), Error)

    assert isinstance(check_creds_usecase.execute(
        url='',
        username=username,
        password=password
    ), Error)
    assert isinstance(check_creds_usecase.execute(
        url=url,
        username='',
        password=password
    ), Error)
    assert isinstance(check_creds_usecase.execute(
        url=url,
        username=username,
        password=''
    ), Error)
