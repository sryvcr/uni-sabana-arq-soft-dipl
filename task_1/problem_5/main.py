from decorator import * 
from hotel import *

if __name__ == "__main__":
    nuevo_hotel = Hotel('El San Luis', 10)
    manager_habitacion = HabitacionManager()

    if nuevo_hotel.get_n_habitaciones()>0:
        habitacion = Habitacion(303)  # Este es el componente concreto
        manager_habitacion.add_habitacion(habitacion.get_numero_habitacion(),habitacion)
        print(habitacion.descripcion())

        #ejemplo donde se agregan 2 funcionalidades adicionales a una instancia
        habitacion_mejorada = FloresFrescas(habitacion)
        habitacion_mejorada = ChocolateGourmet(habitacion_mejorada)

        print(habitacion_mejorada.descripcion())

        print("Se limpiara la habitacion")
        manager_habitacion.desocupar_habitacion(habitacion.get_numero_habitacion(), Habitacion(habitacion.get_numero_habitacion()))
        habitacion_mejorada = None
