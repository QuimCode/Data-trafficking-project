import json

def ordenar_personajes_por_atributo(lista_personajes, atributo, orden):
    lista_ordenada = sorted(lista_personajes.items(), key=lambda x: x[1][atributo], reverse=not orden)
    return lista_ordenada

with open('DBZ_diccionario_general.json', encoding='utf-8') as file:
    diccionario_general = json.load(file)

def ordenar_personajes(diccionario_personajes):
    atributo = input("Ingrese el atributo por el cual desea ordenar los personajes: ")

    while True:
        ascendente_input = input("¿Desea ordenar de forma ascendente? (True/False): ")
        if ascendente_input.lower() in ['true', 'false']:
            ascendente = ascendente_input.lower() == 'true'  # Convertir a booleano
            break
        else:
            print("¡Entrada inválida! Por favor, ingrese 'True' o 'False'.")

    personajes_ordenados = ordenar_personajes_por_atributo(diccionario_personajes, atributo, ascendente)
    for personaje in personajes_ordenados:
        print(personaje)

def ejecutar_ordenamiento():
    ordenar_personajes(diccionario_general)
