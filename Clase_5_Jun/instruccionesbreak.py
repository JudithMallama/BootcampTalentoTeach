#Queremos detener el ciclo cuando encontramos el numero 5
for numero in range(1,11):
    if numero == 5:
        print(f"¡Encontrando el número {numero}! se detiene le ciclo.")
        break #Rompe el ciclo
    print(f"Número actual: {numero}")