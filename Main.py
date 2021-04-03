from Avion import Avion
from SerializationFunctions import *
import os
from Menu import Menu
from HashTable import *



# paths
dirname = os.path.dirname(__file__)
path_aviones = (os.path.join(dirname, 'Aviones.txt'))
path_pilotos = (os.path.join(dirname, 'Pilotos.txt'))

# Estructuras de datos
hasho = HashTable()
aviones = recibir_datos_del_txt(path_aviones)
pilotos = recibir_datos_del_txt(path_pilotos)

avion = Avion("AV1", "MA1", "A00000000")
hasho.insertar(avion)
avion = Avion("AV2", "MA2", "A00000003")
hasho.insertar(avion)
avion = Avion("AV3", "MA3", "A00000009")
hasho.insertar(avion)
avion = Avion("AV4", "MA4", "A00000012")
hasho.insertar(avion)
avion = Avion("AV5", "MA5", "A00000015")
hasho.insertar(avion)
avion = Avion("BV1", "MB1", "B00000001")
hasho.insertar(avion)
avion = Avion("CV1", "MC1", "C00000002")
hasho.insertar(avion)
hasho.eliminar('C00000002')

hasho.print()


def main():



    while True:

        option = input('''\nBienvenido a la Base de Datos de Aviones de Occidente Aviocc
        1. Inserción de un Nuevo Avión
        2. Búsqueda de un Avión
        3. Asignación de un Avión Libre
        4. Liberación de un Avión
        5. Eliminación de un Avión
        6. Salir
        >> ''')

        if option == '1':
            Modulo1()
        elif option == '2':
            Modulo2()
        elif option == '3':
            Modulo3()
        elif option == '4':
            Modulo4()
        elif option == '5':
            Modulo5()
        elif option == '6':
            print('\nSe ha terminado el programa.')
            break
        else:
            print("\nOpcion no valida intente otra vez")

def Modulo1():
    """ while True:
        modelo = input("Ingrese el modelo del avion:\n===> ")
        if modelo.isspace() or len(modelo) == 0:
            continue
        modelo = modelo.strip()
        break
    while True:
        nombre = input("Ingrese el nombre del avion:\n===>")
        if nombre.isspace() or len(nombre) == 0:
            continue
        nombre = nombre.strip()
        break
    nombre = nombre.lstrip()
    counter = int(8-len(str(len(aviones))))
    ceros = ""
    if (len(str(len(aviones)+1)) == len(str(len(aviones)))) or len(aviones) == 0:
        for i in range(counter):
            ceros = ceros+"0"
    else:
        for i in range(counter-1):
            ceros = ceros+"0"
    serial = modelo[0]+ceros+str(len(aviones)+1)
    print(serial)
    newAvion = Avion(nombre, modelo, serial)
    aviones.append(newAvion)
    cargar_datos_en_txt(path_aviones, aviones) """
    print("MODULO #1")


def Modulo2():
    print("MODULO #2")


def Modulo3():
    print("MODULO #3")


def Modulo4():
    print("MODULO #4")


def Modulo5():
    print("MODULO #5")


if __name__ == "__main__":
    pass
    #main()
