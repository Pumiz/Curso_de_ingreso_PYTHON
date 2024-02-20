import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Martín
apellido:   Gomez Valle
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        #Variables
        PRECIO_UNITARIO = 800
        porcentaje_de_descuento = 0
        porcentaje_descuento_adicional = 0

        #Entrada
        marca_elegida = self.combobox_marca.get()
        cantidad_compradas = self.combobox_cantidad.get()
        cantidad_compradas = int(cantidad_compradas)

        #Proceso
        match (cantidad_compradas, marca_elegida):
            case (6, _) | (7, _) | (8, _) | (9, _) | (10, _) | (11, _) | (12, _):
                porcentaje_de_descuento = 50

            case (5, "ArgentinaLuz"):
                porcentaje_de_descuento = 40

            case (5, _):
                porcentaje_de_descuento = 30

            case (4, "ArgentinaLuz") | (4, "FelipeLamparas"):
                porcentaje_de_descuento = 25

            case (4, _):
                porcentaje_de_descuento = 20

            case (3, "ArgentinaLuz"):
                porcentaje_de_descuento = 15

            case (3, "FelipeLamparas"):
                porcentaje_de_descuento = 10

            case (3, _):
                porcentaje_de_descuento = 5

            case (_, _):
                porcentaje_de_descuento = 0

        precio_subtotal = PRECIO_UNITARIO * cantidad_compradas
        calculo_descuento = (precio_subtotal * porcentaje_de_descuento) // 100
        precio_final = precio_subtotal - calculo_descuento

        if precio_final >= 4000:
            porcentaje_descuento_adicional = 5
            calculo_descuento = (precio_final * porcentaje_descuento_adicional) // 100
            precio_final = precio_final - calculo_descuento
        
        #descuento_final =  porcentaje_de_descuento + porcentaje_descuento_adicional

        #Salida
        alert("Factura", f"El precio final por la compra de {cantidad_compradas} lamparas es de ${precio_final} y se le aplicó un descuento del {porcentaje_de_descuento}%")
        
        pass
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()