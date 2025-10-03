import random
def saludar():
    nombre = input("🎮 Bienvenido jugador, ¿Cómo te llamas?: ").lower()
    print(f"🎮 ¡{nombre}, La máquina te reta a un juego de Piedra, Papel o Tijera!") 
    return nombre

def jugar_ronda(nombre, lista, frases_empate, frases_victoria, frases_derrota, resultados, historial):
    maquina = random.choice(lista)

    # El jugador elige
    jugador = None
    while jugador not in lista:
        jugador = input('Elige piedra, papel o tijera: ').lower()
        if jugador not in lista:
            print("Opción inválida. Ingresa solo: piedra, papel o tijera.")

    # Mostrar opciones
    print(f"\n{name_format(nombre)} eligió: {jugador}")
    print(f"La máquina eligió: {maquina}")

    # Las reglas del juego
    if jugador == maquina:
        print(random.choice(frases_empate))
        resultados["empates"] += 1
        ganador = "Empate"
    elif (
        (jugador == "piedra" and maquina == "tijera") or
        (jugador == "tijera" and maquina == "papel") or
        (jugador == "papel" and maquina == "piedra")
    ):
        print(random.choice(frases_victoria))
        resultados["victorias"] += 1
        ganador = nombre
    else:
        print(random.choice(frases_derrota))
        resultados["derrotas"] += 1
        ganador = "Máquina"

    # Guardar el historial
    historial.append((jugador, maquina, ganador))


def mostrar_resultados(resultados, historial):
    print("\n Historial de resultados:")
    print(f"Victorias: {resultados['victorias']}")
    print(f"Derrotas: {resultados['derrotas']}")
    print(f"Empates: {resultados['empates']}")
    print("\n Historial final de partidas (Jugador, Máquina, Ganador):")
    for partida in historial:
        print(partida)

def name_format(nombre):
    """Para que el nombre se vea con mayúscula inicial en mensajes."""
    return nombre.capitalize()

# ================= MAIN =================

def main():
    lista = ['piedra', 'papel', 'tijera']
    historial = []
    resultados = {"victorias": 0, "derrotas": 0, "empates": 0}

    nombre = saludar()

    frases_empate = [
        f"¡Empate! {nombre}, creo que estamos conectados por wifi",
        f"¡Empate! {nombre}, huy aquí hay telepatía",
        f"¡Empate! {nombre}, esto se está poniendo interesante"
    ]

    frases_victoria = [
        f"¡Increíble {nombre}, derrotaste a la máquina!",
        f"¡Eres muy pro {nombre}, has derrotado a la máquina!",
        f"{nombre}, estás imparable, la máquina no tuvo chance."
    ]

    frases_derrota = [
        f"¡Lo siento {nombre}, la máquina reina en este juego, perdiste!",
        f"¡Más suerte para la próxima {nombre}, gané esta vez!",
        f"¡Nadie supera a la máquina, {nombre}, perdiste!"
    ]

    seguir = True
    while seguir:
        jugar_ronda(nombre, lista, frases_empate, frases_victoria, frases_derrota, resultados, historial)

        while True:
            jugar_nuevamente = input("\n¿Quieres jugar otra ronda? (si/no): ").strip().lower()
            if jugar_nuevamente == "si":
                break  
            elif jugar_nuevamente == "no":
                seguir = False
                print("\n Gracias por jugar, ¡Hasta la próxima!")
                mostrar_resultados(resultados, historial)
                break
            else:
                print("Por favor responde exactamente 'si' o 'no'.")

# ================= EJECUCIÓN =================
if __name__ == "__main__":
    main()