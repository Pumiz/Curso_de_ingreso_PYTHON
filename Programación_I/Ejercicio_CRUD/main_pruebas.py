#from Package_Input.Input import *

def get_string_propio(mensaje: str, mensaje_error: str, min_caracteres: int, max_caracteres: int) -> str | None:
    cadena = input(mensaje_error)
    nombre_propio = cadena.capitalize()
    cantidad_caracteres = len(nombre_propio)

    while True:
        cadena = input(mensaje_error)
        nombre_propio = cadena.capitalize()
        cantidad_caracteres = len(nombre_propio)
        
        contiene_numero = False

        for char in cadena:   #recorre caracter por caracter y verifica si contiene un numero
            if char.isdigit():
                contiene_numero = True
                break
        
        if contiene_numero:
            print("No puede contener numeros, reintente...")
            cadena = input(mensaje_error)
            nombre_propio = cadena.capitalize()
            cantidad_caracteres = l en(nombre_propio)
            continue
        
        if cantidad_caracteres <= min_caracteres or cantidad_caracteres >= max_caracteres:
            continue
        else:
            return nombre_propio
        
        print(mensaje_error)


nombre = get_string_propio("Ingrese su nombre: ", "Su nombre esta fuera de rango, reintente: ", 2, 20)

print(nombre)