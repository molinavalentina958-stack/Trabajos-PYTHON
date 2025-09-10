#Crea un diccionario con 5 productos como claves y sus precios como valores

productos = {
    "Manzana": 2000,
    "Arroz": 2200,
    "Huevos": 8000,
    "Leche": 3500,
    "Aceite": 6500,
}
print("Productos:", productos)
caro = max(productos, key=productos.get)
print("El producto más caro es:", caro, "con un precio de:", productos[caro])
barato = min(productos, key=productos.get)
print("El producto más barato es:", barato, "con un precio de:", productos[barato])
promedio = sum(productos.values()) / len(productos)
print("El precio promedio de los productos es:", round(promedio, 2))
