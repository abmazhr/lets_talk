import pytest

from src.application.infrastructure.persistent.in_memory.in_memory import InMemoryUserDatabaseRepository
from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from tests.application.usecase.user.helper import from_dict_to_user


@pytest.fixture(scope='function')
def create_user_usecase():
    db_repository = InMemoryUserDatabaseRepository()
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)

    yield create_user_usecase


def test_valid_create_user(create_user_usecase):
    data = dict(name="Abdulrahman", password='test', age=25)
    created_user = create_user_usecase.execute(data=data)
    testing_user = from_dict_to_user(data=data)

    assert created_user.id is not None
    assert created_user.name == testing_user.name
    assert created_user.password == testing_user.password
    assert created_user.age == testing_user.age
    assert created_user.email == testing_user.email


def test_invalid_create_user(create_user_usecase):
    data = dict()
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid data')

    data = dict(password='test', age=25)
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid name')

    data = dict(name="", password='test', age=25)
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid name')

    data = dict(name="Abdulrahman", password='test', age=10)
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid age')

    data = dict(name="Abdulrahman", password='test', age="s10")
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid age type')

    data = dict(name="Abdulrahman", password='', age=25)
    created_user = create_user_usecase.execute(data=data)
    assert created_user == Error(reason='Not valid password')


def test_invalid_create_user_exists_before(create_user_usecase):
    data = dict(name="Abdulrahman", password='test', age=25)
    _created_user = create_user_usecase.execute(data=data)
    created_again_user = create_user_usecase.execute(data=data)

    assert created_again_user == Error(
        f'This username {data["name"]} does exist before, use different username please.')
