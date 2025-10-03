# Ejercicio 1: Sistema de Gestión de Inventarios
def agregar_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {'precio': precio, 'cantidad': cantidad}
    

def mostrar_inventario(inventario):
    print("\n--- INVENTARIO ---")
    for producto, datos in inventario.items():
        print(f"{producto}: ${datos['precio']} - {datos['cantidad']} unidades")

def buscar_producto(inventario, nombre):
    if nombre in inventario:
        return inventario[nombre]
    else:
        return None

def main():
    inventario = {}
    
    while True:
        print("\n1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(inventario, nombre, precio, cantidad)
                
            elif opcion == 2:
                mostrar_inventario(inventario)
                
            elif opcion == 3:
                nombre = input("Nombre del producto a buscar: ")
                producto = buscar_producto(inventario, nombre)
                if producto:
                    print(f"Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
                else:
                    print("Producto no encontrado")
                    
            elif opcion == 4:
                break
                
            else:
                print("Opción no válida")
                
        except ValueError:
            print("Error: Ingrese un valor numérico válido")
        except Exception as f:
            print(f"Error inesperado: {f}")

if __name__ == "__main__":
    main()
