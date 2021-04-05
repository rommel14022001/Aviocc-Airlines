from Avion import Avion
from SerializationFunctions import *
import os
from Menu import Menu
from HashTable import *

# paths
dirname = os.path.dirname(__file__)
path_HashTable = (os.path.join(dirname, 'HashTable.txt'))

# Estructuras de datos
hasho = HashTable()
hasho = recibir_datos_del_txt(path_HashTable)


def main():

    hasho.print()

    print("\n <-- Bienvenido a la Base de Datos de Aviones de Occidente Aviocc! -->")

    while True:

        menu = Menu([
            'Inserción de un Nuevo Avión',
            'Búsqueda de un Avión',
            'Salir'
        ])

        if menu.opcion == '1':
            insercion()
        elif menu.opcion == '2':
            busqueda()
        elif menu.opcion == '3':
            print('\n<-- Se ha terminado el programa -->\n')
            break
        else:
            print("\n** Opcion no valida intente otra vez **")


def insercion():
    # TODO
    print('\n<-- REGISTRO DE AVION -->')
    while True:

        serial = input('\nIngrese el serial del avion: ')
        # Validar que sea unico
        if(validaciones(serial, 'serial')):
            modelo = input('\nIngrese el modelo del avion: ')
            # Validar que sea unico
            if(hasho.busquedaPorModelo(modelo) == None):
                if(validaciones(modelo, 'modelo')):
                    nombre = input('\nIngrese el nombre del avion: ')
                    # Validar que sea unico
                    if(hasho.busquedaPorNombre(nombre) == None):
                        if(validaciones(nombre, 'nombre')):
                            break
                    else:
                        print('\n** Ya existe un avion con el nombre ingresado. **')
            else:
                print('\n** Ya existe un avion con el modelo ingresado. **')

    newAvion = Avion(nombre, modelo, serial)
    if(hasho.insertar(newAvion)):
        cargar_datos_en_txt(path_HashTable, hasho)
        print('\n \-- Se ha agregado el avion a la base de datos --/')


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

            while True:
                serial = input('\nIngrese el serial del avion: ')
                # VALIDACIONES
                if (validaciones(serial, 'serial')):
                    break

        elif menu.opcion == '2':
            while True:
                nombre = input('\nIngrese el nombre del avion: ')
                # VALIDACIONES
                if (validaciones(nombre, 'nombre')):
                    break

            if hasho.busquedaPorNombre(nombre):
                serial = hasho.busquedaPorNombre(nombre)['avion']['serial']

        elif menu.opcion == '3':
            while True:
                modelo = input('\nIngrese el modelo del avion: ')
                # VALIDACIONES
                if (validaciones(modelo, 'modelo')):
                    break

            if hasho.busquedaPorModelo(modelo):
                serial = hasho.busquedaPorModelo(modelo)['avion']['serial']

        elif menu.opcion == '4':
            return
        else:
            print("\n** Opcion no valida intente otra vez **")
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
                    liberarPiloto(avion)
                else:
                    asignarPiloto(avion)
                break
            elif menu.opcion == '2':
                eliminarAvion(avion.serial)
                break
            elif menu.opcion == '3':
                break
            else:
                print("\n** Opcion no valida intente otra vez **")

    else:
        print('\n\-- Avion no encontrado. --/')


def asignarPiloto(avion):
    nombre_piloto = input('\nNombre del piloto: ')
    if(validaciones(nombre_piloto, 'piloto')):
        hasho.asignarPiloto(avion, nombre_piloto)
        cargar_datos_en_txt(path_HashTable, hasho)
        print(
            f'\n\-- Se ha asignado al piloto: {nombre_piloto} con Exito! --/')


def liberarPiloto(avion):
    hasho.asignarPiloto(avion, None)
    cargar_datos_en_txt(path_HashTable, hasho)
    print('\n\-- Se ha liberado al piloto con Exito! --/')


def eliminarAvion(serial):
    hasho.eliminar(serial)
    cargar_datos_en_txt(path_HashTable, hasho)
    print('\n\-- Se ha eliminado el avion con Exito! --/')
    pass


def validaciones(validar, indicador):
    if(indicador == 'serial'):
        contA = 0
        ContN = 0
        for c in validar:
            if (c.isalpha()):
                contA += 1
            if(c.isdigit()):
                ContN += 1
        # El serial es de 9 caracteres
        if(len(validar) < 9):
            print('\n** Error. El serial de un Avion es de 9 Digitos. **')
        # El primer digito es una letra
        elif not(validar[0].isalpha()):
            print('\n** Error. El primer digito del Serial debe ser una letra. **')
        # El serial contiene una sola letra en mayuscula
        elif not(validar[0].isupper()):
            print(
                '\n** Error. El primer digito del Serial debe ser una letra en Mayusculas. **')
        # El serial contiene una sola letra
        elif(contA > 1):
            print('\n** Error. El serial solo debe contener un Caracter Alfabetico. **')
        # El serial contiene 8 Digitos
        elif(ContN > 8 or ContN < 8):
            print('\n** Error. El serial debe contener 8 numeros. **')
        else:
            return True
    elif (indicador == 'modelo'):
        # Maximo 20 Caracteres
        if(len(validar) > 20):
            print('\n** Error. El modelo de un avion es de Maximo 20 Caracteres. **')
        else:
            return True
    elif (indicador == 'nombre'):
        # Maximo 12 Caracteres
        if(len(validar) > 12):
            print('\n** Error. El nombre de un avion es de Maximo 12 Caracteres. **')
        else:
            return True
    elif (indicador == 'piloto'):
        # Nombre del piloto Maximo 15 Caracteres
        if(len(validar) > 15):
            print('\n** Error. El nombre de un avion es de Maximo 12 Caracteres. **')
        else:
            return True


if __name__ == "__main__":
    main()
