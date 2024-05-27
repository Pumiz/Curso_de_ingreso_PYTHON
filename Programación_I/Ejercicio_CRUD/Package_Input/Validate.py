def validate_number(numero: int|float, minimo: int, maximo: int) -> bool:
    # Valida el numero ingresado con el rango ingresado
    #
    #    Argumento:
    #      numero [int|float] -> Numero ingresado por el usuario
    #      minimo [int] -> Numero para validar minimo rango
    #      maximo [int] -> Numero para validar maximo rango
    #    Retorna:
    #      bandera_validacion -> Flotante indica si el numero esta validado
    if numero < minimo or numero > maximo:
        bandera_validacion = False
    else:
        bandera_validacion = True
    
    return bandera_validacion

def validate_lenght(longitud_cadena: str, maxima_longitud: int) -> bool:
    # _descripcion_
    #
    #    Argumento:
    #      candena [str] -> int -> _description_
    #    Retorna:
    #      retorna -> _description_
    
    if longitud_cadena > maxima_longitud:
        bandera_validacion_str = False
    else:
        bandera_validacion_str = True

    return bandera_validacion_str