from typing import Tuple

from flask import Flask
from flask_socketio import SocketIO

from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.base import FlaskBaseSockets
from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.message import \
    FlaskMessageSockets
from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.publish_online_user import PublishOnlineUserUseCase
from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase


def get_io(*,
           check_user_creds_usecase: CheckUserCredentialsUseCase,
           add_online_user_usecase: AddOnlineUserUseCase,
           remove_online_user_usecase: RemoveOnlineUserUseCase,
           publish_online_user_usecase: PublishOnlineUserUseCase) -> Tuple[Flask, SocketIO]:
    api = Flask(__name__)
    io = SocketIO(api)

    # dependencies
    flask_base_sockets = FlaskBaseSockets(
        check_user_creds_usecase=check_user_creds_usecase,
        add_online_user_usecase=add_online_user_usecase,
        remove_online_user_usecase=remove_online_user_usecase,
        publish_online_user_usecase=publish_online_user_usecase
    )

    # register (maybe we will do it better later so it doesn't be messy right? :D
    io.on_event('connect', flask_base_sockets.on_connect)
    io.on_event('disconnect', flask_base_sockets.on_disconnect)
    io.on_event('message', FlaskMessageSockets().on_message)

    return api, io
