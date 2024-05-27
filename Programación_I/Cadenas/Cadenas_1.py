#1. Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente).
#La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.

matriz_resultado = [
    ["A", 0],
    ["E", 0],
    ["I", 0],
    ["O", 0],
    ["U", 0]
]

def contar_vocales(cadena: str):
    # Indica la cantidad de vocales que tiene una cadena
    #
    #    Argumento:
    #      cadena [str] -> str ingresado por el usuario
    #    Retorna:
    #      retorna -> matriz con resultados

    sumar_a = 0
    sumar_e = 0
    sumar_i = 0
    sumar_o = 0
    sumar_u = 0

    for i in range(len(cadena)):
            
            match (cadena[i]):
                case "a" | "A":
                    sumar_a += 1
                    matriz_resultado[0][1] = sumar_a
                case "e" | "E":
                    sumar_e += 1
                    matriz_resultado[1][1] = sumar_e
                case "i" | "I":
                    sumar_i += 1
                    matriz_resultado[2][1] = sumar_i
                case "o" | "O":
                    sumar_o += 1
                    matriz_resultado[3][1] = sumar_o
                case "u" | "U":
                    sumar_u += 1
                    matriz_resultado[4][1] = sumar_u

string = input("Ingrese una cadena para saber la cantidad de vocales que tiene: ")

contar_vocales(string)

for i in range(5):
    for j in range(2):
        print(f"{matriz_resultado [i][j]:<2}", end = " ")
            
    print("")


