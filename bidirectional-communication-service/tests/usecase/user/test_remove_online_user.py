from uuid import uuid4

import pytest

from src.application.infrastructure.persistent.in_memory import InMemoryOnlineUsersPersistent
from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase
from src.domain.entity.error import Error
from src.domain.entity.success import Success
from src.domain.entity.user_persistence import UserPersistence


@pytest.fixture(scope='function')
def usecases():
    online_user_persistent = InMemoryOnlineUsersPersistent()
    add_online_user_usecase = AddOnlineUserUseCase(online_user_persistent=online_user_persistent)
    remove_online_user_usecase = RemoveOnlineUserUseCase(online_user_persistent=online_user_persistent)

    yield add_online_user_usecase, remove_online_user_usecase


def test_valid_remove_online_user(usecases):
    add_online_user_usecase, remove_online_user_usecase = usecases

    adding_user_data = UserPersistence(username='abdulrahman', socket_id=uuid4().hex)

    add_online_user_usecase.execute(
        user_persistence=adding_user_data
    )

    assert isinstance(remove_online_user_usecase.execute(
        socket_id=adding_user_data.socket_id
    ), Success)


def test_invalid_remove_online_user(usecases):
    add_online_user_usecase, remove_online_user_usecase = usecases

    assert isinstance(remove_online_user_usecase.execute(
        socket_id=""
    ), Error)
