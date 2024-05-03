
filas_a = int(input("Ingrese la cantidad de filas de la matriz A: "))
columnas_a = int(input("Ingrese la cantidad de columnas de la matriz A: "))

matriz_a = [[0]*columnas_a for _ in range (filas_a)]

cantidad_valores = filas_a * columnas_a

for i in range(filas_a):
    for j in range(columnas_a):
        valor = int(input(f"Ingrese el numero en la posicion X({i+1}{j+1}): "))
        matriz_a[i][j] = valor

for i in range(filas_a):
    for j in range(columnas_a):
        print(f"{matriz_a [i][j]:<5}", end = " ")
            
    print("")

####################################################################################

filas_b = int(input("\nIngrese la cantidad de filas de la matriz B: "))
columnas_b = int(input("Ingrese la cantidad de columnas de la matriz B: "))

matriz_b = [[0]*columnas_b for _ in range (filas_b)]


for i in range(filas_b):
    for j in range(columnas_b):
        valor = int(input(f"Ingrese el numero en la posicion X({i+1}{j+1}): "))
        matriz_b[i][j] = valor

for i in range(filas_b):
    for j in range(columnas_b):
        print(f"{matriz_b [i][j]:<5}", end = " ")
            
    print("")

####################################################################################

if columnas_a == filas_b:
    matriz_resultado = [[0]*columnas_b for _ in range (filas_a)]

    for i in range (filas_a):
        for j in range (columnas_b):
            for k in range (filas_b):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]


    for i in range(filas_a):
        for j in range(columnas_b):
            print(f"{matriz_resultado [i][j]:<5}", end = " ")
                
        print("")

else:
    print("Estas matrices no se pueden multiplicar")