from typing import Tuple

from flask import Flask
from flask_socketio import SocketIO

from src.application.infrastructure.web.sockets.implementation.flask_sockets_implementation.base import FlaskBaseSockets
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase


def get_io(*, check_user_creds_usecase: CheckUserCredentialsUseCase) -> Tuple[Flask, SocketIO]:
    api = Flask(__name__)
    io = SocketIO(api)

    # register (maybe we will do it better later so it doesn't be messy right? :D
    io.on_event('connect', FlaskBaseSockets(check_user_creds_usecase=check_user_creds_usecase).on_connect)
    io.on_event('disconnect', FlaskBaseSockets(check_user_creds_usecase=check_user_creds_usecase).on_disconnect)

    return api, io
