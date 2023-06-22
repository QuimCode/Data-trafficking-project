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

# Imprimir los personajes ordenados
# Imprimir los personajes ordenados
# for personaje in personajes_ordenados:
#     clave = personaje[0]
#     valor = personaje[1]
#     print(clave, valor)