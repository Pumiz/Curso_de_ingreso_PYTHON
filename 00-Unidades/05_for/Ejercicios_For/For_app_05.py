import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Martín
apellido:   Gomez Valle
---
Ejercicio: for_05
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_numeros_pares = 0

        numero_ingresado = prompt("UTN", "Ingrese un numero ")
        numero_ingresado = int(numero_ingresado)

        for i in range(2, numero_ingresado+1):
            if i % 2 == 0:
                contador_numeros_pares += 1 
                print(f"\nNumero par hasta el {numero_ingresado}: {i}")

        print(f"La cantida de numeros pares son: {contador_numeros_pares}")
        pass

            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()