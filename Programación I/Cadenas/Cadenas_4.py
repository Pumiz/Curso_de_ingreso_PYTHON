#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.

def eliminar_repetidos(cadena: str):
    # _descripcion_
    #
    #    Argumento:
    #      cadena [str] -> _description_
    #    Retorna:
    #      cadena -> _description_
    caraceter_anterior = cadena[1]

    nva_cadena = ""

    for i in range(len(cadena)):
        if cadena[i] != caraceter_anterior:
            nva_cadena += cadena[i]

    return nva_cadena

string = input("Ingrese una cadena: ")

resultado = eliminar_repetidos(string)

print(f"La cadena sin repetidos queda: {resultado}")