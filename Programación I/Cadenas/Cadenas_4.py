#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def eliminar_repetidos(cadena: str):
    # elimina los caracteres repetidos
    #
    #    Argumento:
    #      cadena [str] -> cadena ingresada por el usuario
    #    Retorna:
    #      cadena -> cadena sin repeticiones

    nva_cadena = ""
    caraceter_anterior = []

    for i in range(0, len(cadena), 1):
        if cadena[i] != caraceter_anterior:
            nva_cadena += cadena[i]
            caraceter_anterior = cadena[i]

    return nva_cadena

string = input("Ingrese una cadena: ")

resultado = eliminar_repetidos(string)

print(f"La cadena sin repetidos queda: {resultado}")