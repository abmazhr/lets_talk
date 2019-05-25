from abc import ABCMeta, abstractmethod
from typing import Union

from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.gateway.http_client import HttpClient


class CheckUserCredentials(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, http_client: HttpClient) -> None: pass

    @abstractmethod
    def execute(self, *, url: str, username: str, password: str) -> Union[Error, Success]: pass
