lista = [
    [1,242,2],
    [1,4,42]
]

numero = 2

for i in range(len(lista)):
    for i in range(i):
        if numero in lista:
            print("True")
        else:
            print("False")