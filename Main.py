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
            insercion()
        elif menu.opcion == '2':
            busqueda()
        elif menu.opcion == '3':
            # TODO: GUARDAR NUEVO HASH TABLE EN BROMA
            print('\nSe ha terminado el programa.')
            break
        else:
            print("\nOpcion no valida intente otra vez")

    

def insercion():
    # TODO
    print('\n<-- REGISTRO DE NUEVO AVION -->')
    while True:
        
        serial = input('\nIngrese el serial del avion: ')
        # Validar que sea unico

        if(validaciones(serial,'serial')):

            modelo = input('\nIngrese el modelo del avion: ')
            # Validar que sea unico
            
            if(validaciones(modelo, 'modelo')):
                
                nombre = input('\nIngrese el nombre del avion: ')
                # Validar que sea unico
                if(validaciones(nombre, 'nombre')):
                    break
        
        
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
            
            while True:
                serial = input('Ingrese serial de avion: ')
                # VALIDACIONES
                if (validaciones(serial, 'serial')):
                    break
            
        elif menu.opcion == '2':
            while True:
                nombre = input('Ingrese nombre de avion: ')
                # VALIDACIONES
                if (validaciones(nombre, 'nombre')):
                    break

            if hasho.busquedaPorNombre(nombre):
                serial = hasho.busquedaPorNombre(nombre)['serial']

        elif menu.opcion == '3':
            while True:
                modelo = input('Ingrese modelo de avion: ')
                # VALIDACIONES
                if (validaciones(modelo, 'modelo')):
                    break

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
    print('\nSe ha eliminado el avion con Exito!')
    # TODO: MENSAJE DE EXISTO
    pass


def validaciones(validar, indicador):
    if(indicador == 'serial'):
        contA = 0
        ContN = 0
        for c in validar:
            if (c.isalpha()):
                contA+=1
            if(c.isdigit()):
                ContN+=1
        # El serial es de 9 caracteres
        if(len(validar) < 9):
            print('\nError. El serial de un Avion es de 9 Digitos.')
        # El primer digito es una letra
        elif not(validar[0].isalpha()):
            print('\nError. El primer digito del Serial debe ser una letra.')
        # El serial contiene una sola letra en mayuscula
        elif not(validar[0].isupper()):
            print('\nError. El primer digito del Serial debe ser una letra en Mayusculas.')
        # El serial contiene una sola letra
        elif(contA > 1):
            print('\nError. El serial solo debe contener un Caracter Alfabetico.')
        # El serial contiene 8 Digitos
        elif(ContN > 8 or ContN < 8):
            print('\nError. El serial debe contener 8 numeros.')
        else:
            return True
    elif (indicador == 'modelo'):
        # Maximo 20 Caracteres
        if(len(validar) > 20):
            print('\nError. El modelo de un avion es de Maximo 20 Caracteres.')
        else:
            return True
    elif (indicador == 'nombre'):
        # Maximo 12 Caracteres
        if(len(validar) > 12):
            print('\nError. El nombre de un avion es de Maximo 12 Caracteres.')
        else:
            return True
            

if __name__ == "__main__":
    main()
