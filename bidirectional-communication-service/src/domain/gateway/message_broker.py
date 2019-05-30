from abc import ABCMeta, abstractmethod
from typing import Dict, Any
from typing import Union as Either

from src.domain.entity.error import Error
from src.domain.entity.success import Success


class MessageBroker(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, configs: Dict[str, Any]) -> None: pass

    @abstractmethod
    def publish_message(self, *, topic: str, message: Dict[str, Any]) -> Either[Error, Success]: pass
