# Bono por estrato y total a pagar
salario = float(input("Ingrese el salario: "))
estrato = int(input("Ingrese el estrato (1-6) :"))
if salario < 0:
    print("Error: el salario no puede ser negativo.")
else: 
    tabla = {1: 0.35, 2: 0.30, 3: 0.25, 4: 0.20, 5: 0.10, 6: 0.10}
    tasa = tabla.get(estrato, 0.0)
    bono = salario * tasa 
    total = salario + bono
    print(f"Bono = {bono}, Total a pagar = {total}")
    