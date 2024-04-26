#Escribir una función que reciba como parámetros una lista de 
#enteros y retorne la posición del valor máximo encontrado.

def posicion_mas_grande(lista: int):
    # Retorna la posicion del numero mas grande
    #
    #    Argumento:
    #      lista [int] -> lista entera ingresada por el usuario
    #    Retorna:
    #      posicion -> posicion numero mas grande
    mas_grande = 0

    for i in range(len(lista)):
        numero = lista[i]
        if numero > mas_grande:
            posicion = i
    
    return posicion

my_lista = [2,3,6,2,7,2]

print(posicion_mas_grande(my_lista))