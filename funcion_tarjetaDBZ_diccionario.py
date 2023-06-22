import json
import copy
from funciones_tarjeta_DBZ import generar_codigo_personaje

def cargar_diccionario_general():
    with open("DBZ_diccionario_general.json", encoding="utf-8") as file:
        diccionario_general = json.load(file)
    return diccionario_general

def agregar_codigos_personajes(diccionario_personajes):

    diccionario_con_codigos = copy.deepcopy(diccionario_personajes)

    for personaje_id, personaje in diccionario_con_codigos.items():
        codigo = generar_codigo_personaje(personaje_id, personaje)
        personaje["Código"] = codigo

    return diccionario_con_codigos


def ejecutar_diccionario_tarjetas():

    diccionario_general = cargar_diccionario_general()

    diccionario_con_codigos = agregar_codigos_personajes(diccionario_general)

    with open("DBZ_diccionario_tarjetas.json", "w", encoding="utf-8") as file:
        json.dump(diccionario_con_codigos, file, indent=4, ensure_ascii=False)

    print("Se ha creado el archivo 'DBZ_diccionario_tarjetas.json' con los códigos de los personajes.")
