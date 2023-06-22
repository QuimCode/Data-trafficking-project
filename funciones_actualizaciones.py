import json
import csv


with open('DBZ_diccionario_general.json', 'r', encoding='utf-8') as file:
    diccionario_general = json.load(file)

def actualizar_personajes_saiyan():

    personajes_saiyan_actualizados = []
    for personaje in diccionario_general.items():
        if 'Saiyan' in personaje['Raza']:
            personaje['Poder de pelea'] = int(personaje['Poder de pelea'] * 1.5)
            personaje['Poder de ataque'] = int(personaje['Poder de ataque'] * 1.7)
            personaje['Habilidad'].append('Transformación nivel dios')
            personajes_saiyan_actualizados.append(personaje)

    nombre_archivo = 'Saiyan_Actualizados.csv'
    with open(nombre_archivo, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Nombre', 'Raza', 'Poder de pelea', 'Poder de ataque', 'Habilidad'])
        writer.writeheader()
        writer.writerows(personajes_saiyan_actualizados)

    print(f"Se han actualizado y guardado los personajes Saiyan en el archivo '{nombre_archivo}'.")