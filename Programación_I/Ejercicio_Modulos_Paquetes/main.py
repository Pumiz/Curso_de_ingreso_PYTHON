from Package_Input.Input import *

edad = get_int("Ingrese su edad ", "La edad ingresada esta fuerda de rango", 18, 100, 3)
print(f"La edad ingresada es: {edad}\n")

altura = get_float("Ingrese su estatura en metros ", "Su altura esta fuera de rango", 1.5, 2.2, 5)
print (f"La altura ingresada es: {altura}\n")

nombre = get_string("Ingrese su nombre", "Su nombre debe tener mas de 1 caracter y menos de 15", 1,15)
print(f"El nombre ingresado es: {nombre}\n")
