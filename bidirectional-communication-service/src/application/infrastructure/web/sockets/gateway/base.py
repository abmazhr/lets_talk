from abc import ABCMeta, abstractmethod

from src.application.usecase.user.add_online_user import AddOnlineUserUseCase
from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase
from src.application.usecase.user.remove_online_user import RemoveOnlineUserUseCase


class BaseSockets(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *,
                 check_user_creds_usecase: CheckUserCredentialsUseCase,
                 add_online_user_usecase: AddOnlineUserUseCase,
                 remove_online_user_usecase: RemoveOnlineUserUseCase) -> None: pass

    @abstractmethod
    def on_connect(self, *args, **kwargs) -> None: pass

    @abstractmethod
    def on_disconnect(self, *args, **kwargs) -> None: pass
