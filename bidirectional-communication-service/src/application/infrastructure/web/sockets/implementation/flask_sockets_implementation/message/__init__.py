from flask import request
from flask_socketio import emit

from src.application.infrastructure.web.sockets.gateway.message import MessageSockets
from src.domain.entity.message import Message


class FlaskMessageSockets(MessageSockets):
    def on_message(self, *args, **kwargs) -> None:
        _sid = request.sid
        message: Message = args[0]

        emit('all', message, broadcast=True)
