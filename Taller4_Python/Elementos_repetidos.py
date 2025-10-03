2. #Lista con elementos repetidos

#Solución

elementos = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unicos = [] #Esto es una lista vacía
for elemento in elementos:
    if elemento not in unicos: #not in = No está dentro de...
        unicos.append(elemento) #Agregar elementos en la lista llamada: unicos
print("Lista sin duplicados:", unicos)
