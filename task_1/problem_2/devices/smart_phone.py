from devices.listener_device import ListenerDevice


class SmartPhone(ListenerDevice):
    def __init__(self, name, brand, operative_system):
        self.__name = name
        self.__brand = brand
        self.__operative_system = operative_system

    def set_name(self, name):
        self.__name = name

    def update(self, message):
        print("Mensaje: {}... Recibido en {} {}".format(str(message), self.__name, self.__brand))
