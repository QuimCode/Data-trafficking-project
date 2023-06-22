import json

def ordenar_personajes_por_atributo(lista_personajes, atributo, orden):
    lista_ordenada = sorted(lista_personajes.items(), key=lambda x: x[1][atributo], reverse=not orden)
    return lista_ordenada

# Cargar el archivo JSON
with open('DBZ_diccionario_general.json', encoding='utf-8') as file:
    diccionario_general = json.load(file)

# Llamar a la función ordenar_personajes_por_atributo con los parámetros adecuados
atributo = "Poder de ataque"
orden_ascendente = True
personajes_ordenados = ordenar_personajes_por_atributo(diccionario_general, atributo, orden_ascendente)

def ordenar_personajes(diccionario_personajes):
    atributo = input("Ingrese el atributo por el cual desea ordenar los personajes: ")

    while True:
        ascendente_input = input("¿Desea ordenar de forma ascendente? (True/False): ")
        if ascendente_input.lower() in ['true', 'false']:
            ascendente = ascendente_input.lower() == "true"
            break
        else:
            print("¡Entrada inválida! Por favor, ingrese 'True' o 'False'.")

    personajes_ordenados = ordenar_personajes_por_atributo(diccionario_personajes, atributo, ascendente)
    for personaje in personajes_ordenados:
        print(personaje)

def ejecutar_ordenamiento():
    ordenar_personajes(diccionario_general)
