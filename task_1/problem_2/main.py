from publisher.message_publisher import MessagePublisher
from publisher.listener import Listener
from devices.smart_phone import SmartPhone
from devices.smart_watch import SmartWatch


def main():
    publisher = MessagePublisher()

    personal_phone_listener = Listener("Oscar", SmartPhone("Personal phone", "iPhone", "iOS"))
    personal_smartwatch_listener = Listener("Oscar", SmartWatch("Apple", "iOS"))
    work_phone_listener = Listener("Oscar", SmartPhone("Work phone", "Samsung", "Android"))

    publisher.suscribe(personal_phone_listener)
    publisher.suscribe(personal_smartwatch_listener)
    publisher.suscribe(work_phone_listener)

    publisher.publish_message("Oscar", "Es hora de hacer pruebas")

    publisher.unsuscribe(work_phone_listener)

    publisher.publish_message("Oscar", "Una prueba más sin mi telefono personal")

    publisher.publish_message("Javier", "Otra prueba con usuario diferente. No debe mostrarlo")

    my_warrior_phone_listener = Listener("Javier", SmartPhone("Warrior phone", "Alcatel", "Android"))
    publisher.suscribe(my_warrior_phone_listener)

    publisher.publish_message("Javier", "Última prueba incluyendo mi teléfono de combate")


if __name__ == "__main__":
    main()
