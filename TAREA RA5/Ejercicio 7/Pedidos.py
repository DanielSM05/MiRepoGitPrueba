# 1. Crear la lista de pedidos
pedidos = [
    {"codigo": "A1", "producto": "SSD", "unidades": 2, "precio": 58},
    {"codigo": "A2", "producto": "RAM", "unidades": 3, "precio": 32},
    {"codigo": "A3", "producto": "SSD", "unidades": 1, "precio": 58}
]

# 2. Mostrar lista completa
print("Lista de pedidos:", pedidos)

# 3. Producto del primer pedido
print("Producto del primer pedido:", pedidos[0]["producto"])

# 4. Unidades del segundo pedido
print("Unidades del segundo pedido:", pedidos[1]["unidades"])

# 5. Modificar unidades del tercer pedido a 5
pedidos[2]["unidades"] = 5
print("Tercer pedido actualizado:", pedidos[2])

# 6. Añadir nuevo pedido A4
nuevo_pedido = {"codigo": "A4", "producto": "Teclado", "unidades": 4, "precio": 25}
pedidos.append(nuevo_pedido)

# 7. Eliminar el segundo pedido
pedidos.pop(1)

# 8. Mostrar lista actualizada
print("Lista de pedidos actualizada:", pedidos)

# 9. Número total de pedidos
print("Número total de pedidos:", len(pedidos))