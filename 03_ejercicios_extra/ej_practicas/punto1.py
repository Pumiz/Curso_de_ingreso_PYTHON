def get_numero_entero():
    # Socilicita un numero, lo valida con funcion isdigit() y lo retorna
    #
    #    Retorna:
    #      numero_ingresado -> _description_
    
    numero_ingresado = input("Ingrese un numero ")
    if numero_ingresado.isdigit():
        numero_ingresado = "El numero ingresado es entero"
    else:
        numero_ingresado = "El numero ingresado no es un entero."
    
    return numero_ingresado

print(get_numero_entero())