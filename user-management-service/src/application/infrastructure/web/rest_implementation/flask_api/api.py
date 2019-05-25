from flask import Flask, request

from src.application.infrastructure.web.rest_implementation.flask_api.user.post import PostUser
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase


def get_api(*,
            create_user_usecase: CreateUserUseCase,
            check_user_credentials_usecase: CheckUserCredentialsUseCase) -> Flask:
    api = Flask(__name__)

    # register (maybe we will do it better later so it doesn't be messy right? :D
    api.add_url_rule(
        '/',
        'health_check',
        lambda: 'Healthy', 200,
        methods=['GET']
    )
    api.add_url_rule(
        '/users',
        'register_user',
        lambda: PostUser(create_user_usecase=create_user_usecase).register_user(
            data=request.json
        ),
        methods=['POST']
    )
    api.add_url_rule(
        '/users/check_credentials',
        'check_user_credentials',
        lambda: PostUser(check_user_credentials_usecase=check_user_credentials_usecase).check_user_credentials(
            data=request.json
        ),
        methods=['POST']
    )

    return api
