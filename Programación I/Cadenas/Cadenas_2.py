#2. Crear una función que reciba una cadena y un caracter.
#La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.

def posicion_del_caracter(cadena: str, caraceter: str):
    # _descripcion_
    #
    #    Argumento:
    #      cadena [str] -> texto ingresado por el usuario
    #      caraceter [str] -> letra ingresada poe el usuario
    #    Retorna:
    #      retorna -> _description_

        for i in range(len(cadena)):
            if cadena[i] == caraceter:
                posicion = i
                break
        return posicion

string = input("Ingrese una cadena: ")
letra = input("Ingrese un caracter: ")

resultado = posicion_del_caracter(string, letra)

print(f"La letra {letra} se encuentra en la posicon {resultado+1}")