import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print

Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno
DNI terminados en  0 o 1

1)informar la cantidad de personas de sexo  femenino
2) la edad promedio de  personas de sexo  masculino
3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)


DNI terminados en  2 o 3

1) informar la cantidad de personas de sexo  masculino
2) la edad promedio de  personas de sexo  nb
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


DNI terminados en  4 o 5

1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  6 o 7

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  8 o 9

1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre
'''
personas_ingresadas = 0
contador_masculino = 0
contador_femenino = 0
contador_nobinario = 0

sexo_mas_ingresado = ""

fiebre = 37
personas_con_fiebre = 0
personas_sin_fiebre = 0
procentaje_con_fiebre = 0
procentaje_sin_fiebre = 0

suma_edad_femenino = 0
promedio_edad_femenino = 0

nombre_temp_baja = ""
temperatura_mas_baja_masculino = 44     #Lo inicializo en 44 grados que es el maximo valor

while personas_ingresadas < 5: #CAMBIAR A 5!!!!!!!!!
    #---------------NOMBRE---------------
    nombre = input("\nIngrese su nombre ")

    #---------------TEMPERATURA---------------
    temperatura = input("Indique su temperatura ")
    temperatura = int(temperatura)

    while temperatura < 35 or temperatura > 42:
        temperatura = input("Su temperatura esta fuera de rango ")
        temperatura = int(temperatura)

    if temperatura >= fiebre:
        personas_con_fiebre += 1
    else: 
        personas_sin_fiebre += 1

    #---------------SEXO---------------
    sexo = input("Indique su sexo (M - F - NB) ")

    while sexo != "M" and sexo != "F" and  sexo != "NB":
        sexo = input("Su sexo es invalido ")

    match sexo:
        case "F":
            contador_femenino += 1
        case "M":
            contador_masculino += 1
            if temperatura_mas_baja_masculino > temperatura:
                nombre_temp_baja = nombre
                temperatura_mas_baja_masculino = temperatura
            else:
                temperatura_mas_baja_masculino = "No se pudo determinar"
        
        case "NB":
            contador_nobinario += 1

    #---------------EDAD---------------
    edad = input("Indique su edad ")
    edad = int(edad)

    while edad <= 0:
        edad = input("Su edad esta fuera de rango ")
        edad = int(edad)


    #---------------FINAL WHILE---------------
    if sexo == "F":
        suma_edad_femenino += edad

    personas_ingresadas += 1


#1)informar la cantidad de personas de sexo  nb
#2) la edad promedio de  personas de sexo  femenino
#3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)




#A-informar cual fue el sexo mas ingresado
if (contador_femenino > contador_masculino) and (contador_femenino > contador_nobinario):
    sexo_mas_ingresado = "Femenino"
elif (contador_masculino > contador_femenino) and (contador_masculino > contador_nobinario):
    sexo_mas_ingresado = "Masculino"
elif (contador_nobinario > contador_femenino) and (contador_nobinario > contador_masculino):
    sexo_mas_ingresado = "No Binario"
else:
    sexo_mas_ingresado = "No se pudo determinar"

print(f"\nEl sexo mas ingresado fue: {sexo_mas_ingresado}")



#B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

procentaje_con_fiebre = (personas_con_fiebre / personas_ingresadas) * 100
procentaje_sin_fiebre = (personas_sin_fiebre / personas_ingresadas) * 100

print(f"El porcentaje de personas con fiebre es de: {procentaje_con_fiebre}%. Sin fiebre el {procentaje_sin_fiebre}%")



#1)informar la cantidad de personas de sexo  nb
print(f"La cantida de persona de sexo No Binario son: {contador_nobinario}")



#2) la edad promedio de  personas de sexo  femenino
if contador_femenino == 0:
    promedio_edad_femenino = "No ingresaron mujeres"
else:
    promedio_edad_femenino = (suma_edad_femenino / contador_femenino)
print(f"El promedio de edad de mujeres es de: {promedio_edad_femenino}")



#3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)
print(f"El nombre de la persona masculina con mas baja temperatura es: {nombre_temp_baja}")