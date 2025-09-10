# Capturar tres números y determinar menor, medio y mayor 
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
nums = sorted ( [a, b, c] )
print(f"Menor = {nums [0]}, Medio = {nums[1]}, Mayor = {nums[2]}")
