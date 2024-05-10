#Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
#A. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
#B. Mostrar la cantidad de números positivos y negativos.
#C. Mostrar la sumatoria de los números pares.
#D. Informar el mayor de los números impares.
#E. Listar todos los números ingresados.
#F. Listar todos los números pares.
#G. Listar los números de las posiciones impares.  
#H. Salir
from os import system
from Ejercicio_Modulos_Paquetes.Package_Array.Array_Generales import *
from Ejercicio_Modulos_Paquetes.Package_Input.Input import *
interactuar = True
numeros_is_ingresados = False

menu = "\n\nA) Ingresar 10 numeros\nB) Cantidad de numeros positivos y negativos\nC) Sumar numeros pares\nD) Numero impar mas grande\nE) Mostrar todos los números ingresados\nF) Mostrar todos los números pares\nG) Mostrar los números de las posiciones impares\nH) Salir\n\nIngrese una opcion: "

while interactuar == True:
    opcion_seleccionada = get_string(menu, "La opcion ingresada no existe", 1)
    system("clear")#   "clear" -> Mac     "cls" -> Windows
    match opcion_seleccionada:
        case "A":
            numeros_ingresados = ingresar_10_numeros()
            numeros_is_ingresados = True

        case "B":
            if numeros_is_ingresados == True: printear_positivos_negativos(numeros_ingresados)
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "C":
            if numeros_is_ingresados == True:
                resultado = sumar_pares(numeros_ingresados)
                print(f"La suma total de los numeros pares es: {resultado}")
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "D":
            if numeros_is_ingresados == True:
                resultado = mayor_impar(numeros_ingresados)
                print(f"El numero impar mas grande es: {resultado}")
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "E":
            if numeros_is_ingresados == True:
                print(f"Los numeros ingresados son: ")
                listar_numero(numeros_ingresados)
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "F":
            if numeros_is_ingresados == True:
                print(f"Los numeros pares ingresados son: ")
                listar_pares(numeros_ingresados)
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "G":
            if numeros_is_ingresados == True:
                print(f"Los numeros impares estan en las siguientes posiciones: ")
                listar_posicion_impares(numeros_ingresados)
            else:
                print("Primero tenes que ingresar los numeros... boludon!")

        case "H":
            print("Gracias por usar mi programa :D")
            interactuar = False

