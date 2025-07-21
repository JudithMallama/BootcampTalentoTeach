# Ejercicio 1: Comparar tres Números
# ==================================

while True:
    try:
        # Pedimos tres números al usuario
        x = int(input("Ingresa el primer número: "))
        y = int(input("Ingresa el segundo número: "))
        z = int(input("Ingresa el tercer número: "))

        # Comprobamos si los tres son iguales
        if x == y == z:
            print("Los tres números son iguales.")
        else:
            # Si no son iguales, encontramos el mayor y el menor
            mayor = max(x, y, z)
            menor = min(x, y, z)
            print(f"El mayor es: {mayor}")
            print(f"El menor es: {menor}")

        # Preguntamos si quiere repetir
        repetir = input("Repetir? (s/n): ")
        if repetir.lower() != 's':
            break

    except ValueError:
        # Si el usuario no ingresa un número válido
        print("Ingresa solo números enteros.")