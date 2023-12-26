from abc import ABCMeta, abstractmethod


class OrderType(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, order):
        raise NotImplementedError()
