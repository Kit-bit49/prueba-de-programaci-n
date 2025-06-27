compradores = {}
stock = {1: 50, 2: 60}

def comprar_entrada():
    print(" Comprar Entrada ")
    nombre = input("Nombre del comprador: ").strip()

    if nombre in compradores:
        print("Error: El nombre ya esta registrado.")
        return

    print("Seleccione una función:")
    print("1. Movimiento Origen con los Tripulantes Shamanes (50 entradas)")
    print("2. Movimiento Origen con Sonrisa MC (60 entradas)")

    funcion_input = input("Función (1 o 2): ").strip()

    if not funcion_input.isdigit():
        print("Error: función inválida.")
        return

    funcion = int(funcion_input)
    if funcion not in [1, 2]:
        print("Error: función inválida.")
        return

    if stock[funcion] > 0:
        compradores[nombre] = funcion
        stock[funcion] -= 1
        print(f"Entrada registrada en función {funcion}! Stock restantes:")
        print(f"  Función 1: {stock[1]}")
        print(f"  Función 2: {stock[2]}")
    else:
        print("Error: No hay entradas disponibles para la función elegida.")

def cambiar_show():
    print(" Cambiar Show ")
    nombre = input("Nombre del comprador: ").strip()

    if nombre not in compradores:
        print("Error: comprador no registrado.")
        return

    funcion_actual = compradores[nombre]
    nueva_funcion = 1 if funcion_actual == 2 else 2

    respuesta = input(f"Cambiar de función {funcion_actual} a {nueva_funcion}? (S/N): ").strip().lower()
    if respuesta != "s":
        print("Se ha cancelado el cambio.")
        return

    if stock[nueva_funcion] > 0:
        stock[funcion_actual] += 1
        stock[nueva_funcion] -= 1
        compradores[nombre] = nueva_funcion
        print(f"Cambio exitoso. Su funcion ahora es {nueva_funcion}.")
    else:
        print("Error: no hay stock en la función elegida.")

def mostrar_stock():
    print(" Totales de Entradas ")
    vendidas_f1 = 50 - stock[1]
    vendidas_f2 = 60 - stock[2]
    print(f"Función 1: Disponibles {stock[1]}, Vendidas {vendidas_f1}")
    print(f"Función 2: Disponibles {stock[2]}, Vendidas {vendidas_f2}")

def main():
    while True:
        print("MENU PRINCIPAL CONCIERTO MOVIMIENTO ORIGEN")
        print("1.- Comprar entrada.")
        print("2.- Cambiar show.")
        print("3.- Stock de entradas.")
        print("4.- Salir.")
        opcion = input("Seleccione una opción: ").strip()

        if not opcion.isdigit():
            print("Debe ingresar una opción válida")
            continue

        opcion = int(opcion)
        if opcion == 1:
            comprar_entrada()
        elif opcion == 2:
            cambiar_show()
        elif opcion == 3:
            mostrar_stock()
        elif opcion == 4:
            print("Programa terminado")
            break
        else:
            print("Debe ingresar una opción válida")

if __name__ == "__main__":
    main()
