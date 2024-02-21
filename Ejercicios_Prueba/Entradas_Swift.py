import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #!X 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #!X 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #!X 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #!X 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltMaiplos de 6.
'''
PRECIO_GENERAL = 16000
PRECIO_CAMPO = 25000
PRECIO_PLATEA = 30000
DESCUENTO_CREDITO = 20
DESCUENTO_DEBITO = 15

seguir_comprando = True
cantidad_entrada_totales = 0

precio_ubicacion = 0
porcentaje_descuento = 0
precio_con_descuento = 0
precio_sin_descuento = 0
precio_final = 0

masculino_campo = 0
femenino_campo = 0
genero_otro_campo = 0

personas_general_credito = 0
suma_edad_general_credito = 0
promedio_edad_general_credito = 0

personas_platea_debito = 0
porcentaje_platea_debito = 0

descuento_credito_pesos = 0
porcentaje_descuento_credito = 0



while seguir_comprando == True:
    #--------------NOMBRE--------------
    nombre = input("Ingrese su nombre: ")

    #--------------EDAD--------------
    edad = input("Ingrese su edad: ")
    edad = int(edad)
    while edad < 16:
        edad = input("Error: Menor a 16. \nReingrese su edad: ")
        edad = int(edad)

    #--------------GENERO--------------
    genero = input("Ingrese su genero: ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("Genero no valido. \nReingrese su genero: ")

    #--------------ENTRADA--------------
    entrada = input("Ingrese su sector deseado: ")
    while entrada != "General" and entrada != "Campo" and entrada != "Platea":
        entrada = input("Sector no valido. \nReingrese el sector que desea comprar: ")

    cantidad_entrada_totales += 1

    match entrada:
        case "General":
            precio_ubicacion = PRECIO_GENERAL

        case "Campo":
            precio_ubicacion = PRECIO_CAMPO

            if genero == "Masculino":
                masculino_campo += 1
            elif genero == "Femenino":
                femenino_campo += 1
            elif genero == "Otro":
                genero_otro_campo += 1
            #Puede ser que esten empatados

        case "Platea":
            precio_ubicacion = PRECIO_PLATEA

    #--------------MEDIO DE PAGO--------------
    medio_pago = input("Ingrese el medio de pago: ")
    while medio_pago != "Efectivo" and medio_pago != "Credito" and medio_pago != "Debito":
        medio_pago = input("Medio de pago no valido. \nReingrese el medio de pago: ")

    match medio_pago:
        case "Credito":
            porcentaje_descuento = DESCUENTO_CREDITO
            porcentaje_descuento_credito += DESCUENTO_CREDITO

            if medio_pago == "Credito":
                personas_general_credito += 1
                suma_edad_general_credito += edad


        case "Debito":
            porcentaje_descuento = DESCUENTO_DEBITO
            if entrada == "Platea":
                personas_platea_debito += 1

    precio_con_descuento = precio_ubicacion - (precio_ubicacion * porcentaje_descuento) // 100

    if medio_pago != "Efectivo":
        print(f"\nEl precio para {entrada} es de {precio_ubicacion} Se le aplico un descuento del {porcentaje_descuento}% Y el precio final es de ${precio_con_descuento}")
    else:
        print(f"\nPara {entrada} el precio es de ${precio_ubicacion}")

    seguir_comprando = question("Salir", "Desea cargar otra compra?")


#!X 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
if (masculino_campo > femenino_campo) and (masculino_campo > genero_otro_campo):
    genero_mas_frecuente_campo = "Masculino"
elif (femenino_campo > masculino_campo) and (femenino_campo > genero_otro_campo):
    genero_mas_frecuente_campo = "Femenino"
elif (genero_otro_campo > masculino_campo) and (genero_otro_campo > femenino_campo):
    genero_mas_frecuente_campo = "Otro"
else:
    genero_mas_frecuente_campo = "No se pudo determinar"

print(f"\n1) El género más frecuente que compraron en 'Campo' es: {genero_mas_frecuente_campo}")


#! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
promedio_edad_general_credito = suma_edad_general_credito / personas_general_credito
print(f"\n2) Cantidad de personas que compraron entradas 'General' pagando con 'Crédito' fueron {personas_general_credito} \n\tY el promedio de su edad es {promedio_edad_general_credito} años.")


#! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito  respecto al total 
#       de personas en la lista.
porcentaje_platea_debito = (personas_platea_debito / cantidad_entrada_totales) * 100
print(f"\n3) El porcentaje para compras en Platea con Debito es: {porcentaje_platea_debito}%")


#! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
descuento_credito_pesos = (precio_ubicacion * porcentaje_descuento_credito) // 100
print(f"\n4) La suma de los descuentos en Credito fue de ${descuento_credito_pesos}")


#! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
#!          edad es un número primo.



