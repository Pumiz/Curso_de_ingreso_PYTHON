
# 4x2 + 9x3 == fila 0 colum 0 resultado   [31    ]
#                                         [      ]

# 4x2 + 9x1 == fila 0 colum 1 resultado   [31  17]
#                                         [      ]

# 7x2 + 9x3 == fila 1 colum 0 resultado   [31  17]
#                                         [41    ]

# 7x1 + 9x1 == fila 1 colum 1 resultado   [31  17]
#                                         [41  16]
matriz_a = [ #2x2
    [4,9],     
    [7,9]      
]

matriz_b = [ #2x2
    [2,2],
    [3,1]
]

M_A = len(matriz_a) #columnas
N_A = len(matriz_a[0]) #filas

M_B = len(matriz_b) #columnas
N_B = len(matriz_b[0]) #filas

resultado = 0

matriz_resultado = [[0] *N_A for _ in range(M_B)]  #2x2

if M_A == N_B:
    for i in range(M_A):
        for j in range(N_A):
            matriz_resultado[i][j] = (matriz_a[i][j] * matriz_b[i][j])

    for i in range(M_A):
        for j in range(N_A):
            print(f"{matriz_resultado[i][j]:3}", end = " ")
        print("")
else:
    print("No se puenden multiplicar")