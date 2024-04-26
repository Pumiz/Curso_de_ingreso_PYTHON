from Input import *

def validate_number(numero: int|float, minimo: int, maximo: int) -> bool:
    # _descripcion_
    #
    #    Argumento:
    #      minimo [int, maximo: int] -> _description_
    #    Retorna:
    #      bandera_validacion -> _description_
    reintentadas = 0

    while numero <= minimo and numero >= maximo:
        bandera_validacion = False
    else:
        bandera_validacion = True

    return bandera_validacion

numero_is_validado = validate_number(89, 18, 99)

if numero_is_validado == True:
    print("El numero esta en rango")
else:
    print("El numero esta fuera de rango")
