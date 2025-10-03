#Crea un diccionario con la información de una persona

persona = {"nombre": "Ana", "edad": 25, "profesión": "Ingenieria"}
print("Diccionario Original:", persona)
persona["ciudad"] = "Medellín"
persona["edad"] = 26
del persona["profesión"]
print("Diccionario Actualizado:", persona)
