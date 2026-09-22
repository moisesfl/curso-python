# UD03\_boletin\_ejercicios\_1

<div id="top"></div>

## Índice de contenidos

*   [Boletín UD03 - Bucles y Comprensiones](#boletin-ud03-bucles-y-comprensiones)
    *   [Ejercicio 1 — Validador de edad](#ejercicio-1-validador-de-edad)
    *   [Ejercicio 2 — Analizador de frase](#ejercicio-2-analizador-de-frase)
    *   [Ejercicio 3 — Limpieza y normalización de lista de textos (list comprehension)](#ejercicio-3-limpieza-y-normalizacion-de-lista-de-textos-list-comprehension)
    *   [Ejercicio 4 — Filtrado numérico con condición doble (if-else dentro de comprehension)](#ejercicio-4-filtrado-numerico-con-condicion-doble-if-else-dentro-de-comprehension)
        *   [Ejercicio 5 — Eliminación de duplicados y clasificación (set comprehension + bucles)](#ejercicio-5-eliminacion-de-duplicados-y-clasificacion-set-comprehension-bucles)
    *   [Ejercicio 6 — Diccionario de cuadrados filtrados (dict comprehension)](#ejercicio-6-diccionario-de-cuadrados-filtrados-dict-comprehension)
    *   [Ejercicio 7 — Inventario y actualización (diccionarios + bucles)](#ejercicio-7-inventario-y-actualizacion-diccionarios-bucles)
    *   [Ejercicio 8 — Búsqueda secuencial en lista (sin funciones)](#ejercicio-8-busqueda-secuencial-en-lista-sin-funciones)
    *   [Ejercicio 9 — Control de saltos (continue) en procesamiento de cadenas](#ejercicio-9-control-de-saltos-continue-en-procesamiento-de-cadenas)
    *   [Ejercicio 10 — Tabla de multiplicar “selectiva” (bucles anidados + continue)](#ejercicio-10-tabla-de-multiplicar-selectiva-bucles-anidados-continue)
    *   [Ejercicio 11 — Generador de cuadrados bajo demanda (generator comprehension)](#ejercicio-11-generador-de-cuadrados-bajo-demanda-generator-comprehension)
    *   [Ejercicio 12 — Parseo de números “sucios” (strings + casting + control)](#ejercicio-12-parseo-de-numeros-sucios-strings-casting-control)
    *   [Ejercicio 13 — Estadística básica de lista (for + acumuladores)](#ejercicio-13-estadistica-basica-de-lista-for-acumuladores)
    *   [Ejercicio 14 — “Mini ETL”: transformar diccionario de alumnos (dict + comprehension)](#ejercicio-14-mini-etl-transformar-diccionario-de-alumnos-dict-comprehension)
    *   [Ejercicio 15 — Reto integrador: clasificación y resumen de compras 🧾 (listas + dict + bucles + comprehensions)](#ejercicio-15-reto-integrador-clasificacion-y-resumen-de-compras-listas-dict-bucles-comprehensions)

# Boletín UD03 - Bucles y Comprensiones[](#boletin-ud03-bucles-y-comprensiones "Permanent link")

## Ejercicio 1 — Validador de edad[](#ejercicio-1-validador-de-edad "Permanent link")

Crea un programa que pida al usuario una edad.

*   Debe repetir la petición **hasta que** el usuario introduzca un número entero válido.
*   Se considera una edad no válida si introduce texto o un número decimal (ej. `"12.5"`).
*   Cuando sea válido:
    
*   Muestra si es **menor de edad** (<18) o **mayor de edad** (≥18).
    
*   Muestra también cuántos intentos inválidos hubo.

> Pistas: `while`, `try/except` (si ya lo habéis visto), `isdigit()` o control manual, `int()`.

- - -

## Ejercicio 2 — Analizador de frase[](#ejercicio-2-analizador-de-frase "Permanent link")

Pide al usuario una frase y:

*   Cuenta cuántas veces aparece cada vocal (**a,e,i,o,u**) ignorando mayúsculas/minúsculas.
*   Guarda el resultado en un diccionario.
*   Muestra:
    
*   El diccionario final
    
*   La vocal más frecuente (si hay empate, muestra todas).

- - -

## Ejercicio 3 — Limpieza y normalización de lista de textos (list comprehension)[](#ejercicio-3-limpieza-y-normalizacion-de-lista-de-textos-list-comprehension "Permanent link")

Dada una lista:

```
datos = ["  Ana ", "luis", "MARIA", "   PeDro", "" , "  "]
```

Genera una nueva lista `nombres` que:

*   Elimine espacios laterales.
*   Descarte entradas vacías tras limpiar.
*   Ponga cada nombre en formato “Capitalizado” (primera mayúscula, resto minúsculas).

**Obligatorio:** usar **list comprehension**.

- - -

## Ejercicio 4 — Filtrado numérico con condición doble (if-else dentro de comprehension)[](#ejercicio-4-filtrado-numerico-con-condicion-doble-if-else-dentro-de-comprehension "Permanent link")

Dada una lista de notas:

```
notas = [2, 10, 5, 4, 7, 3, 9]
```

Crea una lista nueva `estado` con:

*   `"apto"` si la nota ≥ 5
*   `"no apto"` si la nota < 5

**Obligatorio:** usar comprehension con `if-else` en la expresión.

- - -

### Ejercicio 5 — Eliminación de duplicados y clasificación (set comprehension + bucles)[](#ejercicio-5-eliminacion-de-duplicados-y-clasificacion-set-comprehension-bucles "Permanent link")

Dada la lista:

```
valores = [3, 3, 5, 2, 2, 9, 1, 5, 7]
```

*   Crea un conjunto `unicos` usando **set comprehension**.
*   Convierte el conjunto a lista y ordénala de menor a mayor.
*   Recorre la lista ordenada y muestra:
    
*   cada número
    
*   su cuadrado

- - -

## Ejercicio 6 — Diccionario de cuadrados filtrados (dict comprehension)[](#ejercicio-6-diccionario-de-cuadrados-filtrados-dict-comprehension "Permanent link")

Genera un diccionario con `range(1, 21)` donde:

*   La clave sea el número.
*   El valor sea su cuadrado.
*   **Solo** deben incluirse númerosñ los números que sean múltiplos de 3.

**Obligatorio:** dict comprehension con condición.

- - -

## Ejercicio 7 — Inventario y actualización (diccionarios + bucles)[](#ejercicio-7-inventario-y-actualizacion-diccionarios-bucles "Permanent link")

Tienes este inventario:

```
inventario = {"pan": 10, "leche": 5, "huevos": 12}
```

El programa debe permitir en bucle:

1.  pedir un producto
2.  pedir una cantidad (entera)
    
3.  Si el producto no existe, debe añadirlo.
    
4.  Si existe, debe sumar la cantidad.
5.  Si el usuario escribe `"salir"`, termina. Al final muestra:
6.  inventario final
7.  total de unidades (suma de valores)
8.  producto con más unidades

- - -

## Ejercicio 8 — Búsqueda secuencial en lista (sin funciones)[](#ejercicio-8-busqueda-secuencial-en-lista-sin-funciones "Permanent link")

Dada una lista de nombres y un nombre objetivo introducido por teclado:

*   Recorre la lista con `for` e indica si está o no.
*   Si está, muestra su índice (posición).
*   Debe dejar de buscar en cuanto lo encuentre (**usa `break`**).

- - -

## Ejercicio 9 — Control de saltos (continue) en procesamiento de cadenas[](#ejercicio-9-control-de-saltos-continue-en-procesamiento-de-cadenas "Permanent link")

Pide 10 palabras al usuario (una por una) y:

*   Ignora (no guardes) las que tengan longitud menor que 3.
*   Para el resto, guárdalas en una lista en minúsculas.
*   Al final muestra:
    
*   lista final
    
*   cantidad de palabras descartadas

> Usa `continue` para saltarte lo que no interesa.

- - -

## Ejercicio 10 — Tabla de multiplicar “selectiva” (bucles anidados + continue)[](#ejercicio-10-tabla-de-multiplicar-selectiva-bucles-anidados-continue "Permanent link")

Muestra por pantalla la tabla de multiplicar del 1 al 10 (formato `i x j = resultado`)

*   Pero **no imprimas** las filas donde `i` sea par.
*   Y dentro de las filas impares, **no imprimas** los productos donde `j` sea múltiplo de 3.

> Obligatorio: bucles anidados + `continue`.

- - -

## Ejercicio 11 — Generador de cuadrados bajo demanda (generator comprehension)[](#ejercicio-11-generador-de-cuadrados-bajo-demanda-generator-comprehension "Permanent link")

Crea un generador que produzca los cuadrados de `1..100`.

*   Recorre el generador e imprime solo los primeros 10 valores.
*   Sin convertirlo a lista.

> Usa `break` cuando ya hayas impreso 10.

- - -

## Ejercicio 12 — Parseo de números “sucios” (strings + casting + control)[](#ejercicio-12-parseo-de-numeros-sucios-strings-casting-control "Permanent link")

Dada esta lista:

```
entradas = ["10", " 20", "30 ", "x", "40.5", "50", "-7", "  "]
```

Construye una lista de enteros válidos:

*   Acepta enteros con espacios (ej. `" 20"` → `20`)
*   Rechaza vacíos, letras y decimales (`"40.5"` no vale)
*   Acepta negativos (`"-7"` sí vale)

Muestra:

*   lista final
*   suma total
*   cuántos elementos fueron descartados

- - -

## Ejercicio 13 — Estadística básica de lista (for + acumuladores)[](#ejercicio-13-estadistica-basica-de-lista-for-acumuladores "Permanent link")

Pide al usuario 8 números enteros y guarda en una lista. Calcula y muestra:

*   mínimo
*   máximo
*   media (float con 2 decimales)
*   cuántos son pares y cuántos impares

- - -

## Ejercicio 14 — “Mini ETL”: transformar diccionario de alumnos (dict + comprehension)[](#ejercicio-14-mini-etl-transformar-diccionario-de-alumnos-dict-comprehension "Permanent link")

Dado:

```
notas = {"Ana": "7", "Luis": "4", "Maria": "10", "Pepe": "5"}
```

Crea un nuevo diccionario donde:

*   La clave sea el nombre en mayúsculas.
*   El valor sea la nota como entero. Después crea otro diccionario `aprobados` con solo los de nota ≥ 5.

**Obligatorio:** usar dict comprehensions (al menos en una de las transformaciones).

- - -

## Ejercicio 15 — Reto integrador: clasificación y resumen de compras (listas + dict + bucles + comprehensions)[](#ejercicio-15-reto-integrador-clasificacion-y-resumen-de-compras-listas-dict-bucles-comprehensions "Permanent link")

Vas a simular un “carrito de compra” a partir de entradas del usuario.

El programa debe:

1.  Pedir productos hasta que se escriba `"fin"`. Cada entrada tendrá formato: `producto,cantidad,precio_unitario` Ejemplo: `manzanas,2,0.75`
2.  Validar:
    
3.  cantidad debe ser entero > 0
    
4.  precio debe ser float > 0
5.  producto no vacío
6.  si no es válido, descarta esa línea y cuenta errores
7.  Guardar la compra en una estructura adecuada (a tu elección, pero debe permitir luego resumir por producto).
8.  Al final mostrar:
    
9.  Total gastado
    
10.  Diccionario con **total por producto** (sumando cantidades y coste)
11.  Lista de productos ordenados por coste total (de mayor a menor)
12.  Número de líneas inválidas descartadas

> Recomendación: combinar bucles + diccionarios + casting + ordenación + (opcional) comprehensions.

[⬆ Ir arriba](#top)
