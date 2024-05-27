numero = int(input("Ingrese un numero "))

def verificador_par(primer_numero: int):
    # Verifica si el numero ingresado es par o inpar
    #
    #    Argumento:
    #      primer_numero [int] -> numero ingresado
    #    Retorna:
    #      resultado -> string 
    
    if primer_numero % 2 == 0:
        print("El numero ingresado es par")
    else:
        print("El numero ingresado es inpar")

verificador_par(numero)