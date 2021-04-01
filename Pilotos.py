class Piloto():

    def __init__(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setNombre(self, new_nombre):
        self.__nombre = new_nombre
