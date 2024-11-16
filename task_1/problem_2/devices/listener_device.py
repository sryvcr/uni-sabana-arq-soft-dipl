from abc import ABC, abstractmethod


class ListenerDevice(ABC):
    @abstractmethod
    def update(self):
        pass
