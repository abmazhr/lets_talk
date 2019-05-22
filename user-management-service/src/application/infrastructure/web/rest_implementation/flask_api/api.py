from flask import Flask, request

from src.application.infrastructure.web.rest_implementation.flask_api.user.post import PostUser
from src.application.usecase.user.create import CreateUserUseCase


def get_api(create_user_usecase: CreateUserUseCase) -> Flask:
    api = Flask(__name__)

    # register
    api.add_url_rule(
        '/',
        'health_check',
        lambda: 'Healthy', 200,
        methods=['GET']
    )
    api.add_url_rule(
        '/users',
        'post_user',
        lambda: PostUser(create_user_usecase=create_user_usecase).send_request(data=request.json),
        methods=['POST']
    )

    return api
