import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Martín
apellido:   Gomez Valle
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        suma_positivos = 0
        suma_negativos = 0
        cantidad_ceros = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        producto_negativos = 1

        while True:
            numero_ingresado_str = prompt("UTN", "Ingrese un número")

            if not numero_ingresado_str:
                break

            else:
                numero_ingresado = int(numero_ingresado_str)

                if numero_ingresado > 0:
                    suma_positivos += numero_ingresado
                    cantidad_positivos += 1

                elif numero_ingresado < 0:
                    suma_negativos += numero_ingresado
                    cantidad_negativos += 1

                else:
                    cantidad_ceros += 1

        diferencia_positivos = cantidad_positivos - cantidad_negativos

        alert("UTN", f"Suma positivos: {suma_positivos}")
        alert("UTN", f"Suma negativos: {suma_negativos}")
        alert("UTN", f"Cantidad de negativos: {cantidad_negativos}")
        alert("UTN", f"Cantidad de positivos: {cantidad_positivos}")
        alert("UTN", f"Cantidad de ceros: {cantidad_ceros}")
        alert("UTN", f"Diferencia de positivos: {diferencia_positivos}")
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
