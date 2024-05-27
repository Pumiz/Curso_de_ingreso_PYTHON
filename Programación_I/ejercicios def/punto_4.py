def get_validaciones(valor, rango_minimo: float, rango_maximo: float, mensaje: str):
    # Valida un numero entre dos rangos minimos y maximos
    #
    #    Argumento:
    #      valor [None] -> Ingresado por el usuario
    #      rango_minimo [float] -> valor de validacion minima
    #      rango_maximo [float] -> valor de validacion maxima
    #      mensaje [str] -> texto de error
    #    Retorna:
    #      retorna -> valor ingresado validado

    while valor < rango_minimo or valor > rango_maximo:
        valor = input(mensaje)
        valor = float(valor) #Lo parceo en flotante ya que tambien "funciona" como entero

    return valor

edad = int(input("\nIngrese su edad "))
edad = get_validaciones(edad, 18, 100, "Error, reingrese su edad ")

altura = float(input("Ingrese su altura en metros "))
altura = get_validaciones(altura, 1.0, 2.0, "Error, reingrese su altura ")

nombre = str(input("Ingrese su nombre "))

print(f"\n{nombre} tiene {edad} años y mide {altura}m")