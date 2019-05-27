from flask import request
from flask_socketio import send, disconnect

from src.application.infrastructure.web.sockets.gateway.base import BaseSockets
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.configs import CHECK_USER_CREDENTIALS_ROUTE
from src.domain.entity.error import Error
from src.domain.entity.success import Success


class FlaskBaseSockets(BaseSockets):
    def __init__(self, *, check_user_creds_usecase: CheckUserCredentialsUseCase) -> None:
        super().__init__(check_user_creds_usecase=check_user_creds_usecase)
        self.__check_user_creds_usecase = check_user_creds_usecase

    def on_connect(self, *args, **kwargs) -> None:
        sid = request.sid
        username = request.headers.get('username', None)
        password = request.headers.get('password', None)
        if username is not None and password is not None:
            check_creds_result = self.__check_user_creds_usecase.execute(
                url=CHECK_USER_CREDENTIALS_ROUTE,
                username=username,
                password=password
            )
            if isinstance(check_creds_result, Error):
                msg = f'Invalid credentials for user "{username}"'
                print(msg)
                send(msg)
                disconnect(sid=sid)

            if isinstance(check_creds_result, Success):
                msg = f'{sid}:: Connected successfully !'
                print(msg)
                send(msg)
        else:
            msg = f'Invalid credentials data'
            send(msg)
            disconnect(sid=sid)

    def on_disconnect(self, *args, **kwargs) -> None:
        sid = request.sid
        print(f'{sid} :: Disconnected successfully !')
