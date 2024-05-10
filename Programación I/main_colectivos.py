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
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

lista_lineas = [247, 278, 318]

filas = 3
columnas = 5

for i in range(filas):
    for j in range(columnas):
        legajo_choferes[i][j] = random.randint(10, 1000)

printear_matriz(legajo_choferes, 3, 5)

coches = 0
linea = 0

recaudacion_lineas = [0,0,0]

recaudacion_coches = [0,0,0,0,0]

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
            linea_existente = False
            coche_existente = False
            recaudacion_anterior = 0

            linea_trabajada = get_int("Ingrese la linea trabajada: ", "La linea indicada no existe", 1, 3, 3)
            coche_ingresado = get_int("Ingrese el coche trabajado: ", "El numero de coche no existe, reintente", 1, 5, 3)
            recaudacion = get_int("Ingrese lo recaudado: ", "El numero ingresado tiene que ser mas de 0.", 1, 100000000, 3)

            recaudacion_anterior = recaudacion
            for j in range (5):
                for k in range (3):
                    recaudaciones[coche_ingresado-1][linea_trabajada-1] += recaudacion_anterior
            
            printear_matriz(recaudaciones, 5, 3)

        case 2:
            print(f"La recaudacion de las lineas fueron:")
            for i in range(len(linea)):
                print(linea[i], end=" --> ")
                print(recaudacion_lineas[i])


"""
match coches:
    case 1:
        recaudacion_coches[coches-1] += recaudacion
    case 2:
        recaudacion_coches[coches-1] += recaudacion
    case 3:
        recaudacion_coches[coches-1] += recaudacion                            
    case 4:
        recaudacion_coches[coches-1] += recaudacion                            
    case 5:
        recaudacion_coches[coches-1] += recaudacion

match linea:
    case 1:
        recaudacion_lineas[linea-1] += recaudacion
    case 2:
        recaudacion_lineas[linea-1] += recaudacion
    case 3:
        recaudacion_lineas[linea-1] += recaudacion
else:
print("No existe la linea o el coche")
else:
print("El legajo no existe")
"""








