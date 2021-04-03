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

hasho.insertar(Avion('AV1', 'MA1', 'A00000002'))

def main():

    # TODO: CARGAR LOS DATOS EN EL HASH TABLE

    print("Bienvenido a la Base de Datos de Aviones de Occidente Aviocc!")

    while True:

        menu = Menu([
            'Inserción de un Nuevo Avión',
            'Búsqueda de un Avión',
            'Salir'
        ])

        if menu.opcion == '1':
            insertcion()
        elif menu.opcion == '2':
            busqueda()
        elif menu.opcion == '3':
            # TODO: GUARDAR NUEVO HASH TABLE EN BROMA
            print('\nSe ha terminado el programa.')
            break
        else:
            print("\nOpcion no valida intente otra vez")

def insertcion():
    # TODO
    pass

def busqueda():

    while True:
        menu = Menu([
            'Buscar por serial (busqueda hash)',
            'Buscar por nombre (busqueda binaria)',
            'Buscar por modelo (busqueda binaria)',
            'Volver',
        ])

        serial = None

        if menu.opcion == '1':
            serial = input('Ingrese serial de avion: ')
            # TODO: VALIDACIONES
        elif menu.opcion == '2':
            nombre = input('Ingrese nombre de avion: ')
            if hasho.busquedaPorNombre(nombre):
                serial = hasho.busquedaPorNombre(nombre)['serial']
        elif menu.opcion == '3':
            modelo = input('Ingrese modelo de avion: ')
            if hasho.busquedaPorModelo(modelo):
                serial = hasho.busquedaPorModelo(modelo)['serial']
        elif menu.opcion == '4':
            return
        else:
            print("\nOpcion no valida intente otra vez")
            break

        selecionar(serial)
            


def selecionar(serial):
    avion = hasho.getAvion(serial)

    if avion:

        piloto = 'Ninguno'

        if avion.piloto:
            piloto = avion.piloto

        print(f'''  \nAvion Encontrado!
    Serial: {avion.serial}
    Nombre: {avion.name}
    Modelo: {avion.modelo}
    Piloto: {piloto}''')

        menu = None

        while True:
            if avion.piloto:
                menu = Menu([
                    'Liberar Piloto',
                    'Eliminar Avion',
                    'Volver'
                ])
            else:
                menu = Menu([
                    'Asignar Piloto',
                    'Eliminar Avion',
                    'Volver'
                ])

            if menu.opcion == '1':
                if avion.piloto:
                    liberarPiloto()
                else:
                    liberarPiloto()
                break
            elif menu.opcion == '2':
                eliminarAvion(avion.serial)
                break
            elif menu.opcion == '3':
                break
            else:
                print("\nOpcion no valida intente otra vez")


    else:
        print('\nAvion no encontrado.')

def asignarPiloto():
    # TODO:
    pass

def liberarPiloto():
    # TODO:
    pass

def eliminarAvion(serial):
    hasho.eliminar(serial)
    # TODO: MENSAJE DE EXISTO
    pass

if __name__ == "__main__":
    main()
