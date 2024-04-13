numero = int(input("Ingrese un numero "))

def verificador_par(primer_numero: int):
    # Verifica si el numero ingresado es par o inpar
    #
    #    Argumento:
    #      primer_numero [int] -> numero ingresado
    #    Retorna:
    #      resultado -> string 
    
    if primer_numero % 2 == 0:
        resultado = "El numero ingresado es par"
    else:
        resultado = "El numero ingresado es inpar"
    
    return resultado

respuesta = verificador_par(numero)
print(respuesta)