from habilidades import Habilidades
from personaje import Personaje
from personalizar import Personalizar
from personaje import Personaje

class Mago(Personaje, Personalizar):
    def __init__(self, nombre):
        habilidades =[
            Habilidades("Ataque", 0, "Mago"),
            Habilidades("Defensa", 5, "Mago"),
            Habilidades("Habilidad Magica", 10, "Mago"),
        ]
        super().__init__(nombre, "Mago", habilidades)


