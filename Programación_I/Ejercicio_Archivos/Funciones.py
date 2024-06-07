from Package_Input.Input import *
import re
import json

#-----------------------------------DESCOMPRIMIR ARCHIVO-----------------------------------#
def diccionar_archivo(path: str, lista: list) -> list:
    with open(path, "r") as archivo:
        for linea in archivo:
            registro = re.split(",|\n", linea)

            if registro[0] != "id": #Para que no haga un "empleado" con los datos de cada elemento
                empleado = {
                    'id': registro[0],
                    'nombre': registro[1],
                    'apellido': registro[2],
                    'dni': registro[3],
                    'puesto': registro[4],
                    'salario': registro[5]
                }

                lista.append(empleado)
    return lista

#-----------------------------------INGRESAR NUEVO EMPLEADO-----------------------------------#
def get_ultimo_id(lista_con_diccionarios: list) -> int:
    # Funcion que optiene el ID del ultimo empleado de la lista
    #
    #    Argumento:
    #      lista_con_diccionarios [list] -> Lista con los diccionarios de los empleados
    #    Retorna:
    #      id_ultimo_empleado [int] -> Numero de id ultimo empleado
    
    for i in range(len(lista_con_diccionarios)):
        if i == len(lista_con_diccionarios) - 1:
            id_ultimo_empleado = lista_con_diccionarios[i]["id"] # ultimo_empleado = diccionario del ultimo empleado de la lista
            id_ultimo_empleado = int(id_ultimo_empleado)

    return id_ultimo_empleado

def crear_directorio_empleado(lista_empleados: list, nvo_id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    # _descripcion_
    #
    #    Argumento:
    #      Nombre [str, Apellido: str, DNI: int, Puesto: str] -> _descriptio, Salario: intn -> dict_
    #    Retorna:
    #      retorna -> _description_

    dict_empleado = {
        'id': nvo_id,
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'puesto': puesto,
        'salario': salario
    }

    lista_empleados.append(dict_empleado)

    return dict_empleado

def ingresar_empleado_lista(lista_empleados: list, ultimo_id: int):
    puestos_validos = ["Gerente", "Supervisor", "Analista", "Encargado", "Asistente"]
    nvo_id = ultimo_id + 1

    nombre = get_string_propio("Ingrese el nombre: ", "El nombre tiene que tener mas de 2 caracteres y menos de 20: ", 2, 20)
    apellido = get_string_propio("Ingrese el apellido: ", "El apellido tiene que tener mas de 2 caracteres y menos de 20: ", 2, 20)
    dni = get_int("Ingrese el DNI: ", "El DNI esta fuera de rango, reintente: ", 5000000, 99999999, 5)

    while True:
        puesto = get_string_propio("Ingrese su puesto: ", 
            f"El puesto tiene que puesto tiene que ser {puestos_validos} y tener mas de 2 caracteres y menos de 15: ",
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
            print("Ese puesto no existe, reintente")

    salario = get_float("Ingrese el salario: ", "El salario tiene que mayor al salario minimo: ", 234315, 9999999999999, 3)

    diccionerio_empleado = crear_directorio_empleado(lista_empleados, nvo_id, nombre, apellido, dni, puesto, salario)
    lista_empleados.append(diccionerio_empleado)

#-----------------------------------MODIFICAR EMPLEADO-----------------------------------#

def modifcar_elemento_empleado(diccionario_empleado: dict):
    # _descripcion_
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    menu = "1. Nombre\n2. Apellido\n3. DNI\n4. Puesto\n5. Salario\n\nIngrese una opcion: "
    opcion_modificar = get_int(menu, "Solo puede modificar esos atriburos, ingrese una opcion: ", 1, 5,3)
    match menu:
        case 1:
            nvo_elemento = get_string_propio(f"Ingrese el nuevo nombre: ", 
                                    f"El nombre tiene que terner mas de 2 caracteres y menos de 20: "
                                    , 2, 20)
            elemento_modificar = "nombre"
        case 2:
            nvo_elemento = get_string_propio(f"Ingrese el nuevo apellido: ", 
                                    f"El apellido tiene que terner mas de 2 caracteres y menos de 20: "
                                    , 2, 20)
            elemento_modificar = "apellido"
        case 3:
            nvo_elemento = get_int("Ingrese el nuevo numero de DNI: ", 
                                "El DNI tiene que ser mayor a 5.000.000 y menor a 9.999.999",
                                5000000, 9999999, 5)
            elemento_modificar = "dni"
        case 4:
            nvo_elemento = get_string_propio(f"Ingrese el nuevo puesto: ", 
                                    f"El puesto tiene que terner mas de 2 caracteres y menos de 20: "
                                    , 2, 20)
            elemento_modificar = "puesto"
        case 5:
            nvo_elemento = get_float(f"Ingrese el nuevo sueldo en $: ", 
                                f"El sueldo tiene que ser mayor a $234.315: ",
                                234315, 9999999999, 3)
            elemento_modificar = "sueldo"

    while True:
        question_nombre = get_string_propio(f"Está seguro que quiere realizar los cambios?: ", 
                                            "Porfavor solo indique 'Si' / 'No': ", 1, 3) 
        if question_nombre == "Si":
            diccionario_empleado[f'{elemento_modificar}'] = nvo_elemento
            print(f"El {elemento_modificar} se ha cambiado con exito!")
            break
        else:
            break

def modificar_empleado(id_buscar: int, lista_empleados):
    # _descripcion_
    #
    #    Argumento:
    #      id [int] -> _description_
    #    Retorna:
    #      retorna -> _description_
    empleado = lista_empleados[id_buscar - 1]

    question = get_string_propio(f"Desea modificar a {empleado['nombre']} {empleado['apellido']} con DNI: {empleado['dni']}? ",
                    "Porfavor solo indique 'Si' / 'No': ", 1, 3)

    if question == "Si":
        modificar = get_string_lower("Que desea modificar del empleado?: ",
                                    "Solo puedo modificar el Nombre / Apellido / DNI / Puesto / Salario", 2, 9)
        modifcar_elemento_empleado(empleado, modificar)

#-----------------------------------ELIMINAR EMPLEADO-----------------------------------#
def guardar_lista_json(lista, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista, nombre_archivo, indent=4)

def eliminar_empleado(lista_empleados:list, diccionario_eliminar: dict, lista_eliminados: list):
    for i in range(len(lista_empleados)):
        if lista_empleados[i] == diccionario_eliminar:
            print("Empleado encontrado.")
            question = get_string_propio(f"Desea eliminar a {diccionario_eliminar['nombre']} {diccionario_eliminar['apellido']} con DNI: {diccionario_eliminar['dni']}? ",
                    "Porfavor solo indique 'Si' / 'No': ", 1, 3)
            
            if question == "Si":
                empleado_eliminado = lista_empleados.pop(i)
                lista_eliminados.append(empleado_eliminado)
                guardar_lista_json(lista_eliminados, "Eliminados.json")
                print("Eliminado con exito")
                return empleado_eliminado
            else:
                break
