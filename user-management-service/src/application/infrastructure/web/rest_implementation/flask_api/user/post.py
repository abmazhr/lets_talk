from typing import Dict, Any, Optional

from dpcontracts import require
from flask import jsonify

from src.application.infrastructure.web.rest_gateway.user_rest_gateway import UserRestApiGateway, \
    UserRegistrationResponse, UserJson, UserCheckCredentialsResponse, ValidityOfUserCredentials
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user import User


class PostUser(UserRestApiGateway.Post):
    def __init__(self, *, create_user_usecase: Optional[CreateUserUseCase] = None,
                 check_user_credentials_usecase: Optional[CheckUserCredentialsUseCase] = None) -> None:
        super().__init__(create_user_usecase=create_user_usecase,
                         check_user_credentials_usecase=check_user_credentials_usecase)
        self.__create_user_usecase = create_user_usecase
        self.__check_user_credentials_usecase = check_user_credentials_usecase

    def register_user(self, *, data: Dict[str, Any]) -> UserRegistrationResponse:
        require(
            "'create_user_usecase' is required here",
            lambda args: self.__create_user_usecase is not None
        )

        result = self.__create_user_usecase.execute(
            data=data
        )
        if isinstance(result, Error):
            return jsonify(result._asdict()), 400

        if isinstance(result, User):
            return jsonify(UserJson.from_user(user=result)._asdict()), 200

    def check_user_credentials(self, *, data: Dict[str, Any]) -> UserCheckCredentialsResponse:
        require(
            "'check_user_credentials_usecase' is required here",
            lambda args: self.__check_user_credentials_usecase is not None
        )

        result = self.__check_user_credentials_usecase.execute(
            data=data
        )
        if isinstance(result, Error):
            return jsonify(ValidityOfUserCredentials(valid=False)._asdict()), 400

        if isinstance(result, Success):
            return jsonify(ValidityOfUserCredentials(valid=True)._asdict()), 202
