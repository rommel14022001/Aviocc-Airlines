from Avion import *
from Pilotos import *
from SerializationFunctions import *


def bienvenida(aviones, pilotos):

    print("***BIENVENIDO A AVIOCC AIRLINES\nGRACIAS POR PREFERIRNOS!!!***")

    opcion = '0'

    avionesTxtRoute = "C:\\Users\\DELL\\Desktop\\PERSONAL PROJECTS\\Proyecto2Orga\\Aviones.txt"
    pilotosTxtRoute = "C:\\Users\\DELL\\Desktop\\PERSONAL PROJECTS\\Proyecto2Orga\\Pilotos.txt"
    while int(opcion) != 6:
        opcion = '0'
        while int(opcion) > 6 or int(opcion) < 1:
            print('''
            \n    
            ***MENU***\n
            
            1. Inserción de un Nuevo Avión a la Base de Datos (Se insertan sin Piloto asignado)\n
            2. Búsqueda de un Avión en la Base de Datos, Permitiendo:\n
                . Búsqueda por Serial\n
                . Búsqueda por Modelo.\n
                . Búsqueda por Nombre.\n
            3. Asignación de un Avión Libre (Sin piloto asignado actualmente) a un piloto (Buscando dicho avión ya sea por Serial, Modelo o Nombre)\n
            4. Liberación de un Avión. Es decir, limpiar su campo “Piloto”\n
            5. Eliminación de un Avión de la Flota (Físicamente)\n

        ''')

            opcion = input("===> ")
            while opcion.isnumeric() == False:
                print('''
                \n    
                ***MENU***\n
                
                1. Inserción de un Nuevo Avión a la Base de Datos (Se insertan sin Piloto asignado)\n
                2. Búsqueda de un Avión en la Base de Datos, Permitiendo:\n
                    . Búsqueda por Serial\n
                    . Búsqueda por Modelo.\n
                    . Búsqueda por Nombre.\n
                3. Asignación de un Avión Libre (Sin piloto asignado actualmente) a un piloto (Buscando dicho avión ya sea por Serial, Modelo o Nombre)\n
                4. Liberación de un Avión. Es decir, limpiar su campo “Piloto”\n
                5. Eliminación de un Avión de la Flota (Físicamente)\n
                6.Salir del sistema.\n
            ''')
                opcion = input("===> ")

        opcion = int(opcion)

        if opcion == 1:
            Modulo1(avionesTxtRoute, aviones)
        elif opcion == 2:
            Modulo2(avionesTxtRoute, aviones)
        elif opcion == 3:
            Modulo3(avionesTxtRoute, aviones)
        elif opcion == 4:
            Modulo4(avionesTxtRoute, aviones)
        elif opcion == 5:
            Modulo5(aviones, pilotos)


def Modulo1(avionesTxtRoute, aviones):

    while True:

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
    for i in range(counter):
        ceros = ceros+"0"

    serial = modelo[0]+ceros+str(len(aviones)+1)
    print(serial)

    newAvion = Avion(nombre, modelo, serial)
    aviones.append(newAvion)
    cargar_datos_en_txt(avionesTxtRoute, aviones)
    # pass


def Modulo2(aviones):
    pass


def Modulo3(aviones, pilotos):

    pass


def Modulo4(avionesTxtRoute, aviones):
    pass


def Modulo5(aviones, pilotos):

    pass
