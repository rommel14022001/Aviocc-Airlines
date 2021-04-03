from Avion import *
from SerializationFunctions import *
import os
from Menu import Menu
from HashTable import *


hasho = HashTable()
'''----------------------------------------------'''
avion = Avion("COMETA", "BTW 222", "B00000001")
hasho.AddAvion(avion)
avion = Avion("METEORO", "BTW 111", "B00000004")
hasho.AddAvion(avion)
avion = Avion("Rayo", "BTW 333", "B00000013")
hasho.AddAvion(avion)
avion = Avion("Relampago", "BTW 433", "B00000010")
hasho.AddAvion(avion)
avion = Avion("Rojo", "BTW 533", "B00000019")
hasho.AddAvion(avion)
avion = Avion("azul", "BTW 633", "B00000022")
hasho.AddAvion(avion)
avion = Avion("mariposa", "BTW 733", "B00000025")
hasho.AddAvion(avion)
avion = Avion("Avestruz", "BTW 833", "B00000028")
hasho.AddAvion(avion)

avion = Avion("verde", "BTW 911", "B00000031")
hasho.AddAvion(avion)
avion = Avion("amarillo", "BTW 1333", "B00000034")
hasho.AddAvion(avion)
avion = Avion("Rosado", "BTW 1433", "B00000037")
hasho.AddAvion(avion)
avion = Avion("gris", "BTW 1533", "B00000040")
hasho.AddAvion(avion)
avion = Avion("negro", "BTW 1633", "B00000043")
hasho.AddAvion(avion)
avion = Avion("morado", "BTW 1733", "B00000049")
hasho.AddAvion(avion)


# # # print(hasho.hash)
# avion = Avion("COLOSO", "BTW 333", "B00000002")
# hasho.AddAvion(avion)
# avion = Avion("RAYO", "BTW 444", "B00000005")
# hasho.AddAvion(avion)
# avion = Avion("HALCON", "BTW 555", "B00000003")
# hasho.AddAvion(avion)
print("AQUIII")
print(hasho.hash[1])
hasho.eliminarAvionSerial("B00000031")
print(hasho.hash[1])
# print(hasho.hash[1])
# print(hasho.indicesNombres)
# print(hasho.indicesModelo)
'''-----------------------------------------------'''

# paths
# dirname = os.path.dirname(__file__)
# path_aviones = (os.path.join(dirname, 'Aviones.txt'))
# path_pilotos = (os.path.join(dirname, 'Pilotos.txt'))

# # Estructuras de datos
# aviones = recibir_datos_del_txt(path_aviones)
# pilotos = recibir_datos_del_txt(path_pilotos)


# def main():

#     opcion = 0

#     while opcion != 6:
#         menu = Menu([
#             'Inserción de un Nuevo Avión',
#             'Búsqueda de un Avión',
#             'Asignación de un Avión Libre',
#             'Liberación de un Avión',
#             'Eliminación de un Avión',
#             'Salir'
#         ])

#         opcion = int(menu.opcion)

#         if opcion == 1:
#             Modulo1()
#         elif opcion == 2:
#             Modulo2()
#         elif opcion == 3:
#             Modulo3()
#         elif opcion == 4:
#             Modulo4()
#         elif opcion == 5:
#             Modulo5()
#         elif opcion == 6:
#             print('Se termino chao')
#             break
#         else:
#             print("Opcion no valida intente otravez")


# def Modulo1():

#     while True:

#         modelo = input("Ingrese el modelo del avion:\n===> ")
#         if modelo.isspace() or len(modelo) == 0:
#             continue
#         modelo = modelo.strip()
#         break

#     while True:

#         nombre = input("Ingrese el nombre del avion:\n===>")
#         if nombre.isspace() or len(nombre) == 0:
#             continue
#         nombre = nombre.strip()
#         break

#     nombre = nombre.lstrip()
#     counter = int(8-len(str(len(aviones))))
#     ceros = ""

#     if (len(str(len(aviones)+1)) == len(str(len(aviones)))) or len(aviones) == 0:
#         for i in range(counter):
#             ceros = ceros+"0"
#     else:
#         for i in range(counter-1):
#             ceros = ceros+"0"

#     serial = modelo[0]+ceros+str(len(aviones)+1)
#     print(serial)

#     newAvion = Avion(nombre, modelo, serial)
#     aviones.append(newAvion)
#     cargar_datos_en_txt(path_aviones, aviones)


# def Modulo2():
#     print("MODULO #2")


# def Modulo3():
#     print("MODULO #3")


# def Modulo4():
#     print("MODULO #4")


# def Modulo5():
#     print("MODULO #5")


# if __name__ == "__main__":
#     main()
