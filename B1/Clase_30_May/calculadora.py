#Función menú: muestras las opciones del menú
def menu():
    while True:
        # Mostramos el menú con opciones
        print("\n-- Calculadora --")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. Divición")
        print("5. Salir")
        
        #Le pide al usuario las opciones de menú
        opcion= input ("Selecione una opción:")
        
        #Verifica la opción del usurio, mediante if aninados.
        if opcion =="1":
            add() 
        elif opcion =="2":
            subtract()
        elif opcion=="3":
            multiply()
        elif opcion =="4":
            divide()
        elif opcion == "5":
            print("¡Hasta luego!")
            break  # Terminamos el ciclo y salimos del programa
        else:
            print("Opción no válida. Intente de nuevo.")

   
def values():
    while True:
        try:
             #pedimos los número al usuario
            x=int(input("Ingrese el primer número: "))
            y=int(input("Ingrese el segundo número: "))
            #Retornas los valores de x y y, para que puedena ser usados en otras funciones
            return x,y
        #En caso que el valor no sea valido, le pide al usiario ingreasar los números nuevamente
        except ValueError:
            print ("El valor no es valido, por favor ingrese el valor de nuevo")
  

#Funcion sumar         
def add():
    print("*********SUMA*********")
    #Saca los valores del la función Values() para usarse en la suma
    x, y = values()
    #Realiza la suma
    result=x+y
    #Imprime el resultado
    print(f"la suma de {x} y {y} es: {result}" )
def subtract():
    print("*********RESTA********")
    #Saca los valores del la función Values() para usarse en la resta
    x, y = values()
    #Realiza la resta
    result=x-y
    print(f"la resta de {x} y {y} es: {result} " )

def multiply():
    print("*******MULTIPLICACIÓN******")
     #Saca los valores del la función Values() para usarse en la multiplicación
    x, y = values()
    #Realiza la multiplicacón
    result= x*y
    print(f"la multiplicación de {x} y {y} es: {result}" )

def divide():
    print("******DIVISIÓN*******")
    while True:
         #Saca los valores del la función Values() para usarse en la división
        x, y = values()
        #Si el dividendo es cero, el programa genera un error, por lo cual este if comprubea si este es diferente a cero
        if y!=0:
            #Si el 'y' o dividendo es diferente a cero se realiza la división
            result=x/y
            print(f"la divición de {x} y {y} es: {result}" )
            break
        #Si el 'y' es cero entonce el programa pide nuevamente los valores de 'x' y 'y'
        else:
            print("El dividendo no puede ser cero, ingresa los valores nuevamente")
                      
menu()
