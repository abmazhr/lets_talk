from abc import ABCMeta, abstractmethod
from typing import Dict, Any, NamedTuple, Union

from src.domain.entity.error import Error


class Response(NamedTuple):
    data: Dict[str, Any]
    status: int


class HttpClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, configs: Dict[str, Any] = None) -> None: pass

    @abstractmethod
    def post(self, *, url: str, data: Dict[str, Any]) -> Union[Error, Response]: pass
