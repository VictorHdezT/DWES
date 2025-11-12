def cajero():
    cuenta = {"nombre": "Víctor", "saldo": 1200.0}

    while True:
        print(f"Bienvenid@, {cuenta['nombre']}")
        print("1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Elije una opcion: ")

        if opcion == "1":
            print(f"Saldo actual: {cuenta['saldo']} €")
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese la cantidad de dinero a ingresar: "))
                if cantidad > 0:
                    cuenta["saldo"] += cantidad
                    print(f"Has ingresado {cantidad} €. El nuevo saldo es {cuenta['saldo']} €.")
                else:
                    print("Introduzca una cantidad positiva.")
            except ValueError:
                print("Error, cantidad no válida.")

        elif opcion == "3":
            try:
                cantidad = float(input("Ingrese la cantidad de dinero a retirar: "))
                if cantidad > 0:
                    cuenta["saldo"] -= cantidad
                    print(f"Has retirado {cantidad} €. El nuevo saldo es {cuenta['saldo']} €.")
                else:
                    print("Introduzca una cantidad positiva.")
            except ValueError:
                print("Error, cantidad no válida.")

        elif opcion == "4":
            print("Gracias por usar nuestros servicios. No se olvide de recoger la tarjeta!")
            break

        else:
            print("Introduzca una opcion valida.")

if __name__ == "__main__":
    cajero()
