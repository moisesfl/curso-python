# Reto Integrador: Sistema de Gestión y Análisis de Calificaciones

## Descripción del Ejercicio
En este ejercicio práctico construirás una aplicación de consola interactiva en Python para procesar, limpiar y analizar el expediente académico de una clase.

Partiendo de una serie de datos iniciales en bruto, aplicarás estructuras de control iterativas (`for`, `while`), control de flujo (`break`, `continue`), bucles anidados para estructuras bidimensionales y las diferentes formas de comprensiones de colecciones (`list`, `set` y `dict comprehensions`).

---

## Datos Iniciales
Copia las siguientes estructuras de datos al inicio de tu programa:

```python
# Nombres con espacios de más y formatos irregulares
alumnos_raw = ["  ana gomez ", "LUIS PEREZ", "  maria LOPEZ  ", "   pedro RUIZ"]

# Matriz de notas: Cada sublista contiene las notas de los 3 trimestres de cada alumno
notas_trimestres = [
    [8.0, 9.0, 8.5],  # Notas de Ana
    [4.0, 5.0, 3.0],  # Notas de Luis
    [9.0, 10.0, 9.5], # Notas de María
    [3.0, 4.0, 3.5]   # Notas de Pedro
]

# Registro de asignaturas impartidas con duplicados y espacios
asignaturas_raw = ["  Python", "Python", "bases de Datos", "python", "Bases de Datos  "]
```

---

## Requisitos y Pasos a Implementar

### 1. Limpieza de Nombres (`List Comprehension`)
Genera una nueva lista llamada `alumnos` a partir de `alumnos_raw` utilizando una **list comprehension**. Debes eliminar los espacios en blanco sobrantes en los extremos (`.strip()`) y dar formato de título a cada nombre (`.title()`).

### 2. Cálculo de Medias Trimestrales (`Bucles Anidados`)
Procesa la matriz `notas_trimestres` utilizando dos bucles `for` anidados:
- **Bucle externo**: Recorre cada alumno.
- **Bucle interno**: Suma las notas de los tres trimestres del alumno actual.

Al finalizar el bucle interno, calcula la nota media de cada alumno, redondéala a 2 decimales y guárdala en una lista llamada `notas_medias`.

### 3. Clasificación Condicional (`List Comprehension` con `if-else`)
Crea una lista llamada `estados` usando **list comprehension** con una condición doble previa al `for`. Asigna la cadena `"Apto"` si la nota media del alumno es igual o superior a `5.0`, o `"No Apto"` en caso contrario.

### 4. Filtrado de Aprobados (`Dict Comprehension`)
Crea un diccionario denominado `aprobados_dict` utilizando **dict comprehension**. Asocia cada nombre de alumno con su nota media, incluyendo únicamente a aquellos alumnos con una media mayor o igual a `5.0`.

### 5. Catálogo de Asignaturas Únicas (`Set Comprehension`)
Obtén un conjunto llamado `asignaturas_unicas` usando **set comprehension** sobre `asignaturas_raw`, eliminando espacios y duplicados.

### 6. Búsqueda Secuencial de Alumnos (`for` + `break` / *Early Exit*)
Implementa un algoritmo de búsqueda que pida un nombre por teclado, lo busque en la lista `alumnos` e imprima la posición e información del alumno. Utiliza `break` para interrumpir el bucle inmediatamente al encontrar la primera coincidencia (*salida anticipada*).

### 7. Menú de Consola Interactivo (`while True`, `break`, `continue`)
Envuelve todas las funcionalidades anteriores en un bucle interactivo `while True` que muestre un menú con las siguientes opciones:
1. Ver alumnos y sus notas medias.
2. Ver actas de estado (`Apto`/`No Apto`).
3. Ver diccionario de aprobados.
4. Ver asignaturas únicas.
5. Buscar alumno por nombre.
6. Salir (utiliza `break` para finalizar la ejecución).

Si el usuario introduce una opción no válida, utiliza `continue` para reiniciar el bucle y solicitar la opción nuevamente.
