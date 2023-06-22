from funciones_normalizadoras import *
from funciones_contabilidad import calcular_promedio_poder
import csv
import json

def crear_diccionario_y_guardar():
    nuevo_diccionario = {}
    nombres_procesados = set()  # Conjunto para almacenar los nombres de los personajes procesados

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

            promedio_combate = int(calcular_promedio_poder(ataque, defensa))

            nuevo_diccionario[nombre_normalizado] = {
                "Raza": ', '.join(raza_normalizada),
                "Promedio de Combate": promedio_combate,
                "Habilidad": ', '.join(habilidad_normalizada)
            }


    with open('DBZ_diccionario_juego.json', 'w', encoding='utf-8') as file:
        json.dump(nuevo_diccionario, file, indent=4, ensure_ascii=False)

crear_diccionario_y_guardar()
