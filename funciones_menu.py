##-------------------------------------------------------------------------------------------------------##
from diccionario_datos import ejecutar_impresion_diccionario
from funciones_contabilidad import *
from funciones_juego import *
from funciones_lectoras_y_buscadoras import *
from funciones_actualizaciones import *
from funciones_tarjeta_DBZ import ejecutar_menu
from funcion_tarjetaDBZ_diccionario import ejecutar_diccionario_tarjetas
from funciones_de_ordenamiento import *

with open('DBZ_diccionario_general.json', 'r', encoding='utf-8') as file:
    diccionario_general = json.load(file)

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
            ejecutar_impresion_diccionario(diccionario_general)
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
            ejecutar_ordenamiento()
        elif opcion == "10":
            ejecutar_menu()
        elif opcion == "11":
            ejecutar_diccionario_tarjetas()
        elif opcion == "12":
            print("Saliendo del programa ...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

mostrar_menu()
