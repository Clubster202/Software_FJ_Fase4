from demo import ejecutar_demo

def menu():
    while True:
        print("\\n===== SOFTWARE FJ =====")
        print("1. Ejecutar demostración de 12 operaciones")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            ejecutar_demo()
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    try:
        menu()
    except (KeyboardInterrupt, EOFError):
        print("\\nEjecución interrumpida por el usuario.")
    finally:
        print("Aplicación finalizada.")

