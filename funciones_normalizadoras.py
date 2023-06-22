def normalizar_nombre(nombre):
    nombre_normalizado = nombre.strip()
    return nombre_normalizado


def normalizar_raza(raza):
    raza = raza.lstrip()  

    if raza == "Shin-jin" or raza == "Three-Eyed People":
        return [raza]
    elif "-" in raza:
        partes = raza.split("-")
        return [parte.strip() for parte in partes]
    else:
        raza_normalizada = raza.strip()
        return [raza_normalizada]


def normalizar_habilidad(habilidad):
    habilidad = habilidad.replace("$%", " ")
    habilidad = habilidad.strip()

    if "|" in habilidad:
        partes = habilidad.split("|")
        return [parte.strip() for parte in partes]
    else:
        habilidad_normalizada = habilidad.strip()
        return [habilidad_normalizada]
