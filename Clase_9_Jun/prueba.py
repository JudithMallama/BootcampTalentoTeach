import csv
def leer_estudiantes(nombre_archivo):
    estudiantes = []  # Lista para almacenar los estudiantes
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)
        
        # Imprimimos los encabezados para verificar que son correctos
        print("Encabezados:", lector.fieldnames)
        
        estudiantes = list(lector)  # Convertimos los datos a una lista de diccionarios
        
        # Imprimimos cada estudiante de la lista
        for est in estudiantes:
            print(f"nombre: {est['nombre']} - Edad: {est['edad']} - Calificación: {est['calificaciones']}")
        
    return estudiantes


archivo_csv= 'estudiantes.csv' 
leer_estudiantes(archivo_csv)

