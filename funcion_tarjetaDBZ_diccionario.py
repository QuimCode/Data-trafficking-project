import json
import copy

def cargar_diccionario_general():
    with open("DBZ_diccionario_general.json", encoding="utf-8") as file:
        diccionario_general = json.load(file)
    return diccionario_general

def generar_codigo_personaje(personaje_id, personaje):
    nombre = personaje["Nombre"]
    ganador = ""

    if personaje["Poder de ataque"] > personaje["Poder de pelea"]:
        ganador = "A"
    elif personaje["Poder de ataque"] < personaje["Poder de pelea"]:
        ganador = "P"
    else:
        ganador = "AP"

    valor_maximo = max(personaje["Poder de ataque"], personaje["Poder de pelea"])
    id_personaje = str(personaje_id).zfill(9)

    codigo = f"{nombre[0]}-{ganador}-{valor_maximo}-{id_personaje}"
    return codigo

def agregar_codigos_personajes(diccionario_personajes):
    # Realizar una copia del diccionario para evitar sobrescribir el original
    diccionario_con_codigos = copy.deepcopy(diccionario_personajes)

    # Utilizar la función generar_codigo_personaje para agregar el código a cada personaje
    for personaje_id, personaje in diccionario_con_codigos.items():
        codigo = generar_codigo_personaje(personaje_id, personaje)
        personaje["Código"] = codigo

    return diccionario_con_codigos


def ejecutar_diccionario_tarjetas():
    # Cargar el diccionario general desde el archivo
    diccionario_general = cargar_diccionario_general()

    # Agregar los códigos a cada personaje en una copia del diccionario
    diccionario_con_codigos = agregar_codigos_personajes(diccionario_general)

    # Guardar el diccionario modificado en un nuevo archivo JSON
    with open("DBZ_diccionario_tarjetas.json", "w", encoding="utf-8") as file:
        json.dump(diccionario_con_codigos, file, indent=4, ensure_ascii=False)

    print("Se ha creado el archivo 'DBZ_diccionario_tarjetas.json' con los códigos de los personajes.")
