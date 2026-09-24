# UD04\_1-Funciones


## Índice de contenidos

*   [Unidad 4: Funciones en Python](#unidad-4-funciones-en-python)
    *   [1.Qué ventajas tiene la programación funcional](#1que-ventajas-tiene-la-programacion-funcional)
        *   [1.1. El papel de las funciones en programación](#11-el-papel-de-las-funciones-en-programacion)
        *   [1.2. Funciones y programación funcional](#12-funciones-y-programacion-funcional)
        *   [1.3. Limitaciones de la programación estructurada sin funciones](#13-limitaciones-de-la-programacion-estructurada-sin-funciones)
        *   [1.4. Ventajas del uso de funciones en Python](#14-ventajas-del-uso-de-funciones-en-python)
    *   [2.Funciones built-in de Python](#2funciones-built-in-de-python)
        *   [2.1. Conceptos](#21-conceptos)
        *   [2.2. Visualizar las funciones](#22-visualizar-las-funciones)
        *   [2.3. Tabla de funciones built-in](#23-tabla-de-funciones-built-in)
        *   [2.4. Ejemplos de uso](#24-ejemplos-de-uso)
    *   [3.Definición de funciones](#3definicion-de-funciones)
        *   [3.1. Sintaxis básica](#31-sintaxis-basica)
        *   [3.2. Ámbito y retorno](#32-ambito-y-retorno)
        *   [3.3. Argumentos posicionales](#33-argumentos-posicionales)
        *   [3.4. Argumentos keyword](#34-argumentos-keyword)
        *   [3.5. Valores por defecto](#35-valores-por-defecto)
        *   [3.6. Argumentos opcionales](#36-argumentos-opcionales)
        *   [3.7. Lista o tupla como argumento](#37-lista-o-tupla-como-argumento)
        *   [3.8 Número de argumentos posicionales no definido (\*args)](#38-numero-de-argumentos-posicionales-no-definido-args)
        *   [3.9. Número de argumentos keyword no definido (\*\*kwargs)](#39-numero-de-argumentos-keyword-no-definido-kwargs)
        *   [3.10. Combinación de distintos tipos de argumentos](#310-combinacion-de-distintos-tipos-de-argumentos)
        *   [3.11. Documentar funciones](#311-documentar-funciones)


# Unidad 4: Funciones en Python[](#unidad-4-funciones-en-python "Permanent link")

- - -

**Índice**

```
1. Qué ventajas tiene la programación funcional
2. Funciones built-in de Python.
3. Definición de funciones.
```

- - -

## 1.Qué ventajas tiene la programación funcional[](#1que-ventajas-tiene-la-programacion-funcional "Permanent link")

### 1.1. El papel de las funciones en programación[](#11-el-papel-de-las-funciones-en-programacion "Permanent link")

En programación, una **función** es una unidad lógica que encapsula un conjunto de instrucciones con un propósito bien definido. Su objetivo principal es **abstraer comportamiento**, permitiendo que un programa se construya a partir de bloques reutilizables, comprensibles y verificables de forma independiente.

Desde un punto de vista conceptual, una función:

*   Recibe **entradas** (parámetros).
*   Ejecuta un **proceso interno**.
*   Devuelve un **resultado** (opcional).
*   Oculta los detalles de implementación al resto del programa.

Este modelo se alinea directamente con la forma en que se resuelven problemas complejos: dividiéndolos en subproblemas más simples y manejables.

### 1.2. Funciones y programación funcional[](#12-funciones-y-programacion-funcional "Permanent link")

En el paradigma de **programación funcional**, las funciones son el elemento central del diseño del programa. Aunque Python no es un lenguaje puramente funcional, **incorpora plenamente los principios fundamentales de este paradigma**, como:

*   Uso intensivo de funciones.
*   Separación clara entre datos y lógica.
*   Preferencia por funciones pequeñas, claras y específicas.
*   Minimización de efectos secundarios.

En este contexto, las funciones se entienden como **transformaciones de datos**, lo que favorece:

*   Código más predecible.
*   Menor dependencia entre partes del programa.
*   Mayor facilidad para razonar sobre el comportamiento del sistema.

### 1.3. Limitaciones de la programación estructurada sin funciones[](#13-limitaciones-de-la-programacion-estructurada-sin-funciones "Permanent link")

La **programación estructurada clásica**, cuando se basa únicamente en secuencias, condicionales y bucles dentro de un único bloque principal, presenta varios problemas a medida que el programa crece:

*   Repetición de código para realizar las mismas tareas.
*   Programas largos y difíciles de leer.
*   Dificultad para localizar errores.
*   Escasa reutilización de soluciones.
*   Dependencia excesiva del orden del código.

Sin funciones, cualquier cambio en una lógica repetida obliga a modificar múltiples fragmentos del programa, aumentando el riesgo de errores y el coste de mantenimiento.

### 1.4. Ventajas del uso de funciones en Python[](#14-ventajas-del-uso-de-funciones-en-python "Permanent link")

El uso sistemático de funciones introduce mejoras claras frente a la programación puramente estructurada:

*   **Modularidad**: Las funciones permiten dividir un programa en módulos lógicos independientes. Cada función se encarga de una tarea concreta, facilitando la organización del código.
    
*   **Reutilización del código**: Una función puede utilizarse múltiples veces sin necesidad de reescribir el mismo conjunto de instrucciones, reduciendo duplicidades.
    
*   **Legibilidad y claridad**: Un programa compuesto por funciones bien nombradas es más fácil de leer, ya que el código se aproxima al lenguaje natural y describe _qué se hace_ en lugar de _cómo se hace_ en cada punto.
    
*   **Mantenimiento y evolución**: Si una funcionalidad cambia, basta con modificar la función correspondiente. El resto del programa permanece intacto.
    
*   **Pruebas y depuración**: Las funciones pueden probarse de forma aislada, lo que facilita la detección de errores y la validación del comportamiento esperado.
    
*   **Abstracción**: El programador puede usar una función sin conocer su implementación interna, lo que permite centrarse en el diseño global del programa.
    

- - -

## 2.Funciones built-in de Python[](#2funciones-built-in-de-python "Permanent link")

### 2.1. Conceptos[](#21-conceptos "Permanent link")

Las _built-in_ son funciones incluidas en el intérprete de Python que nos permiten realizar diferentes operaciones sobre distintos tipos de datos:

*   Documentación: [funciones en python](https://docs.python.org/3/library/functions.html)
*   W3Schools: [W3Schools - funciones en python](https://www.w3schools.com/python/python_ref_functions.asp)

Las **funciones built-in** de Python son un conjunto de utilidades disponibles **sin necesidad de importar módulos**, ya que forman parte del núcleo del lenguaje. Estas funciones se encuentran accesibles a través del espacio de nombres **`builtins`** (y, de forma interna, también mediante `__builtins__`).

> En la práctica, cuando llamas a `print()`, `len()` o `type()`, estás usando **funciones built-in**.

### 2.2. Visualizar las funciones[](#22-visualizar-las-funciones "Permanent link")

Para **ver las funciones por consola** en el intérprete:

*   Ver las funciones raíz:

```
dir(__builtins__)
```

*   Ver las funciones embebidas para usar:

```
dir(__builtins__)
```

*   Ver información de la función:

```
help(función)
```

Ejemplo:

```
help(len)
```

*   Ver la documentación con **doc** :

```
print(len.__doc__)
```

*   Ver el nombre y tipo de la función:

```
print(len.__name__)
print(type(len))
```

### 2.3. Tabla de funciones built-in[](#23-tabla-de-funciones-built-in "Permanent link")

| Función | ¿Para qué sirve? | Ejemplo rápido |
| --- | --- | --- |
| `print()` | Muestra información por consola | `print("Hola")` |
| `input()` | Lee una entrada del usuario (string) | `nombre = input()` |
| `len()` | Longitud de una colección | `len([1,2,3])` |
| `type()` | Devuelve el tipo de un objeto | `type(3.14)` |
| `int()` | Convierte a entero | `int("7")` |
| `float()` | Convierte a decimal | `float("3.5")` |
| `str()` | Convierte a texto | `str(10)` |
| `bool()` | Convierte a booleano | `bool(0)` |
| `list()` | Crea/convierte a lista | `list("abc")` |
| `tuple()` | Crea/convierte a tupla | `tuple([1,2])` |
| `set()` | Crea/convierte a conjunto | `set([1,1,2])` |
| `dict()` | Crea/convierte a diccionario | `dict(a=1)` |
| `range()` | Genera secuencia de enteros | `range(5)` |
| `sum()` | Suma elementos numéricos | `sum([1,2,3])` |
| `min()` | Mínimo de una colección | `min([2,9,1])` |
| `max()` | Máximo de una colección | `max([2,9,1])` |
| `abs()` | Valor absoluto | `abs(-7)` |
| `round()` | Redondeo | `round(3.1416, 2)` |
| `pow()` | Potencia | `pow(2, 3)` |
| `divmod()` | Cociente y resto | `divmod(7, 3)` |
| `sorted()` | Ordena y devuelve nueva lista | `sorted([3,1])` |
| `reversed()` | Iterador en orden inverso | `reversed([1,2])` |
| `enumerate()` | Iterar con índice | `enumerate(["a","b"])` |
| `zip()` | Une iterables por posición | `zip([1,2],[3,4])` |
| `map()` | Aplica función a iterable | `map(f, datos)` |
| `filter()` | Filtra por condición | `filter(cond, datos)` |
| `any()` | True si alguno es True | `any([0,1,0])` |
| `all()` | True si todos son True | `all([1,1,1])` |
| `isinstance()` | Comprueba tipo (recomendado) | `isinstance(3, int)` |
| `id()` | Identificador (dirección interna) | `id(obj)` |
| `dir()` | Lista atributos de un objeto | `dir(str)` |
| `help()` | Ayuda/documentación | `help(print)` |
| `open()` | Abre ficheros | `open("a.txt")` |
| `format()` | Da formato a valores | `format(10, "04d")` |
| `chr()` | Unicode a carácter | `chr(65)` |
| `ord()` | Carácter a Unicode | `ord("A")` |
| `bin()` | Entero a binario | `bin(10)` |
| `oct()` | Entero a octal | `oct(10)` |
| `hex()` | Entero a hexadecimal | `hex(10)` |

### 2.4. Ejemplos de uso[](#24-ejemplos-de-uso "Permanent link")

*   len() – longitud de una colección

```
texto = "Python"
print(len(texto))  # 6
```

*   type() – tipo de un dato

```
x = 3.14
print(type(x))  # <class 'float'>
```

*   sum() – suma de valores numéricos

```
numeros = [10, 20, 30]
print(sum(numeros))  # 60
```

*   sorted() – ordenación (devuelve lista nueva)

```
valores = [5, 2, 9, 1]
print(sorted(valores))  # [1, 2, 5, 9]
print(valores)          # [5, 2, 9, 1] (no cambia)
```

*   range() – generación de secuencias en bucles

```
for i in range(3):
    print(i)
# 0
# 1
# 2
```

- - -

## 3.Definición de funciones[](#3definicion-de-funciones "Permanent link")

### 3.1. Sintaxis básica[](#31-sintaxis-basica "Permanent link")

#### Funciones sin devolución de valor[](#funciones-sin-devolucion-de-valor "Permanent link")

Una función puede ejecutar instrucciones sin devolver ningún resultado explícito. En ese caso, Python devuelve implícitamente el valor especial `None`.

```
def mostrar_mensaje():
    print("Hola, esto es una función sin retorno")

mostrar_mensaje()
```

Este tipo de funciones se utiliza habitualmente para mostrar información, registrar datos o realizar acciones sin producir un resultado directo.

#### Funciones con devolución de valor[](#funciones-con-devolucion-de-valor "Permanent link")

Cuando una función debe producir un resultado que será utilizado posteriormente, se emplea la instrucción `return`.

```
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)
```

**Características importantes**:

*   `return` finaliza la ejecución de la función.
*   Una función puede devolver cualquier tipo de dato.
*   El valor devuelto puede almacenarse en una variable o utilizarse directamente.

### 3.2. Ámbito y retorno[](#32-aambito-y-retorno "Permanent link")


El **ámbito** de una variable es el contexto en el que existe. Una variable nace donde se crea y desaparece cuando su ámbito termina.

En Python hay dos que importan ahora:

* **Local** — el de una función. Existe desde que se invoca hasta que termina. **No se ve desde fuera.**
* **Global** — el del programa. Todo lo que se define fuera de cualquier función, y es accesible desde cualquier punto.

### Variables locales

Las variables creadas dentro de una función **solo existen allí**:

```python
def calcular(a, b):
    media = (a + b) / 2      # `media` es local
    return media

resultado = calcular(3, 5)
print(resultado)             # 4.0
print(media)                 # NameError: name 'media' is not defined
```

Los **parámetros también son locales**: `a` y `b` no existen fuera de la función.

Esto no es una limitación, es lo que hace útiles a las funciones: se puede usar `i` o `total` dentro de una función sin miedo a pisar una variable de fuera que se llame igual.

### Leer el global desde dentro

Una función **puede leer** una variable global:

```python
IVA = 0.21

def con_iva(base):
    return base + base * IVA    # lee IVA del ámbito global

con_iva(100)                    # 121.0
```

Pero si se le **asigna** un valor, Python crea una variable local nueva y la global queda intacta:

```python
contador = 0

def incrementar():
    contador = contador + 1     # UnboundLocalError

incrementar()
```

> Existe la palabra `global` para forzar que se modifique la de fuera, pero **mejor evitarla**. Una función que cambia variables globales es imposible de probar sola y de razonar. Si hace falta devolver un valor, **se devuelve**:

> ```python
> def incrementar(contador):
>     return contador + 1
>
> contador = incrementar(contador)
> ```

### Qué pasa con lo que se pasa a una función

Aquí hay una diferencia que sorprende, y depende de si el dato es **mutable** o no.

Con los **inmutables** —números, cadenas, tuplas— la función no puede tocar el original:

```python
def incrementar(n):
    n = n + 1
    print("Dentro:", n)

numero = 5
incrementar(numero)
print("Fuera:", numero)
```

```text
Dentro: 6
Fuera: 5
```

Con los **mutables** —listas, diccionarios, conjuntos— **sí puede**:

```python
def anadir(lista):
    lista.append(4)

nums = [1, 2, 3]
anadir(nums)
print(nums)          # [1, 2, 3, 4]
```

La función no recibió una copia: recibió **la misma lista**.

> **Esto causa errores difíciles de encontrar**

> Una función que modifica la lista que recibe está cambiando algo de fuera sin que se vea en la llamada. `anadir(nums)` no insinúa que `nums` va a quedar distinta.
>
> Si no se quiere modificar el original, **se trabaja con una copia**:
>
> ```python
> def anadir(lista):
>     nueva = lista.copy()
>     nueva.append(4)
>     return nueva
> ```

> La regla que evita casi todos estos problemas: **una función recibe datos, calcula y devuelve un resultado**. Si además modifica cosas de fuera, deja de ser previsible.

### 3.2. Argumentos posicionales[](#32-argumentos-posicionales "Permanent link")

Los **argumentos posicionales** se asignan a los parámetros según el orden en el que se pasan durante la llamada a la función.

```
def dividir(a, b):
    return a / b

resultado = dividir(10, 2)
print(resultado)
```

**Observaciones**: - El orden es determinante. - Cambiar el orden puede provocar errores o resultados incorrectos.

### 3.3. Argumentos _keyword_[](#33-argumentos-keyword "Permanent link")

Los **argumentos keyword** permiten indicar explícitamente a qué parámetro corresponde cada valor.

```
def presentar(nombre, edad):
    print("Nombre:", nombre)
    print("Edad:", edad)

presentar(edad=20, nombre="Luis")
```

**Ventajas**: - El orden de los argumentos deja de ser relevante. - Mejora la legibilidad del código. - Reduce errores en funciones con muchos parámetros.

### 3.4. Valores por defecto[](#34-valores-por-defecto "Permanent link")

Un parámetro puede definirse con un **valor por defecto**, que se utilizará si el argumento correspondiente no se proporciona en la llamada.

```
def saludar(nombre, idioma="es"):
    if idioma == "es":
        print("Hola", nombre)
    else:
        print("Hello", nombre)

saludar("Ana")
saludar("Ana", "en")
```

**Regla fundamental**: - Los parámetros con valores por defecto deben situarse al final de la lista de parámetros.

### 3.5. Argumentos opcionales[](#35-argumentos-opcionales "Permanent link")

Los argumentos opcionales se implementan mediante valores por defecto y permiten que una función se invoque de distintas maneras.

```
def calcular_precio(precio, descuento=0):
    return precio - precio * descuento

print(calcular_precio(100))
print(calcular_precio(100, 0.2))
```

Este enfoque evita duplicar funciones y proporciona mayor flexibilidad.

### 3.6. Lista o tupla como argumento[](#36-lista-o-tupla-como-argumento "Permanent link")

Una función puede recibir estructuras de datos completas, como listas o tuplas, para procesar múltiples valores.

```
def mostrar_elementos(datos):
    for elemento in datos:
        print(elemento)

numeros = [1, 2, 3, 4]
mostrar_elementos(numeros)
```

**Consideraciones**: - Se pasa una referencia a la estructura. - La función puede recorrer, leer o modificar su contenido.

### 3.7 Número de argumentos posicionales no definido (`*args`)[](#37-numero-de-argumentos-posicionales-no-definido-args "Permanent link")

Cuando no se conoce de antemano cuántos argumentos posicionales se van a recibir, se utiliza `*args`.

```
def sumar_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(5, 10, 15, 20))
```

**Características**: - `args` es una tupla. - El nombre `args` es una convención; el asterisco es obligatorio.

### 3.8. Número de argumentos keyword no definido (`**kwargs`)[](#38-numero-de-argumentos-keyword-no-definido-kwargs "Permanent link")

Para aceptar un número variable de argumentos con nombre se utiliza `**kwargs`.

```
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, ":", valor)

mostrar_datos(nombre="Ana", edad=25, ciudad="Madrid")
```

**Características**: - `kwargs` es un diccionario. - Resulta muy útil para configuraciones dinámicas.



### 3.10. Combinación de distintos tipos de argumentos[](#310-combinacion-de-distintos-tipos-de-argumentos "Permanent link")

Python permite combinar diferentes tipos de argumentos siguiendo este orden:

1.  Argumentos posicionales
2.  `*args`
3.  Argumentos keyword
4.  `**kwargs`

```
def ejemplo(a, b, *args, opcion=True, **kwargs):
    print(a, b)
    print(args)
    print(opcion)
    print(kwargs)

ejemplo(1, 2, 3, 4, opcion=False, extra="dato")
```

### 3.11. Documentar funciones[](#311-documentar-funciones "Permanent link")

Una función bien hecha **debería poder usarse sin leer su interior**. Para ello hay que decir qué hace, qué recibe y qué devuelve.

### Docstrings

Un **docstring** es una cadena de texto en la **primera línea del cuerpo** de una función. No es un comentario: forma parte de la función y se puede consultar mientras el programa corre.

```python
def con_iva(base):
    """Devuelve el importe con IVA del 21 % añadido."""
    return base + base * 0.21
```

Para funciones con más miga, se escribe en varias líneas indicando parámetros y retorno:

```python
def calcular_nota(examen, practicas, asistencia=0):
    """Calcula la nota final de la asignatura.

    Parámetros:
        examen (float): nota del examen, de 0 a 10.
        practicas (float): nota de las prácticas, de 0 a 10.
        asistencia (float): puntos extra por asistencia. Por defecto 0.

    Devuelve:
        float: la nota final, con un máximo de 10.
    """
    nota = examen * 0.6 + practicas * 0.4 + asistencia
    return min(nota, 10)
```

### Para qué sirve de verdad

No es burocracia: **queda accesible desde el propio Python**.

```python
help(con_iva)
```

```text
Help on function con_iva in module __main__:

con_iva(base)
    Devuelve el importe con IVA del 21 % añadido.
```

Y también:

```python
print(con_iva.__doc__)
```

Por eso funciona `help(len)` o `help(print)`: las funciones internas también tienen docstring. El editor lo muestra al escribir la llamada.

> **Comentario y docstring no son lo mismo**
> 
> ```python
> # Esto es un comentario: explica CÓMO funciona por dentro
> """Esto es un docstring: explica QUÉ hace, para quién la usa"""
> ```
> 
> El comentario desaparece al ejecutar; el docstring se queda. Y van dirigidos a gente distinta: el comentario, a quien modifique la función; el docstring, a quien la llame.

### Anotaciones de tipo (type hinting)

Ya se vieron en la UD1 con las variables. En las funciones indican el tipo de cada parámetro y el del retorno:

```python
def con_iva(base: float) -> float:
    """Devuelve el importe con IVA del 21 % añadido."""
    return base + base * 0.21
```

La flecha `->` indica lo que devuelve.

> **Son solo descriptivas.** Si se llama `con_iva("cien")`, Python no protesta por la anotación: fallará después al intentar multiplicar. Sirven para quien lee el código y para que el editor avise, no para validar nada.

### Qué documentar

> **No hace falta un docstring de diez líneas en todas las funciones. La regla razonable:**
> 
> * **Siempre**: una línea diciendo qué hace, en cualquier función que no sea evidente por el nombre.
> * **Además, los parámetros y el retorno** cuando hay más de un parámetro, o cuando el significado no se adivina.
> * **Comentarios dentro** solo donde el *cómo* no se entienda solo. Un comentario que repite lo que ya dice el código es ruido que además envejece mal.


[⬆ Ir arriba](#top)
