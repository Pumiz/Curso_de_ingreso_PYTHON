def get_flotante():
    # Socilicita un flotante, lo valida y lo retorna
    #
    #    Retorna:
    #      retorna -> _description_
    float_ingresante = input("Ingrese un flotante ")
    float_ingresante = float(float_ingresante)

    if type(float_ingresante) == float:
        print("Lo ingresado es del tipo flotante.")\
        
get_flotante()