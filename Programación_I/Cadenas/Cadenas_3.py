#Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. 
#Deberá retornar un valor booleano indicando lo sucedido.


def is_palindromo(cadena: str) -> bool:
    # Verifica si una cadena es un Palíndromo
    #
    #    Argumento:
    #      cadena [str] -> cadena ingresada por el usuario
    #    Retorna:
    #      resultado -> booleano
    is_palindromo = False
    largo_cadena = (len(cadena)-1)
    nva_cadena = ""

    for i in range(largo_cadena, -1, -1):
        nva_cadena += cadena[i]

    if cadena == nva_cadena:
        is_palindromo = True
        
    return is_palindromo


cadena = input("Ingrese una cadena: ")

print(is_palindromo(cadena))