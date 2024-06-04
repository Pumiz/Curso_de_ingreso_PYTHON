while True:
    # Aquí irían las acciones o cambios de tu programa
    print("Realizando cambios en el programa...")

    # Preguntar al usuario si desea continuar
    respuesta = input("¿Quieres seguir haciendo cambios? (si/no): ").strip().lower()
    
    if respuesta != 'si':
        print("Terminando el programa...")
        break
