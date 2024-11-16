from publisher.listener import Listener


class MessagePublisher:
    def __init__(self, ):
        self.__listeners = list()

    def suscribe(self, listener):
        self.__listeners.append(listener)

    def unsuscribe(self, listener):
        self.__listeners.remove(listener)

    def publish_message(self, user, message):
        for listener in self.__listeners:
            if listener.user == user:
                listener.device.update(message)
