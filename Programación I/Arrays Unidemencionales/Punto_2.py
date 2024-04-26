#Escribir una función parecida a la anterior, 
#pero la misma deberá calcular y devolver el promedio de los números positivos.

#Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el p
#romedio de todos los números.

def promedio_numeros_positivos(lista_numerica: int) -> float:
    # Promedia los numeros enteros positivos de un array
    #
    #    Argumento:
    #      lista_numerica [int] -> array ingresada por el usuario
    #    Retorna:
    #      promedio_lista [float] -> promedio de todos los numeros positivos
    suma_total = 0
    contador_numeros = 0

    for i in range(len(lista_numerica)):
        numero = lista[i]
        if numero >= 0:
            suma_total += numero
            contador_numeros += 1 
            promedio_lista = suma_total / contador_numeros
    
    return promedio_lista

lista = [3, 8, -3, 10, -45, 23, 1]

print(promedio_numeros_positivos(lista))
