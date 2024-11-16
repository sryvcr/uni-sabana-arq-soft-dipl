from abc import ABC, abstractmethod


class Interfaz_Personaje(ABC):
    @abstractmethod
    def clone(self):
        pass
