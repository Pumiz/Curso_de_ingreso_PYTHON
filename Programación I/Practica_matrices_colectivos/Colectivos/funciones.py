def printear_matriz(matriz, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            print(f"{matriz [i][j]:<5}", end = " ")
                
        print("")
