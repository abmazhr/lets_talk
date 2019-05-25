from abc import ABCMeta, abstractmethod
from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.message import Message
from src.domain.entity.success import Success


class SendMessage(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *, message: Message) -> Union[Error, Success]: pass
