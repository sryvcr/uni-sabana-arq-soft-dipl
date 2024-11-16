## El patron creacional escogido fue Prototype

from tipos_heroes.mago import Mago
from tipos_heroes.arquero import Arquero
from tipos_heroes.guerrero import Guerrero
from habilidades import Habilidades
from mostrar_informacion import MostrarInformacion


guerrero1 = Guerrero("Tony Stark")
mago1 = Mago("Dr. Strange")
arquero1 = Arquero("Hawkeye")

info = MostrarInformacion()
print("\nHeroe principal - guerrero:")
info.mostrar_informacion(guerrero1)

print("\nHeroe principal - mago:")
info.mostrar_informacion(mago1)

print("\nHeroe principal - arquero:")
info.mostrar_informacion(arquero1)

guerrero_clonado = guerrero1.clone()
mago_clonado = mago1.clone()
arquero_clonado = arquero1.clone()

guerrero_clonado.personalizar(
    nuevo_nombre="Capitan America",
    nueva_clase="guerrero")

mago_clonado.personalizar(
    nuevo_nombre="wong",
    nueva_clase="mago",
    nuevas_habilidades=[
        Habilidades("Habilidad Magica", 28, "mago")
    ]
)

arquero_clonado.personalizar(
    nuevo_nombre="Kate Bishop",
    nueva_clase="arquero"
)

print("\nHeroe clonado - Guerrero:")
info.mostrar_informacion(guerrero_clonado)

print("\nHeroe clonado - mago:")
info.mostrar_informacion(mago_clonado)

print("\nHeroe clonado - arquero:")
info.mostrar_informacion(arquero_clonado)
