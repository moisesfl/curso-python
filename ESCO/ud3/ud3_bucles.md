# UD03-Bucles

<div id="top"></div>

## Índice de contenidos

*   [UD03 – Estructuras iterativas (bucles) en Python](#ud03-estructuras-iterativas-bucles-en-python)
    *   [1\. Introducción a las estructuras iterativas](#1-introduccion-a-las-estructuras-iterativas)
    *   [2\. Bucle for](#2-bucle-for)
        *   [Sintaxis general](#sintaxis-general)
        *   [2.1. Iteraciones genéricas](#21-iteraciones-genericas)
        *   [2.2. Iteraciones por listas y tuplas](#22-iteraciones-por-listas-y-tuplas)
        *   [2.3. Iteraciones por secuencias (range())](#23-iteraciones-por-secuencias-range)
        *   [2.4. Iteraciones por diccionarios](#24-iteraciones-por-diccionarios)
        *   [2.5. Bucles anidados](#25-bucles-anidados)
        *   [2.6. Uso de break y continue](#26-uso-de-break-y-continue)
    *   [3\. Bucle while](#3-bucle-while)
        *   [Sintaxis general](#sintaxis-general_1)
        *   [3.1. Bucle while](#31-bucle-while)
        *   [3.2. Bucles anidados mixtos de while y for](#32-bucles-anidados-mixtos-de-while-y-for)
        *   [3.3. Uso de break y continue](#33-uso-de-break-y-continue)
        *   [3.4. Uso de while(true)](#34-uso-de-whiletrue)

# UD03 – Estructuras iterativas (bucles) en Python[](#ud03-estructuras-iterativas-bucles-en-python "Permanent link")

- - -

## 1\. Introducción a las estructuras iterativas[](#1-introduccion-a-las-estructuras-iterativas "Permanent link")

Las **estructuras iterativas**, también conocidas como **bucles**, permiten ejecutar un mismo bloque de instrucciones **de forma repetida** mientras se cumpla una determinada condición o mientras existan elementos que recorrer.

El uso de bucles es fundamental en programación, ya que permite:

*   Evitar la repetición innecesaria de código.
*   Automatizar tareas repetitivas.
*   Recorrer estructuras de datos como listas, tuplas o diccionarios.
*   Implementar algoritmos de búsqueda, validación y procesamiento de datos.

En Python existen **dos tipos principales de estructuras iterativas**:

*   **Bucle `for`**: se utiliza cuando se conoce de antemano el número de iteraciones o cuando se desea recorrer una colección de elementos.
*   **Bucle `while`**: se utiliza cuando la repetición depende de una condición lógica que puede variar durante la ejecución del programa.

- - -

## 2\. Bucle `for`[](#2-bucle-for "Permanent link")

El bucle `for` en Python se utiliza para **recorrer secuencias** (listas, tuplas, rangos, diccionarios, cadenas de texto, etc.) y ejecutar un bloque de instrucciones para cada elemento.

### Sintaxis general[](#sintaxis-general "Permanent link")

```
for variable in secuencia:
    instrucciones
```

- - -

### 2.1. Iteraciones genéricas[](#21-iteraciones-genericas "Permanent link")

En ocasiones no es necesario utilizar la variable de control del bucle. Para estos casos se emplea el guion bajo (`_`) como convención.

```
for _ in range(5):
    print("Hola")
```

Este bucle imprime la palabra _Hola_ cinco veces.

- - -

### 2.2. Iteraciones por listas y tuplas[](#22-iteraciones-por-listas-y-tuplas "Permanent link")

El bucle `for` permite recorrer directamente los elementos de una lista o tupla.

```
lista = [10, 20, 30]

for elemento in lista:
    print(elemento)
```

```
tupla = ("rojo", "verde", "azul")

for color in tupla:
    print(color)
```

- - -

### 2.3. Iteraciones por secuencias (`range()`)[](#23-iteraciones-por-secuencias-range "Permanent link")

La función `range()` genera una secuencia de números y es muy utilizada con el bucle `for`.

```
for i in range(5):
    print(i)
```

También puede especificarse inicio, fin y salto:

```
for i in range(2, 10, 2):
    print(i)
```

- - -

### 2.4. Iteraciones por diccionarios[](#24-iteraciones-por-diccionarios "Permanent link")

En los diccionarios se puede iterar sobre:

*   Claves
*   Valores
*   Pares clave–valor

```
diccionario = {"a": 1, "b": 2, "c": 3}

for clave in diccionario:
    print(clave)
```

```
for valor in diccionario.values():
    print(valor)
```

```
for clave, valor in diccionario.items():
    print(clave, valor)
```

- - -

### 2.5. Bucles anidados[](#25-bucles-anidados "Permanent link")

Un **bucle anidado** es un bucle dentro de otro bucle. Se utilizan cuando es necesario trabajar con estructuras bidimensionales o combinaciones de elementos.

```
for i in range(3):
    for j in range(2):
        print(i, j)
```

En este caso, el bucle interno se ejecuta completamente por cada iteración del bucle externo.

**Output**:

```
0 0
0 1
1 0
1 1
2 0
2 1
```

**Ejemplo 1**: Crear una figura de 6\*6 asteriscos.

```
for i in range(6):              # filas
    for j in range(6):              # columnas
        print("* ", end="")             # end="" evita el salto de linea.
    print()                 # Salto de línea
```

**Ejemplo 2**: Crear una figura triángulo rectángulo.

```
for i in range(1, 7):
    for j in range(i):
        print("*", end="")
    print()
```

**Ejemplo 3**: Crear una figura triángulo equilátero.

```
# Definimos la altura del triángulo equilátero
altura = 6

# Bucle exterior: controla el número de filas del triángulo
for i in range(altura):

    # Imprime los espacios en blanco necesarios para centrar el triángulo
    # En la primera fila imprime más espacios, y va disminuyendo en cada iteración
    for j in range(altura - i - 1):
        print(" ", end="")

    # Imprime los asteriscos de la fila actual
    # El número de asteriscos sigue la fórmula: 2 * i + 1
    for k in range(2 * i + 1):
        print("*", end="")

    # Salto de línea al finalizar cada fila del triángulo
    print()
```

- - -

### 2.6. Uso de `break` y `continue`[](#26-uso-de-break-y-continue "Permanent link")

*   **`break`**: finaliza el bucle de forma inmediata.
*   **`continue`**: salta a la siguiente iteración del bucle.

Ejemplo con `break`:

```
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```
0
1
2
3
4
```

Ejemplo con `continue`:

```
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

- - -

## 3\. Bucle `while`[](#3-bucle-while "Permanent link")

El bucle `while` se ejecuta **mientras una condición sea verdadera**. Es adecuado cuando no se conoce previamente el número de iteraciones.

### Sintaxis general[](#sintaxis-general_1 "Permanent link")

```
while condicion:
    instrucciones
```

- - -

### 3.1. Bucle `while`[](#31-bucle-while "Permanent link")

Ejemplo básico:

```
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

Es fundamental que la condición del bucle llegue a ser falsa para evitar **bucles infinitos**.

- - -

### 3.2. Bucles anidados mixtos de `while` y `for`[](#32-bucles-anidados-mixtos-de-while-y-for "Permanent link")

Es posible combinar ambos tipos de bucles dentro de un mismo programa.

Ejemplo:

```
i = 1

while i <= 3:
    for j in range(2):
        print(i, j)
    i += 1
```

Output:

```
1 0
1 1
2 0
2 1
3 0
3 1
```

- - -

### 3.3. Uso de `break` y `continue`[](#33-uso-de-break-y-continue "Permanent link")

Al igual que en el bucle `for`, el bucle `while` admite las sentencias `break` y `continue`.

Ejemplo:

```
numero = 0

while True:
    numero += 1
    if numero == 3:
        continue
    if numero == 6:
        break
    print(numero)
```

Output:

```
1
2
4
5
```

### 3.4. Uso de `while(true)`[](#34-uso-de-whiletrue "Permanent link")

En Python, la expresión `True` representa un valor booleano siempre verdadero. Cuando se utiliza en un bucle `while`, provoca que el bucle se ejecute **de forma indefinida**, es decir, se convierte en un **bucle infinito**.

#### Sintaxis[](#sintaxis "Permanent link")

```
while True:
    instrucciones
```

Este tipo de bucle solo finaliza si se produce:

*   Un `break`
*   Una excepción
*   La finalización forzada del programa

#### Ejemplo de `while True`[](#ejemplo-de-while-true "Permanent link")

```
while True:
    numero = int(input("Introduce un número positivo: "))

    if numero > 0:
        print("Número válido")
        break
    else:
        print("El número debe ser positivo")
```

**¿Qué hace este código?**

*   El programa solicita un número al usuario de forma repetida.
*   Mientras el número no sea positivo, el bucle continúa ejecutándose.
*   Cuando se introduce un valor correcto, se ejecuta `break` y el bucle finaliza.

#### ¿Por qué `while True` no es una buena práctica?[](#por-que-while-true-no-es-una-buena-practica "Permanent link")

Aunque `while True` **funciona correctamente**, su uso presenta varios inconvenientes desde el punto de vista del diseño y la legibilidad del código:

**1\. Menor claridad semántica**

La condición real de salida del bucle **no es visible en la cabecera**, sino oculta dentro del cuerpo del bucle mediante uno o varios `break`.

Esto dificulta:

*   La lectura del código.
*   El mantenimiento.
*   La comprensión rápida de cuándo termina el bucle.

**2\. Mayor riesgo de errores**

Si se olvida incluir un `break` o este no se alcanza por un error lógico, el programa quedará atrapado en un **bucle infinito real**, consumiendo recursos y bloqueando la ejecución.

**3\. Dificulta la depuración**

Los bucles infinitos hacen más compleja la detección de errores, especialmente para programadores en formación, ya que el flujo del programa no está claramente definido.

[⬆ Ir arriba](#top)
