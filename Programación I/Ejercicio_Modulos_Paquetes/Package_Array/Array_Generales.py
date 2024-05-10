from Ejercicio_Modulos_Paquetes.Package_Array.Especificas import *

#A. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
def ingresar_10_numeros():
    # Solicita 10 numeros, los valida y los incerta en la lista
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    #    Retorna:
    #      lista_numeros_ingresados -> Lista de los numeros
    lista_numeros_ingresados = [0] * 10
    cantidad_reingresos = 10
    posicion = 1

    for posicion in range(cantidad_reingresos):
        numero = int(input("Ingrese un numero "))
        while numero < -1000 or numero > 1000:
            numero = int(input("El numero tiene que ser mayor a -1000 y menor que 1000, reingrese "))
        else:
            lista_numeros_ingresados[posicion] = numero

    return lista_numeros_ingresados


#B. Mostrar la cantidad de números positivos y negativos.
def printear_positivos_negativos(lista):
    # Muestra la cantidad de numeros positivos, negativos y ceros
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    contador_positivos = 0
    contador_negativos = 0
    contador_ceros = 0

    for i in range(len(lista)):
        numero = lista[i]
        if positivo_or_negativo(numero) == "Positivo":
            contador_positivos +=  1
        elif positivo_or_negativo(numero) == "Negativo":
            contador_negativos += 1

    print(f"Hay {contador_positivos} numeros positivos y hay {contador_negativos} numeros negativos")


#C. Mostrar la sumatoria de los números pares.
def sumar_pares(lista):
    # Retorna la suma de los numero pares
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    #    Retorna:
    #      suma_positivos -> suma de los numeros positivos
    suma_pares = 0

    for i in range(len(lista)):
        numero = lista[i]
        if par_or_impar(numero) == "Par":
            suma_pares += numero

    return suma_pares


#D. Informar el mayor de los números impares.
def mayor_impar(lista):
    # Muestra el mayor numero impar
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    #    Retorna:
    #      impar_mayor -> Mayor numero impar
    impar_mayor = 0
    for i in range(len(lista)):
        numero = lista[i]
        if (par_or_impar(numero) == "Impar" and numero > impar_mayor) or (numero == 1):
            impar_mayor = numero

    return impar_mayor


#E. Listar todos los números ingresados.
    # Muestra los numeros de la lista
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
def listar_numero(lista):

    for i in range(len(lista)):
        print(lista[i])


#F. Listar todos los números pares.
def listar_pares(lista):
    # Muestra solo los numeros pares
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    for i in range(len(lista)):
        numero = lista[i]

        if par_or_impar(numero) == "Par" and numero != 0:
            print(numero)


#G. Listar los números de las posiciones impares. 
def listar_posicion_impares(lista):
    # Muestra posicion de los numeros impares
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    posicion = 0
    for posicion in range(len(lista)):
        numero = lista[posicion]

        if par_or_impar(numero) == "Impar":
            print(posicion + 1)