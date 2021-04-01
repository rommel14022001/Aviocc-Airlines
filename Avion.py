from SerializationFunctions import *


class Avion():

    def __init__(self, nombre, modelo, serial):
        self.__name = nombre
        self.__serial = serial
        self.__modelo = modelo
        # self.piloto

    def getName(self):
        return self.__name

    def getSerial(self):
        return self.__serial

    def getModelo(self):
        return self.__modelo

    def setName(self, new_name):
        self.__name = new_name

    def setSerial(self, new_serial):
        self.__serial = new_serial

    def setModelo(self, new_modelo):
        self.__modelo = new_modelo
