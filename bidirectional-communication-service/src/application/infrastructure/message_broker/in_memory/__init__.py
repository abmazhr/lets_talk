from queue import Queue
from typing import Dict, Any, Union as Either

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.message_broker import MessageBroker


class InMemoryMessageBroker(MessageBroker):
    def __init__(self, *, configs: Dict[str, Any] = None) -> None:
        super().__init__(configs=configs)
        self.__broker = Queue()  # in memory ;)

    def publish_message(self, *, topic: str, message: Dict[str, Any]) -> Either[Error, Success]:
        # since this is in-memory so no need th e  topic :)
        self.__broker.put(item=message)
        return Success(data=None)
