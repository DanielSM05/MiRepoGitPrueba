# 1. Crear el diccionario por producto
teclado = {"nombre": "Teclado", "cantidad": 32, "precio": 4.50}
raton   = {"nombre": "Ratón",   "cantidad": 21, "precio": 3.75}
monitor = {"nombre": "Monitor", "cantidad": 11, "precio": 69.90}

# 2. Almacenar en lista
inventario = [teclado, raton, monitor]

# 3. Mostrar la lista completa
print("Inventario Completo", inventario)

# 4. Nombre del segundo producto
print("Nombre del segundo producto:", inventario[1]["nombre"])

# 5. Modificar cantidad de monitores a 4
inventario[2]["cantidad"] = 4
print("Monitor actualizado:", inventario[2])

# 6. Añadir nuevo producto Webcam
webcam = {"nombre": "Webcam", "cantidad": 2, "precio": 39.90}
inventario.append(webcam)

# 7. Eliminar el ratón (índice 1)
inventario.pop(1)

# 8. Mostrar inventario actualizado y número de productos
print("Inventario actualizado:", inventario)
print("Número de productos:", len(inventario))