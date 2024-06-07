import json

# Ejemplo de lista con diccionarios
lista = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 28}
]

def guardar_lista_json(lista, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        json.dump(lista, archivo, indent=4)  # Guarda la lista en el archivo JSON con una sangría de 4 espacios

guardar_lista_json(lista, "datos.json")
