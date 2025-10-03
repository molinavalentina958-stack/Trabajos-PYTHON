1. #Crear una lista de números enteros desordenados

Fila = Horizontal
Columna = Vertical

#Solución

'''numeros = [34, 12, 5, 99, 67, 43, 21] #Esto es un array (Arreglo), [=Corchete
#Ordenar en orden ascendente (De menor a mayor)

for i in range(len(numeros)) #len = longitud del array
    for j in range(i + 1,len(numeros)) #Cicilo anidado
       if numeros [i]>numero[j]:
          numeros[i], numeros[j] = numeros[j], numeros[i] #Intercambiar posiciones
print("Orden ascendente:", numeros)'''

numero1= [34, 12, 5, 99, 67, 43, 21] 
numero2= [34, 12, 5, 99, 67, 43, 21] 
numeros.sort()# menor a mayor
numeros.sort(reverse=True)# mayor a menor
print(numero1)
print(numero2)
