def sumar_naturales(numero: int) -> int:
    # Suma todos los numero individuales --> si le doy el 10 suma 1+2+3....+9+10 = 55
    #
    #    Argumento:
    #      numero [int] -> _description_
    #    Retorna:
    #      resultado_suma -> _description_
    
    if numero == 0:
        return 1
    else:
        return numero + sumar_naturales(numero - 1)

numero_ingresado = int(input("Ingrese los numeros naturales "))
print(f"El resultado es:{sumar_naturales(numero_ingresado)}")



