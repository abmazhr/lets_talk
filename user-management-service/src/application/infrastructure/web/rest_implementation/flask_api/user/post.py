from typing import Dict, Any

from flask import jsonify

from src.application.infrastructure.web.rest_gateway.user_rest_gateway import UserRestApiGateway, PostResponse, UserJson
from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.user import User


class PostUser(UserRestApiGateway.Post):
    def __init__(self, *, create_user_usecase: CreateUserUseCase) -> None:
        super().__init__(create_user_usecase=create_user_usecase)
        self.__usecase = create_user_usecase

    def send_request(self, *, data: Dict[str, Any]) -> PostResponse:
        result = self.__usecase.execute(
            data=data
        )
        if isinstance(result, Error):
            return jsonify(result._asdict()), 400

        if isinstance(result, User):
            return jsonify(UserJson.from_user(user=result)._asdict()), 200
