#Crea una lista de litas (Matriz) de 3x3 con números enteros

matriz = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]
print("Matriz:")
for fila in matriz:
    print(fila)

print("Diagonal principal:", [matriz[i][i] for i in range(len(matriz))])
print("Diagonal secundaria:", [matriz[i][len(matriz)-1-i] for i in range(len(matriz))])
