# 1. Solicitar los 7 días uno a uno
dia1 = input("Introduce el nombre del día 1: ")
dia2 = input("Introduce el nombre del día 2: ")
dia3 = input("Introduce el nombre del día 3: ")
dia4 = input("Introduce el nombre del día 4: ")
dia5 = input("Introduce el nombre del día 5: ")
dia6 = input("Introduce el nombre del día 6: ")
dia7 = input("Introduce el nombre del día 7: ")

# 2. Almacenar en tupla respetando el orden
dias = (dia1, dia2, dia3, dia4, dia5, dia6, dia7)
print("Tupla de días:", dias)

# 3. Solicitar número entre 1 y 7
numero = int(input("Introduce un número entre 1 y 7: "))

# 4. Mostrar el día correspondiente (índice = numero - 1)
print("El día correspondiente es:", dias[numero - 1])