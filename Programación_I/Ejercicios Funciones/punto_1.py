def get_numero_entero():
    # Socilicita un numero y lo retorna
    #
    #    Retorna:
    #      numero_ingresado -> _description_
    
    numero_ingresado = input("Ingrese un numero ")
    numero_ingresado = int(numero_ingresado)
    
    return numero_ingresado

print(f"El número ingresado es: {get_numero_entero()}")