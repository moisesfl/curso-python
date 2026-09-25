# UD04\_2-Python-lambda


## Índice de contenidos

*   [Unidad 4: Funciones lambda en Python](#unidad-4-funciones-lambda-en-python)
    *   [Recursos](#recursos)
    *   [¿Qué es una función lambda?](#que-es-una-funcion-lambda)
    *   [Sintaxis y reglas](#sintaxis-y-reglas)
    *   [Cuándo usar lambda (y cuándo no)](#cuando-usar-lambda-y-cuando-no)
    *   [Ejemplos básicos](#ejemplos-basicos)
    *   [Lambdas con map, filter, sorted y reduce](#lambdas-con-map-filter-sorted-y-reduce)
        *   [map(function, iterable) → transforma elementos](#mapfunction-iterable-transforma-elementos)
        *   [filter(function, iterable) → selecciona elementos](#filterfunction-iterable-selecciona-elementos)
        *   [sorted(iterable, key=function, reverse=False) → ordena con una clave](#sortediterable-keyfunction-reversefalse-ordena-con-una-clave)
        *   [Acumulador: functools.reduce(function, iterable\[, initializer\])](#acumulador-functoolsreducefunction-iterable-initializer)
    *   [Rendimiento y legibilidad](#rendimiento-y-legibilidad)
    *   [Ejercicios propuestos](#ejercicios-propuestos)
        *   [Enunciados](#enunciados)
        *   [Soluciones](#soluciones)

# Unidad 4: Funciones `lambda` en Python[](#unidad-4-funciones-lambda-en-python "Permanent link")

- - -

## Recursos[](#recursos "Permanent link")

*   Documentación oficial: `help(lambda)` y módulo `functools`

## ¿Qué es una función `lambda`?[](#que-es-una-funcion-lambda "Permanent link")

Una **función `lambda`** es una función **anónima y pequeña** que se define en una sola expresión. Sirve para crear funciones rápidas **en línea**, normalmente como argumento de otras funciones.

*   Equivalente a una función `def`, pero **sin nombre** y **de una sola expresión**.
*   Ideal para **operaciones simples** y de **vida corta**.

- - -

## Sintaxis y reglas[](#sintaxis-y-reglas "Permanent link")

```
lambda argumentos: expresión
```

*   La **expresión** debe devolver un valor (implícitamente).
*   No admite **múltiples sentencias** (no `return`, no `for`/`while` explícitos, no `try` completo, etc.).
*   Puede usar **operadores ternarios**, llamadas a funciones, comprensiones y expresiones cortas.

**Ejemplos de firmas válidas:**

```
lambda x: x * 2
lambda a, b: (a + b) / 2
lambda x, y=0: x**2 + y  # con valor por defecto
lambda *args: sum(args)
lambda **kwargs: kwargs.get("clave", None)
```

- - -

## Cuándo usar `lambda` (y cuándo no)[](#cuando-usar-lambda-y-cuando-no "Permanent link")

 Úsalo cuando: - La lógica es **simple** y mejora la **fluidez** del código. - Necesitas una función **rápida y local** (ej. `key=` en `sorted`).

 Evítalo cuando: - La lógica es **compleja** o necesita **documentación** → mejor `def`. - Debes **reutilizar** la función en varios lugares → nómbrala con `def`.

- - -

## Ejemplos básicos[](#ejemplos-basicos "Permanent link")

```
# Duplicar un número
doble = lambda x: x * 2
print(doble(5))  # 10

# Media de dos valores
media = lambda a, b: (a + b) / 2
print(media(4, 8))  # 6.0

# Valor absoluto “manual” con condicional
absoluto = lambda x: x if x >= 0 else -x
print(absoluto(-3))  # 3
```

- - -

## Lambdas con `map`, `filter`, `sorted` y `reduce`[](#lambdas-con-map-filter-sorted-y-reduce "Permanent link")

### `map(function, iterable)` → transforma elementos[](#mapfunction-iterable-transforma-elementos "Permanent link")

Toma una lista de números enteros y genera una nueva lista que contiene el cuadrado de cada uno de esos números, utilizando una función lambda junto con la función map. Finalmente, muestra el resultado por pantalla.

```
# Se define una lista de números enteros
nums = [1, 2, 3, 4]

# Se utiliza map para aplicar una función lambda a cada elemento de la lista 'nums'
# La función lambda recibe un valor 'x' y devuelve su cuadrado (x * x)
# map genera un iterable con los resultados, que se convierte en lista con list()
cuadrados = list(map(lambda x: x * x, nums))

# Se imprime la lista resultante, que contiene el cuadrado de cada número original
print(cuadrados)  # [1, 4, 9, 16]
```

### `filter(function, iterable)` → selecciona elementos[](#filterfunction-iterable-selecciona-elementos "Permanent link")

Filtra una lista de números enteros y genera una nueva lista que contiene únicamente los números pares, utilizando una función lambda junto con la función filter.

```
# Se define una lista de números enteros
nums = [1, 2, 3, 4, 5, 6]

# Se utiliza filter para evaluar cada elemento de la lista 'nums'
# La función lambda recibe un valor 'x' y comprueba si es par
# La condición x % 2 == 0 devuelve True para números pares y False para impares
# filter conserva únicamente los elementos para los que la condición es True
# El resultado es un iterable que se convierte en lista con list()
pares = list(filter(lambda x: x % 2 == 0, nums))

# Se imprime la lista resultante, que contiene solo los números pares
print(pares)  # [2, 4, 6]
```

### `sorted(iterable, key=function, reverse=False)` → ordena con una clave[](#sortediterable-keyfunction-reversefalse-ordena-con-una-clave "Permanent link")

Ordena una lista de cadenas de texto según la longitud de cada palabra, de menor a mayor, utilizando una función lambda como criterio de ordenación en la función sorted.

```
# Se define una lista de cadenas de texto
palabras = ["Python", "es", "maravilloso"]

# Se utiliza la función sorted para ordenar la lista 'palabras'
# El parámetro key permite indicar el criterio de ordenación
# La función lambda recibe una cadena 's' y devuelve su longitud con len(s)
# sorted utiliza ese valor numérico para ordenar las palabras de menor a mayor longitud
ordenadas = sorted(palabras, key=lambda s: len(s))

# Se imprime la lista resultante, ordenada según la longitud de cada palabra
print(ordenadas)  # ['es', 'Python', 'maravilloso']
```

### Acumulador: `functools.reduce(function, iterable[, initializer])`[](#acumulador-functoolsreducefunction-iterable-initializer "Permanent link")

Calcula el producto de todos los números contenidos en una lista, utilizando la función reduce del módulo functools junto con una función lambda. La operación va acumulando el resultado multiplicando cada elemento de la lista, y finalmente muestra el valor total por pantalla.

```
# Se importa la función reduce desde el módulo functools
from functools import reduce

# Se define una lista de números enteros
nums = [1, 2, 3, 4]

# Se utiliza reduce para aplicar una operación acumulativa sobre la lista 'nums'
# La función lambda recibe dos parámetros:
#   - acc: el acumulador, que almacena el resultado parcial
#   - x: el valor actual de la lista que se está procesando
# En cada iteración se multiplica el acumulador por el valor actual
# El valor inicial del acumulador se establece en 1 (initializer), ya que para no modifica la multiplicación (en suma sería un 0)
producto = reduce(lambda acc, x: acc * x, nums, 1)

# Se imprime el resultado final, que corresponde al producto de todos los elementos
print(producto)  # 24
```

>  Consejo: En Python idiomático, muchas veces `sum`, comprensiones o bucles son más claros que `map/filter/reduce`.

- - -

## Rendimiento y legibilidad[](#rendimiento-y-legibilidad "Permanent link")

*   **Rendimiento:** similar a una función `def` pequeña; evita usarlas en **caminos críticos** si complican la lectura.
*   **Legibilidad:** si la expresión supera ~1 línea o encadena demasiadas operaciones, **usa `def` con nombre**.
*   **Depuración:** lambdas no tienen nombre → logs/tracebacks menos informativos.

- - -

## Ejercicios propuestos[](#ejercicios-propuestos "Permanent link")

### Enunciados[](#enunciados "Permanent link")

1.  **Dobles pares:** Dada una lista de enteros, usa `filter` + `map` con lambdas para quedarte con pares y multiplicarlos por 2.
    
2.  **Calculadora funcional:** Implementa un diccionario de operaciones (`+, -, *, /`) que seleccione la operación por clave y la aplique.
    

### Soluciones[](#soluciones "Permanent link")

#### 1) Dobles pares[](#1-dobles-pares "Permanent link")

```
nums = [1, 2, 3, 4, 5, 6]
res = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
print(res)  # [4, 8, 12]
```

#### 2) Calculadora funcional[](#2-calculadora-funcional "Permanent link")

```
ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else float("inf"),
}
operacion = ops["+"]
print (operacion (10,5))

#Forma abreviada
print(ops["+"](10, 5))  # 15
print(ops["/"](10, 0))  # inf
```

- - -

[⬆ Ir arriba](#top)

