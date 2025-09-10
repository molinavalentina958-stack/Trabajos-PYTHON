# Determinar si el salario es integral (>= 13 * SMMLV)
salario = float(input("Ingrese el salario: "))
smmlv = float(input("Ingrese el SMMLV vigente: "))
if salario < 0 or smmlv <= 0:
    print("Valores inva¡lidos.")
else: 
    print("Salario integral" if salario >= 13 * smmlv else "Salario NO integral")
        