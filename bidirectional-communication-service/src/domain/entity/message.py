import enum
from typing import NamedTuple


class MessageType(enum):
    TEXT = 0


class Message(NamedTuple):
    message: str
    messageType: MessageType
    fromSocketId: str
    toSocketId: str
