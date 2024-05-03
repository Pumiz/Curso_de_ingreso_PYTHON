from os import system

#el legajo debe existir dentro de una matriz de legajos
legajo_choferes = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]       # los 15 choferes        1x5
]

lineas = [1,2,3]
lista_coches = [1,2,3,4,5]

coches = 0
linea = 0

recaudacion_lineas = [0,0,0]

recaudacion_coches = [0,0,0,0,0]

interactuar = True

menu = "\n\n1) Cargar Planilla\n2) Mostrar la recaudación de cada coches y líneas.\n3) Calcular y mostrar recaudación por línea.\n4) Calcular y mostrar recaudación por coche.\n5) Calcular y mostrar la recaudación total.\n6) Salir\n\nIngrese una opcion: "

while interactuar == True:
    opcion_seleccionada = int(input(menu))
    system("cls")#   "clear" -> Mac     "cls" -> Windows
    match opcion_seleccionada:
        case 1:
            #nombre = input("Ingrese su nombre: ")
            legajo = int(input("Ingrese su legajo: "))
            
            legajo_existente = False
            linea_existente = False
            coche_existente = False

            for i in range(legajo):
                while i in legajo_choferes:
                    legajo_existente = True
                    break

            if legajo_existente == True:
                linea_trabajada = int(input("Ingrese la linea: "))
                coche_ingresado = int(input("Ingrese el coche: "))
                recaudacion = int(input("Ingrese la recaudacion: "))

                if linea_trabajada in lineas:
                    linea_existente = True

                if coche_ingresado in coches:
                    coche_existente = True
                
                if coche_existente and linea_existente:

                    match coches:
                        case 1:
                            recaudacion_coches[coches-1] += recaudacion
                        case 2:
                            recaudacion_coches[coches-1] += recaudacion
                        case 3:
                            recaudacion_coches[coches-1] += recaudacion                            
                        case 4:
                            recaudacion_coches[coches-1] += recaudacion                            
                        case 5:
                            recaudacion_coches[coches-1] += recaudacion

                    match linea:
                        case 1:
                            recaudacion_lineas[linea-1] += recaudacion
                        case 2:
                            recaudacion_lineas[linea-1] += recaudacion
                        case 3:
                            recaudacion_lineas[linea-1] += recaudacion
                else:
                    print("No existe la linea o el coche")
            else:
                print("El legajo no existe")


        case 2:
            print(f"La recaudacion de las lineas fueron:")
            for i in range(len(linea)):
                print(linea[i], end=" --> ")
                print(recaudacion_lineas[i])







