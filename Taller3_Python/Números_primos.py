#Números primos en un rango
limite = int(input("Ingrese el limite: "))
print(f"Números primos entre 1 y {limite}:")

for numero in range(2, limite + 1):
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)
        