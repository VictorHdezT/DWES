def gestor_lista():
    lista_compra = []

    while True:
        print("---LISTA DE LA COMPRA---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Ver lista de productos")
        print("4. Vaciar lista")
        print("5. Salir")

        opcion = input("Elije una opcion: ")

        if opcion == "1":
            producto = input("Escriba una producto: ").lower().strip()
            if producto in lista_compra:
                print("El producto se encuentra en la lista")
            else:
                lista_compra.append(producto)
                print(f"{producto} se ha añadido a la lista. ")
        elif opcion == "2":
            producto = input("Escriba una producto: ").lower().strip()
            if producto in lista_compra:
                lista_compra.remove(producto)
                print(f"{producto} se ha eliminado a la lista. ")
            else:
                print("El producto no se encuentra en la lista. ")
        elif opcion == "3":
            if lista_compra:
                for p in sorted(lista_compra):
                    print(f"- {p}")
            else:
                print("No hay ninguna lista disponible")
        elif opcion == "4":
            decision = input("¿Estás seguro de que quieres eliminar esta lista? (s/n)").lower()
            if decision == "s":
                lista_compra.clear()
                print("Se ha eliminado la lista. ")
            elif decision == "n":
                print("Uf! Menos mal...")
            else:
                print("Introduzca una letra válida")

        elif opcion == "5":
            print("Chao!")
            break

if __name__ == "__main__":
    gestor_lista()









