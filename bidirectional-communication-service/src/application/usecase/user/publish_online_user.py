from typing import Union as Either, Dict, Any

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.message_broker import MessageBroker


class PublishOnlineUserUseCase:
    def __init__(self, *, message_broker: MessageBroker) -> None:
        self.__broker = message_broker

    def execute(self, *, topic: str, message: Dict[str, Any]) -> Either[Error, Success]:
        return self.__broker.publish_message(
            topic=topic,
            message=message
        )
