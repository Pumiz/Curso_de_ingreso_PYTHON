def get_descuento(precio: float, descuento: float) -> float:
    # Recibe precio original y aplica el descuento indicado
    #
    #    Argumento:
    #      precio [float] -> 1834.99
    #      descuento [float] -> 20
    #    Retorna:
    #      precio_final -> precio final con descuento
    precio_final = precio * descuento / 100
    precio_final = precio - precio_final
    
    
    return precio_final  

precio_consumidor_final = get_descuento(1834.99, 20)
print(f"El precio final del producto es {precio_consumidor_final}")





#funcion para buscar y reemplazar un valor, por ej esta el 3 y le digo que el 3 lo reemplaze por un 5

#funcion para sumar los numero que contiene un array