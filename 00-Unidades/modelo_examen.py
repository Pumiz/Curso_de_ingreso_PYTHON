import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        continuar = True

        contador_masculino = 0
        contador_femenino = 0
        contador_nobinario = 0
        genero_mas_ingresado = None



        while continuar:
            nombre = prompt("Nombre", "Ingrese su nombre")


            temperatura = prompt("Temperatura", "Ingrese su temperatura")
            temperatura = float(temperatura)
            while temperatura < 35 and temperatura > 42:
                temperatura = prompt("Error", "Reingrese la temperatura")
                temperatura = float(temperatura)

            genero = prompt("genero", "Ingrese su genero")
            while genero != "f" and genero != "m" and genero != "nb":
                genero = prompt("Error", "Reingrese su genero f - m - nb")

            match genero:
                case "f":
                    contador_femenino += 1

                case "m":
                    contador_masculino += 1 

                case "nb":
                    contador_nobinario += 1

            edad = prompt("edad", "Ingrese su edad")
            edad = int(edad)
            while edad <= 0:
                edad = prompt("Error", "Reingrese su edad (mayor que 0)")
                edad = int(edad)





            continuar = question("Salir", "Quiere cargar mas datos?")


        if (contador_nobinario > contador_femenino) or (contador_nobinario > contador_masculino):
            genero_mas_ingresado = "No Binario"
        elif (contador_femenino > contador_masculino):
            genero_mas_ingresado = "Femenino"
        else:
            genero_mas_ingresado = "Masculino"
            

        print(f"El genero mas ingresado es {genero_mas_ingresado}")



        pass 

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
