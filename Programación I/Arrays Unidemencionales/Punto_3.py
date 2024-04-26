#Escribir una función que calcule y retorne el producto de todos los elementos 
#de la lista que recibe como parámetro.

def producto_array(lista: int):
    # _descripcion_
    #
    #    Argumento:
    #      lista [int] -> _description_
    #    Retorna:
    #      resultado_producto -> _description_
    
    for i in range(len(lista)):
        numero = 1
        resultado_producto = numero * i
    
    return resultado_producto

my_lista = [1, 3, 5]

print(producto_array(my_lista))

"""def calcular_producto(lista):
    producto = 1
    for elemento in lista:
        producto *= elemento
    return producto

# Ejemplo de uso:
mi_lista = [1, 3, 5]
resultado = calcular_producto(mi_lista)
print("El producto de los elementos de la lista es:", resultado)
"""