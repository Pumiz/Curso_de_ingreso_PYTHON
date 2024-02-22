import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:

    #!X 1) - Tipo de instrumento que menos se operó en total.
    #!X 2) - Cantidad de usuarios que compraron entre 50 y 200 MEP 
    #!X 3) - Cantidad de usuarios que no compraron CEDEAR 
    #!X 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #!X 5) - Nombre y posicion del usuario que invirtio menos dinero
    #!x 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #!X 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''
#--------------VARIABLES--------------
cantidad_usarios = 0

instrumento_menos_operado = 0
contador_cantidad_mep = 0
contador_cantidad_cedear = 0
contador_cantidad_bonos = 0
contador_no_compra_cedear = 0

contador_50_200_meps = 0

primer_compra_bonos_cedear = True
nombre_compra_bonos_cedear = ""
cantidad_compra_bonos_cedear = 0

capital_minimo = 1000000
posicion_menos_invirtio = 1
nombre_menos_invirtio = ""

suma_capital_cedear = 0
promedio_capital_cedear = 0

suma_cantidad_mep = 0
promedio_cantidad_mep = 0

#--------------WHILE--------------
while cantidad_usarios < 3:                  #UMMENTAR A 5 
    #--------------NOMBRE--------------
    nombre = input("\nIngrese su nombre ")

    #--------------CAPITAL--------------
    capital = input("Ingrese el monto que desea invertir ")
    capital = int(capital)
    while capital < 10000:
        capital = input("La cantidad debe ser mas de $10.000. \nReingrese la capital: ")
        capital = int(capital)

    if capital < capital_minimo:
        capital_minimo = capital
        posicion_menos_invirtio += cantidad_usarios
        nombre_menos_invirtio = nombre

    #--------------INSTRUMENTO--------------
    instrumento = input("Ingrese en donde queire invertir ")

    while instrumento != "CEDEAR" and instrumento != "BONOS" and instrumento != "MEP":
        instrumento = input("Intrumento no valido. \nReingrese el instrumento: ")

    match instrumento:
        case "CEDEAR":
            contador_cantidad_cedear += 1 
            suma_capital_cedear += capital
        case "MEP":
            contador_cantidad_mep += 1
            contador_no_compra_cedear += 1
        case "BONOS":
            contador_cantidad_bonos += 1
            contador_no_compra_cedear += 1

    #--------------CANTIDAD--------------
    cantidad_instrumento = input(f"Cuantos {instrumento} desea comprar? ")
    cantidad_instrumento = int(cantidad_instrumento)
    while cantidad_instrumento < 0:
        cantidad_instrumento = input("La cantidad debe ser mas de 1. \nReingrese la cantidad: ")
        cantidad_instrumento = int(cantidad_instrumento)

    if instrumento == "MEP":
        suma_cantidad_mep += cantidad_instrumento

        if cantidad_instrumento > 50 and cantidad_instrumento < 200:
            contador_50_200_meps += 1

        #Promedio de cantidad de instrumentos  MEP vendidos en total

    if primer_compra_bonos_cedear == True and (instrumento == "BONOS" or instrumento == "CEDEAR"):
        nombre_compra_bonos_cedear = nombre
        cantidad_compra_bonos_cedear = cantidad_instrumento
        primer_compra_bonos_cedear = False #De esta manera cuando se encuentra al primero no se vuelve a preguntar

    cantidad_usarios += 1


#--------------RESULTADOS / MUESTREO--------------
#! 1) - Tipo de instrumento que menos se operó en total.
if (contador_cantidad_cedear < contador_cantidad_mep) and (contador_cantidad_cedear < contador_cantidad_bonos):
    instrumento_menos_operado = "CEDEAR"
elif (contador_cantidad_mep < contador_cantidad_cedear) and (contador_cantidad_mep < contador_cantidad_bonos):
    instrumento_menos_operado = "MEP"
elif (contador_cantidad_bonos < contador_cantidad_cedear) and (contador_cantidad_bonos < contador_cantidad_mep):
    instrumento_menos_operado = "BONOS"
else:
    instrumento_menos_operado = "No se pudo determinar"

print(f"\n1) El instrumento menos elegido fue: {instrumento_menos_operado}")


#!X 2) - Cantidad de usuarios que compraron entre 50 y 200 MEP 
print(f"\n2) Los usuarios que compraron mas de 50 y menos de 200 dolares MEP fueron: {contador_50_200_meps}")


#! 3) - Cantidad de usuarios que no compraron CEDEAR 
print(f"\n3) La cantidad de usuarios que NO compraron CEDEARS son: {contador_no_compra_cedear}")


#! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
print(f"\n4) El primer usuario que compro BONOS o CEDEAR se llama {nombre_compra_bonos_cedear} y compro {cantidad_compra_bonos_cedear}.")


#! 5) - Nombre y posicion del usuario que invirtio menos dinero
print(f"\n5) La persona que menos capital invirtio se llama: {nombre_menos_invirtio} y fue el usuario N°{posicion_menos_invirtio}")


#! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
promedio_capital_cedear = suma_capital_cedear / cantidad_usarios
print(f"\n6) El promedio de dinero invertirdo en CEDEAR es ${promedio_capital_cedear}")


#! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total  
promedio_cantidad_mep = suma_cantidad_mep / cantidad_usarios
print(f"\n7) El promedio de la cantidad vendida en dolar MEP es {promedio_cantidad_mep}")