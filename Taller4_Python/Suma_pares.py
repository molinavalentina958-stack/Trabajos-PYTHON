3. #Crea una lista de números enteros

#Solución 

numeros = [10, 15, 22, 33, 42, 55, 60]
#El primer num: es para almacenar los pares 
suma_pares = sum(num for num in numeros if num % 2 == 0) 
print("Suma de números pares:", suma_pares)
