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
        if numero > 0:
            contador_positivos +=  1
        elif numero < 0:
            contador_negativos += 1
        else:
            contador_ceros += 1

    print(f"Hay {contador_positivos} numeros positivos\nHay {contador_negativos} numeros negativos\nY hay {contador_ceros} ceros")


#C. Mostrar la sumatoria de los números pares.
def sumar_pares(lista):
    # Retorna la suma de los numero pares
    #
    #    Argumento:
    #      lista -> Lista ingresada por el usuario
    #    Retorna:
    #      suma_positivos -> suma de los numeros positivos
    suma_positivos = 0

    for i in range(len(lista)):
        numero = lista[i]
        if numero > 0:
            suma_positivos += numero

    return suma_positivos


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
        if numero % 2 == 1 and numero > impar_mayor:
            impar_mayor = numero

        elif numero == 1 and numero > impar_mayor:
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

        if numero % 2 == 0 and numero != 0:
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

        if numero % 2 == 1:
            print(posicion + 1)