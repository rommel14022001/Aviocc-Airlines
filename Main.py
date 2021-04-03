from Avion import Avion
from SerializationFunctions import *
import os
from Menu import Menu
from HashTable import *


hasho = HashTable()
avion = Avion("AV1", "", "B0000000")
hasho.insertar(avion)
avion = Avion("AV2", "", "B0000003")
hasho.insertar(avion)
avion = Avion("AV3", "", "B0000006")
hasho.insertar(avion)
avion = Avion("AV4", "", "B0000009")
hasho.insertar(avion)
avion = Avion("AV5", "", "B0000012")
hasho.insertar(avion)
avion = Avion("AV6", "", "B0000015")
hasho.insertar(avion)
avion = Avion("AV7", "", "B0000018")
hasho.insertar(avion)
avion = Avion("BV1", "", "B0000021")
hasho.insertar(avion)
avion = Avion("BV2", "", "B0000024")
hasho.insertar(avion)
avion = Avion("BV3", "", "B00000027")
hasho.insertar(avion)
avion = Avion("BV4", "", "B0000030")
hasho.insertar(avion)
avion = Avion("BV5", "", "B00000033")
hasho.insertar(avion)
avion = Avion("BV6", "", "B00000036")
hasho.insertar(avion)
avion = Avion("BV7", "", "B00000039")
hasho.insertar(avion)
hasho.eliminarAvionSerial("B0000021")
hasho.eliminarAvionSerial("B0000024")
hasho.print()

indice = hasho.busquedaPorNombre('BV1')

if indice:
    print(hasho.indicesNombres[indice])

# print(hasho.table[0][0][0].name)
# print(hasho.table[0][0][1])
# print(hasho.table[0][1][0].name)


# '''----------------------------------------------'''
# avion = Avion("COMETA", "BTW 222", "B00000001")
# hasho.AddAvion(avion)
# avion = Avion("METEORO", "BTW 111", "B00000004")
# hasho.AddAvion(avion)
# avion = Avion("Rayo", "BTW 333", "B00000013")
# hasho.AddAvion(avion)
# avion = Avion("Relampago", "BTW 433", "B00000010")
# hasho.AddAvion(avion)
# avion = Avion("Rojo", "BTW 533", "B00000019")
# hasho.AddAvion(avion)
# avion = Avion("azul", "BTW 633", "B00000022")
# hasho.AddAvion(avion)
# avion = Avion("mariposa", "BTW 733", "B00000025")
# hasho.AddAvion(avion)
# avion = Avion("Avestruz", "BTW 833", "B00000028")
# hasho.AddAvion(avion)

# avion = Avion("verde", "BTW 911", "B00000031")
# hasho.AddAvion(avion)
# avion = Avion("amarillo", "BTW 1333", "B00000034")
# hasho.AddAvion(avion)
# avion = Avion("Rosado", "BTW 1433", "B00000037")
# hasho.AddAvion(avion)
# avion = Avion("gris", "BTW 1533", "B00000040")
# hasho.AddAvion(avion)
# avion = Avion("negro", "BTW 1633", "B00000043")
# hasho.AddAvion(avion)
# avion = Avion("morado", "BTW 1733", "B00000049")
# hasho.AddAvion(avion)
# avion = Avion("celeste", "BTW 1833", "B00000052")
# hasho.AddAvion(avion)

# # # # print(hasho.hash)
# # avion = Avion("COLOSO", "BTW 333", "B00000002")
# # hasho.AddAvion(avion)
# # avion = Avion("RAYO", "BTW 444", "B00000005")
# # hasho.AddAvion(avion)
# # avion = Avion("HALCON", "BTW 555", "B00000003")
# # hasho.AddAvion(avion)
# print("AQUIII")
# print(hasho.table[1])
# hasho.eliminarAvionSerial("B00000001")
# print(hasho.table[1])
# # print(hasho.hash[1])
# # print(hasho.indicesNombres)
# # print(hasho.indicesModelo)
# '''-----------------------------------------------'''

# paths
# dirname = os.path.dirname(__file__)
# path_aviones = (os.path.join(dirname, 'Aviones.txt'))
# path_pilotos = (os.path.join(dirname, 'Pilotos.txt'))

# # Estructuras de datos
# aviones = recibir_datos_del_txt(path_aviones)
# pilotos = recibir_datos_del_txt(path_pilotos)


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
            break
        elif option == '2':
            Modulo2()
            break
        elif option == '3':
            Modulo3()
            break
        elif option == '4':
            Modulo4()
            break
        elif option == '5':
            Modulo5()
            break
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
    main()
