#3 Realizar una funcion recursiva que la suma de los digitos de un numero

def sumar_digitos(numero: int):
    # suma los digitos de un numero
    #
    #    Argumento:
    #      numero [int] -> numero ingresado por el usuario
    #    Retorna:
    #      suma_de_los_digitos -> resultado de la suma
    
    if numero <= 10:
        return numero
    else:
        return numero % 10 + sumar_digitos(numero // 10)
    
print(sumar_digitos(2345))