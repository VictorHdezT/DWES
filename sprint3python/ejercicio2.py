
import random

opciones = ["piedra","papel","tijera","lagarto","spock"]

reglas = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijera", "piedra"]
}

numero_rondas = input("Introduce un numero de rondas: ")

def partidas_gp(jugador, maquina):
    if jugador == maquina:
        return  0
    elif maquina in reglas[jugador]:
        return 1
    else:
        return -1

jugar = ("s")

while jugar == "s":
    jugador = input("Elige entre: piedra, papel, piedra, lagarto o spock: ").lower()

    while jugador not in opciones:
        input("Apuesta no válida, elija otra jugada:").lower()

    maquina = random.choice(opciones)
    print(f"La maquina eligió: {maquina}")

    if jugador == maquina:
            print("Empate!")
    elif maquina in reglas[jugador]:
            print("Has ganado! Felicidades.")
    else:
        print("Has perdido... Que pena.")

    jugar = input("Echamos otra? (s/n): ").lower()