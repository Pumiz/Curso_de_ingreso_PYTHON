"""
import funciones  #Importa todo y tengo que llamarla con 'nombre_del_archivo.funcion_a_llamar()'

numero_1 = 5
numero_2 = 3

print(f"\nEl resultado de la suma es: {funciones.sumar(numero_1, numero_2)}")"""


from funciones import sumar  # Si pongo '*' importo todo lo de ese archivo en cambio así solo 
#                              importe la o las funciones que solicito

numero_1 = 5
numero_2 = 3

print(f"\nEl resultado de la suma es: {sumar(numero_1, numero_2)}")