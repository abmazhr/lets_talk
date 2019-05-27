from uuid import uuid4

import pytest

from src.application.infrastructure.persistent.in_memory import InMemoryOnlineUsersPersistent
from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence


@pytest.fixture(scope='function')
def usecase():
    online_user_persistent = InMemoryOnlineUsersPersistent()
    add_online_user_usecase = AddOnlineUserUseCase(online_user_persistent=online_user_persistent)

    yield add_online_user_usecase


def test_valid_add_online_user(usecase):
    data = UserPersistence(username='abdulrahman', socket_id=uuid4().hex)

    assert isinstance(usecase.execute(
        user_persistence=data
    ), Success)


def test_invalid_add_online_user(usecase):
    data = UserPersistence(username='abdulrahman', socket_id=uuid4().hex)
    usecase.execute(
        user_persistence=data
    )
    assert isinstance(usecase.execute(
        user_persistence=data
    ), Error)

    data = UserPersistence(username='', socket_id=uuid4().hex)
    assert isinstance(usecase.execute(
        user_persistence=data
    ), Error)

    data = UserPersistence(username='abdulrahman', socket_id='')
    assert isinstance(usecase.execute(
        user_persistence=data
    ), Error)

    data = {}
    assert isinstance(usecase.execute(
        user_persistence=data
    ), Error)
