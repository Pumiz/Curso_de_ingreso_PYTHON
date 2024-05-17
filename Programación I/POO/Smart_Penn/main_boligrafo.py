#En el módulo Main, crear un bolígrafo de tinta “Azul” y un grosor “Fino” 
#y otro de tinta “Rojo” y un grosor “Grueso”

from class_boligrafo import *

boligrafo_1 = Boligrafo("Fino", "Azul")
boligrafo_2 = Boligrafo("Grueso", "Rojo")

print(boligrafo_1.escribir("Hola buenos dias, como estas? Mañana tenemos programacion"))
print(boligrafo_2.escribir("Hola buenos dias, como estas? Mañana tenemos programacion"))

print("\n" + boligrafo_1.recargar(40))
print(boligrafo_2.recargar(20))


