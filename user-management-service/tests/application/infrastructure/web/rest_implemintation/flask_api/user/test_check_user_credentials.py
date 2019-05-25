from typing import Dict, Any

import pytest

from src.application.infrastructure.persistent.in_memory.in_memory import InMemoryUserDatabaseRepository
from src.application.infrastructure.web.rest_implementation.flask_api.api import get_api
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase


@pytest.fixture(scope='module')
def api():
    db_repository = InMemoryUserDatabaseRepository()
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)
    check_user_credentials_usecase = CheckUserCredentialsUseCase(db_repository=db_repository)
    api = get_api(
        create_user_usecase=create_user_usecase,
        check_user_credentials_usecase=check_user_credentials_usecase
    )

    yield api


def test_valid_post_user(api):
    register_user_data = {'name': 'Abdulrahman', 'age': 25, 'password': 'test', 'email': 'abmazhr@gmail.com'}
    check_credentials_data = {'username': 'Abdulrahman', 'password': 'test'}

    with api.test_client() as client:
        _registration_response = client.post('/users', json=register_user_data)
        check_credentials_response = client.post('/users/check_credentials', json=check_credentials_data)
        json_data: Dict[str, Any] = check_credentials_response.get_json()

        assert json_data['valid'] == True
        assert check_credentials_response.status_code == 202


def test_invalid_post_user(api):
    register_user_data = {'name': 'Abdulrahman', 'age': 25, 'password': 'test', 'email': 'abmazhr@gmail.com'}
    check_credentials_data = {'username': 'Abdulrahman', 'password': 'invalid'}

    with api.test_client() as client:
        _registration_response = client.post('/users', json=register_user_data)
        check_credentials_response = client.post('/users/check_credentials', json=check_credentials_data)
        json_data: Dict[str, Any] = check_credentials_response.get_json()

        assert json_data['valid'] == False
        assert check_credentials_response.status_code == 400
