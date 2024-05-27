from os import system
import random
from Ejercicio_Modulos_Paquetes.Package_Input.Input import *
from Practica_matrices_colectivos.Colectivos.funciones import *

legajo_choferes = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

recaudaciones = [
#  L1,L2,L3
    [0,0,0], #Coche 1
    [0,0,0], #Coche 2
    [0,0,0], #Coche 3
    [0,0,0], #Coche 4
    [0,0,0]  #Coche 5
]

filas = 5
columnas = 3

recaudacion_linea_1 = 0
recaudacion_linea_2 = 0
recaudacion_linea_3 = 0

recaudacion_coche_1 = 0
recaudacion_coche_2 = 0
recaudacion_coche_3 = 0
recaudacion_coche_4 = 0
recaudacion_coche_5 = 0

total_recaudacion = 0

texto_por_columna = ["Linea 1:", "Linea 2:", "Linea 3:"]
texto_por_fila = ["Coche 1: ", "Coche 2: ", "Coche 3: ", "Coche 4: ", "Coche 5: "]

for i in range(columnas):
    for j in range(filas):
        legajo_choferes[i][j] = random.randint(10, 1000)

printear_matriz(legajo_choferes, 3, 5) #Printeo la matriz para saber cuales legajos existen

interactuar = False

menu = "\n1) Cargar Planilla\n2) Mostrar la recaudación de cada coches y líneas.\n3) Calcular y mostrar recaudación por línea.\n4) Calcular y mostrar recaudación por coche.\n5) Calcular y mostrar la recaudación total.\n6) Salir\n\nIngrese una opcion: "

legajo = get_int("Ingrese su legajo: ", "El legajo esta fuera de rango, reintente", 10, 1000, 3)
for fila in legajo_choferes:
    if legajo in fila:
        interactuar = True
    else:
        print("El legajo ingresado no existe ")

while interactuar == True:
    opcion_seleccionada = get_int(menu, "La opcion ingresada no existe, reintente.", 1, 6, 3) #Al estar dentro del while true no sale si  se terminan los reintentos
    system("clear")#   "clear" -> Mac     "cls" -> Windows
    match opcion_seleccionada:
        case 1:
            linea_trabajada = get_int("Ingrese la linea trabajada: ", "La linea indicada no existe", 1, 3, 3)
            coche_ingresado = get_int("Ingrese el coche trabajado: ", "El numero de coche no existe, reintente", 1, 5, 3)
            recaudacion = get_int("Ingrese lo recaudado: ", "El numero ingresado tiene que ser mas de 0.", 1, 100000000, 3) #Puse de maximo 100000000 como si no hubiera maximo

            recaudaciones[coche_ingresado-1][linea_trabajada-1] += recaudacion
            print("Planilla cargada con exito!")

        case 2:
            print("Las recaudaciones de los coches y lineas son las siguientes: ")
            imprimir_matriz_con_texto(recaudaciones, texto_por_columna, texto_por_fila)

        case 3:
            for i in range(filas):
                recaudacion_linea_1 += recaudaciones[i][0]
                recaudacion_linea_2 += recaudaciones[i][1]
                recaudacion_linea_3 += recaudaciones[i][2]
            print(f"La linea 1, genero: ${recaudacion_linea_1}\nLa linea 2, genero: ${recaudacion_linea_2}\nLa linea 3, genero: ${recaudacion_linea_3}")

        case 4:
            for i in range(columnas):
                recaudacion_coche_1 += recaudaciones[0][i]
                recaudacion_coche_2 += recaudaciones[1][i]
                recaudacion_coche_3 += recaudaciones[2][i]
                recaudacion_coche_4 += recaudaciones[3][i]
                recaudacion_coche_5 += recaudaciones[4][i]
            print(f"El coche 1 genero: ${recaudacion_coche_1}\nEl coche 2 genero: ${recaudacion_coche_2}\nEl coche 3 genero: ${recaudacion_coche_3}\nEl coche 4 genero: ${recaudacion_coche_4}\nEl coche 5 genero: ${recaudacion_coche_5}\n")

        case 5:
            for i in range(filas):
                for j in range(columnas):
                    total_recaudacion += recaudaciones[i][j]
            print(f"El total de todo lo recaudado es de: ${total_recaudacion}")

        case 6:
            print("Gracias por indicar la recaudacion!")
            interactuar = False


