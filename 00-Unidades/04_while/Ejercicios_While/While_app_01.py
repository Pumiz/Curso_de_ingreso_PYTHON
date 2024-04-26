import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre:     Martín
apellido:   Gomez Valle
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_cantidad_ganadores = 0

        suma_gando_ruleta = 0
        promedio_ganado_ruleta = 0
        contador_ganadores_ruleta = 0

        maximo_retiro = 0
        nombre_mas_gano = None
        genero_mas_gano = None

        contador_ganadores_tragamonedas = 0
        porcentaje_jugadores_tragamonedas = 0


        contador_ganadores_poker = 0
        juego_menos_elegido = None

        suma_ganado_no_poker = 0
        promedio_ganado_no_poker = 0
        contador_ganado_no_poker = 0

        porcentaje_ganado_poker = 0
        porcentaje_ganado_tragamonedas = 0
        porcentaje_ganado_ruleta = 0


        continuar_cargando_usuarios = True

        #-------------WHILE----------------
        while continuar_cargando_usuarios:
            #-------------NOMBRE----------------
            nombre = input("\nIngrese su nombre ")

            #-------------IMPORTE----------------
            importe_retirar = input("Ingrese cuanto quiere retirar ")
            importe_retirar = int(importe_retirar)
            while importe_retirar < 1000:
                importe_retirar = input("Para retirar tiene que ser mas de $1000, reingrese monto ")
                importe_retirar = int(importe_retirar)

            #-------------JUEGO----------------
            juego = input("Ingrese el juego (Ruleta, Poker, Tragamonedas) ")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = input("Su juego esta fuera de rango, reingreselo. (Ruleta, Poker, Tragamonedas) ")

            match juego:
                case "Ruleta":
                    suma_gando_ruleta += importe_retirar
                    contador_ganadores_ruleta += 1

                    if importe_retirar > 15000:
                        contador_ganado_no_poker += 1
                        suma_ganado_no_poker += importe_retirar

                case "Tragamonedas":
                    contador_ganadores_tragamonedas += 1

                    if importe_retirar > 15000:
                        contador_ganado_no_poker += 1
                        suma_ganado_no_poker += importe_retirar

                case "Poker":
                    contador_ganadores_poker += 1



            #-------------GENERO----------------
            genero = input("Ingrese su genero (“Femenino”, “Masculino”, “Otro”) ")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = input("Su genero esta fuera de rango, reingreselo. (“Femenino”, “Masculino”, “Otro”) ")


            #-------------SALIDA----------------

            if importe_retirar > maximo_retiro:
                nombre_mas_gano = nombre
                genero_mas_gano = genero
                maximo_retiro = importe_retirar



            contador_cantidad_ganadores += 1

            continuar_cargando_usuarios = question("Salir", "Desea seguir cargando usuarios?")
            #desea_salir = input("Desea salir? ")
            #if desea_salir == "SALIR":                           #NO ME ANDA EL QUESTION :(
            #    continuar_cargando_usuarios = False
            #elif desea_salir == "SI":
            #    continuar_cargando_usuarios = True



        #1. Nombre y género de la persona que más ganó.
        print(f"\n1. El nombre de la persona que mas gano es: {nombre_mas_gano} y su genero es {genero_mas_gano}")

        #2. Promedio de dinero ganado en Ruleta.
        if contador_ganadores_ruleta == 0:
            promedio_ganado_ruleta = "No se pudo determinar"
        else: 
            promedio_ganado_ruleta = suma_gando_ruleta / contador_ganadores_ruleta
        print(f"2. El promedio de dinero gando en la ruleta es de ${promedio_ganado_ruleta}")

        #3. Porcentaje de personas que jugaron en el Tragamonedas.
        porcentaje_jugadores_tragamonedas = (contador_ganadores_tragamonedas * 100) / contador_cantidad_ganadores
        print(f"3. El porcentaje de personas que jugaron tragamonedas es de: {porcentaje_jugadores_tragamonedas}%")

        #4. Cuál es el juego menos elegido por los ganadores.
        if (contador_ganadores_ruleta < contador_ganadores_tragamonedas) or (contador_ganadores_ruleta < contador_ganadores_poker):
            juego_menos_elegido = "Ruleta"
        elif (contador_ganadores_tragamonedas < contador_ganadores_ruleta) or (contador_ganadores_tragamonedas < contador_ganadores_poker):
            juego_menos_elegido = "Tragamonedas"
        elif (contador_ganadores_poker < contador_ganadores_ruleta) or (contador_ganadores_poker < contador_ganadores_tragamonedas):
            juego_menos_elegido = "Poker"
        else:
            juego_menos_elegido = "No se pudo determinar"

        print(f"4. El juego menos elegido es: {juego_menos_elegido}")


        #5. Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
        if contador_ganado_no_poker == 0:
            promedio_ganado_no_poker = "No se pudo determinar"
        else: 
            promedio_ganado_no_poker = suma_ganado_no_poker / contador_ganado_no_poker
        print(f"5. El promedio de dinero gando de las personas que NO jugaron Poker es de ${promedio_ganado_no_poker}")


        #6. Porcentaje de dinero en función de cada juego'''
        porcentaje_jugadores_tragamonedas = (contador_ganadores_tragamonedas * 100) / contador_cantidad_ganadores
        porcentaje_ganado_poker = (contador_ganadores_poker * 100) / contador_cantidad_ganadores
        porcentaje_ganado_ruleta = (contador_ganadores_ruleta * 100) / contador_cantidad_ganadores

        print(f"6. El porcentaje de personas que jugaron tragamonedas es de: {porcentaje_jugadores_tragamonedas}% para Poker es: {porcentaje_ganado_poker}% y para Ruleta es: {porcentaje_ganado_ruleta}%")

    pass
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()