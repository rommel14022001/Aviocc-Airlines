from Avion import *


class HashTable():

    def __init__(self):
        self.table = [
            [
                [None, None], [None, None], [None, None],
                [None, None], [None, None], [None, None], [None, None]
            ],
            [
                [None, None], [None, None], [None, None],
                [None, None], [None, None], [None, None], [None, None]
            ],
            [
                [None, None], [None, None], [None, None],
                [None, None], [None, None], [None, None], [None, None]
            ],
        ]
        self.indicesNombres = []
        self.indicesModelo = []
        self.indicesPiloto = []

    # hash function
    # @param serial: string ej.'A61023124'
    # @returns indice: number [0,2] en hash table
    def hash(self, serial):
        return int(serial[1:]) % 3

    # busqueda de posicion libre en matrix
    # @returns pocision: vector(i, j, k) | None si no hay espacio | False si ya existe un avion con algun dato repetido
    def buscarPosicionLibre(self, serial):
        i = self.hash(serial)
        res = []

        for j in range(7):
            for k in range(2):
                if self.table[i][j][k] == None:
                    res = [i, j, k]
                    return res
                elif self.table[i][j][k].serial == serial:
                    return False

        return None

    # busqueda de posicion ocupada en matrix
    # @returns pocision: vector(i, j, k) | None si no existe avion con serial
    def buscarPosicionPorSerial(self, serial):
        i = self.hash(serial)       # Busqueda Hash

        for j in range(7):          # Busqueda Secuencial
            for k in range(2):
                if self.table[i][j][k] != None:
                    if self.table[i][j][k].serial == serial:
                        return [ i, j, k ]

        return None

    def getAvion(self, serial):
        if not serial:
            return None
        posicion = self.buscarPosicionPorSerial(serial)

        if posicion:
            return self.table[ posicion[0] ][ posicion[1] ][ posicion[2] ]
        else:
            return None

    def insertarEnIndices(self, avion):
        self.indicesNombres.append(
            {'name': avion.name, 'serial': avion.serial})

        self.indicesModelo.append(
            {'modelo': avion.modelo, 'serial': avion.serial})

        self.indicesNombres.sort(key=self.sortByName)
        self.indicesModelo.sort(key=self.sortByModel)

    def insertarEnIndicePiloto(self, avion):
        self.indicesPiloto.append(
            { 'piloto': avion.piloto, 'serial': avion.serial }
        )
        self.indicesPiloto.sort(key=self.sortByPilot)

    def eliminarEnIndicePiloto(self, avion):
        if avion.piloto:
            self.indicesPiloto.pop(self.busquedaPorPiloto(avion.piloto)['indice'])


    def eliminarEnIndices(self, avion):
        self.indicesModelo.pop(self.busquedaPorModelo(avion.modelo)['indice'])
        self.indicesNombres.pop(self.busquedaPorNombre(avion.name)['indice'])


    def print(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                for k in range(len(self.table[i][j])):
                    print(' ', end='')
                    if self.table[i][j][k]:
                        print(f'{self.table[i][j][k].piloto}', end='')
                    else:
                        print('NONE', end='')
                print(' | ', end='')
            print('\n')

    def insertar(self, avion):
        posicion = self.buscarPosicionLibre(avion.serial)
        repetido = False

        if self.busquedaPorModelo(avion.modelo) or self.busquedaPorNombre(avion.name):
            repetido = True

        if not repetido:
            if posicion:
                i = posicion[0]
                j = posicion[1]
                k = posicion[2]
                self.table[i][j][k] = avion
                self.insertarEnIndices(avion)
                return True
            elif posicion == None:
                print("\n** NO HAY MAS ESPACIO PARA AGREGAR ESTE AVION **")
            elif posicion == False:
                print("\n** YA SE ENCUENTRA REGISTRADO UN AVION CON ESE SERIAL **")
        else:
            print("\n** YA SE ENCUENTRA UN AVION REGISTRADO CON UNO DE LOS DATOS INGRESADOS. **")

    def eliminar(self, serial):
        posicion = self.buscarPosicionPorSerial(serial)

        if posicion:
            i = posicion[0]
            j = posicion[1]
            k = posicion[2]
            avion = self.table[i][j][k]
            arr = []
            for x in range(7):
                for y in range(2):
                    arr.append(self.table[i][x][y])
            arr.pop(j * 2 + k)
            arr.append(None)

            newArr = []

            for e in range(0, 14, 2):
                newArr.append([ arr[e], arr[e + 1] ])

            self.table[i] = newArr
            self.eliminarEnIndices(avion)
        else:
            print("\n\-- NO EXISTE AVION CON ESTE SERIAL --/")

    def AddAvion(self, avion):

        serial = avion.serial
        codigo = serial[1:]
        codigo = int(codigo)
        residuo = codigo % 3

        # VALIDAR DE QUE EL AVION CON ESE SERIAL NO ESTE REGISTRADO YA EN EL HASH TABLE
        if self.isAvionRegistered(residuo, serial):

            print("\n***ERROR***")
            print("\-- EL AVION CON ESE SERIAL YA SE ENCUENTRA REGISTRADO!!! --/")

        else:

            espacio_disp = False
            indice_I = -1
            indice_J = -1
            print("serial", serial)
            print("residuo", residuo)

            for i in range(len(self.table[residuo])):

                for j in range(len(self.table[residuo][i])):

                    if self.table[residuo][i][j] == None:
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
                self.table[residuo][indice_I][indice_J] = avion

                self.indicesNombres.append(
                    {'name': avion.name, 'serial': avion.serial})

                self.indicesModelo.append(
                    {'modelo': avion.modelo, 'serial': avion.serial})

                self.indicesNombres.sort(key=self.sortByName)
                self.indicesModelo.sort(key=self.sortByModel)
            else:
                print("\n** NO HAY MAS ESPACIO PARA AGREGAR ESTE AVION **")

    def sortByName(self, e):
        return e['name']

    def sortByModel(self, e):
        return e['modelo']

    def sortByPilot(self, e):
        return e['piloto']

    def eliminarAvionSerial(self, serial):

        serial = serial
        codigo = serial[1:]
        codigo = int(codigo)
        residuo = codigo % 3

        if self.isAvionRegistered(residuo, serial):
            encontrado = False
            for x in range(len(self.table[residuo])):

                for y in range(len(self.table[residuo][x])):

                    if self.table[residuo][x][y] != None:

                        if self.table[residuo][x][y].serial == serial:
                            encontrado = True
                            break
                if encontrado:
                    break

            if encontrado:
                avion = self.buscarAvion(residuo, serial)
                if avion != None:
                    self.eliminarEnIndices(avion)

                self.table[residuo][x][y] = None
                # CORRER LA FUNCION PARA ORDENAR EL HASH
                self.ordenarHash(residuo)

            else:
                print("\n** EL AVION CON ESE SERIAL NO SE ENCUENTRA REGISTRADO!!! **")

        else:

            print("\n***ERROR***")
            print("\-- EL AVION CON ESE SERIAL NO SE ENCUENTRA REGISTRADO!!! --/")

    def isAvionRegistered(self, residuo, serial):

         # VALIDAR DE QUE EL AVION CON ESE SERIAL NO ESTE REGISTRADO YA EN EL HASH TABLE
        registrado = False
        for x in range(len(self.table[residuo])):

            for y in range(len(self.table[residuo][x])):

                if self.table[residuo][x][y] != None:
                    if self.table[residuo][x][y].serial == serial:
                        registrado = True
                        break
            if registrado:
                break
        if registrado:
            return True
        else:
            return False

    def buscarAvion(self, residuo, serial):
        # FUNCION QUE TE RETORNA UN AVION DEL HASH "SI EXISTE"

        avion = None
        for x in range(len(self.table[residuo])):

            for y in range(len(self.table[residuo][x])):

                if self.table[residuo][x][y] != None:
                    if self.table[residuo][x][y].serial == serial:
                        avion = self.table[residuo][x][y]
                        break
            if avion != None:
                break

        return avion

    def ordenarHash(self, residuo):
        new_hash = []

        for x in range(len(self.table[residuo])):

            for y in range(len(self.table[residuo][x])):

                new_hash.append(self.table[residuo][x][y])

        self.table = [

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
        print("======", new_hash)
        for x in range(len(self.table[residuo])):

            for y in range(len(self.table[residuo][x])):
                cambio = False

                while indiceNewHash < len(new_hash):
                    if new_hash[indiceNewHash] == None:

                        indiceNewHash += 1
                    else:

                        self.table[residuo][x][y] = new_hash[indiceNewHash]
                        indiceNewHash += 1
                        cambio = True
                        break
                if cambio:
                    continue

    def busquedaPorNombre(self, nombre):
        low = 0
        high = len(self.indicesNombres) - 1

        while low <= high:

            mid = (high + low) // 2

            if self.indicesNombres[mid]['name'] < nombre:
                low = mid + 1

            elif self.indicesNombres[mid]['name'] > nombre:
                high = mid - 1

            else:
                return { 'avion': self.indicesNombres[mid], 'indice': mid }

        return None

    def busquedaPorModelo(self, modelo):
        low = 0
        high = len(self.indicesModelo) - 1

        while low <= high:

            mid = (high + low) // 2

            if self.indicesModelo[mid]['modelo'] < modelo:
                low = mid + 1

            elif self.indicesModelo[mid]['modelo'] > modelo:
                high = mid - 1

            else:
                return { 'avion': self.indicesModelo[mid], 'indice': mid }

        return None
    
    def busquedaPorPiloto(self, piloto):
        low = 0
        high = len(self.indicesPiloto) - 1

        while low <= high:

            mid = (high + low) // 2

            if self.indicesPiloto[mid]['piloto'] < piloto:
                low = mid + 1

            elif self.indicesPiloto[mid]['piloto'] > piloto:
                high = mid - 1

            else:
                return { 'avion': self.indicesPiloto[mid], 'indice': mid }

        return None

    def asignarPiloto(self, avion, piloto):

        if piloto:
            if not self.busquedaPorPiloto(piloto):  # Si no existe piloto:
                avion.piloto = piloto
                self.insertarEnIndicePiloto(avion)
            else:
                # TODO: MENSAJE DE REPETIDO
                print('YA EXISTE PILOTO EN OTRO AVION')
        else:
                self.eliminarEnIndicePiloto(avion)
                avion.piloto = piloto