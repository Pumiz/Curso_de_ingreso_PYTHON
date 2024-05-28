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

historial_de_empleados = empleados_trabajando






interactuar = True

menu = "\n1. Ingresar Empleado.\n2. Modifical empleado.\n3. Eliminar empleado.\n4. Mostrar datos.\n5. Calcular salario promedio.\n6. Buscar empleado por DNI.\n7. Ordenar empleados.\n7. Salir.\n\nIngrese una opcion: "

#legajo = get_int("Ingrese su legajo: ", "El legajo esta fuera de rango, reintente", 10, 1000, 3)
#for fila in legajo_choferes:
#    if legajo in fila:
#        interactuar = True
#    else:
#        print("El legajo ingresado no existe ")

while interactuar:
    opcion_seleccionada = get_int(menu, "La opcion ingresada no existe, reintente.", 1, 8, 3) #Al estar dentro del while true no sale si  se terminan los reintentos
    system("clear")#   "clear" -> Mac     "cls" -> Windows
    match opcion_seleccionada:
        case 1:
            if len(empleados_trabajando) < 20:
                nvo_empleado = ingresar_empleado_lista(empleados_trabajando)
            else:
                print(f"No se puede agregar otro empleado. Los empleados trabajando ya son {len(empleados_trabajando)}...")

        case 2:
            for i in range(len(empleados_trabajando)):
                print(empleados_trabajando[i])

        case 3:
            pass

        case 4:
            pass

        case 5:
            pass

        case 6:
            pass

        case 7:
            pass

        case 8:
            pass
