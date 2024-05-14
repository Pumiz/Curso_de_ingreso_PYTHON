#Escribir una función que calcule y retorne el producto de todos los elementos 
#de la lista que recibe como parámetro.

def producto_array(lista: list):
    # Multiplica los numero del array
    #
    #    Argumento:
    #      lista [int] -> Lista ingresada por el usuario
    #    Retorna:
    #      resultado_producto -> Calculo Productos
    resultado_producto = 1

    for i in range(0 , len(lista), 1):
        resultado_producto *= lista[i]
    
    return resultado_producto

my_lista = [2, 3, 6, 3]

resultado = producto_array(my_lista)

print(f"El resultado de productos es: {resultado}")

