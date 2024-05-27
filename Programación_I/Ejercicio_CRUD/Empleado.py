from Package_Input.Input import *

def iniciar_diccionario(nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    # _descripcion_
    #
    #    Argumento:
    #      Nombre [str, Apellido: str, DNI: int, Puesto: str] -> _descriptio, Salario: intn -> dict_
    #    Retorna:
    #      retorna -> _description_
    
    dict_empleados = {
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'puesto': puesto,
        'salario': salario
    }
    
    return dict_empleados

def ingresar_empleado_lista(empleados: list):
    # _descripcion_
    #
    #    Argumento:
    #      empleados [list] -> _description_
    #    Retorna:
    #      retorna -> _description_
    
    nombre = get_string("Ingrese su nombre", "Reingrese", 1, 15)
    
    return nombre