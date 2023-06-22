from funciones_normalizadoras import *
from funciones_contabilidad import calcular_promedio_poder
import csv
import json

def reemplazar_caracteres_especiales(texto):
    # Reemplazar caracteres especiales
    texto = texto.replace('\u00ed', 'í')
    texto = texto.replace('\u00f3', 'ó')
    # Agregar más reemplazos si es necesario

    return texto

def crear_diccionario_y_guardar():
    nuevo_diccionario = {}
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

            # Verificar si el nombre ya ha sido procesado (eliminación de repeticiones)
            if nombre_normalizado in nombres_procesados:
                continue  # Saltar a la siguiente iteración si el nombre está duplicado
            else:
                nombres_procesados.add(nombre_normalizado)  # Agregar el nombre al conjunto de nombres procesados

            # Calcular el promedio de pelea y ataque
            promedio_combate = calcular_promedio_poder(ataque, defensa)

            # Reemplazar caracteres especiales en la raza y habilidad
            raza_normalizada = [reemplazar_caracteres_especiales(r) for r in raza_normalizada]
            habilidad_normalizada = [reemplazar_caracteres_especiales(h) for h in habilidad_normalizada]

            # Guardar los datos normalizados en el diccionario
            nuevo_diccionario[nombre_normalizado] = {
                "Raza": ', '.join(raza_normalizada),
                "Promedio de Combate": promedio_combate,
                "Habilidad": ', '.join(habilidad_normalizada)
            }

    # Guardar el nuevo diccionario en un archivo JSON sin escape de caracteres Unicode
    with open('DBZ_diccionario_juego.json', 'w', encoding='utf-8') as file:
        json.dump(nuevo_diccionario, file, indent=4, ensure_ascii=False)

# Llamada a la función para crear el diccionario y guardar en el archivo JSON
crear_diccionario_y_guardar()
