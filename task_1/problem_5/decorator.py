from abc import ABC, abstractmethod


# Componete interfaz
class ComponenteHabitacion(ABC):
    @abstractmethod
    def descripcion(self):
        pass


# Componente concreto
class Habitacion(ComponenteHabitacion):
    def __init__(self, numero_habitacion: int):
        self.__numero_habitacion = numero_habitacion
        self.__camas = 2
        self.__ventanas = 2
        self.__balcon = 1
        self.__mesas = 4
        self.__muebles = 2
        self.__closet = 2

    def get_numero_habitacion(self) -> int:
        return self.__numero_habitacion

    def set_numero_habitacion(self,nuevo_numero_habitacion:int) -> int:
        self.__numero_habitacion = nuevo_numero_habitacion

    def descripcion(self):
        return f"Habitación numero {self.__numero_habitacion} con {self.__camas} camas, {self.__ventanas} ventanas, {self.__balcon} balcón, {self.__mesas} mesas, {self.__muebles} muebles y {self.__closet} closets."


# Decorador base
class DecoradorHabitacion(ComponenteHabitacion):
    _component: ComponenteHabitacion = None

    def __init__(self, component: ComponenteHabitacion) -> None:
        self._component = component

    def descripcion(self) -> str:
        # Delegar la llamada al componente envuelto
        return self._component.descripcion()


# Decoradores concretos
# Implementacion de nuevas funcionalidades
class FloresFrescas(DecoradorHabitacion):
    def descripcion(self):
        return super().descripcion() + " Incluye flores frescas."


class ChocolateGourmet(DecoradorHabitacion):
    def descripcion(self):
        return super().descripcion() + " Incluye chocolate gourmet."


class VinoAltaCalidad(DecoradorHabitacion):
    def descripcion(self):
        return super().descripcion() + " Incluye vino de alta calidad."
