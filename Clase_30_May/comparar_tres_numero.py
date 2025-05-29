# =======================================
#Ejercicico 1: Comprar tres números"
# =======================================

def comparar_numeros():
    while True:
        try:
            #pedimos los número al usuario
            x=int(input("Ingrese el primer número"))
            y=int(input("Ingrese el segundo número"))
            z=int(input("Ingrese el tercero número"))
       
       
            #Comprobamos si los tres son iguales
            if x==y   and x==z:
                print("los tres números son iguales")
            else:
            #Si no son iguales, buscamos cuál es el mayor y cuál es el menor
       
            #Si x es e mayor o ifuala los otros dos
                if x >=y and x>=z:
                    print(f"El mayor es {x}")
                    #ahora comparamos y y z para saber cúall es el menor
                    if y > z:
                        print(f"El menor es {y}")
                    else:
                        print(f"El menor es {y}")
            
                #Si y es el mayor o igual a los otros dos
                elif y>x and y >=z:
                    print(f"El mayor es {y}")
                    #Comparamos x y z para encontrar el menor
                    if x >=z:
                        print(f"El menor es {z}")
                    else:
                        print(f"El menor es {x}")
                    
                #Si z es el mayor
                elif z>=x and z>=y:
                    print(f"El menor es {x}")
                    #Comparamos x y y para determnar el menor
                    if x>= y:
                        print(f"El menor es {y}")
                    else:
                        print(f"El menor {x}")
            break # Salimos del ciclo si no hay error
    
        except ValueError:
         #Si el usuario ingresa algo que no es númro entero
            print("Entrada inválida. Por favor , ingrese solo número enteros.")
            
# Función principal que muestra el menú
def menu():
    while True:
        # Mostramos el menú con opciones
        print("\n-- Menú --")
        print("1. Comparar tres números")
        print("2. Salir")

        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == "1":
            comparar_numeros()  # Llamamos a la función que compara los números
        elif opcion == "2":
            print("¡Hasta luego!")
            break  # Terminamos el ciclo y salimos del programa
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamamos a la función principal para iniciar el programa
menu()
        
    
