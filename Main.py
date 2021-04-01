

from MainFunctions import *
from Avion import *
from SerializationFunctions import *


def main():
    # Estructuras de datos
    aviones = []
    pilotos = []

    aviones = recibir_datos_del_txt(
        "C:\\Users\\DELL\\Desktop\\PERSONAL PROJECTS\\Proyecto2Orga\\Aviones.txt", aviones)
    pilotos = recibir_datos_del_txt(
        "C:\\Users\\DELL\\Desktop\\PERSONAL PROJECTS\Proyecto2Orga\\Pilotos.txt", pilotos)

    bienvenida(aviones, pilotos)

    avion = Avion('BTW', 'HOLAA')

    print(avion.getName())


main()
