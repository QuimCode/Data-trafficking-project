import json

# Importar el diccionario desde el archivo JSON
with open('DBZ_diccionario_general.json', 'r', encoding='utf-8') as file:
    diccionario_general = json.load(file)

def generar_listado_personajes():
    # Solicitar la raza y habilidad al usuario
    raza = input("Ingrese la raza buscada: ").lower()
    habilidad_busqueda = input("Ingrese la habilidad buscada: ").lower()

    if raza.isdigit():
        print("Error: La raza no puede ser un número. Por favor, ingrese un nombre válido.")
        return

    if habilidad_busqueda.isdigit():
        print("Error: La habilidad no puede ser un número. Por favor, ingrese una habilidad válida.")
        return
    
    # Obtener los personajes que cumplen con los criterios de raza y habilidad
    personajes_que_cumplen = []
    for personaje in diccionario_general.values():
        if raza in personaje['Raza'] and habilidad_busqueda in personaje['Habilidad']:
            habilidades = ", ".join(personaje['Habilidad'])
            personajes_que_cumplen.append(f"{personaje['Nombre']} - {personaje['Poder de pelea']} - {habilidades}")

    # Si no se encontraron resultados, sugerir revisar mayúsculas y espacios
    if not personajes_que_cumplen:
        print("No se encontraron personajes con los criterios especificados. Por favor, revise las mayúsculas y los espacios en blanco.")
        return

    # Crear una lista de resultados con los datos requeridos
    resultados = []
    for personaje in personajes_que_cumplen:
        nombre, poder_ataque, habilidades = personaje.split(' - ')
        otras_habilidades = [habilidad for habilidad in habilidades.split(', ') if habilidad != habilidad_busqueda]
        resultado = f"{nombre} - {poder_ataque} - {', '.join(otras_habilidades)}"
        resultados.append(resultado)

    # Guardar los resultados en un archivo JSON
    nombre_archivo = f"{raza}_{habilidad_busqueda}.json"
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        json.dump(resultados, file, indent=4, ensure_ascii=False)


def leer_archivo_json():
    raza = input("Ingrese la raza del archivo que busco con anterioridad: ")
    habilidad_busqueda = input("Ingrese la habilidad del archivo que busco con anterioridad: ")

    if raza.isdigit():
        print("Error: La raza no puede ser un número. Por favor, ingrese un nombre válido.")
        return

    if habilidad_busqueda.isdigit():
        print("Error: La habilidad no puede ser un número. Por favor, ingrese una habilidad válida.")
        return

    # Construir el nombre del archivo
    nombre_archivo = f"{raza}_{habilidad_busqueda}.json"

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            personajes = json.load(file)
            for personaje in personajes:
                print(personaje)
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'. Verifique la raza y habilidad ingresadas, RECUERDE, deben ser las anteriormente buscadas.")