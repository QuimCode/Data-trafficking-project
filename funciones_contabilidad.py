from diccionario_datos import *

def listar_cantidad_por_raza(diccionario):
    
    cantidad_por_raza = {}

    for personaje in diccionario.values():
        razas = personaje["Raza"]

        if isinstance(razas, list):
            for raza in razas:
                if raza in cantidad_por_raza:
                    cantidad_por_raza[raza] += 1
                else:
                    cantidad_por_raza[raza] = 1
        else:
            if razas in cantidad_por_raza:
                cantidad_por_raza[razas] += 1
            else:
                cantidad_por_raza[razas] = 1

    for raza, cantidad in cantidad_por_raza.items():
        print(f"Raza: {raza} - Cantidad: {cantidad}")


def listar_personajes_por_raza(diccionario):
    personajes_por_raza = {}

    for id, personaje in diccionario.items():
        razas = personaje["Raza"]

        for raza in razas:
            raza_key = raza.strip()

            if raza_key in personajes_por_raza:
                personajes_por_raza[raza_key].append(personaje)
            else:
                personajes_por_raza[raza_key] = [personaje]

    for raza, personajes in personajes_por_raza.items():
        print(f"Raza: {raza}")
        for personaje in personajes:
            nombre = personaje["Nombre"]
            poder_ataque = personaje["Poder de ataque"]
            print(f"Nombre: {nombre} - Poder de ataque: {poder_ataque}")
        print()


def calcular_promedio_poder(poder_pelea, poder_ataque):
    return (poder_pelea + poder_ataque) / 2


def buscar_personaje_por_habilidad(diccionario):
    habilidad_buscar = input("Ingrese la descripción de la habilidad: ")

    personajes_encontrados = []

    for personaje in diccionario.values():
        habilidades_personaje = personaje.get("Habilidad", [])

        if habilidad_buscar in habilidades_personaje:
            personajes_encontrados.append(personaje)

    if personajes_encontrados:
        for personaje in personajes_encontrados:
            nombre = personaje["Nombre"]
            raza = personaje["Raza"]
            poder_pelea = personaje["Poder de pelea"]
            poder_ataque = personaje["Poder de ataque"]
            promedio_poder = calcular_promedio_poder(poder_pelea, poder_ataque)

            print("\nNombre:", nombre)
            print("Raza:", raza)
            print("Promedio de poder:", promedio_poder)
    else:
        print("No se encontraron personajes con esa habilidad.")