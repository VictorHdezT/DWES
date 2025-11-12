class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False

    def mostrar_info(self):
        estado = " Completada" if self.completada else " Pendiente"
        return f"{self.titulo} - {estado}"

    def marcar_completada(self):
        self.completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.titulo = nuevo_titulo
        self.descripcion = nueva_descripcion


def main():
    tareas = []

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Crear tarea")
        print("2. Mostrar todas")
        print("3. Marcar como completada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            tareas.append(Tarea(titulo, descripcion))
            print("Tarea creada correctamente.")

        elif opcion == "2":
            if tareas:
                for t in tareas:
                    print(t.mostrar_info())
            else:
                print("No hay tareas registradas.")

        elif opcion == "3":
            titulo = input("Título de la tarea a completar: ").lower()
            for t in tareas:
                if t.titulo.lower() == titulo:
                    t.marcar_completada()
                    print("Tarea completada.")
                    break
            else:
                print("Tarea no encontrada.")

        elif opcion == "4":
            titulo = input("Título de la tarea a editar: ").lower()
            for t in tareas:
                if t.titulo.lower() == titulo:
                    nuevo_titulo = input("Nuevo título: ")
                    nueva_descripcion = input("Nueva descripción: ")
                    t.editar(nuevo_titulo, nueva_descripcion)
                    print("Tarea actualizada.")
                    break
            else:
                print("Tarea no encontrada.")

        elif opcion == "5":
            titulo = input("Título de la tarea a eliminar: ").lower()
            for t in tareas:
                if t.titulo.lower() == titulo:
                    tareas.remove(t)
                    print("Tarea eliminada.")
                    break
            else:
                print("Tarea no encontrada.")

        elif opcion == "6":
            print("Saliendo del gestor de tareas. ")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
