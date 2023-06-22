import csv   
import json
from funciones_normalizadoras import *
from funciones_contabilidad import *

dato_diccionario = {}
nombres_procesados = set()  # Conjunto para almacenar los nombres de los personajes procesados

with open('DBZ.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)

    for row in reader:
        id = int(row[0])
        nombre = row[1]
        raza = row[2]
        ataque = int(row[3])
        defensa = int(row[4])
        habilidad = row[5]

        # Normalizar los valores
        nombre_normalizado = normalizar_nombre(nombre)
        raza_normalizada = normalizar_raza(raza)
        habilidad_normalizada = normalizar_habilidad(habilidad)

        # Verificar si el nombre ya ha sido procesado (eliminacion de repeticion)
        if nombre_normalizado in nombres_procesados:
            continue  # Saltar a la siguiente iteración si el nombre está duplicado
        else:
            nombres_procesados.add(nombre_normalizado)  # Agregar el nombre al conjunto de nombres procesados

        # Guardar los datos normalizados en el diccionario
        dato_diccionario[id] = {
            "Nombre": nombre_normalizado,
            "Raza": raza_normalizada,
            "Poder de pelea": ataque,
            "Poder de ataque": defensa,
            "Habilidad": habilidad_normalizada
        }

# Guardar los datos en el diccionario por ID
diccionario_general = {}
for id, personaje in dato_diccionario.items():
    diccionario_general[id] = {
        "Nombre": personaje["Nombre"],
        "Raza": personaje["Raza"],
        "Poder de pelea": personaje["Poder de pelea"],
        "Poder de ataque": personaje["Poder de ataque"],
        "Habilidad": personaje["Habilidad"]
    }

# Guardar el diccionario en un archivo JSON
with open('DBZ_diccionario_general.json', 'w', encoding='utf-8') as file:
    json.dump(diccionario_general, file, indent=4, ensure_ascii=False)

################################################################--################################################################








# Convertir el diccionario a una cadena JSON con formato legible

# # Imprimir el diccionario con formato
# for id, datos in dato_diccionario.items():
#     print(f"ID: {id}")
#     for clave, valor in datos.items():
#         print(f"{clave}: {valor}")
#     print()  # Salto de línea entre cada ID

# Eliminar la clave 'id' del diccionario y normalizar los datos
