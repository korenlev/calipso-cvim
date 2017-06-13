from abc import ABC, abstractmethod


class ListenerBase(ABC):

    @staticmethod
    @abstractmethod
    def listen(self):
        pass
