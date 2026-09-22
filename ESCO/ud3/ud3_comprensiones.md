# UD03\_2-Comprensiones

<div id="top"></div>

## Índice de contenidos

- [UD03\_2-Comprensiones](#ud03_2-comprensiones)
  - [Índice de contenidos](#índice-de-contenidos)
- [Unidad 3 – Comprehensions en Python](#unidad-3--comprehensions-en-python)
  - [1. Concepto de comprehension](#1-concepto-de-comprehension)
  - [2. List Comprehensions](#2-list-comprehensions)
    - [2.1 Sintaxis general](#21-sintaxis-general)
    - [2.2 List comprehension con condición](#22-list-comprehension-con-condición)
    - [2.3 Transformación de datos con list comprehensions](#23-transformación-de-datos-con-list-comprehensions)
  - [3. Comprehensions con estructuras condicionales](#3-comprehensions-con-estructuras-condicionales)
    - [3.1 Condición simple (`if` al final)](#31-condición-simple-if-al-final)
    - [3.2 Condición doble (`if – else` dentro de la expresión)](#32-condición-doble-if--else-dentro-de-la-expresión)
  - [4. Set Comprehensions](#4-set-comprehensions)
    - [4.1 Sintaxis](#41-sintaxis)
  - [5. Dict Comprehensions](#5-dict-comprehensions)
    - [5.1 Sintaxis](#51-sintaxis)
    - [5.2 Dict comprehension con condición](#52-dict-comprehension-con-condición)
  - [6. Generator Comprehensions](#6-generator-comprehensions)
    - [6.1 Sintaxis](#61-sintaxis)
  - [7. Comprehensions con funciones existentes](#7-comprehensions-con-funciones-existentes)
  - [8. Cuándo usar comprehensions y cuándo no](#8-cuándo-usar-comprehensions-y-cuándo-no)
    - [Ventajas🔗](#ventajas)
    - [No recomendable cuando:](#no-recomendable-cuando)
  - [9. Buenas prácticas](#9-buenas-prácticas)
  - [10. Comparación: bucle tradicional vs comprehension](#10-comparación-bucle-tradicional-vs-comprehension)

# Unidad 3 – Comprehensions en Python[](#unidad-3-comprehensions-en-python "Permanent link")

Las **comprehensions** (comprensiones) son una característica avanzada del lenguaje Python que permiten **crear nuevas colecciones de datos de forma concisa, legible y eficiente**, a partir de otras colecciones existentes. Su uso está estrechamente relacionado con la programación funcional y con el tratamiento de estructuras iterables.

Python dispone de cuatro tipos principales de comprehensions:

*   List comprehensions
*   Set comprehensions
*   Dict comprehensions
*   Generator comprehensions

En este tema se estudian en profundidad, con ejemplos claros y progresivos.

- - -

## 1\. Concepto de comprehension[](#1-concepto-de-comprehension "Permanent link")

Una comprehension es una **forma compacta de escribir bucles y condiciones** para construir colecciones como listas, conjuntos o diccionarios en **una sola expresión**.

Desde un punto de vista conceptual, una comprehension:

*   Itera sobre una secuencia (lista, tupla, rango, etc.).
*   Aplica opcionalmente una condición.
*   Genera un nuevo conjunto de datos.

Su objetivo principal es:

*   Reducir código repetitivo.
*   Mejorar la legibilidad cuando la lógica es sencilla.
*   Facilitar operaciones de filtrado y transformación de datos.

- - -

## 2\. List Comprehensions[](#2-list-comprehensions "Permanent link")

### 2.1 Sintaxis general[](#21-sintaxis-general "Permanent link")

```
[expresion for elemento in iterable]
```

Ejemplo equivalente sin comprehension:

```
cuadrados = []
for i in range(5):
    cuadrados.append(i * i)
```

Con list comprehension:

```
cuadrados = [i * i for i in range(5)]
```

- - -

### 2.2 List comprehension con condición[](#22-list-comprehension-con-condicion "Permanent link")

Se puede añadir una condición para filtrar los elementos.

```
pares = [i for i in range(10) if i % 2 == 0]
```

Equivalente tradicional:

```
pares = []
for i in range(10):
    if i % 2 == 0:
        pares.append(i)
```

- - -

### 2.3 Transformación de datos con list comprehensions[](#23-transformacion-de-datos-con-list-comprehensions "Permanent link")

```
nombres = ["ana", "luis", "maria"]
nombres_mayus = [nombre.upper() for nombre in nombres]
```

Uso típico:

*   Conversión de tipos
*   Normalización de datos
*   Procesamiento previo de listas

- - -

## 3\. Comprehensions con estructuras condicionales[](#3-comprehensions-con-estructuras-condicionales "Permanent link")

### 3.1 Condición simple (`if` al final)[](#31-condicion-simple-if-al-final "Permanent link")

```
mayores = [n for n in edades if n >= 18]
```

### 3.2 Condición doble (`if – else` dentro de la expresión)[](#32-condicion-doble-if-else-dentro-de-la-expresion "Permanent link")

```
resultado = ["apto" if nota >= 5 else "no apto" for nota in notas]
```

Observación importante:

*   El `if-else` va **antes del `for`** cuando forma parte de la expresión.
*   El `if` filtrado va **después del `for`**.

- - -

## 4\. Set Comprehensions[](#4-set-comprehensions "Permanent link")

Las **set comprehensions** crean conjuntos (`set`), eliminando automáticamente duplicados.

### 4.1 Sintaxis[](#41-sintaxis "Permanent link")

```
{expresion for elemento in iterable}
```

Ejemplo:

```
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = {n for n in numeros}
```

Resultado:

```
{1, 2, 3, 4, 5}
```

Uso típico:

*   Eliminación de duplicados
*   Obtención de valores únicos
*   Operaciones de conjuntos

- - -

## 5\. Dict Comprehensions[](#5-dict-comprehensions "Permanent link")

Las **dict comprehensions** permiten crear diccionarios de forma compacta.

### 5.1 Sintaxis[](#51-sintaxis "Permanent link")

```
{clave: valor for elemento in iterable}
```

Ejemplo:

```
numeros = [1, 2, 3, 4]
cuadrados = {n: n * n for n in numeros}
```

Resultado:

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

- - -

### 5.2 Dict comprehension con condición[](#52-dict-comprehension-con-condicion "Permanent link")

```
aprobados = {alumno: nota for alumno, nota in notas.items() if nota >= 5}
```

Uso habitual:

*   Filtrar diccionarios
*   Transformar claves o valores
*   Crear estructuras de acceso rápido

- - -

## 6\. Generator Comprehensions[](#6-generator-comprehensions "Permanent link")

Las **generator comprehensions** son similares a las list comprehensions, pero **no generan la colección completa**, sino que producen los valores bajo demanda.

### 6.1 Sintaxis[](#61-sintaxis "Permanent link")

```
(expresion for elemento in iterable)
```

Ejemplo:

```
generador = (i * i for i in range(5))
```

Uso:

```
for valor in generador:
    print(valor)
```

Características:

*   Menor consumo de memoria.
*   Ideales para grandes volúmenes de datos.
*   Se recorren una sola vez.

- - -

## 7\. Comprehensions con funciones existentes[](#7-comprehensions-con-funciones-existentes "Permanent link")

Las comprehensions se integran perfectamente con funciones y estructuras ya conocidas.

```
valores = ["10", "20", "30"]
enteros = [int(v) for v in valores]
```

```
longitudes = [len(palabra) for palabra in palabras]
```

- - -

## 8\. Cuándo usar comprehensions y cuándo no[](#8-cuando-usar-comprehensions-y-cuando-no "Permanent link")

### Ventajas[](#ventajas "Permanent link")

*   Código más compacto.
*   Mayor expresividad.
*   Menos líneas para operaciones simples.
*   Muy utilizadas en Python profesional.

### No recomendable cuando:[](#no-recomendable-cuando "Permanent link")

*   La lógica es compleja o muy anidada.
*   Se requieren múltiples condiciones difíciles de leer.
*   Se sacrifica claridad por brevedad.

Ejemplo poco legible (a evitar):

```
resultado = [x for x in datos if x > 0 if x % 2 == 0 if x < 100]
```

- - -

## 9\. Buenas prácticas[](#9-buenas-practicas "Permanent link")

*   Priorizar la **legibilidad** frente a la concisión extrema.
*   No abusar de comprehensions anidadas.
*   Usar nombres de variables claros.
*   Limitar la complejidad de la expresión.

Ejemplo correcto y legible:

```
pares_positivos = [n for n in numeros if n > 0 and n % 2 == 0]
```

- - -

## 10\. Comparación: bucle tradicional vs comprehension[](#10-comparacion-bucle-tradicional-vs-comprehension "Permanent link")

| Bucle tradicional | Comprehension |
| --- | --- |
| Más líneas de código | Código compacto |
| Muy explícito | Más expresivo |
| Fácil para principiantes | Requiere práctica |
| Flexible para lógica compleja | Ideal para lógica simple |

- - -

[⬆ Ir arriba](#top)
