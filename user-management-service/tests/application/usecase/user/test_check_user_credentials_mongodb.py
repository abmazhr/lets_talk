from uuid import uuid4

import pytest

from src.application.infrastructure.persistent.mongodb.mongodb import MongoUserDatabaseRepository
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.create import CreateUserUseCase
from src.configs import (
    SERVICE_RUNTIME,
    MONGODB_HOST,
    MONGODB_PORT
)
from src.domain.entity.error import Error
from src.domain.entity.success import Success

skip_or_not = pytest.mark.skipif(
    SERVICE_RUNTIME != 'container',
    reason="locally will be testing on in-memory-database simply for now"
)


@pytest.fixture(scope='function')
def usecases():
    db_repository = MongoUserDatabaseRepository(configs={
        'MONGODB_HOST': MONGODB_HOST,
        'MONGODB_PORT': MONGODB_PORT,
        'MONGODB_NAME': uuid4().hex
    })
    create_user_usecase = CreateUserUseCase(db_repository=db_repository)
    check_user_creds_usecase = CheckUserCredentialsUseCase(db_repository=db_repository)

    yield create_user_usecase, check_user_creds_usecase


@skip_or_not
def test_valid_user_credentials(usecases):
    create_user_usecase, check_user_creds_usecase = usecases

    data = dict(name="abdulrahman", password='test', age=25, email='abmazhr@gmail.com')
    _created_user = create_user_usecase.execute(data=data)
    retrieved_check_creds = check_user_creds_usecase.execute(
        data={'username': data['name'], 'password': data['password']}
    )

    assert isinstance(retrieved_check_creds, Success)


@skip_or_not
def test_invalid_user_credentials(usecases):
    create_user_usecase, check_user_creds_usecase = usecases

    data = dict(name="abdulrahman", password='test', age=25, email='abmazhr@gmail.com')
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
