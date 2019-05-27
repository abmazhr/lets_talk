from typing import Dict, Any, Union

from flask_socketio import SocketIOTestClient

from src.application.infrastructure.persistent.in_memory import InMemoryOnlineUsersPersistent
from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.io import get_io
from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.http_client import HttpClient, Response


class FakeHttpClient(HttpClient):
    def __init__(self, *, configs: Dict[str, Any] = None) -> None:
        super().__init__(configs=configs)
        self.__configs = configs

    def post(self, *, url: str, data: Dict[str, Any]) -> Union[Error, Response]:
        return self.__configs['result']


def test_valid_connection():
    http_client = FakeHttpClient(configs={'result': Success(data={'valid': True})})
    online_user_persistent = InMemoryOnlineUsersPersistent()

    check_user_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)
    add_online_user_usecase = AddOnlineUserUseCase(online_user_persistent=online_user_persistent)
    remove_online_user_usecase = RemoveOnlineUserUseCase(online_user_persistent=online_user_persistent)

    api, io = get_io(
        check_user_creds_usecase=check_user_creds_usecase,
        add_online_user_usecase=add_online_user_usecase,
        remove_online_user_usecase=remove_online_user_usecase
    )
    client = SocketIOTestClient(app=api, socketio=io, headers={'username': 'fake', 'password': 'fake'})

    assert client.is_connected() is True


def test_invalid_connection():
    http_client = FakeHttpClient(configs={'result': Success(data={'valid': False})})
    online_user_persistent = InMemoryOnlineUsersPersistent()

    check_user_creds_usecase = CheckUserCredentialsUseCase(http_client=http_client)
    add_online_user_usecase = AddOnlineUserUseCase(online_user_persistent=online_user_persistent)
    remove_online_user_usecase = RemoveOnlineUserUseCase(online_user_persistent=online_user_persistent)

    api, io = get_io(
        check_user_creds_usecase=check_user_creds_usecase,
        add_online_user_usecase=add_online_user_usecase,
        remove_online_user_usecase=remove_online_user_usecase
    )

    client = SocketIOTestClient(app=api, socketio=io, headers={'username': 'fake', 'password': 'fake'})
    assert client.is_connected() is False

    client = SocketIOTestClient(app=api, socketio=io, headers={})
    assert client.is_connected() is False

    client = SocketIOTestClient(app=api, socketio=io, headers={'username': '', 'password': 'fake'})
    assert client.is_connected() is False

    client = SocketIOTestClient(app=api, socketio=io, headers={'username': 'fake', 'password': ''})
    assert client.is_connected() is False
