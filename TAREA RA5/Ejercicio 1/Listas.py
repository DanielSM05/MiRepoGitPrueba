# 1. Crear la lista del 1 al 10
numeros = list(range(1, 11))
print("Lista inicial:", numeros)

# 2. Modificar la quinta posición (índice 4) por 99
numeros[4] = 99
print("Tras modificar la 5ª posición:", numeros)

# 3. Añadir 11 al final
numeros.append(11)
print("Tras añadir 11:", numeros)

# 4. Eliminar el valor 7
numeros.remove(7)
print("Tras eliminar el 7:", numeros)

# 5. Mostrar lista resultante y total de elementos
print("Lista resultante:", numeros)
print("Número total de elementos:", len(numeros))