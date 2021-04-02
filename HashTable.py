from Avion import *
from ListaEnlazada2 import *


class HashTable():

    def __init__(self):
        self.hash = [

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]
            ],

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]

            ],

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]
            ]
        ]
        self.indicesNombres = []
        self.indicesModelo = []

    def AddAvion(self, avion):

        serial = avion.serial
        codigo = serial[1:]
        codigo = int(codigo)
        residuo = codigo % 3

        # VALIDAR DE QUE EL AVION CON ESE SERIAL NO ESTE REGISTRADO YA EN EL HASH TABLE
        if self.isAvionRegistered(residuo, serial):

            print("***ERROR***")
            print("EL AVION CON ESE SERIAL YA SE ENCUENTRA REGISTRADO!!!")

        else:

            espacio_disp = False
            indice_I = -1
            indice_J = -1
            print("serial", serial)
            print("residuo", residuo)

            for i in range(len(self.hash[residuo])):

                for j in range(len(self.hash[residuo][i])):

                    if self.hash[residuo][i][j] == None:
                        espacio_disp = True
                        indice_I = i
                        indice_J = j
                    if espacio_disp:
                        break
                if espacio_disp:
                    break

            if espacio_disp:
                print("i", indice_I)
                print("j", indice_J)
                self.hash[residuo][indice_I][indice_J] = avion

                self.indicesNombres.append(
                    {'name': avion.name, 'serial': avion.serial})

                self.indicesModelo.append(
                    {'modelo': avion.modelo, 'serial': avion.serial})

                self.indicesNombres.sort(key=self.sortByName)
                self.indicesModelo.sort(key=self.sortByModel)
            else:
                print("NO HAY MAS ESPACIO PARA AGREGAR ESTE AVION")

    def sortByName(self, e):
        return e['name']

    def sortByModel(self, e):
        return e['modelo']

    def eliminarAvionSerial(self, serial):

        serial = serial
        codigo = serial[1:]
        codigo = int(codigo)
        residuo = codigo % 3

        if self.isAvionRegistered(residuo, serial):
            encontrado = False
            for x in range(len(self.hash[residuo])):

                for y in range(len(self.hash[residuo][x])):

                    if self.hash[residuo][x][y] != None:

                        if self.hash[residuo][x][y].serial == serial:
                            encontrado = True
                            break
                if encontrado:
                    break

            if encontrado:
                self.hash[residuo][x][y] = None
                # CORRER LA FUNCION PARA ORDENAR EL HASH
                self.ordenarHash(residuo)

            else:
                print("EL AVION CON ESE SERIAL NO SE ENCUENTRA REGISTRADO!!!")

        else:

            print("***ERROR***")
            print("EL AVION CON ESE SERIAL NO SE ENCUENTRA REGISTRADO!!!")

    def isAvionRegistered(self, residuo, serial):

         # VALIDAR DE QUE EL AVION CON ESE SERIAL NO ESTE REGISTRADO YA EN EL HASH TABLE
        registrado = False
        for x in range(len(self.hash[residuo])):

            for y in range(len(self.hash[residuo][x])):

                if self.hash[residuo][x][y] != None:
                    if self.hash[residuo][x][y].serial == serial:
                        registrado = True
                        break
            if registrado:
                break
        if registrado:
            return True
        else:
            return False

    def ordenarHash(self, residuo):
        new_hash = []

        for x in range(len(self.hash[residuo])):

            for y in range(len(self.hash[residuo][x])):

                new_hash.append(self.hash[residuo][x][y])

        self.hash = [

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]
            ],

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]

            ],

            [
                [None, None], [None, None], [None, None], [
                    None, None], [None, None], [None, None], [None, None]
            ]
        ]

        indiceNewHash = 0
        print(new_hash)
        finish = False
        print("======",new_hash)
        for x in range(len(self.hash[residuo])):

            for y in range(len(self.hash[residuo][x])):
                cambio = False

                while indiceNewHash < len(new_hash):
                    if new_hash[indiceNewHash] == None:

                        indiceNewHash += 1
                    else:

                        self.hash[residuo][x][y] = new_hash[indiceNewHash]
                        indiceNewHash += 1
                        cambio = True
                        break
                if cambio:
                    continue
