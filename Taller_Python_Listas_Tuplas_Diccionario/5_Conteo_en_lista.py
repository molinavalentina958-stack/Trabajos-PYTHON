#Crea una lista 

from collections import Counter
lista = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6]
conteo = Counter(lista)
print("Conteo de la lista:")
for numero, cantidad in conteo.items():
    print(f"El número {numero} aparece {cantidad} veces")
