# 1. Crear el diccionario de calificaciones
calificaciones = {
    "Alicia": [7, 8, 6],
    "Bruno":  [5, 4, 6],
    "Celia":  [9, 8, 9],
    "Diego":  [6, 6, 5]
}

# 2. Mostrar diccionario completo
print("Diccionario completo:", calificaciones)

# 3. Calificaciones de Alicia
print("Calificaciones de Alicia:", calificaciones["Alicia"])

# 4. Segunda actividad de Bruno (índice 1)
print("Segunda actividad de Bruno:", calificaciones["Bruno"][1])

# 5. Modificar tercera calificación de Diego (índice 2) a 7
calificaciones["Diego"][2] = 7
print("Diego actualizado:", calificaciones["Diego"])

# 6. Añadir a Elena
calificaciones["Elena"] = [8, 7, 9]

# 7. Eliminar a Bruno
del calificaciones["Bruno"]

# 8. Mostrar diccionario actualizado y resúmenes
print("Diccionario actualizado:", calificaciones)
print("Estudiantes (keys):", calificaciones.keys())
print("Calificaciones (values):", calificaciones.values())
print("Número total de estudiantes:", len(calificaciones))