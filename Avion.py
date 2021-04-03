from SerializationFunctions import *


class Avion():

    def __init__(self, nombre, modelo, serial):
        self.name = nombre
        self.serial = serial
        self.modelo = modelo
        self.piloto = None
        self.siguiente = None
