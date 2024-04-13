def validar_ingresos():
    # Pide tres datos de distintos tipos, los valida con el parceo y printea si es correcto.
    
    numeros_enteros = input("Ingrese un numero entero: ")
    numeros_enteros = int(numeros_enteros)
    numeros_flotantes = input("Ingrese un numero decimal: ")
    numeros_flotantes = float(numeros_flotantes)
    cadenas = input("Ingrese una cadena: ")

    if type(numeros_enteros) == int:
        print("\nEl numero ingresado es entero")

    if type(numeros_flotantes) == float:
        print("El numero flotante ingresado es un decimal")

    if type(cadenas) == str:
        print("Lo ingresado es una cadena")

validar_ingresos()


'''

def get_numero_entero():
    # Socilicita un numero, lo valida con funcion isdigit() y lo retorna
    #
    #    Retorna:
    #      numero_ingresado -> _description_
    
    numero_ingresado = input("Ingrese un numero ")
    if numero_ingresado.isdigit():
        numero_ingresado = "El numero ingresado es entero"
    else:
        numero_ingresado = "El numero ingresado no es un entero."
    
    return numero_ingresado

print(get_numero_entero())


def get_cadena():
    # Socilicita un numero, lo valida y lo retorna
    #
    #    Retorna:
    #      cadena_ingresadad -> caracteres ingresados
    
    cadena_ingresada = input("Ingrese una cadena ")

    if type(cadena_ingresada) == str:
        print("El valor ingresado es una cadena.")
    else:
        print("El valor ingresado no es una cadena.")

get_cadena()'''