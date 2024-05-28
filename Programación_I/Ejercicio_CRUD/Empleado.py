from Package_Input.Input import *

def get_ultimo_id(lista_con_diccionario: list) -> int:
    # Funcion que optiene el ID del ultimo empleado de la lista
    #
    #    Argumento:
    #      lista_con_diccionario [list] -> Lista con los diccionarios de los empleados
    #    Retorna:
    #      id_ultimo_empleado [int] -> Numero de id ultimo empleado
    
    for i in range(len(lista_con_diccionario)):
        if i == len(lista_con_diccionario) - 1:
            ultimo_empleado = lista_con_diccionario[i] # ultimo_empleado = diccionario del ultimo empleado de la lista
            id_ultimo_empleado = ultimo_empleado["id"] # id_ultimo_empleado = ID del ultimo empleado de la lista 😎

    return id_ultimo_empleado

def crear_directorio_empleado(ultimo_id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    # _descripcion_
    #
    #    Argumento:
    #      Nombre [str, Apellido: str, DNI: int, Puesto: str] -> _descriptio, Salario: intn -> dict_
    #    Retorna:
    #      retorna -> _description_
    id_nvo = ultimo_id + 1
    dict_empleado = {
        'id': id_nvo,
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'puesto': puesto,
        'salario': salario
    }
    return dict_empleado


def ingresar_empleado_lista(lista_empleados: list) -> list:
    # _descripcion_
    #
    #    Argumento:
    #      empleados [list] -> _description_
    #    Retorna:
    #      retorna -> _description_
    
    puestos_validos = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]

    nombre = get_string_propio("Ingrese su nombre: ", "Su nombre tiene que tener mas de 2 caracteres y menos de 20: ", 2, 20)
    apellido = get_string_propio("Ingrese su apellido: ", "Su apellido tiene que tener mas de 2 caracteres y menos de 20: ", 2, 20)
    dni = get_int("Ingrese su DNI: ", "Su DNI esta fuera de rango, reintente: ", 5000000, 99999999, 5)

    while True:
        puesto = get_string_propio("Ingrese su puesto: ", 
            f"Su puesto tiene que puesto tiene que ser {puestos_validos} y tener mas de 2 caracteres y menos de 15: ",
            2, 15)
        cadena_valida = False

        # Recorrer la lista y comparar cada elemento
        for i in puestos_validos:
            if puesto == i:
                cadena_valida = True
                break

        # Verificar si la cadena es válida
        if cadena_valida:
            break
        else:
            print("Su puesto no existe, reintente")

    salario = get_float("Ingrese su salario: ", "Su salario tiene que mayor al salario minimo: ", 234315, 9999999999999, 3)

    ultimo_id = get_ultimo_id(lista_empleados)

    lista_empleados.append(crear_directorio_empleado(ultimo_id, nombre, apellido, dni, puesto, salario))

    print("Empleado cargado con exito!")
    

    return lista_empleados   #Puedo retornar otra nueva lista o actualizar la ya hardcodeada.