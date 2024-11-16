from habilidades import Habilidades
from personaje import Personaje
from personalizar import Personalizar
from personaje import Personaje

class Arquero(Personaje, Personalizar):
    def __init__(self, nombre):
        habilidades =[
            Habilidades("Ataque", 5, "Arquero"),
            Habilidades("Defensa", 10, "Arquero"),
            Habilidades("Habilidad Magica", 0, "Arquero"),
        ]
        super().__init__(nombre, "Arquero", habilidades)


