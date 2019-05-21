from abc import ABCMeta, abstractmethod


class RestApiGateway(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self): pass
