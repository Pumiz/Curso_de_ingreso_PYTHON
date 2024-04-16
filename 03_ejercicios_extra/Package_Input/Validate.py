import Input

numero_entero = Input.get_int("Ingrese su edad ", "La edad es fuera de rango", 18, 99, 3)

print(f"El numero ingresado es: {numero_entero}")

flotante = Input.get_float("Ingrese su altura metros ", "La altura esta fuera de rango", 1.0, 2.0, 3)
print(f"El flotante ingresado es: {flotante}")

Input.get_string("UTN FRA Avellaneda", 20)