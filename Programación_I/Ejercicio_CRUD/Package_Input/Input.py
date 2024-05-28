#1. Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:
from Package_Input.Validate import *

def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, cant_reintentos: int) -> int|None:
    # Solicita un numero y lo valida segun la cantidad de intentos ingresados.
    #
    #    Argumento:
    #      mensaje [str] -> Texto de ingreso
    #      mensaje_error [str] -> Texto de error
    #      minimo [int] -> Rango minimo validacion
    #      maximo [int] -> Rango maximo validacion
    #      cant_reintentos [int] -> Cantidad de cant_reintentos
    #    Retorna:
    #      numero -> Numero validado o None
    reintentos = 1

    numero = int(input(mensaje))

    while validate_number(numero, minimo, maximo) == False:
        print(mensaje_error)

        if reintentos == cant_reintentos or cant_reintentos == 0:
            numero = None
            break

        else:
            for i in range(0, cant_reintentos, 1):
                numero = int(input(mensaje))
                reintentos += 1
                break
    return numero

#Repetir el mismo procedimiento para un dato de tipo float.
def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, cant_reintentos: int) -> float|None:
    # Solicita un numero y lo valida segun la cantidad de intentos ingresados.
    #
    #    Argumento:
    #      mensaje [str] -> Texto de ingreso
    #      mensaje_error [str] -> Texto de error
    #      minimo [float] -> Rango minimo validacion
    #      maximo [float] -> Rango maximo validacion
    #      cant_reintentos [int] -> Cantidad de cant_reintentos
    #    Retorna:
    #      numero -> Numero validado o None
    reintentos = 1

    numero = float(input(mensaje))

    while validate_number(numero, minimo, maximo) == False:
        print(mensaje_error)

        if reintentos == cant_reintentos or cant_reintentos == 0:
            numero = None
            break

        else:
            for i in range(0, cant_reintentos, 1):
                numero = float(input(mensaje))
                reintentos += 1
                break
    return numero

#2.Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
def get_string(mensaje: str, mensaje_error: str, min_caracteres: int, max_caracteres: int) -> str|None:
    # Retorna cantidad de caracteres de una cadena
    #
    #    Argumento:
    #      cadena [str] -> String ingresada por el usuario
    #      longitud [int] -> Cantidad de caracteres maximos a validar
    #    Retorna:
    #      cantidad_caracteres -> _description_
    cadena = input(mensaje)
    cantidad_caracteres = len(cadena)
    while cantidad_caracteres <= min_caracteres or cantidad_caracteres >= max_caracteres:
        cadena = input(mensaje_error)
        cantidad_caracteres = len(cadena)

    else:
        return cadena


def get_string_propio(mensaje: str, mensaje_error: str, min_caracteres: int, max_caracteres: int) -> str|None:
    # Retorna cantidad de caracteres de una cadena
    #
    #    Argumento:
    #      cadena [str] -> String ingresada por el usuario
    #      longitud [int] -> Cantidad de caracteres maximos a validar
    #    Retorna:
    #      cantidad_caracteres -> _description_
    cadena = input(mensaje)
    nombre_propio = cadena.capitalize()
    cantidad_caracteres = len(nombre_propio)

    contiene_numero = False

    for char in cadena:
        if char.isdigit():  #analiza caracter por caracter y se fija si es un digito
            contiene_numero = True

    while contiene_numero:
        cadena = input("No puede contener numero, reingrese: ")
        nombre_propio = cadena.capitalize()
        cantidad_caracteres = len(nombre_propio)

        for char in nombre_propio:
            if char.isdigit():  #analiza caracter por caracter y se fija si es un digito
                continue
            else:
                contiene_numero = False


    

    while cantidad_caracteres <= min_caracteres or cantidad_caracteres >= max_caracteres:
        cadena = input(mensaje_error)
        nombre_propio = cadena.capitalize()
        cantidad_caracteres = len(nombre_propio)

    else:
        return nombre_propio
