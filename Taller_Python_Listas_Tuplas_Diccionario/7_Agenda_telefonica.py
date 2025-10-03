#Crea un diccionario donde las llaves sean nombres de personas y los valores sean sus números de teléfono

agenda = {"Valentina": "3136059771", "Santiago": "3212345678", "Andrea": "3211248404"}
print("Agenda original:", agenda)
print("Número de Valentina:", agenda.get("Valentina"))
agenda["Santiago"] = "3104884587"
print("Número actualizado de Santiago:", agenda.get("Santiago"))
agenda.pop("Andrea")
print("Agenda actualizada:", agenda)
