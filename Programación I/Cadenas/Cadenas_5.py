#5. Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.
#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

def eliminar_vocales(cadena: str):
    # _descripcion_
    #
    #    Argumento:
    #      cadena [str] -> _description_
    #    Retorna:
    #      retorna -> _description_
    nva_cadena = ""
    
    for i in range(len(cadena)):
        match cadena[i]:
            case "a" | "A":
                pass
            case "e" | "E":
                pass            
            case "i" | "I":
                pass            
            case "o" | "O":
                pass
            case "u" | "U":
                pass
            case _:
                nva_cadena += cadena[i]

    return nva_cadena

cadena = input("Ingrese una cadena pra eliminar las vocales: ")

resultado = eliminar_vocales(cadena)

print(f"La cadena sin vocales queda {resultado}")