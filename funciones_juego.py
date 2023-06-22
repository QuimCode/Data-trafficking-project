import json
import random
from datetime import datetime

def jugar_batalla():
    with open('DBZ_diccionario_juego.json', 'r', encoding='utf-8') as file:
        diccionario_juego = json.load(file)

    personaje_usuario = input("Selecciona un personaje: ")

    if personaje_usuario not in diccionario_juego:
        print("El personaje seleccionado no existe, recuerde ingresar su nombre y no un ID o numero.")
        return
    
    # if personaje_usuario.isdigit():
    #     print("Error: La raza no puede ser un número. Por favor, ingrese un nombre válido.")
    #     return

    oponente = random.choice(list(diccionario_juego.keys()))

    poder_ataque_usuario = diccionario_juego[personaje_usuario]["Promedio de Combate"]
    poder_ataque_oponente = diccionario_juego[oponente]["Promedio de Combate"]

    if poder_ataque_usuario > poder_ataque_oponente:
        ganador = personaje_usuario
        perdedor = oponente
    elif poder_ataque_usuario < poder_ataque_oponente:
        ganador = oponente
        perdedor = personaje_usuario
    else:
        print("¡Es un empate!")
        return

    fecha_batalla = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resultado_batalla = f"\nFecha: {fecha_batalla}\nGanador: {ganador} ---&--- Perdedor: {perdedor}"

    with open('resultados_batallas.txt', 'a') as file:
        file.write(resultado_batalla + "\n")
