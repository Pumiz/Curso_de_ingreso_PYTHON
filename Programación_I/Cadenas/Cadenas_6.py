#6. Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.
#Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá retornar el valor 2.

def contar_subcadena(cadena, subcadena):
    veces_encontrada = 0
    bandera_encontro = True

    for i in range(len(cadena)):
        bandera_encontro = True

        for j in range(len(subcadena)):
            if cadena[i+j] != subcadena[j]:
                bandera_encontro = False
                break

        if bandera_encontro == True:
            veces_encontrada += 1
    
    return veces_encontrada

string = "El pan del panadero paniciente"
subcadena = "pan"

aparicion_resultado = contar_subcadena(string, subcadena)
print(f"La palabra '{subcadena}' aparece {aparicion_resultado} veces en la cadena: {string}")