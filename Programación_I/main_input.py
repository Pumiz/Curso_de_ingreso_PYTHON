from Ejercicio_Modulos_Paquetes.Package_Input.Input import *

nombre = get_string("Ingrese su nombre ", "Su nombre tiene que tener mas de 2 caracteres y menos de 15", 2, 10)
print(nombre)

edad = get_int("Ingrese su edad ", "Su edad tiene que ser mas de 1 y menos de 100 ", 1, 100, 3)
print(edad)

altura = get_float("Ingrese su altura en m ", "Su altura tiene que ser mas de 0.5 caracteres y menos de 2.2 ", 0.5, 2.2, 3)
print(altura)