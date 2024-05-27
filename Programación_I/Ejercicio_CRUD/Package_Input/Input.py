#1. Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

from Validate import validate_lenght,validate_number

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
    while cantidad_caracteres <= min_caracteres and cantidad_caracteres >= max_caracteres:
        cadena = input(mensaje_error)

    else:
        return cadena
