class Habilidades:
    def __init__(self, nombre, poder, tipo_heroe):
        self.nombre = nombre
        self.poder = poder
        self.tipo_heroe = tipo_heroe

    def __str__(self):
        return f"{self.nombre} ({self.tipo_heroe}) - Capacidad: {self.poder}"
