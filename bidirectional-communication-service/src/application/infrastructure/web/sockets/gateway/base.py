from abc import ABCMeta, abstractmethod

from src.application.usecase.user.check_creds import CheckUserCredentialsUseCase


class BaseSockets(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, *, check_user_creds_usecase: CheckUserCredentialsUseCase) -> None: pass

    @abstractmethod
    def on_connect(self, *args, **kwargs) -> None: pass

    @abstractmethod
    def on_disconnect(self, *args, **kwargs) -> None: pass
