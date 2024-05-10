#4 Realizar una funcion para calcular el numero de Fibonacci de un numero ingresasdo por consola

def calcular_fibonacci(numero: int):
    # _descripcion_
    #
    #    Argumento:
    #      numero [int] -> _description_
    #    Retorna:
    #      retorna -> _description_
    if numero <= 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

numero = int(input("Ingrese un numero para calcular su Fibonacci: "))

resultado = calcular_fibonacci(numero)

print(f"El Fibonacci de {numero} es: {resultado}")


