#Crea una tupla con los nombres de 5 países

paises = ("Colombia", "Suiza", "Argentina", "Brasil", "México")
print("Tupla original: ", paises)
# paises[0] = "Perú"
print("\nLas tuplas no se pueden modificar")
paises_lista = list(paises)
print("\nConvertir a lista:", paises_lista)
paises_lista[0] = "Perú"
print("\nLista modificada:", paises_lista)
paises_modificados = tuple(paises_lista)
print("\nConvertir a tupla:", paises_modificados)
