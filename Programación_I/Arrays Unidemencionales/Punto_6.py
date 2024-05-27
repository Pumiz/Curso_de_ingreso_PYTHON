#6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, 
#un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia 
#del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de 
#reemplazos realizados.

def reemplazar_nombres(lista: list, nombres_a_reemplazar: list, nvo_nombre: str) -> int:
    # _descripcion_
    #
    #    Argumento:
    #      lista [list, nombre_reemplazar: str, nvo_nombre: str] -> _description_
    #    Retorna:
    #      retorna -> _description_
    reemplazasos_hechos = 0
    
    for i in range(len(lista)):
        if lista[i] in nombres_a_reemplazar:
            reemplazasos_hechos += 1
            lista[i] = nvo_nombre

    return reemplazasos_hechos

lista_nombres = ["Jose", "Pepe", "Lucas", "Lucia", "Ágatha"]

nombre_reemplazar = ["Pepe", "Lucas"]

nombre_incluir = "Martin"

lista_resultado = reemplazar_nombres(lista_nombres, nombre_reemplazar, nombre_incluir)

print(f"Hubieron {lista_resultado} reemplazos")