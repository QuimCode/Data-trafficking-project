# 1. Traer datos desde archivo: Guardar el contenido del archivo DBZ.csv en una colección. Tener en
# cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
# un personaje puede tener más de una raza y más de una habilidad.

# 2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
# corresponden a esa raza.

# 3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
# personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
# repetirse en los distintos listados.

# 4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
# deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.

# 5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
# batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
# guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
# el nombre del perdedor. Ese archivo anexará cada dato.txt

# 6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
# cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
# guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
# búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
# Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
# Nombre del archivo:
# Saiyan_Genki_Dama.Json
# Datos :
# Goten - 3000 - Kamehameha + Tambor del trueno
# Goku - 5000000 - Kamehameha + Super Saiyan 2

# 7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción

# 8. Salir del programa.

##-------------------------------------------------------------------------------------------------------##


from funciones_contabilidad import *
from diccionario_datos import *
from funciones_juego import *
from funciones_lectoras_y_buscadoras import *
from funciones_actualizaciones import *
from funciones_tarjeta_DBZ import ejecutar_menu
from funcion_tarjetaDBZ_diccionario import ejecutar_diccionario_tarjetas
import funciones_de_ordenamiento

def mostrar_menu():
    while True:
        print("=== MENÚ ===")
        print("1. Mostrar diccionario de personajes")
        print("2. Mostrar cantidad de personajes por raza")
        print("3. Mostrar cantidad de personajes/poder por raza")
        print("4. Buscar personaje por habilidad")
        print("5. Jugar Batalla")
        print("6. Buscar por Raza y Habilidad")
        print("7. Leer Json")
        print("8. Actualizar raza Saiyan")
        print("9. Odenar lista")
        print("10. Generar tarjeta DBZ")
        print("11. Crear diccionario de tarjetas DBZ")
        print("12. Salir del programa")
        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            for id, datos in diccionario_general.items():
                print(f"ID: {id}")
                for clave, valor in datos.items():
                    print(f"{clave}: {valor}")
                print()
        elif opcion == "2":
            listar_cantidad_por_raza(diccionario_general)
        elif opcion == "3":
            listar_personajes_por_raza(diccionario_general)
        elif opcion == "4":
            buscar_personaje_por_habilidad(diccionario_general)
        elif opcion == "5":
            jugar_batalla()
        elif opcion == "6":
            generar_listado_personajes()
        elif opcion == "7":
            leer_archivo_json()
        elif opcion == "8":
            actualizar_personajes_saiyan()
        elif opcion == "9":
            personajes_ordenados = funciones_de_ordenamiento.ordenar_personajes_por_atributo(diccionario_general, "Nombre", True)
            for personaje in personajes_ordenados:
                print(personaje)
        elif opcion == "10":
            # Mover la llamada a la función dentro de este bloque
            ejecutar_menu()
        elif opcion == "11":
            ejecutar_diccionario_tarjetas()
        elif opcion == "12":
            print("Saliendo del programa ...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

mostrar_menu()
