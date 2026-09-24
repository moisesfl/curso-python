import random
from pprint import pprint

# Datos iniciales "sucios" (simulando entrada irregular de datos)
alumnos_raw = ["  ana gómez ", "LUIS PEReZ", "  maria LOPEZ  ", "   pedro RUIZ"]
notas_trimestres = [[random.randint(1, 10) for _ in range(3)] for _ in range(4)]
pprint(notas_trimestres, width=20)
asignaturas_raw = ["Python   ", " Python", "Bases de datos   ", "Python", " bases de Datos"]

# 1. LIST COMPREHENSION: Limpieza de cadenas (strip + title)
alumnos = [nombre.strip().title() for nombre in alumnos_raw]

# PASO 2. BUCLES ANIDADOS: Cálculo de la nota media a partir de los trimestres
notas_medias = []
for i in range(len(alumnos)):  # Bucle externo: recorre cada alumno
    suma = 0
    num_trimestres = len(notas_trimestres[i])
    
    for nota in notas_trimestres[i]:  # Bucle interno: recorre las notas del alumno
        suma += nota
        
    media = suma / num_trimestres
    notas_medias.append(round(media, 2))

# PASO 3. LIST COMPREHENSION CON IF-ELSE: Clasificación según la media calculada
estados = ["Apto" if media >= 5.0 else "No Apto" for media in notas_medias]


# PASO 4. DICT COMPREHENSION: Diccionario de aprobados usando las medias
aprobados_dict = {alumno: media for alumno, media in zip(alumnos, notas_medias) if media >= 5.0} 

# PASO 5. SET COMPREHENSION: Extracción de asignaturas únicas
asignaturas_unicas = {asig.strip().title() for asig in asignaturas_raw}

# PASO 6 Y 7. MENÚ INTERACTIVO (while True, break, continue) Y BÚSQUEDA (for + break)
while True:
    print("\n" + "="*50)
    print("   SISTEMA DE GESTIÓN Y ANÁLISIS DE CALIFICACIONES")
    print("="*50)
    print("1. Ver alumnos y sus notas medias (Bucles Anidados + List Comp)")
    print("2. Ver actas de estado [Apto/No Apto] (List Comp con if-else)")
    print("3. Ver diccionario de aprobados (Dict Comprehension)")
    print("4. Ver asignaturas únicas (Set Comprehension)")
    print("5. Buscar alumno en el registro (For + Break / Early Exit)")
    print("6. Salir")
    
    opcion = input("\nSeleccione una opción (1-6): ").strip()
    
    if opcion == "1":
        print("\n--- Expediente de Alumnos y Media Trimestral ---")
        for alumno, trimestres, media in zip(alumnos, notas_trimestres, notas_medias):
            print(f"• {alumno:<15} | Trimestres: {trimestres} -> Media: {media}")
            
    elif opcion == "2":
        print("\n--- Calificación Final ---")
        for alumno, media, estado in zip(alumnos, notas_medias, estados):
            print(f"• {alumno:<15} | Media: {media:<4} | Estado: {estado}")
            
    elif opcion == "3":
        print("\n--- Cuadro de Honor (Aprobados >= 5.0) ---")
        for alumno, media in aprobados_dict.items():
            print(f"• {alumno}: {media}")
            
    elif opcion == "4":
        print("\n--- Asignaturas Únicas ---")
        for asig in asignaturas_unicas:
            print(f"• {asig}")
            
    elif opcion == "5":
        busqueda = input("\nIngrese el nombre a buscar: ").strip().title()
        encontrado = False
        for i, alumno in enumerate(alumnos):
            if alumno == busqueda:
                print(f"¡Coincidencia encontrada! '{alumno}' está en la posición {i} con media de {notas_medias[i]}.")
                encontrado = True
                break  # Early exit: interrumpe la búsqueda
        if not encontrado:
            print(f"El alumno '{busqueda}' no se encuentra en la lista.")
            
    elif opcion == "6":
        print("\n¡Gracias por utilizar el sistema! Finalizando...")
        break  # Rompe el bucle while True
        
    else:
        print("Opción no válida. Intente de nuevo.")
        continue  # Vuelve al inicio del bucle