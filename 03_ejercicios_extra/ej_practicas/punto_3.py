def get_cadena():
    # Socilicita un numero, lo valida y lo retorna
    #
    #    Retorna:
    #      cadena_ingresadad -> caracteres ingresados
    
    cadena_ingresada = input("Ingrese una cadena ")

    return cadena_ingresada

print(f"La cadena ingresada dice: {get_cadena()}")