# 1. Crear el diccionario productos
productos = {
    "Teclado": 25.99,
    "Ratón": 15.50,
    "Monitor": 189.90,
    "Webcam": 39.90
}
print("Diccionario productos:", productos)

# 2. Crear diccionario seleccionados accediendo por clave
seleccionados = {
    "Teclado": productos["Teclado"],
    "Ratón": productos["Ratón"]
}

# 3. Mostrar ambos diccionarios
print("Diccionario seleccionados:", seleccionados)