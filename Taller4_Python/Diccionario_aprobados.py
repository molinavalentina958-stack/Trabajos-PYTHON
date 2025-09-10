8. #Diccionario de estudiantes y notas

#Solución

estudiantes = {"Ana":85, "Luis":58, "Pedro":70, "Sofia":45, "María":90}
aprobados = {nombre: nota for nombre, nota in estudiantes.items() if nota >=60}
print("Estudiantes aprobados:", aprobados)
