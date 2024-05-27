def positivo_or_negativo(numero: int|float):
    # Determina si el numero es positivo o negativo
    #
    #    Argumento:
    #      numero [int|float] -> Numero ingresado por el usuario
    #    Retorna:
    #      retorna -> String "Positivo" o "Negativo"
    
    if numero > 0:
        resultado = "Positivo"
    elif numero < 0:
        resultado = "Negativo"
    else:
        resultado = "Cero"

    return resultado

def par_or_impar(numero: int|float):
    # _descripcion_
    #
    #    Argumento:
    #      numero [int|float] -> _description_
    #    Retorna:
    #      resultado -> _description_
    
    if numero == 0:
        pass
    elif numero % 2 == 0:
        resultado = "Par"
    elif numero % 2 == 1:
        resultado = "Impar"

    return resultado