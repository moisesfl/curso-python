# UD04\_3-Recursividad

Generado a partir de Markdown · Conversor Python

## Índice de contenidos

*   [UD04 — Recursividad en Python ](#ud04-recursividad-en-python)
    *   [1\. ¿Qué es la recursividad?](#1-que-es-la-recursividad)
    *   [2\. Estructura típica de una función recursiva](#2-estructura-tipica-de-una-funcion-recursiva)
    *   [3\. Ventajas y desventajas](#3-ventajas-y-desventajas)
        *   [Ventajas](#ventajas)
        *   [Desventajas](#desventajas)
    *   [4\. Ejemplos típicos (con comentarios dentro del código)](#4-ejemplos-tipicos-con-comentarios-dentro-del-codigo)
        *   [4.1 Factorial (n!) ](#41-factorial-n)
        *   [4.2 Fibonacci (sin y con memoización) ](#42-fibonacci-sin-y-con-memoizacion)
        *   [4.3 Suma de los primeros n números (1 + 2 + ... + n) ➕](#43-suma-de-los-primeros-n-numeros-1-2-n)
        *   [4.4 Suma de una lista (sin usar sum) ](#44-suma-de-una-lista-sin-usar-sum)
        *   [4.5 Contar elementos de una lista (sin len) ](#45-contar-elementos-de-una-lista-sin-len)
        *   [4.6 Potencia (a^b) sin usar \*\* ](#46-potencia-ab-sin-usar)
        *   [4.7 Máximo común divisor (MCD) — algoritmo de Euclides ](#47-maximo-comun-divisor-mcd-algoritmo-de-euclides)
        *   [4.8 Invertir una cadena recursivamente ](#48-invertir-una-cadena-recursivamente)
        *   [4.9 Comprobar palíndromo (recursivo) ](#49-comprobar-palindromo-recursivo)
        *   [4.10 Búsqueda binaria recursiva (en lista ordenada) ](#410-busqueda-binaria-recursiva-en-lista-ordenada)
        *   [4.11 Aplanar (flatten) una lista anidada ](#411-aplanar-flatten-una-lista-anidada)
        *   [4.12 Torres de Hanoi (clásico de recursividad) ](#412-torres-de-hanoi-clasico-de-recursividad)
        *   [4.13 Ordenación recursiva (Merge Sort) ](#413-ordenacion-recursiva-merge-sort)
        *   [4.14 Backtracking: generar permutaciones ](#414-backtracking-generar-permutaciones)
    *   [5\. Errores típicos en recursividad (y cómo evitarlos)](#5-errores-tipicos-en-recursividad-y-como-evitarlos)
    *   [6\. Profundidad de recursión y RecursionError](#6-profundidad-de-recursion-y-recursionerror)

# UD04 — Recursividad en Python [](#ud04-recursividad-en-python "Permanent link")

## 1\. ¿Qué es la recursividad?[](#1-que-es-la-recursividad "Permanent link")

La **recursividad** es una técnica de programación en la que una **función se llama a sí misma** para resolver un problema dividiéndolo en **subproblemas más pequeños** del mismo tipo.

En una función recursiva siempre deben existir:

*   **Caso base**: condición que **detiene** la recursión.
*   **Caso recursivo**: parte que **reduce** el problema y llama de nuevo a la función.
*   **Progreso**: en cada llamada recursiva el problema debe hacerse **más pequeño** (o más cercano al caso base).

Si no existe caso base (o no se alcanza), se produce un **bucle recursivo infinito** y Python terminará con un error (normalmente `RecursionError`).

```
función(n)
│
└─ ¿CASO BASE?
    ├─ Sí → devolver resultado y terminar
    │
    └─ No
       └─ llamar a función(n-1)
           │
           ├─ ¿CASO BASE?
           │    └─ Sí → devolver resultado
           │
           └─ No
               └─ llamar a función(n-2)
                    ...
```

- - -

## 2\. Estructura típica de una función recursiva[](#2-estructura-tipica-de-una-funcion-recursiva "Permanent link")

```
def funcion_recursiva(entrada):
    # 1) CASO BASE: condición de parada
    if condicion_base(entrada):
        return resultado_base

    # 2) PASO RECURSIVO: reducir el problema
    subproblema = reducir(entrada)

    # 3) LLAMADA RECURSIVA: resolver el subproblema
    return combinar(entrada, funcion_recursiva(subproblema))
```

- - -

## 3\. Ventajas y desventajas[](#3-ventajas-y-desventajas "Permanent link")

### Ventajas[](#ventajas "Permanent link")

*   Permite soluciones **elegantes** y **cortas** en problemas naturalmente recursivos (árboles, backtracking, divide y vencerás).
*   Facilita el razonamiento en problemas que se definen en términos de sí mismos.

### Desventajas[](#desventajas "Permanent link")

*   Puede ser **menos eficiente** que una solución iterativa (coste extra de llamadas).
*   Riesgo de **desbordar la profundidad de recursión** (stack).
*   Si no se diseña bien, puede repetir cálculos (ej. Fibonacci sin memoización).

- - -

## 4\. Ejemplos típicos (con comentarios dentro del código)[](#4-ejemplos-tipicos-con-comentarios-dentro-del-codigo "Permanent link")

### 4.1 Factorial (n!) [](#41-factorial-n "Permanent link")

**Definición**:

*   `n! = n * (n-1)!`
*   Caso base: `0! = 1`

```
def factorial(n: int) -> int:
    # Validamos que el factorial tenga sentido para n no negativo
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    # CASO BASE: factorial de 0 o 1 es 1
    if n in (0, 1):
        return 1

    # PASO RECURSIVO: reducimos el problema calculando factorial(n-1)
    # y lo combinamos multiplicando por n
    return n * factorial(n - 1)
```

**Traza de llamadas**:

A continuación veremos que una función recursiva es como una cadena de llamadas que se apilan y luego se resuelven hacia atrás.

1.  Fase 1: llamadas recursivas

```
factorial(5)
→ 5 * factorial(4)

factorial(4)
→ 4 * factorial(3)

factorial(3)
→ 3 * factorial(2)

factorial(2)
→ 2 * factorial(1)

factorial(1)
→ 1   ← CASO BASE
```

1.  Fase 2: retornos

```
factorial(1) devuelve 1

factorial(2) devuelve 2 * 1 = 2

factorial(3) devuelve 3 * 2 = 6

factorial(4) devuelve 4 * 6 = 24

factorial(5) devuelve 5 * 24 = 120
```

- - -

### 4.2 Fibonacci (sin y con memoización) [](#42-fibonacci-sin-y-con-memoizacion "Permanent link")

**Definición**:

La serie de Fibonacci es una sucesión de números en la que cada término se obtiene sumando los dos anteriores.

*   `F(0)=0`, `F(1)=1`
*   `F(n) = F(n-1) + F(n-2)`

**Esquema visual**:

```
# Primeros términos de la serie
n:      0   1   2   3   4   5   6   7
F(n):   0   1   1   2   3   5   8  13
```

```
# Sucesión de Fibonacci
0, 1,
   └── 0 + 1 = 1
        └── 1 + 1 = 2
             └── 1 + 2 = 3
                  └── 2 + 3 = 5
                       └── 3 + 5 = 8
```

#### a) Versión recursiva simple[](#a-version-recursiva-simple "Permanent link")

```
def fibonacci_lento(n: int) -> int:
    # Validamos entrada
    if n < 0:
        raise ValueError("Fibonacci no está definido para n negativo.")

    # CASOS BASE
    if n == 0:
        return 0
    if n == 1:
        return 1

    # PASO RECURSIVO: se recalculan muchas veces los mismos valores
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)
```

#### b) Versión con memoización (más eficiente)[](#b-version-con-memoizacion-mas-eficiente "Permanent link")

> **¿Qué es la [memoización](https://es.wikipedia.org/wiki/Memoización)?**: es una técnica de optimización utilizada en programación (especialmente en recursividad y programación dinámica) que consiste en guardar los resultados de cálculos ya realizados para no volver a repetirlos.

Comparación conceptual:

```
#Sin memoización 

fibonacci(4)
├─ fibonacci(3)
│  ├─ fibonacci(2)
│  │  ├─ fibonacci(1)
│  │  └─ fibonacci(0)
│  └─ fibonacci(1)
└─ fibonacci(2)
   ├─ fibonacci(1)
   └─ fibonacci(0)

# Con memoización

fibonacci(4)
├─ fibonacci(3)  ← se calcula una vez
├─ fibonacci(2)  ← se calcula una vez
├─ fibonacci(1)  ← se reutiliza
└─ fibonacci(0)  ← se reutiliza
```

Código:

```
def fibonacci_memo(n: int, memo: dict[int, int] | None = None) -> int:
    # Inicializamos el diccionario de memoización si no existe
    if memo is None:
        memo = {}

    # Validamos entrada
    if n < 0:
        raise ValueError("Fibonacci no está definido para n negativo.")

    # Si ya hemos calculado F(n), lo devolvemos sin recalcular
    if n in memo:
        return memo[n]

    # CASOS BASE
    if n == 0:
        memo[0] = 0
        return 0
    if n == 1:
        memo[1] = 1
        return 1

    # PASO RECURSIVO: calculamos y guardamos el resultado
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    # Devolvemos el valor ya memorizado
    return memo[n]
```

- - -

### 4.3 Suma de los primeros n números (1 + 2 + ... + n) ➕[](#43-suma-de-los-primeros-n-numeros-1-2-n "Permanent link")

Traza de llamadas:

```
# Fase de descenso (llamadas recursivas)

suma_1_a_n(4)
→ 4 + suma_1_a_n(3)

suma_1_a_n(3)
→ 3 + suma_1_a_n(2)

suma_1_a_n(2)
→ 2 + suma_1_a_n(1)

suma_1_a_n(1)
→ 1 + suma_1_a_n(0)

suma_1_a_n(0)
→ 0   ← CASO BASE


# Fase de ascenso (retornos)

suma_1_a_n(0) devuelve 0

suma_1_a_n(1) devuelve 1 + 0 = 1

suma_1_a_n(2) devuelve 2 + 1 = 3

suma_1_a_n(3) devuelve 3 + 3 = 6

suma_1_a_n(4) devuelve 4 + 6 = 10
```

Código:

```
def suma_1_a_n(n: int) -> int:
    # Validamos que n sea natural (>= 0)
    if n < 0:
        raise ValueError("n debe ser >= 0.")

    # CASO BASE: si n es 0, la suma es 0
    if n == 0:
        return 0

    # PASO RECURSIVO: sumamos n + suma_1_a_n(n-1)
    return n + suma_1_a_n(n - 1)
```

- - -

### 4.4 Suma de una lista (sin usar sum) [](#44-suma-de-una-lista-sin-usar-sum "Permanent link")

Traza de llamadas:

```
# Fase de llamadas recursivas

suma_lista([1, 2, 3])
→ 1 + suma_lista([2, 3])

suma_lista([2, 3])
→ 2 + suma_lista([3])

suma_lista([3])
→ 3 + suma_lista([])

suma_lista([])
→ 0   ← CASO BASE

# Fase de retornos
suma_lista([]) devuelve 0

suma_lista([3]) devuelve 3 + 0 = 3

suma_lista([2, 3]) devuelve 2 + 3 = 5

suma_lista([1, 2, 3]) devuelve 1 + 5 = 6
```

Código:

```
def suma_lista(nums: list[int]) -> int:
    # CASO BASE: si la lista está vacía, su suma es 0
    if len(nums) == 0:
        return 0

    # PASO RECURSIVO:
    # - Tomamos el primer elemento (nums[0])
    # - Sumamos la suma del resto de la lista (nums[1:])
    return nums[0] + suma_lista(nums[1:])
```

- - -

### 4.5 Contar elementos de una lista (sin len) [](#45-contar-elementos-de-una-lista-sin-len "Permanent link")

Traza de llamadas:

```
# Fase de llamadas recursivas
contar_lista(["a", "b", "c"])
→ 1 + contar_lista(["b", "c"])

contar_lista(["b", "c"])
→ 1 + contar_lista(["c"])

contar_lista(["c"])
→ 1 + contar_lista([])

contar_lista([])
→ 0   ← CASO BASE


# Fase de retornos
contar_lista([]) devuelve 0

contar_lista(["c"]) devuelve 1 + 0 = 1

contar_lista(["b", "c"]) devuelve 1 + 1 = 2

contar_lista(["a", "b", "c"]) devuelve 1 + 2 = 3
```

Código:

```
def contar_lista(nums: list[object]) -> int:
    # CASO BASE: lista vacía -> 0 elementos
    if nums == []:
        return 0

    # PASO RECURSIVO: 1 (por el primer elemento) + contar el resto
    return 1 + contar_lista(nums[1:])
```

- - -

### 4.6 Potencia (a^b) sin usar \*\* [](#46-potencia-ab-sin-usar "Permanent link")

Traza de llamadas:

```
# Fase de llamadas recursivas

potencia(2, 3)
→ 2 * potencia(2, 2)

potencia(2, 2)
→ 2 * potencia(2, 1)

potencia(2, 1)
→ 2 * potencia(2, 0)

potencia(2, 0)
→ 1   ← CASO BASE

# Fase de retornos

potencia(2, 0) devuelve 1

potencia(2, 1) devuelve 2 * 1 = 2

potencia(2, 2) devuelve 2 * 2 = 4

potencia(2, 3) devuelve 2 * 4 = 8
```

Código:

*   Caso base: `a^0 = 1`

```
def potencia(a: int, b: int) -> int:
    # Validamos exponente no negativo para simplificar el ejemplo
    if b < 0:
        raise ValueError("Este ejemplo asume b >= 0.")

    # CASO BASE: cualquier número elevado a 0 es 1
    if b == 0:
        return 1

    # PASO RECURSIVO: a^b = a * a^(b-1)
    return a * potencia(a, b - 1)
```

- - -

### 4.7 Máximo común divisor (MCD) — algoritmo de Euclides [](#47-maximo-comun-divisor-mcd-algoritmo-de-euclides "Permanent link")

Traza de llamadas:

```
# Fase de llamadas recursivas

mcd(48, 18)
→ mcd(18, 48 % 18)
→ mcd(18, 12)

mcd(18, 12)
→ mcd(12, 18 % 12)
→ mcd(12, 6)

mcd(12, 6)
→ mcd(6, 12 % 6)
→ mcd(6, 0)

mcd(6, 0)
→ 6   ← CASO BASE

# Fase de retornos
mcd(6, 0) devuelve 6
mcd(12, 6) devuelve 6
mcd(18, 12) devuelve 6
mcd(48, 18) devuelve 6
```

Código:

*   `mcd(a, b) = mcd(b, a % b)`
*   Caso base: cuando `b == 0`, `mcd(a, 0) = a`

```
def mcd(a: int, b: int) -> int:
    # Normalizamos a valores no negativos
    a, b = abs(a), abs(b)

    # CASO BASE: si b es 0, el MCD es a
    if b == 0:
        return a

    # PASO RECURSIVO: reducimos usando el resto
    return mcd(b, a % b)
```

- - -

### 4.8 Invertir una cadena recursivamente [](#48-invertir-una-cadena-recursivamente "Permanent link")

Traza de llamadas:

```
# Fase de llamadas recursivas
invertir_cadena("hola")
→ "a" + invertir_cadena("hol")

invertir_cadena("hol")
→ "l" + invertir_cadena("ho")

invertir_cadena("ho")
→ "o" + invertir_cadena("h")

invertir_cadena("h")
→ "h"   ← CASO BASE


# Fase de retornos
invertir_cadena("h") devuelve "h"

invertir_cadena("ho") devuelve "o" + "h" = "oh"

invertir_cadena("hol") devuelve "l" + "oh" = "loh"

invertir_cadena("hola") devuelve "a" + "loh" = "aloh"
```

Código:

```
def invertir_cadena(s: str) -> str:
    # CASO BASE: una cadena vacía o de 1 carácter ya está "invertida"
    if len(s) <= 1:
        return s

    # PASO RECURSIVO:
    # - Tomamos el último carácter (s[-1])
    # - Lo concatenamos con la inversión del resto (s[:-1])
    return s[-1] + invertir_cadena(s[:-1])
```

- - -

### 4.9 Comprobar palíndromo (recursivo) [](#49-comprobar-palindromo-recursivo "Permanent link")

Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.

Traza de llamadas:

```
# Llamadas recursivas

es_palindromo("anitalavalatina")
→ extremos: a == a ✔
→ llama a es_palindromo("nitalavalatin")

es_palindromo("nitalavalatin")
→ extremos: n == n ✔
→ llama a es_palindromo("italavalati")

es_palindromo("italavalati")
→ extremos: i == i ✔
→ llama a es_palindromo("talavalat")

es_palindromo("talavalat")
→ extremos: t == t ✔
→ llama a es_palindromo("alavala")

es_palindromo("alavala")
→ extremos: a == a ✔
→ llama a es_palindromo("laval")

es_palindromo("laval")
→ extremos: l == l ✔
→ llama a es_palindromo("ava")

es_palindromo("ava")
→ extremos: a == a ✔
→ llama a es_palindromo("v")

es_palindromo("v")
→ True   ← CASO BASE


# Retornos
#   - No se construye un valor nuevo
#   - El True del caso base se propaga hacia arriba

es_palindromo("v") devuelve True
es_palindromo("ava") devuelve True
es_palindromo("laval") devuelve True
es_palindromo("alavala") devuelve True
es_palindromo("talavalat") devuelve True
es_palindromo("italavalati") devuelve True
es_palindromo("nitalavalatin") devuelve True
es_palindromo("anitalavalatina") devuelve True
```

Código:

```
def es_palindromo(s: str) -> bool:
    # Normalizamos: quitamos espacios y pasamos a minúsculas
    s = "".join(ch.lower() for ch in s if ch.isalnum())

    # CASO BASE: 0 o 1 caracteres siempre forman un palíndromo
    if len(s) <= 1:
        return True

    # Si los extremos no coinciden, ya no es palíndromo
    if s[0] != s[-1]:
        return False

    # PASO RECURSIVO: comprobamos el interior de la cadena
    return es_palindromo(s[1:-1])
```

- - -

### 4.10 Búsqueda binaria recursiva (en lista ordenada) [](#410-busqueda-binaria-recursiva-en-lista-ordenada "Permanent link")

Requisitos: - La lista debe estar **ordenada**.

Código:

```
# nums = [1, 3, 5, 7, 9, 11, 13]

def busqueda_binaria(nums: list[int], objetivo: int, izquierda: int = 0, derecha: int | None = None) -> int:
    # Si derecha no se especifica, la ponemos al último índice válido
    if derecha is None:
        derecha = len(nums) - 1

    # CASO BASE: si el rango es inválido, no encontramos el objetivo
    if izquierda > derecha:
        return -1

    # Calculamos el punto medio del rango actual
    medio = (izquierda + derecha) // 2

    # Si el medio es el objetivo, devolvemos su índice
    if nums[medio] == objetivo:
        return medio

    # Si el objetivo es menor, buscamos en la mitad izquierda
    if objetivo < nums[medio]:
        return busqueda_binaria(nums, objetivo, izquierda, medio - 1)

    # Si el objetivo es mayor, buscamos en la mitad derecha
    return busqueda_binaria(nums, objetivo, medio + 1, derecha)
```

Traza de llamadas:

```
# Fase de llamadas recursivas

busqueda_binaria(nums, 7, 0, 6)
→ medio = (0 + 6) // 2 = 3
→ nums[3] = 7 ✔

# fase de retornos
busqueda_binaria(...) devuelve 3
```

- - -

### 4.11 Aplanar (flatten) una lista anidada [](#411-aplanar-flatten-una-lista-anidada "Permanent link")

Ejemplo: - Entrada: `[1, [2, 3], [4, [5, 6]]]` - Salida: `[1, 2, 3, 4, 5, 6]`

```
def aplanar(lista: list) -> list:
    # CASO BASE: si la lista está vacía, devolvemos lista vacía
    if lista == []:
        return []

    # Tomamos el primer elemento y el resto
    primero = lista[0]
    resto = lista[1:]

    # Si el primero es una lista, aplanamos primero y resto, y concatenamos
    if isinstance(primero, list):
        return aplanar(primero) + aplanar(resto)

    # Si no es lista, lo metemos como elemento y aplanamos el resto
    return [primero] + aplanar(resto)
```

🔍 Consulta en un LLM la traza de llamadas para tener un esqueama visual.

- - -

### 4.12 Torres de Hanoi (clásico de recursividad) [](#412-torres-de-hanoi-clasico-de-recursividad "Permanent link")

1.  Información sobre el problema: [Wikipedia: Torres de Hanoi](https://es.wikipedia.org/wiki/Torres_de_Hanói)
    
2.  Traza de llamadas:
    

```
# Llamadas recursivas
hanoi(3, A, B, C)
├── hanoi(2, A, C, B)
│   ├── hanoi(1, A, B, C)
│   │   → Mover disco 1 desde A hasta C
│   ├── Mover disco 2 desde A hasta B
│   └── hanoi(1, C, A, B)
│       → Mover disco 1 desde C hasta B
├── Mover disco 3 desde A hasta C
└── hanoi(2, B, A, C)
    ├── hanoi(1, B, C, A)
    │   → Mover disco 1 desde B hasta A
    ├── Mover disco 2 desde B hasta C
    └── hanoi(1, A, B, C)
        → Mover disco 1 desde A hasta C

# Secuencia de movimientos de los discos (aquí no hay retornos)
1. Mover disco 1 desde A hasta C
2. Mover disco 2 desde A hasta B
3. Mover disco 1 desde C hasta B
4. Mover disco 3 desde A hasta C
5. Mover disco 1 desde B hasta A
6. Mover disco 2 desde B hasta C
7. Mover disco 1 desde A hasta C
```

Problema: - Mover `n` discos desde **Origen** a **Destino** usando **Auxiliar** - Sin poner un disco grande encima de uno pequeño.

```
def hanoi(n: int, origen: str, auxiliar: str, destino: str) -> None:
    # CASO BASE: si solo hay 1 disco, se mueve directamente
    if n == 1:
        print(f"Mover disco 1 desde {origen} hasta {destino}")
        return

    # PASO 1: mover n-1 discos de origen a auxiliar usando destino como apoyo
    hanoi(n - 1, origen, destino, auxiliar)

    # PASO 2: mover el disco grande (n) de origen a destino
    print(f"Mover disco {n} desde {origen} hasta {destino}")

    # PASO 3: mover n-1 discos de auxiliar a destino usando origen como apoyo
    hanoi(n - 1, auxiliar, origen, destino)
```

- - -

### 4.13 Ordenación recursiva (Merge Sort) [](#413-ordenacion-recursiva-merge-sort "Permanent link")

Idea: - Divide la lista en mitades, ordena cada mitad recursivamente y luego **fusiona**.

```
def merge_sort(nums: list[int]) -> list[int]:
    # CASO BASE: una lista de 0 o 1 elemento ya está ordenada
    if len(nums) <= 1:
        return nums

    # Dividimos la lista en dos mitades
    mitad = len(nums) // 2
    izquierda = nums[:mitad]
    derecha = nums[mitad:]

    # Ordenamos recursivamente cada mitad
    izquierda_ordenada = merge_sort(izquierda)
    derecha_ordenada = merge_sort(derecha)

    # Fusionamos las dos mitades ordenadas
    return fusionar(izquierda_ordenada, derecha_ordenada)


def fusionar(a: list[int], b: list[int]) -> list[int]:
    # i y j son punteros para recorrer a y b
    i = 0
    j = 0
    resultado = []

    # Mientras queden elementos en ambos, tomamos el menor
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1

    # Añadimos lo que quede en a (si queda)
    resultado.extend(a[i:])

    # Añadimos lo que quede en b (si queda)
    resultado.extend(b[j:])

    return resultado
```

🔍 Consulta en un LLM la traza de llamadas para tener un esqueama visual.

- - -

### 4.14 Backtracking: generar permutaciones [](#414-backtracking-generar-permutaciones "Permanent link")

Backtracking = explorar posibilidades, y “deshacer” (backtrack) para probar otras.

> **¿Qué es el Backtracking?** El backtracking es una técnica de programación recursiva que consiste en: explorar todas las soluciones posibles de un problema, avanzando paso a paso y “volviendo atrás” cuando una opción ya no sirve. La idea clave es: Elegir una opción Probarla (llamada recursiva) Deshacer la elección implícitamente al volver de la recursión Probar la siguiente opción Se usa cuando: No sabemos cuál es la solución correcta a priori Hay que generar o comprobar todas las combinaciones posibles

Código:

```
def permutaciones(nums: list[int]) -> list[list[int]]:
    # Lista donde guardaremos todas las permutaciones encontradas
    resultado: list[list[int]] = []

    def backtrack(actual: list[int], restantes: list[int]) -> None:
        # CASO BASE: si no quedan elementos, actual es una permutación completa
        if restantes == []:
            resultado.append(actual[:])  # copiamos la lista actual
            return

        # Para cada posible elección, elegimos un elemento y seguimos
        for i in range(len(restantes)):
            elegido = restantes[i]  # elemento que vamos a usar ahora

            # Construimos el nuevo estado:
            # - actual + [elegido]
            # - restantes sin el elegido
            nuevo_actual = actual + [elegido]
            nuevo_restantes = restantes[:i] + restantes[i + 1:]

            # Llamada recursiva para continuar
            backtrack(nuevo_actual, nuevo_restantes)

    # Iniciamos el backtracking con permutación vacía y todos los elementos disponibles
    backtrack([], nums)

    return resultado
```

🔍 Consulta en un LLM la traza de llamadas para tener un esqueama visual.

- - -

## 5\. Errores típicos en recursividad (y cómo evitarlos)[](#5-errores-tipicos-en-recursividad-y-como-evitarlos "Permanent link")

1.  **Olvidar el caso base**
2.  La función se llama infinitamente hasta `RecursionError`.
3.  **No reducir el problema**
4.  Aunque exista caso base, nunca se alcanza.
5.  **Modificar listas compartidas sin cuidado**
6.  En backtracking, si reutilizas la misma lista, recuerda copiar o “deshacer” cambios.
7.  **Fibonacci sin memoización**
8.  Repite cálculos y se vuelve muy lento para n medianos.

- - -

## 6\. Profundidad de recursión y RecursionError[](#6-profundidad-de-recursion-y-recursionerror "Permanent link")

Python limita el número de llamadas recursivas anidadas. Si el problema requiere mucha profundidad, se suele preferir:

*   Un enfoque **iterativo**
*   Estructuras de datos (pila/stack) para simular recursión
*   Rediseñar la solución (divide y vencerás, memoización, etc.)

- - -

[⬆ Ir arriba](#top)

