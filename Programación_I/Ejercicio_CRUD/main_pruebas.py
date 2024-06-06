def ordenar_ascendente(lista_empleados: list, elemento: str):
    """
    Ordena una lista de diccionarios en orden ascendente basado en el valor de la clave proporcionada.
    
    Args:
    lista_empleados (list): Lista de diccionarios a ordenar.
    elemento (str): Clave del diccionario por la cual se ordenará la lista.
    
    Returns:
    list: Lista ordenada de diccionarios.
    """
    n = len(lista_empleados)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lista_empleados[j][elemento] > lista_empleados[j+1][elemento]:
                lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]
                swapped = True
        if not swapped:
            break
    return lista_empleados

# Ejemplo de uso
empleados = [
    {"nombre": "Ana", "edad": 28, "salario": 3000},
    {"nombre": "Luis", "edad": 22, "salario": 2500},
    {"nombre": "Pedro", "edad": 35, "salario": 4000},
    {"nombre": "María", "edad": 30, "salario": 3200}
]

print("Lista original:")
for empleado in empleados:
    print(empleado)

empleados_ordenados = ordenar_ascendente(empleados, "edad")

print("\nLista ordenada por edad:")
for empleado in empleados_ordenados:
    print(empleado)
