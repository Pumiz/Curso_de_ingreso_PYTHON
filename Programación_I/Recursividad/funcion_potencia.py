#2. Realizar una función recursiva que calcule la potencia de un número:
#Logica
#bandera_resultado = True
#cantidad_exponenciales = 1
#base_nva = base
#
#while bandera_resultado == True:
#    if cantidad_exponenciales < exponente_ingresado:
#        for cantidad_exponenciales in range(cantidad_exponenciales, exponente_ingresado):
#
#            resultado = base_nva * base
#            base_nva = resultado
#            cantidad_exponenciales += 1
#
#            break
#    else:
#        bandera_resultado = False
#
#print(resultado)


def calcular_potencia(base: int, exponente: int):
    # _descripcion_
    #
    #    Argumento:
    #      base [int, exponente: int] -> _description_
    #    Retorna:
    #      numero_potenciado -> _description_
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base_ingresada = int(input("Ingrese la base "))
exponente_ingresado = int(input("Ingrese el exponente "))

print(f"El resultado de {base_ingresada} elevado a {exponente_ingresado} es: {calcular_potencia(base_ingresada, exponente_ingresado)}")
