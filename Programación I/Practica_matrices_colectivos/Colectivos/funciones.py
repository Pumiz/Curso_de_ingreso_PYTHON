def printear_matriz(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz [i][j]:<5}", end = " ")
                
        print("")

def imprimir_matriz_con_texto(matriz, texto_por_columna, texto_por_fila):
    for texto in texto_por_columna:
        print(f"\t{texto}", end="\t")
    print("\n")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{texto_por_fila[i]}",f"{matriz[i][j]:<10}", end="\t")
        print("\n")
