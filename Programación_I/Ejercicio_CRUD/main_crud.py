from Package_Input.Input import *
from Ejercicio_CRUD.Empleado import *

empleados = []

nombre = get_string("Ingrese su nombre", "Su nombre tiene que tener mas de 2 caracteres y menos de 15", 2, 10)

print(nombre)