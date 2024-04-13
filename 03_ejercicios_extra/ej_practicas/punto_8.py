numero_ingresado = int(input("Ingrese la base "))
exponente_ingresado = int(input("Ingrese el exponente "))

def potenciar(numero: int, exponente: int):
    # _descripcion_
    #
    #    Argumento:
    #      numero [int, exponente: int] -> _description_
    #    Retorna:
    #      resultado -> resutlado de la potencia
    
    numero_potenciado = numero_ingresado ** exponente
    
    return numero_potenciado

resultado = potenciar(numero_ingresado, exponente_ingresado)
print(f"El resultado de {numero_ingresado} elevado {exponente_ingresado} es de {resultado}")