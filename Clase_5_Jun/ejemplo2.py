#Escribe un programa que imprima  todos los números de 1 al 10, e
#Excepto el número 4 y el número 7. 
#usa continue para omitir esos números

for number in range (1,10):
    if(number==4 or number==7):
        print(f"Se salto el número {number}")
        continue
    print(f"Número actual: {number}")
    