from typing import NamedTuple

MessageType = str


class Message(NamedTuple):
    message: str
    messageType: MessageType
    fromSocketId: str
