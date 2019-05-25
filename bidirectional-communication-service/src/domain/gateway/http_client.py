from abc import ABCMeta, abstractmethod
from typing import Dict, Any, NamedTuple


class Response(NamedTuple):
    data: Dict[str, Any]
    status: int


class HttpClient(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, configs: Dict[str, Any]) -> None: pass

    @abstractmethod
    def post(self, *, url: str, data: Dict[str, Any]) -> Response: pass
