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

hasho.insertar(Avion('AV1', 'MA1', 'A00000001'))
hasho.insertar(Avion('BV1', 'MB1', 'A00000002'))
hasho.insertar(Avion('CV1', 'MC1', 'A00000003'))

hasho.insertar(Avion('AV2', 'MA2', 'A00000004'))
hasho.insertar(Avion('BV2', 'MB2', 'A00000005'))
hasho.insertar(Avion('CV2', 'MC2', 'A00000006'))

hasho.insertar(Avion('AV3', 'MA3', 'A00000007'))
hasho.insertar(Avion('BV3', 'MB3', 'A00000008'))
hasho.insertar(Avion('CV3', 'MC3', 'A00000009'))

hasho.insertar(Avion('AV4', 'MA4', 'A00000010'))
hasho.insertar(Avion('BV4', 'MB4', 'A00000011'))
hasho.insertar(Avion('CV4', 'MC4', 'A00000012'))

hasho.insertar(Avion('AV5', 'MA5', 'A00000013'))
hasho.insertar(Avion('BV5', 'MB5', 'A00000014'))
hasho.insertar(Avion('CV5', 'MC5', 'A00000015'))

# Avion('NP1', 'MP1', 'A00000016')

hasho.eliminar('A00000005')

hasho.print()

def main():
    
    # TODO: CARGAR LOS DATOS EN EL HASH TABLE

    print(" <-- Bienvenido a la Base de Datos de Aviones de Occidente Aviocc! -->")

    
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
        if(validaciones(serial,'serial')):
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
        print(' \-- Se ha agregado el avion a la base de datos --/')
        
        


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
                serial = hasho.busquedaPorNombre(nombre)['avion']['serial']

        elif menu.opcion == '3':
            while True:
                modelo = input('Ingrese modelo de avion: ')
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
                print("\n** Opcion no valida intente otra vez **")


    else:
        print('\n\-- Avion no encontrado. --/')

def asignarPiloto():
    # TODO:
    pass

def liberarPiloto():
    # TODO:
    pass

def eliminarAvion(serial):
    hasho.eliminar(serial)
    print('\n\-- Se ha eliminado el avion con Exito! --/')
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
            print('\n** Error. El serial de un Avion es de 9 Digitos. **')
        # El primer digito es una letra
        elif not(validar[0].isalpha()):
            print('\n** Error. El primer digito del Serial debe ser una letra. **')
        # El serial contiene una sola letra en mayuscula
        elif not(validar[0].isupper()):
            print('\n** Error. El primer digito del Serial debe ser una letra en Mayusculas. **')
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
            

if __name__ == "__main__":
    main()
