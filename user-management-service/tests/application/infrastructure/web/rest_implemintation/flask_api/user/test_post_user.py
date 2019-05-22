from typing import Dict, Any

import pytest

from src.application.infrastructure.persistent.in_memory.in_memory import InMemoryUserDatabaseRepository
from src.application.infrastructure.web.rest_implementation.flask_api.api import get_api
from src.application.usecase.user.create import CreateUserUseCase


@pytest.fixture(scope='module')
def api():
    db_repository = InMemoryUserDatabaseRepository()
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)
    api = get_api(create_user_usecase=create_user_usecase)

    yield api


def test_valid_post_user(api):
    data = {'name': 'Abdulrahman', 'age': 25, 'password': 'test', 'email': 'abmazhr@gmail.com'}

    with api.test_client() as client:
        response = client.post('/users', json=data)
        json_data: Dict[str, Any] = response.get_json()

        assert json_data['userName'] == data['name']
        assert json_data['userAge'] == data['age']
        assert json_data['userEmail'] == data['email']
        assert json_data['userId'] is not None


def test_invalid_post_user(api):
    data = {'name': 'Abdulrahman', 'password': 'test', 'age': -1}  # age should be > 18 in our business logic ;)

    with api.test_client() as client:
        response = client.post('/users', json=data)
        json_data: Dict[str, Any] = response.get_json()

        assert json_data['reason'] == "Not valid age"
