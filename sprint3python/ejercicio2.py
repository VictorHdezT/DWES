import random

reglas = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["tijera", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["piedra", "tijera"]
}



opciones = list(reglas.keys())

def determinar_resultado(usuario, cpu):
    if usuario == cpu:
        return 0
    elif cpu in reglas[usuario]:
        return 1
    else:
        return -1

def jugar_partida():
    while True:
        try:
            n = int(input("¿Cuantas rondas desea jugar? (Número impar = o > de 1)."))
            if n >= 1 and n % 2 == 1:
                break
            else:
                print("Debe ser un número impar mayor o igual que 1. ")
        except ValueError:
            print("Por favor, introduzca un número válido. ")

    victorias_usuario = 0
    victorias_cpu = 0
    rondas_ganar = n % 2 + 1

    while victorias_usuario < rondas_ganar and victorias_cpu < rondas_ganar:
        usuario = input("Elige piedra, papel, tijera, lagarto o spock: ").lower()
        if usuario not in opciones:
            print("Por favor, elija una opción válida. Intentelo de nuevo")
            continue
        cpu = random.choice(opciones)
        print(f"La CPU escogió: {cpu}")

        resultado = determinar_resultado(usuario, cpu)
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print("¡Ganas la ronda!")
            victorias_usuario += 1
        else:
            print("Gana la CPU")
            victorias_cpu += 1

        print(f"Marcador -> Usuario: {victorias_usuario} | CPU: {victorias_cpu} | Rondas: {rondas_ganar}")

    if victorias_cpu < victorias_usuario:
        print("¡Felicidades, has ganado la partida!")
    else:
        print("La CPU ha ganado la partida")

    repetir = input("Quieres jugar otra vez? (s/n): ").lower()
    if repetir == "s":
        jugar_partida()

if __name__ == "__main__":
    jugar_partida()
