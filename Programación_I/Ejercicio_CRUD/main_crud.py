from Package_Input.Input import *
from Empleado import *
from os import system

empleados_trabajando = [{'id': 1, 'nombre': 'Lucas', 'apellido': 'Rodriguez', 'dni': 8652638, 'puesto': 'Asistente', 'salario': 350000.0},
            {'id': 2, 'nombre': 'Carlos', 'apellido': 'Pomelo', 'dni': 7357903, 'puesto': 'Analista', 'salario': 450000.0},
            {'id': 3, 'nombre': 'Pepe', 'apellido': 'Gonzales', 'dni': 7357904, 'puesto': 'Analista', 'salario': 450000.0},
            {'id': 4, 'nombre': 'Enzo', 'apellido': 'Gomez', 'dni': 7357905, 'puesto': 'Encargado', 'salario': 500000.0},
            {'id': 5, 'nombre': 'Juan', 'apellido': 'Gocillo', 'dni': 7357906, 'puesto': 'Encargado', 'salario': 500000.0},
            {'id': 6, 'nombre': 'Juan', 'apellido': 'Perez', 'dni': 8357907, 'puesto': 'Encargado', 'salario': 500000.0},
            {'id': 7, 'nombre': 'Valentin', 'apellido': 'Martinez', 'dni': 9357908, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 8, 'nombre': 'Valentino', 'apellido': 'Sociedad', 'dni': 6357909, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 9, 'nombre': 'Santiago', 'apellido': 'Perez', 'dni': 7357910, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 10, 'nombre': 'Santino', 'apellido': 'Santo', 'dni': 5357911, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 11, 'nombre': 'Lucia', 'apellido': 'Perez', 'dni': 7357912, 'puesto': 'Analista', 'salario': 450000.0},
            {'id': 12, 'nombre': 'Ludmila', 'apellido': 'Martinez', 'dni': 7357913, 'puesto': 'Encargado', 'salario': 500000.0},
            {'id': 13, 'nombre': 'Josefina', 'apellido': 'Gomez', 'dni': 6357914, 'puesto': 'Encargado', 'salario': 500000.0},
            {'id': 14, 'nombre': 'Josue', 'apellido': 'Delphi', 'dni': 7357915, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 15, 'nombre': 'Justin', 'apellido': 'Marks', 'dni': 8357916, 'puesto': 'Gerente', 'salario': 650000.0},
            {'id': 16, 'nombre': 'Julian', 'apellido': 'Richards', 'dni': 9357917, 'puesto': 'Asistente', 'salario': 350000.0},
            {'id': 17, 'nombre': 'Juliana', 'apellido': 'Enciso', 'dni': 6357918, 'puesto': 'Asistente', 'salario': 350000.0},
            {'id': 18, 'nombre': 'Marcos', 'apellido': 'Alberca', 'dni': 7357919, 'puesto': 'Asistente', 'salario': 350000.0},]


historial_de_empleados = empleados_trabajando.copy() #Copio de esta manera para que no se actualice todo el tiempo :)

ultimo_id = get_ultimo_id(historial_de_empleados)

interactuar = True

menu = "\n1. Ingresar empleado.\n2. Modificar empleado.\n3. Eliminar empleado.\n4. Mostrar datos.\n5. Calcular salario promedio.\n6. Buscar empleado por DNI.\n7. Ordenar empleados.\n8. Salir.\n\nIngrese una opcion: "

while interactuar:
    opcion_seleccionada = get_int(menu, "La opcion ingresada no existe, reintente.", 1, 8, 3) #Al estar dentro del while true no sale si  se terminan los reintentos
    system("clear")
    match opcion_seleccionada:
        case 1:
            if len(empleados_trabajando) < 20:
                nvo_empleado = ingresar_empleado_lista(empleados_trabajando, historial_de_empleados, ultimo_id)
                ultimo_id = get_ultimo_id(historial_de_empleados)
            else:
                print(f"No se puede agregar otro empleado. Los empleados trabajando ya son {len(empleados_trabajando)}...")

        case 2:
            id_a_modificar = get_int("Ingrese la ID del empleado que desea modificar: ",
                                    "La ID ingresada no corresponde a un empleado", 1, 100, 5)
            if id_a_modificar <= ultimo_id:
                modificar_empleado(id_a_modificar, empleados_trabajando)
            else:
                print("El empleado que desea modificar no existe...")
    
        case 3:
            id_a_eliminar = get_int("Ingrese la ID del empleado que desea eliminar: ",
                                    "La ID ingresada no corresponde a un empleado", 1, 100, 5)
            
            if id_a_eliminar <= ultimo_id:
                empleado = empleados_trabajando[id_a_eliminar - 1]
                eliminar_empleado(empleados_trabajando, empleado)
            else:
                print("El empleado que quiere eliminar no existe...")

        case 4:
            mostrar(empleados_trabajando)

        case 5:
            suma_sueldos = 0
            for i in range(len(empleados_trabajando)):
                sueldo = empleados_trabajando[i]['salario']
                suma_sueldos += sueldo

            promedio_sueldos = suma_sueldos / len(empleados_trabajando)
            print(f"El promedio de los sueldos es de: ${promedio_sueldos:.2f}") #El .2f solo muestras los 2 primeros decimales


        case 6:
            dni_buscar = get_int("Ingrese el DNI del empleado que desea buscar: ",
                                "El numero de DNI tiene que ser mayor a 5.000.000 y menor a 9.999.999: ", 
                                5000000, 9999999, 3)
            buscar_dni(empleados_trabajando, dni_buscar)
            
        case 7:
            elemento_mostrar = get_string_lower("Ingrese como quiere listar los empleados: ", 
                                                "Solo puede listarlos por; Nombre, Apellido o Salario: ", 6, 8)
            metodo = get_string_propio("Los quiere ordenar de manera 'Ascendente' o 'Desendente'? ", 
                                        "Solo se puede ordenar de mandera 'Ascendente' o 'Desendente': ", 10, 10)
            ordenar_empleados(empleados_trabajando, elemento_mostrar, metodo)
            

        case 8:
            print("Grcias por utilizar el programa :D.")
            interactuar = False
