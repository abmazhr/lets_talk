import pytest

from src.application.infrastructure.persistent.in_memory.in_memory import InMemoryUserDatabaseRepository
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success


@pytest.fixture(scope='function')
def usecases():
    db_repository = InMemoryUserDatabaseRepository()
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)
    check_user_creds_usecase = CheckUserCredentialsUseCase(db_repository=db_repository)

    yield create_user_usecase, check_user_creds_usecase


def test_valid_user_credentials(usecases):
    create_user_usecase, check_user_creds_usecase = usecases

    data = dict(name="Abdulrahman", password='test', age=25)
    _created_user = create_user_usecase.execute(data=data)
    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': data['name'], 'password': data['password']}
    )

    assert isinstance(retrieved_check_creds, Success)


def test_invalid_user_credentials(usecases):
    create_user_usecase, check_user_creds_usecase = usecases

    data = dict(name="abdulrahman", password='test', age=25)
    _created_user = create_user_usecase.execute(data=data)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'password': 'invalid'}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': '', 'password': 'invalid'}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': 'abdulrahman', 'password': ''}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': 'invalid', 'password': 'test'}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': 'abdulrahman', 'password': 'invalid'}
    )
    assert isinstance(retrieved_check_creds, Error)

    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': 'abdulrahman', 'password': 'invalid'}
    )
    assert isinstance(retrieved_check_creds, Error)
