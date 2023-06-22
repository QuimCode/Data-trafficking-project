import csv   
import json
from funciones_normalizadoras import *
from funciones_contabilidad import *

dato_diccionario = {}
nombres_procesados = set()

with open('DBZ.csv', 'r', encoding='utf-8-sig') as file:
    lectura = csv.reader(file)

    for fila in lectura:
        id = int(fila[0])
        nombre = fila[1]
        raza = fila[2]
        ataque = int(fila[3])
        defensa = int(fila[4])
        habilidad = fila[5]

        nombre_normalizado = normalizar_nombre(nombre)
        raza_normalizada = normalizar_raza(raza)
        habilidad_normalizada = normalizar_habilidad(habilidad)

        if nombre_normalizado in nombres_procesados:
            continue  
        else:
            nombres_procesados.add(nombre_normalizado) 

        dato_diccionario[id] = {
            "Nombre": nombre_normalizado,
            "Raza": raza_normalizada,
            "Poder de pelea": ataque,
            "Poder de ataque": defensa,
            "Habilidad": habilidad_normalizada
        }


diccionario_general = {}
for id, personaje in dato_diccionario.items():
    diccionario_general[id] = {
        "Nombre": personaje["Nombre"],
        "Raza": personaje["Raza"],
        "Poder de pelea": personaje["Poder de pelea"],
        "Poder de ataque": personaje["Poder de ataque"],
        "Habilidad": personaje["Habilidad"]
    }


with open('DBZ_diccionario_general.json', 'w', encoding='utf-8') as file:
    json.dump(diccionario_general, file, indent=4, ensure_ascii=False)

################################################################--################################################################