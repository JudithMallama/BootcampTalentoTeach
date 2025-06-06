#Recorrer una liata de palabras hasta encontrar la palabra "salir"
palabras= ["Hola", "mundo", "python", "continuar", "salir", "fin"]

for palabra in palabras:
    if palabra == "continuar":
        print("Se encontro 'continuar', se salta esta palabra.")
        continue #Salta la palabra "Continuar"
    elif palabra == "salir":
        print("Encontro la palabra 'Salir', temina el ciclo")
        break
    print(f"Palabra actual: {palabra}")