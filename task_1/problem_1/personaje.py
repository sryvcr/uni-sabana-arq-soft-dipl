import copy
from habilidades import Habilidades
from personalizar import Personalizar
from interfaz_personaje import Interfaz_Personaje
from mostrar_informacion import MostrarInformacion


class Personaje(Interfaz_Personaje):
    def __init__(self, nombre, clase, habilidades=None, nivel=1, experiencia=0, puntos_habilidad=0):
        self.nombre = nombre
        self.clase = clase
        self.habilidades = habilidades if habilidades else []
        self.nivel = nivel
        self.experiencia = experiencia
        self.puntos_habilidad = puntos_habilidad

    def agregar_habilidad(self, habilidad):
        self.habilidades.append(habilidad)

    def personalizar(self, nuevo_nombre=None, nueva_clase=None, nuevas_habilidades=None):
        Personalizar.personalizar(self, nuevo_nombre, nueva_clase, nuevas_habilidades)

    def clone(self):
        return copy.deepcopy(self)
