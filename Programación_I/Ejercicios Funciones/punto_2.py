def get_flotante():
    # Socilicita un flotante y lo retorna
    #
    #    Retorna:
    #      retorna -> _description_
    float_ingresante = input("Ingrese un flotante ")
    float_ingresante = float(float_ingresante)

    return float_ingresante
        

print(f"El numero ingresado es: {get_flotante()}")