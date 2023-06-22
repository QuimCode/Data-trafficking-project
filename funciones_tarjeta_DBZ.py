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

    codigo = f"\n{nombre[0]}-{ganador}-{valor_maximo}-{id_personaje}\n"
    return codigo

def generar_codigo_personaje_menu(diccionario):
    id_personaje = input("Ingrese el ID del personaje: ")
    personaje = diccionario.get(id_personaje)
    if personaje:
        codigo = generar_codigo_personaje(id_personaje, personaje)
        print(codigo)
    else:
        print("No se encontró un personaje con el ID ingresado.")

def ejecutar_menu():
    # Cargar el diccionario de personajes desde el archivo
    diccionario_general = cargar_diccionario_general()

    # Solicitar al usuario que ingrese el ID del personaje
    id_personaje = input("Ingrese el ID del personaje: ")

    # Obtener el personaje correspondiente al ID ingresado
    personaje = diccionario_general.get(id_personaje)

    # Verificar si se encontró un personaje con el ID ingresado
    if personaje:
        # Generar el código para el personaje
        codigo = generar_codigo_personaje(id_personaje, personaje)
        print(codigo)
    else:
        print("No se encontró un personaje con el ID ingresado.")