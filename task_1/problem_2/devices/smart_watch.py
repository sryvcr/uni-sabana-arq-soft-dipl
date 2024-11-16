from devices.listener_device import ListenerDevice


class SmartWatch(ListenerDevice):
    def __init__(self, brand, operative_system):
        self.__brand = brand
        self.__operative_system = operative_system

    def update(self, message):
        print("Mensaje: {}... Recibido en mi smartwatch {}".format(str(message), self.__operative_system))
