from habilidades import Habilidades
from personaje import Personaje
from personalizar import Personalizar
from personaje import Personaje

class Guerrero(Personaje, Personalizar):
    def __init__(self, nombre):
        habilidades =[
            Habilidades("Ataque", 10, "Guerrero"),
            Habilidades("Defensa", 5, "Guerrero"),
            Habilidades("Habilidad Magica", 0, "Guerrero"),
        ]
        super().__init__(nombre, "Guerrero", habilidades)


