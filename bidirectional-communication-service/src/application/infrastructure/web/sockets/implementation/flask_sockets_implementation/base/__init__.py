from flask import request
from flask_socketio import send, disconnect

from src.application.infrastructure.web.sockets.gateway.base import BaseSockets
from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase
from src.configs import CHECK_USER_CREDENTIALS_ROUTE
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence


class FlaskBaseSockets(BaseSockets):
    def __init__(self, *, check_user_creds_usecase: CheckUserCredentialsUseCase,
                 add_online_user_usecase: AddOnlineUserUseCase,
                 remove_online_user_usecase: RemoveOnlineUserUseCase) -> None:
        super().__init__(check_user_creds_usecase=check_user_creds_usecase,
                         add_online_user_usecase=add_online_user_usecase,
                         remove_online_user_usecase=remove_online_user_usecase)
        self.__check_user_creds_usecase = check_user_creds_usecase
        self.__add_online_user_usecase = add_online_user_usecase
        self.__remove_online_user_usecase = remove_online_user_usecase

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
                adding_online_user_result = self.__add_online_user_usecase.execute(
                    user_persistence=UserPersistence(username=username, socket_id=sid)
                )
                if isinstance(adding_online_user_result, Error):
                    msg = adding_online_user_result.reason
                    send(msg)
                    disconnect(sid=sid)

                if isinstance(adding_online_user_result, Success):
                    msg = f'{sid}:: Connected successfully !'
                    print(msg)
                    send(msg)
        else:
            msg = f'Invalid credentials data'
            send(msg)
            disconnect(sid=sid)

    def on_disconnect(self, *args, **kwargs) -> None:
        sid = request.sid
        removing_online_user_result = self.__remove_online_user_usecase.execute(
            socket_id=sid
        )
        if isinstance(removing_online_user_result, Error):
            msg = removing_online_user_result.reason
            print(f"{sid} :: Disconnected with error,\n{msg}")
            disconnect(sid=sid)
        if isinstance(removing_online_user_result, Success):
            msg = f'{sid} :: Disconnected successfully !'
            print(msg)
            disconnect(sid=sid)
