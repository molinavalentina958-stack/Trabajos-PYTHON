# Verificar si el nombre es "Bon Jovi Ernesto"
nombre = input("Ingrese el nombre")
limpio = " ".join(nombre.split()).strip().lower()
print("Sí es 'Bon jovi Ernesto'" if limpio == "bon jovi ernesto" else "No es 'Bon Jovi Ernesto'")
