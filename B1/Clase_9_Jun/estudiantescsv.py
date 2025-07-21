import csv
import os

# Función para crear el archivo CSV si no existe
def crear_archivo_si_no_existe(nombre_archivo):
    # Verificamos si el archivo ya existe
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8-sig') as archivo:
            campos = ['nombre', 'edad', 'calificacion']  # Los encabezados del CSV
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()  # Escribimos los encabezados en el archivo
        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    else:
        print(f"El archivo '{nombre_archivo}' ya existe.")

# Función para leer los datos del archivo CSV
def leer_estudiantes(nombre_archivo):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)


        # Limpiar los encabezados (quitar espacios extra si los hay)
        lector.fieldnames = [campo.strip() for campo in lector.fieldnames]
        
        estudiantes = list(lector)
        
        # Verificamos los encabezados leídos
        if estudiantes:
            print(f"Encabezados del archivo: {', '.join(estudiantes[0].keys())}")
        
        # Imprimimos los estudiantes
        for est in estudiantes:
            print(f"nombre:{est['nombre']} - Edad: {est['edad']} - Calificación: {est['calificacion']}")
        
        return estudiantes

# Función para agregar un nuevo estudiante al archivo CSVimport csv
import os

def agregar_estudiante(nombre_archivo):
    # Pedimos al usuario los datos
    nombre = input("Nombre del estudiante: ").strip()
    edad = input("Edad del estudiante: ").strip()
    calificacion = input("Calificación del estudiante: ").strip()

    # Validamos que la edad y calificación sean números
    if not edad.isdigit() or not calificacion.isdigit():
        print("Error: La edad y la calificación deben ser números.")
        return
    
    # Convertimos los valores a enteros
    edad = int(edad)
    calificacion = int(calificacion)

    campos = ['nombre', 'edad', 'calificacion']
    
    # Si el archivo no existe, lo creamos con los encabezados
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
    
    # Abrimos el archivo en modo agregar
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writerow({'nombre': nombre, 'edad': edad, 'calificacion': calificacion})  # Escribimos la nueva línea

    print(f"Estudiante {nombre} agregado correctamente.")


# Función para calcular el promedio de las calificaciones
def calcular_promedio(estudiantes):
    # Convertimos las calificaciones a enteros
    calificaciones = [int(e['calificacion']) for e in estudiantes]
    promedio = sum(calificaciones) / len(calificaciones)  # Calculamos el promedio
    print(f"Promedio de calificaciones: {promedio:.2f}")

# Programa principal
archivo_csv = 'estudiantes.csv'  # Ruta del archivo CSV

# Crear el archivo si no existe
crear_archivo_si_no_existe(archivo_csv)

# Mostrar la lista de estudiantes
print("\n--- Lista de estudiantes ---")
estudiantes = leer_estudiantes(archivo_csv)

# Agregar un nuevo estudiante
print("\n--- Agregar nuevo estudiante ---")
agregar_estudiante(archivo_csv)

# Mostrar la nueva lista de estudiantes
print("\n--- Nueva lista de estudiantes ---")
estudiantes = leer_estudiantes(archivo_csv)

# Calcular y mostrar el promedio de las calificaciones
print("\n--- Cálculo de promedio ---")
calcular_promedio(estudiantes)
