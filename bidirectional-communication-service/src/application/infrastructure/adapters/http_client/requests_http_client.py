from typing import Dict, Any, Union

import requests

from src.domain.entity.error import Error
from src.domain.gateway.http_client import HttpClient, Response


class RequestsHttpClient(HttpClient):
    def __init__(self, *, configs: Dict[str, Any] = None) -> None:
        super().__init__(configs=configs)
        self.__http_client = requests.session()

    def post(self, *, url: str, data: Dict[str, Any]) -> Union[Error, Response]:
        try:
            response = self.__http_client.post(
                url=url,
                json=data,
                timeout=3
            )
            return Response(data=response.json() or dict(), status=response.status_code)
        except:
            return Error(reason=f"Error posting request to url '{url}'")
