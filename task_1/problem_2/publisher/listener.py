from dataclasses import dataclass
from devices.listener_device import ListenerDevice


@dataclass
class Listener:
    user: str
    device: ListenerDevice
