#5. Escribir una función que reciba como parámetros una lista de enteros
#y muestre la/las posiciones en donde se encuentra el valor máximo hallado

def posicion_mas_grande(lista: list):
    # _descripcion_
    #
    #    Argumento:
    #      lista [list] -> _description_
    #    Retorna:
    #      retorna -> _description_
    mas_grande = 0
    lista_posiciones = []
    
    for i in range(len(lista)):
        if lista[i] > mas_grande:
            mas_grande = lista[i]
            lista_posiciones = [i]

        elif lista[i] == mas_grande:
            lista_posiciones.append(i)
    
    return lista_posiciones

lista = [6,3,78,9,78,23]

lista_resultado = posicion_mas_grande(lista)

print("Las posiciones de los numeros mas grandes se encuentran en: ")
for i in range(len(lista_resultado)):
    print(lista_resultado[i])