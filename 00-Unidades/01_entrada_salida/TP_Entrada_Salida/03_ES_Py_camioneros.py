import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:     Martín
apellido:   Gomez Valle
---
TP: ES_Camioneros
---
Enunciado:

3.	Para el departamento de logística:

	A.	Es necesario saber la cantidad camiones que harian falta para transportar los materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la cantidad de toneladas necesarias de materiales a transportar. El programa deberá informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por viaje 3500kg

    B.	A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo (en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir a una velocidad máxima y constante de 90 km/h  

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Toneladas")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_toneladas = customtkinter.CTkEntry(master=self)
        self.txt_toneladas.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Kilómetros")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_kilometros = customtkinter.CTkEntry(master=self)
        self.txt_kilometros.grid(row=1, column=1)
       
        self.btn_cantidad_camiones = customtkinter.CTkButton(master=self, text="Calcular cantidad de camiones", command=self.btn_cantidad_camiones_on_click)
        self.btn_cantidad_camiones.grid(row=3, pady=10, padx=30 ,columnspan=2, sticky="nsew")
        
        self.btn_tiempo_llegada = customtkinter.CTkButton(master=self, text="Calcular tiempo de llegada", command=self.btn_tiempo_llegada_on_click)
        self.btn_tiempo_llegada.grid(row=4, pady=10, padx=30, columnspan=2, sticky="nsew")
    
    def btn_cantidad_camiones_on_click(self):
        cantidad_carga_x_camion = 3.5 # toneladas

        toneladas_materiales = self.txt_toneladas.get()
        toneladas_materiales = float(toneladas_materiales)
        
        camiones_llenos = toneladas_materiales // cantidad_carga_x_camion
        toneladas_sobrantes = toneladas_materiales % cantidad_carga_x_camion

        camiones_extras = (toneladas_sobrantes > 0)
        camiones_totales = camiones_extras + camiones_llenos

        respuesta = f"Para transportar las {toneladas_materiales}T se necesitan {camiones_totales} camiones."

        alert("Bienvenido", respuesta)

        pass

    def btn_tiempo_llegada_on_click(self):
        km_x_hora_camion = 90 #km/h
        minutos_por_hora = 60 #60 minutos

        cantidad_de_km = self.txt_kilometros.get()
        cantidad_de_km = float(cantidad_de_km)

        horas_completas = cantidad_de_km // km_x_hora_camion
        km_restantes = cantidad_de_km % km_x_hora_camion

        calculo_minutos = (km_restantes / km_x_hora_camion) * 100 #transformo el 0,x en x,0 (lo transformo en un numero entero)
        minutos_restantes = (minutos_por_hora * calculo_minutos) / 100

        respuesta = f"Para realizar {cantidad_de_km}km se tardarian {int(horas_completas)}hs y {int(minutos_restantes)} minutos."

        alert("Bienvenido", respuesta)
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()