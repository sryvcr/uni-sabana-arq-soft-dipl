class MostrarInformacion:
    def mostrar_informacion(self, personaje):
        print(f"Nombre: {personaje.nombre}")
        print(f"Clase: {personaje.clase}")
        print(f"Nivel: {personaje.nivel}")
        print(f"Experiencia: {personaje.experiencia}")
        print(f"Puntos de habilidad: {personaje.puntos_habilidad}")
        print("Habilidades:")
        for habilidad in personaje.habilidades:
            print(f"{habilidad}")
