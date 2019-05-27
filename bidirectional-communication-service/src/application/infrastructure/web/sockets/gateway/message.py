from abc import ABCMeta, abstractmethod


class MessageSockets(metaclass=ABCMeta):
    @abstractmethod
    def on_message(self, *args, **kwargs) -> None: pass
