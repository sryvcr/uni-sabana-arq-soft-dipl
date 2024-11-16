class Hotel:
    def __init__(self, nombre: str, n_habitaciones: int) -> None:
        self.__nombre = nombre
        self.__n_habitaciones = n_habitaciones

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_n_habitaciones(self):
        return self.__n_habitaciones

    def restar_maximo_habitaciones(self) -> None:
        self.__n_habitaciones -= 1

    def diccionario_habitaciones(self, habitaciones: object) -> dict:
        return habitaciones.get_habitaciones()


class HabitacionManager:
    def __init__(self):
        self.__habitaciones = {}

    def add_habitacion(self, numero_habitacion: int, habitacion: object) -> None:
        numero_habitacion = str(numero_habitacion)
        self.__habitaciones[numero_habitacion] = habitacion
        print("Habitación creada")

    def restar_maximo_habitaciones(self, hotel: Hotel) -> None:
        hotel.restar_maximo_habitaciones()

    # Método para obtener el diccionario de habitaciones
    def get_habitaciones(self):
        return self.__habitaciones

    def buscar_habitacion(self, numero_habitacion) -> str:
        if self.__habitaciones.get(numero_habitacion) is not None:
            return 'Habitacion existente'

    def desocupar_habitacion(self, numero_habitacion, habitacion_generica) -> None:
        self.__habitaciones[numero_habitacion] = habitacion_generica
