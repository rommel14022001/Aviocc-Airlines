import pickle
import os


def recibir_datos_del_txt(nombre_txt, datos):

    lectura_binaria = open(nombre_txt, 'rb')

    if os.stat(nombre_txt).st_size != 0:
        datos = pickle.load(lectura_binaria)

    lectura_binaria.close()

    return datos


def cargar_datos_en_txt(nombre_txt, datos):

    escritura_binaria = open(nombre_txt, 'wb')

    datos = pickle.dump(datos, escritura_binaria)

    escritura_binaria.close()
