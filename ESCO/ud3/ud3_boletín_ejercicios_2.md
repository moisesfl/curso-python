# UD03\_boletin\_ejercicios\_2

<div id="top"></div>

## Índice de contenidos

*   [Boletín de Ejercicios – UD03: Estructuras iterativas (bucles) en Python](#boletin-de-ejercicios-ud03-estructuras-iterativas-bucles-en-python)
    *   [Ejercicio 1 — Búsqueda secuencial (lineal) con “early exit”](#ejercicio-1-busqueda-secuencial-lineal-con-early-exit)
        *   [Enunciado](#enunciado)
    *   [Ejercicio 2 — Búsqueda binaria (lista ordenada, sin funciones)](#ejercicio-2-busqueda-binaria-lista-ordenada-sin-funciones)
        *   [Enunciado](#enunciado_1)
    *   [Ejercicio 3 — Two Sum (dos números que suman un objetivo, sin funciones)](#ejercicio-3-two-sum-dos-numeros-que-suman-un-objetivo-sin-funciones)
        *   [Enunciado](#enunciado_2)
    *   [Ejercicio 4 — Validación de paréntesis, corchetes y llaves (sin funciones)](#ejercicio-4-validacion-de-parentesis-corchetes-y-llaves-sin-funciones)
        *   [Enunciado](#enunciado_3)
    *   [Ejercicio 5 — Búsqueda de subcadena (patrón) sin find, sin in, sin funciones](#ejercicio-5-busqueda-de-subcadena-patron-sin-find-sin-in-sin-funciones)
        *   [Enunciado](#enunciado_4)

# Boletín de Ejercicios – UD03: Estructuras iterativas (bucles) en Python[](#boletin-de-ejercicios-ud03-estructuras-iterativas-bucles-en-python "Permanent link")

- - -

## Ejercicio 1 — Búsqueda secuencial (lineal) con “early exit”[](#ejercicio-1-busqueda-secuencial-lineal-con-early-exit "Permanent link")

### Enunciado[](#enunciado "Permanent link")

Dada una lista de números enteros y un número objetivo, recorre la lista **de izquierda a derecha** para localizar el objetivo.

*   Si lo encuentras, muestra: `Número encontrado en la posición X`.
*   Si no lo encuentras, muestra: `Número no encontrado`.
*   Debes **parar** el bucle cuando lo encuentres (usa `break`).

- - -

## Ejercicio 2 — Búsqueda binaria (lista ordenada, sin funciones)[](#ejercicio-2-busqueda-binaria-lista-ordenada-sin-funciones "Permanent link")

### Enunciado[](#enunciado_1 "Permanent link")

Dada una lista de números **ordenada ascendentemente** y un número objetivo:

*   Implementa una **búsqueda binaria** usando `while`.
*   Si el objetivo está, muestra: `Número encontrado en la posición X`.
*   Si no está, muestra: `Número no encontrado`.

> **Nota:** la búsqueda binaria solo es válida si la lista está ordenada.

- - -

## Ejercicio 3 — Two Sum (dos números que suman un objetivo, sin funciones)[](#ejercicio-3-two-sum-dos-numeros-que-suman-un-objetivo-sin-funciones "Permanent link")

### Enunciado[](#enunciado_2 "Permanent link")

Dada una lista de enteros y un valor objetivo, determina si existen **dos posiciones distintas** `i` y `j` tal que: `numeros[i] + numeros[j] == objetivo`

*   Si existe, muestra: `Índices: i y j` y termina el programa (usa `break`).
*   Si no existe, muestra: `No existen dos números que sumen el objetivo`.

> **Restricción:** resuélvelo con bucles (sin diccionarios y sin funciones).

- - -

## Ejercicio 4 — Validación de paréntesis, corchetes y llaves (sin funciones)[](#ejercicio-4-validacion-de-parentesis-corchetes-y-llaves-sin-funciones "Permanent link")

### Enunciado[](#enunciado_3 "Permanent link")

Dada una cadena que contiene solo los caracteres `()[]{}`, comprueba si está **balanceada**:

*   Cada apertura debe cerrarse con el mismo tipo.
*   El orden de cierre debe ser correcto.

Muestra:

*   `Paréntesis balanceados` si es correcta.
*   `Paréntesis no balanceados` si no lo es.

> **Pista:** usa una **pila** (lista) y `append()`/`pop()`.

- - -

## Ejercicio 5 — Búsqueda de subcadena (patrón) sin `find`, sin `in`, sin funciones[](#ejercicio-5-busqueda-de-subcadena-patron-sin-find-sin-in-sin-funciones "Permanent link")

### Enunciado[](#enunciado_4 "Permanent link")

Dado un `texto` y un `patron`, busca manualmente (carácter a carácter) la **primera posición** donde aparece `patron` dentro de `texto`.

*   Si aparece, muestra: `Patrón encontrado en la posición X`.
*   Si no aparece, muestra: `Patrón no encontrado`.

> **Restricción:** no uses `find()`, `in` ni expresiones regulares.

- - -

[⬆ Ir arriba](#top)
