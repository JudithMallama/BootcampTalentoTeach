#Se define una función llamada comparar_numeros que no recibe parámetros.
def comparar_numeros():
    #Se solicita al usuario que ingrese el primer número. 
    #El input() devuelve un string, y int() lo convierte a un número entero, que se guarda en la variable x.
    x = int(input("Digite el número 1: "))
    #Se repite el proceso anterior, pero para el segundo número, almacenándolo en la variable y.
    y = int(input("Digite el número 2: "))

    #Se evalúa si el primer número (x) es mayor que el segundo (y).
    if x > y:
        #Si x es mayor, se imprime un mensaje diciendo que x es mayor que y, usando el método format() para insertar los valores en la cadena.
        print("{} es mayor que {}".format(x, y))
    #Si x no es mayor que y, se evalúa si x es menor que y.
    elif x < y:
        #Si x es menor que y, se imprime un mensaje indicando que y es mayor que x.
        print("{} es mayor que {}".format(y, x))
    #Si ninguna de las condiciones anteriores se cumple, significa que x es igual a y.
    else:
    #Se imprime un mensaje indicando que ambos números son iguales, mostrando uno de ellos.
        print("Ambos números son iguales: {}".format(x))

#Se define una función llamada menu, que será el menú principal del programa.
def menu():
    #Se inicia un bucle while infinito, que continuará ejecutándose hasta que el usuario elija salir.
    while True:
        #Imprime el encabezado del menú.
        print("\n--- Menú ---")
        #Opción 1 del menú: comparar dos números.
        print("1. Comparar dos números")
        #Opción 2 del menú: salir del programa.
        print("2. Salir")
        #Se pide al usuario que seleccione una opción y se guarda en la variable opcion.
        opcion = input("Seleccione una opción (1 o 2): ")
        #Si el usuario elige la opción "1", se ejecuta la función comparar_numeros.
        if opcion == "1":
            comparar_numeros()
        #Si el usuario elige "2", se prepara para salir del programa.
        elif opcion == "2":
            print("¡Hasta luego!")
            #Sale del bucle while, terminando la ejecución del menú.
            break
        else:
            #Si el usuario introduce cualquier otra opción que no sea "1" o "2"... y si hay un erro en el codigo se repite el menu
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú principal
menu()