primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
tercer_numero = int(input("Ingrese el tercer numero: "))

def get_mas_grande(primer_numero: int, segundo_numero: int, tercer_numero: int):
    # Recibe tres numero e indica cual es el mas grande
    #
    #    Argumento:
    #      primer_numero [int] -> numero ingresado por el usurio
    #      segundo_numero [int] -> numero ingresado por el usuario
    #      tercer_numero [int] -> numero ingresado por el usuario
    #    Retorna:
    #      numero_mas_grande -> mayor de todos los ingresados
    
    if primer_numero > segundo_numero and primer_numero > tercer_numero:
        numero_mas_grande = f"primer numero con {primer_numero}"
    elif segundo_numero > tercer_numero:
        numero_mas_grande = f"segundo numero con {segundo_numero}"
    else:
        numero_mas_grande = f"tercer numero con {tercer_numero}"
    
    return numero_mas_grande

resultado = get_mas_grande(primer_numero, segundo_numero, tercer_numero)

print(f"El numero más grande es el {resultado}")