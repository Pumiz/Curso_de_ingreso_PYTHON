from Package_Input.Input import *
#-----------------------------------ID INCREMENTAL-----------------------------------#
def get_ultimo_id(lista_con_diccionarios: list) -> int:
    # Funcion que optiene el ID del ultimo empleado de la lista
    #
    #    Argumento:
    #      lista_con_diccionarios [list] -> Lista con los diccionarios de los empleados
    #    Retorna:
    #      id_ultimo_empleado [int] -> Numero de id ultimo empleado
    
    for i in range(len(lista_con_diccionarios)):
        if i == len(lista_con_diccionarios) - 1:
            ultimo_empleado = lista_con_diccionarios[i] # ultimo_empleado = diccionario del ultimo empleado de la lista
            id_ultimo_empleado = ultimo_empleado["id"] # id_ultimo_empleado = ID del ultimo empleado de la lista 😎

    return id_ultimo_empleado

#-----------------------------------CREAR EMPLEADO-----------------------------------#

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


def ingresar_empleado_lista(lista_empleados: list, lista_total_empleados: list, ultimo_id: int):
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

    lista_empleados.append(crear_directorio_empleado(ultimo_id, nombre, apellido, dni, puesto, salario))
    lista_total_empleados.append(crear_directorio_empleado(ultimo_id, nombre, apellido, dni, puesto, salario))


    print("Empleado cargado con exito!")
    

    #return lista_empleados   #Puedo retornar otra nueva lista o actualizar la ya hardcodeada.

#-----------------------------------MODIFICAR EMPLEADO-----------------------------------#

def modifcar_elemento_empleado(diccionario_empleado: dict, elemento_modificar: str):
    # _descripcion_
    #
    #    Argumento:
    #      parametro [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_
    if elemento_modificar == "salario":
            nvo_elemento = get_float(f"Ingrese el nuevo sueldo en $: ", 
                                f"El sueldo tiene que ser mayor a $234.315: ",
                                234315, 9999999999, 3)

    elif elemento_modificar == "dni":
        nvo_elemento = get_int("Ingrese el nuevo numero de DNI: ", 
                                "El DNI tiene que ser mayor a 5.000.000 y menor a 9.999.999",
                                5000000, 9999999, 5)

    else:
        nvo_elemento = get_string_propio(f"Ingrese el {elemento_modificar} a reemplazar: ", 
                                    f"El {elemento_modificar} tiene que terner mas de 2 caracteres y menos de 20: "
                                    , 2, 20)

    while True:
        question_nombre = get_string_propio(f"Está seguro que quiere cambiar el {elemento_modificar} por: {nvo_elemento}?: ", 
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
def eliminar_empleado(lista_empleados:list, diccionario_eliminar: dict):
    # _descripcion_
    #
    #    Argumento:
    #      id_a_eliminar [tipoDeDato] -> _description_
    #    Retorna:
    #      retorna -> _description_

    for i in range(len(lista_empleados)):
        if lista_empleados[i] == diccionario_eliminar:
            print("Empleado encontrado.")
            question = get_string_propio(f"Desea eliminar a {diccionario_eliminar['nombre']} {diccionario_eliminar['apellido']} con DNI: {diccionario_eliminar['dni']}? ",
                    "Porfavor solo indique 'Si' / 'No': ", 1, 3)
            
            if question == "Si":
                empleado_eliminado = lista_empleados.pop(i)
                print("Eliminado con exito")
                return empleado_eliminado
            else:
                break


#-----------------------------------MOSTRAR-----------------------------------#
def mostrar_empleados(lista_empleados):
    # Encabezados de la tabla
    headers = ["Nombre", "Apellido", "Puesto", "Salario"]
    
    # Calcular el ancho máximo de cada columna
    col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *[empleado.values() for empleado in lista_empleados])]


def mostrar(lista_empleados: list):
    print("*"*73)
    print(f"|      NOMBRE     |     APELLIDO    |      PUESTO     |      SALARIO    |")
    print("-"*73)
    for i in range(len(lista_empleados)):
        print(f"|  {lista_empleados[i]['nombre']:<13}  |", end = "")
        print(f"  {lista_empleados[i]['apellido']:<13}  |", end = "")
        print(f"  {lista_empleados[i]['puesto']:<13}  |", end = "")
        print(f"  ${lista_empleados[i]['salario']:<12}  |")
    print("*"*73)

#-----------------------------------BUSCAR POR DNI-----------------------------------#
def buscar_dni(lista_empleados: list, dni_buscar: int):
    dni_no_encontrado = True

    for i in range(len(lista_empleados)):
        if lista_empleados[i]['dni'] == dni_buscar:
            dni_no_encontrado = False
            print("Empleado encontrado!")
            print(f"DNI: {lista_empleados[i]['dni']} || ID: {lista_empleados[i]['id']} || NOMBRE: {lista_empleados[i]['nombre']} || APELLIDO: {lista_empleados[i]['apellido']} || PUESTO: {lista_empleados[i]['puesto']} || SALARIO: ${lista_empleados[i]['salario']}")

    if dni_no_encontrado:
        print("El DNI ingresado no corresponde a ningun empleado")

#-----------------------------------ORDENAMIENTO -----------------------------------#

def ordenar_empleados(lista_empleados: list, elemento: str, metodo: str):

    for i in range(len(lista_empleados)):
        for j in range(0, len(lista_empleados)-i-1):
            if metodo == "Ascendente":
                if lista_empleados[j][elemento] > lista_empleados[j+1][elemento]:
                    lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]
            elif metodo == "Desendente":
                if lista_empleados[j][elemento] < lista_empleados[j+1][elemento]:
                    lista_empleados[j], lista_empleados[j+1] = lista_empleados[j+1], lista_empleados[j]

    question = get_string_propio("La lista se ha ordenado con exito!\nQuiere ver como quedo? ", "Indique solo 'Si' o 'No': ", 2, 2)
    if question == "Si":
        mostrar(lista_empleados)





