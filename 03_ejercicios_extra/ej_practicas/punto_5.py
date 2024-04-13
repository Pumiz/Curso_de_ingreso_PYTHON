radio_ingresado = input("Ingrese el radio del circulo en metros para calcular el area: ")
radio_ingresado = float(radio_ingresado)

def get_area(radio: float):
    # Recibe el radio en metros y calcula el area en metros cuadrados.
    #
    #    Argumento:
    #      radio [float] -> dato ingresado por el usuario
    #    Retorna:
    #      area -> valor del area
    pi = 3.141592
    area = pi * (radio**2)
    
    return area  


print(f"El area de circilo es de: {get_area(radio_ingresado)} m2")
