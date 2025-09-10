# Saludo según sexo
sexo = input("Ingrese el sexo (M/F/Otro) : ").strip().lower()
nombre = input("Ingrese el nombre (opcional) : ").strip()
if sexo in ("m", "masculino", "h", "hombre") :
    print(f"Hola, señor {nombre or 'Usuario'}.")
elif sexo in ("f", "femenino", "mujer") :
    print(f"Hola, señora {nombre or 'Usuario'}.")
else: 
    print(f"Hola, {nombre or 'Usuario'}.")
        