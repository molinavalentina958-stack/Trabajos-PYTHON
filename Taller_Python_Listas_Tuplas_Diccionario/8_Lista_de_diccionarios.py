#Crea una lista llamada estudiantes que contenga 3 diccionarios

from statistics import mean
estudiantes = [
    {"nombre": "Melissa", "edad": 22, "nota": 3.5},
    {"nombre": "Juan", "edad": 25, "nota": 4.0},
    {"nombre": "Lorena", "edad": 20, "nota": 4.5},
]
print("Nombres:", [e["nombre"] for e in estudiantes])
print("Promedio de las notas:", round(mean([e["nota"] for e in estudiantes]), 2))
mejor = max(estudiantes, key=lambda e: e["nota"])
print("Mejor estudiante:", mejor["nombre"], "con la nota", mejor["nota"])
