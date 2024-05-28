empleados = [{'id': 1, 'nombre': 'Lucas', 'apellido': 'Rodriguez', 'dni': 8652638, 'puesto': 'Asistente', 'salario': 350000.0},
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
            {'id': 18, 'nombre': 'Marcos', 'apellido': 'Alberca', 'dni': 7357919, 'puesto': 'Asistente', 'salario': 350000.0}]

for i in range(len(empleados)):
    if i == len(empleados) - 1:
        ultimo_empleado = empleados[i] #directorio del ultimo empleado de la lista
        id_ultimo_empleado = ultimo_empleado["id"] #ID del ultimo empleado de la lista 😎

print(type(ultimo_empleado))
print(id_ultimo_empleado)