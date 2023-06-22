import re
from unidecode import unidecode

def normalizar_nombre(nombre):
    # Eliminar espacios adicionales
    nombre_normalizado = nombre.strip()
    return nombre_normalizado



def normalizar_raza(raza):
    raza = raza.lstrip()  # Eliminar espacios en blanco iniciales

    if raza == "Shin-jin" or raza == "Three-Eyed People":
        # Devolver la raza en formato de lista
        return [raza]
    elif "-" in raza:
        # Dividir la cadena por "-"
        partes = raza.split("-")

        # Retornar una lista con las partes normalizadas
        return [parte.strip() for parte in partes]
    else:
        # Si no hay "-", se normaliza la raza normalmente
        raza_normalizada = raza.strip()

        # Retornar la raza normalizada como una lista con un único valor
        return [raza_normalizada]



def normalizar_habilidad(habilidad):
    habilidad = habilidad.replace("$%", " ")  # Reemplazar los caracteres "$%" por un espacio
    habilidad = habilidad.strip()  # Eliminar espacios en blanco al inicio y al final

    if "|" in habilidad:
        # Dividir la cadena por "|"
        partes = habilidad.split("|")

        # Retornar una lista con las partes normalizadas
        return [parte.strip() for parte in partes]
    else:
        # Si no hay "|", se normaliza la habilidad normalmente
        habilidad_normalizada = habilidad.strip()

        # Retornar la habilidad normalizada como una lista con un único valor
        return [habilidad_normalizada]
