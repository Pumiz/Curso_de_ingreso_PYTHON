#1. Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:


def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, cant_reintentos: int) -> int|None:
    # Solicita un numero y lo valida segun la cantidad de intentos ingresados.
    #
    #    Argumento:
    #      mensaje [str] -> Texto de ingreso
    #    Retorna:
    #      numero -> Numero ingresado
    numero = int(input(mensaje))
    while numero <= minimo or numero >= maximo:
        print(mensaje_error)

        for i in range(0, cant_reintentos):
            numero = int(input(mensaje))
            i += 1
            numero = None
            break
        
    return numero

def get_float(mensaje: str, mensaje_error: str, minimo: int, maximo: int, cant_reintentos: int) -> int|None:
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

    numero = float(input(mensaje))
    while numero <= minimo or numero >= maximo:
        print(mensaje_error)

        for i in range(0, cant_reintentos):
            numero = float(input(mensaje))
            i += 1
            numero = None
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
