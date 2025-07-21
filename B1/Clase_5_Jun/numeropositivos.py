#crear un programa que pida números al usuario de un en uno.
#el programa pides números mietras sena positivos
#Si el ususario ingresa un numero negativo
#El programa mostrara un mesaje que diga "Número negativo destectado. Fin del programa "

while True:
    number= int(input("Ingrese un número: "))
    if number <0:
        print(f"Numero negativo detectado: {number}")
        break