import json

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

def generar_codigo_personaje_menu(diccionario):
    id_personaje = input("Ingrese el ID del personaje: ")
    personaje = diccionario.get(id_personaje)
    if personaje:
        codigo = generar_codigo_personaje(id_personaje, personaje)
        print(f"\n{codigo}\n")
    else:
        print("No se encontró un personaje con el ID ingresado.")

def ejecutar_menu():
    diccionario_general = cargar_diccionario_general()

    generar_codigo_personaje_menu(diccionario_general)
