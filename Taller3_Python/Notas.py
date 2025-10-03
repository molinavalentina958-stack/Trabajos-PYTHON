#Clasificación de notas
aprobadas = 0
reprobadas = 0

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    if nota >= 6:
        aprobadas += 1
    else:
        reprobadas += 1

print(f"Aprobadas: {aprobadas}")
print(f"Reprobadas: {reprobadas}")
