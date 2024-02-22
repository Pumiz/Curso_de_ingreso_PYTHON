import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Martín
apellido:   Gomez Valle
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        ultimo_nombre = ""
        maximos_votos = 0
        minimo_votos = 1000000
        mas_votado = ""
        menos_votado = ""
        votos_totales = 0
        suma_edades = 0
        cantidad_candidatos = 0
        promedio_edades = 0
        edad_menos_votado = 0


        while True:
            nombre = prompt("Bienvenido", "Ingrese su nombre")

            if nombre == None:
                nombre = ultimo_nombre
                break

            edad = prompt("Bienvenido", "Ingrese su edad")
            edad = int(edad)
            #if edad <= 25:
            #    alert("Error", "Usted no esta en el rango de edad para este cuestionario")
            #    break
            suma_edades += edad

            cantidad_votos = prompt("Bienvenido", "Ingrese la cantidad de votos")
            cantidad_votos = int(cantidad_votos)

            if cantidad_votos < 0:
                alert("Error", "La cantidad de votos no puede ser menor a 0")
                break
            votos_totales += cantidad_votos

            if cantidad_votos > maximos_votos:
                maximos_votos = cantidad_votos
                mas_votado = nombre

            if cantidad_votos < minimo_votos:
                minimo_votos = cantidad_votos
                menos_votado = nombre
                edad_menos_votado = edad

        ultimo_nombre = nombre
        cantidad_candidatos += 1
        promedio_edades = suma_edades / cantidad_candidatos
            
        alert("Bienvenido", f"a. {mas_votado} fue el mas votado con un total de: {maximos_votos} votos")
        alert("Bienvenido", f"b. {menos_votado} con {edad_menos_votado} años obtuvo la menor cantidad de votos: {minimo_votos}")
        alert("Bienvenido", f"c. El promedio de edad de los condidatos es: {promedio_edades}")
        alert("Bienvenido", f"d. La cantidad de votos totales fueron: {votos_totales}")
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
