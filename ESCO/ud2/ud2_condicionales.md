# UD02-Condicionales
<div id="top"></div>

## Índice de contenidos

- [UD02-Condicionales](#ud02-condicionales)
  - [Índice de contenidos](#índice-de-contenidos)
- [Unidad 2 - Sentencias condicionales en Python](#unidad-2---sentencias-condicionales-en-python)
  - [Índice](#índice)
  - [1) Tipos de sentencias condicionales en Python](#1-tipos-de-sentencias-condicionales-en-python)
    - [1.1. Estructura condicional simple: `if`](#11-estructura-condicional-simple-if)
      - [Descripción](#descripción)
      - [Características](#características)
      - [Uso adecuado](#uso-adecuado)
      - [Ejemplos de uso típico](#ejemplos-de-uso-típico)
    - [1.2. Estructura condicional doble: `if – else`](#12-estructura-condicional-doble-if--else)
      - [Descripción](#descripción-1)
      - [Características](#características-1)
      - [Uso adecuado](#uso-adecuado-1)
    - [Ejemplos de uso típico](#ejemplos-de-uso-típico-1)
    - [1.3. Estructura condicional múltiple: `if – elif – else`](#13-estructura-condicional-múltiple-if--elif--else)
      - [Descripción](#descripción-2)
      - [Características](#características-2)
      - [Uso adecuado](#uso-adecuado-2)
      - [Ejemplos de uso típico](#ejemplos-de-uso-típico-2)
    - [1.4. Estructuras condicionales anidadas](#14-estructuras-condicionales-anidadas)
      - [Descripción](#descripción-3)
      - [Características](#características-3)
      - [Uso adecuado](#uso-adecuado-3)
      - [Recomendaciones](#recomendaciones)
    - [1.5. Expresiones condicionales (operador ternario)](#15-expresiones-condicionales-operador-ternario)
      - [Descripción](#descripción-4)
      - [Características](#características-4)
      - [Uso adecuado](#uso-adecuado-4)
      - [Uso no recomendado](#uso-no-recomendado)
    - [1.6. Estructura de selección múltiple: `match – case` (Python 3.10+)](#16-estructura-de-selección-múltiple-match--case-python-310)
      - [Descripción](#descripción-5)
      - [Características](#características-5)
      - [Uso adecuado](#uso-adecuado-5)
      - [Ventajas frente a `if – elif`](#ventajas-frente-a-if--elif)
    - [1.7. Comparación general de las estructuras condicionales](#17-comparación-general-de-las-estructuras-condicionales)
    - [1.8. Buenas prácticas en el uso de condicionales](#18-buenas-prácticas-en-el-uso-de-condicionales)
  - [2) Condiciones](#2-condiciones)
    - [2.1. Lógica en tests](#21-lógica-en-tests)
    - [Tabla resumen](#tabla-resumen)
    - [Tabla de operadores lógicos](#tabla-de-operadores-lógicos)
    - [2.2. Pertenecia e identidad](#22-pertenecia-e-identidad)
      - [Pertenencia](#pertenencia)
      - [Identidad](#identidad)
    - [2.3. Comprobar el tipo de un objeto](#23-comprobar-el-tipo-de-un-objeto)
    - [2.4. Valores Truthy/Falsy](#24-valores-truthyfalsy)
    - [2.5. Evaluación por cortocircuito](#25-evaluación-por-cortocircuito)
  - [3) Estructura conidiconal `if` en Python](#3-estructura-conidiconal-if-en-python)
    - [3.1. Simple](#31-simple)
    - [3.2. If-else](#32-if-else)
    - [3.3. If-elif-else](#33-if-elif-else)
    - [3.4. If-elif-elif](#34-if-elif-elif)
    - [3.5. Operador ternario](#35-operador-ternario)
    - [3.6. Anidado](#36-anidado)
    - [3.7. Comparaciones en listas](#37-comparaciones-en-listas)
  - [4) Estructura de selección `match` en Python](#4-estructura-de-selección-match-en-python)
    - [4.1.  Resumen rápido de variantes](#41--resumen-rápido-de-variantes)
    - [4.2. Sintaxis básica](#42-sintaxis-básica)
    - [4.3. Tuplas](#43-tuplas)
    - [4.4. Listas](#44-listas)
    - [4.5. Diccionarios](#45-diccionarios)
    - [4.6. Objetos](#46-objetos)
    - [4.7. Condicionales](#47-condicionales)

# Unidad 2 - Sentencias condicionales en Python[](#unidad-2-sentencias-condicionales-en-python "Permanent link")

- - -

## Índice[](#indice "Permanent link")

```
1. Tipos de sentencias condicionales en Python.
2. Condiciones.
3. Estructura condicional `if`.
4. Estructura de selección `match`.
```

- - -

## 1) Tipos de sentencias condicionales en Python[](#1-tipos-de-sentencias-condicionales-en-python "Permanent link")

Las **estructuras condicionales** permiten que un programa tome decisiones y ejecute distintos bloques de instrucciones en función de si se cumple o no una condición. En Python, estas estructuras se basan en la evaluación de **expresiones lógicas** que devuelven valores booleanos (`True` o `False`).

A continuación se describen **todas las estructuras condicionales disponibles en Python**, junto con sus **usos adecuados** y recomendaciones prácticas.

### 1.1. Estructura condicional simple: `if`[](#11-estructura-condicional-simple-if "Permanent link")

#### Descripción[](#descripcion "Permanent link")

La estructura `if` permite ejecutar un bloque de instrucciones **únicamente cuando una condición es verdadera**.

#### Características[](#caracteristicas "Permanent link")

*   Evalúa una sola condición.
*   Si la condición es falsa, no se ejecuta ninguna acción alternativa.
*   Es la forma más básica de toma de decisiones.

#### Uso adecuado[](#uso-adecuado "Permanent link")

*   Validaciones simples.
*   Comprobaciones puntuales (por ejemplo, verificar si un valor cumple una condición mínima).
*   Casos en los que **no es necesario actuar si la condición no se cumple**.

#### Ejemplos de uso típico[](#ejemplos-de-uso-tipico "Permanent link")

*   Comprobar si un número es positivo.
*   Verificar si un usuario tiene permisos.
*   Validar que un dato no sea nulo o vacío.

### 1.2. Estructura condicional doble: `if – else`[](#12-estructura-condicional-doble-if-else "Permanent link")

#### Descripción[](#descripcion_1 "Permanent link")

La estructura `if – else` permite elegir entre **dos caminos excluyentes**:  
uno cuando la condición es verdadera y otro cuando es falsa.

#### Características[](#caracteristicas_1 "Permanent link")

*   Siempre se ejecuta uno de los dos bloques.
*   Aporta claridad cuando existen dos alternativas claras.

#### Uso adecuado[](#uso-adecuado_1 "Permanent link")

*   Decisiones binarias (sí / no).
*   Casos en los que **siempre debe ejecutarse una acción**, independientemente del resultado de la condición.

### Ejemplos de uso típico[](#ejemplos-de-uso-tipico_1 "Permanent link")

*   Aprobado o suspenso.
*   Mayor de edad o menor de edad.
*   Acceso permitido o denegado.

### 1.3. Estructura condicional múltiple: `if – elif – else`[](#13-estructura-condicional-multiple-if-elif-else "Permanent link")

#### Descripción[](#descripcion_2 "Permanent link")

Esta estructura permite evaluar **varias condiciones de forma secuencial**, ejecutando el bloque correspondiente a la **primera condición que sea verdadera**.

#### Características[](#caracteristicas_2 "Permanent link")

*   Las condiciones se evalúan en orden.
*   Solo se ejecuta un bloque.
*   El bloque `else` es opcional y actúa como caso por defecto.

#### Uso adecuado[](#uso-adecuado_2 "Permanent link")

*   Clasificación de valores en rangos.
*   Menús simples basados en opciones numéricas o textuales.
*   Situaciones con **pocas alternativas claramente diferenciadas**.

#### Ejemplos de uso típico[](#ejemplos-de-uso-tipico_2 "Permanent link")

*   Calificaciones (suspenso, aprobado, notable, sobresaliente).
*   Tarifas según edad.
*   Estados de un proceso (iniciado, en curso, finalizado).

### 1.4. Estructuras condicionales anidadas[](#14-estructuras-condicionales-anidadas "Permanent link")

#### Descripción[](#descripcion_3 "Permanent link")

Consisten en **colocar una estructura condicional dentro de otra**, permitiendo decisiones más complejas y jerárquicas.

#### Características[](#caracteristicas_3 "Permanent link")

*   Permiten modelar lógica compleja.
*   Pueden reducir la legibilidad si se abusa de ellas.
*   Requieren especial cuidado con la indentación.

#### Uso adecuado[](#uso-adecuado_3 "Permanent link")

*   Cuando una decisión depende del resultado de otra previa.
*   Validaciones en varios niveles (por ejemplo, comprobar primero si un dato existe y después su valor).

#### Recomendaciones[](#recomendaciones "Permanent link")

*   Evitar niveles de anidación excesivos.
*   Considerar alternativas como `elif` o `match` si la lógica lo permite.

### 1.5. Expresiones condicionales (operador ternario)[](#15-expresiones-condicionales-operador-ternario "Permanent link")

#### Descripción[](#descripcion_4 "Permanent link")

Python permite escribir una condición en **una sola línea**, devolviendo un valor u otro según el resultado de la condición.

#### Características[](#caracteristicas_4 "Permanent link")

*   Sintaxis compacta.
*   Devuelve un valor, no un bloque de instrucciones.
*   Mejora la concisión, pero puede afectar a la legibilidad.

#### Uso adecuado[](#uso-adecuado_4 "Permanent link")

*   Asignaciones simples basadas en una condición.
*   Casos muy claros y cortos.

#### Uso no recomendado[](#uso-no-recomendado "Permanent link")

*   Condiciones complejas.
*   Lógica difícil de interpretar en una sola línea.

### 1.6. Estructura de selección múltiple: `match – case` (Python 3.10+)[](#16-estructura-de-seleccion-multiple-match-case-python-310 "Permanent link")

#### Descripción[](#descripcion_5 "Permanent link")

La estructura `match` permite comparar un valor con **distintos patrones**, ejecutando el bloque asociado al primer patrón que coincida.

#### Características[](#caracteristicas_5 "Permanent link")

*   Similar a `switch` en otros lenguajes.
*   Más clara y legible que múltiples `elif` en ciertos casos.
*   Soporta patrones avanzados, no solo valores simples.

#### Uso adecuado[](#uso-adecuado_5 "Permanent link")

*   Menús de opciones.
*   Evaluación de estados o códigos.
*   Comparaciones claras contra valores constantes.

#### Ventajas frente a `if – elif`[](#ventajas-frente-a-if-elif "Permanent link")

*   Mayor legibilidad cuando hay muchas alternativas.
*   Código más estructurado y mantenible.
*   Especialmente útil en programas con múltiples casos bien definidos.

### 1.7. Comparación general de las estructuras condicionales[](#17-comparacion-general-de-las-estructuras-condicionales "Permanent link")

| Estructura | Nº de condiciones | Uso principal |
| --- | --- | --- |
| `if` | 1   | Validación simple |
| `if – else` | 1   | Decisión binaria |
| `if – elif – else` | Varias | Clasificación o alternativas múltiples |
| Condicional anidada | Varias | Decisiones jerárquicas complejas |
| Ternario | 1   | Asignaciones simples |
| `match – case` | Muchas | Selección múltiple clara y estructurada |

### 1.8. Buenas prácticas en el uso de condicionales[](#18-buenas-practicas-en-el-uso-de-condicionales "Permanent link")

*   Priorizar **claridad y legibilidad** frente a código compacto.
*   Evitar anidaciones profundas.
*   Usar `match` cuando haya muchas alternativas basadas en un mismo valor.
*   Mantener condiciones simples y expresivas.
*   Documentar decisiones complejas mediante comentarios.

- - -

## 2) Condiciones[](#2-condiciones "Permanent link")

Cuando se aplican a estructuras de control, los tests tienen como objetivo:

```
- Validar todas las ramas de decisión.
- Comprobar condiciones verdaderas y falsas.
- Verificar entradas normales y entradas límite.
- Detectar bucles infinitos o ejecuciones incorrectas.
```

En esencia, los tests garantizan que el flujo del programa es correcto.

### 2.1. Lógica en tests[](#21-logica-en-tests "Permanent link")

###  Tabla resumen[](#tabla-resumen "Permanent link")

| Tipo de test | Operadores / Funciones | Ejemplo |
| --- | --- | --- |
| Comparación | `==`, `!=`, `<`, `>`, `<=`, `>=` | `x > 10` |
| Encadenada | `a < b < c` | `0 < x < 5` |
| Lógicos | `and`, `or`, `not` | `x > 0 and par(x)` |
| Pertenencia | `in`, `not in` | `"a" in texto` |
| Identidad | `is`, `is not` | `x is None` |
| Truthiness / Falsiness | valores `True` / `False` | `if lista:` |
| Tipo | `isinstance()` | `isinstance(x, str)` |

###  Tabla de operadores lógicos[](#tabla-de-operadores-logicos "Permanent link")

| Operador | Descripción | Ejemplo |
| --- | --- | --- |
| `and` | Devuelve verdadero si ambas expresiones son verdaderas | `x < 5 and x < 10` |
| `or` | Devuelve verdadero si al menos una expresión es verdadera | `x < 5 or x < 4` |
| `not` | Invierte el resultado de la expresión lógica | `not (x < 5 and x < 10)` |

### 2.2. Pertenecia e identidad[](#22-pertenecia-e-identidad "Permanent link")

#### Pertenencia[](#pertenencia "Permanent link")

Se usan para comprobar si un elemento está dentro de una secuencia (cadena, lista, tupla, diccionario, etc.):

```
if "a" in "hola":
    print("La 'a' está")

if item not in lista:
    print("No encontrado")
```

#### Identidad[](#identidad "Permanent link")

Comprueban si dos nombres se refieren al mismo objeto en memoria:

```
# Ejemplo 1:
if variable is None:
    print("Está vacío")

# Ejemplo 2:
if x is not y:
    print("Son objetos distintos")
```

### 2.3. Comprobar el tipo de un objeto[](#23-comprobar-el-tipo-de-un-objeto "Permanent link")

*   Comprobando el tipo de un valor:

```
if isinstance(valor, int):
    print("Es un entero")
```

*   Comprobando vaarios tipos a la vez:

```
if isinstance(x, (int, float)):
    print("Es numérico")
```

### 2.4. Valores Truthy/Falsy[](#24-valores-truthyfalsy "Permanent link")

Python considera algunos valores como **falsos (`False`) de forma implícita**:

*   `0`, `0.0`
*   `""` (cadena vacía)
*   `[]` (lista vacía)
*   `{}` (diccionario vacío)
*   `set()` (conjunto vacío)
*   `None`
*   `False`

Cualquier otro valor se considera **truthy** (verdadero).

Ejemplo típico:

```
if lista:
    print("La lista NO está vacía")
else:
    print("Lista vacía")
```

### 2.5. Evaluación por cortocircuito[](#25-evaluacion-por-cortocircuito "Permanent link")

Python no evalúa la segunda parte de una condición si la primera ya determina el resultado:

```
if lista and lista[0] == 5:
    print("La lista empieza por 5")
```

Si lista está vacía, no se evalúa lista\[0\] y se evita un IndexError.

- - -

## 3) Estructura conidiconal `if` en Python[](#3-estructura-conidiconal-if-en-python "Permanent link")

### 3.1. Simple[](#31-simple "Permanent link")

**Estructura**:

`````
if valor1 == valor2:
    acción
````

**Ejemplo**:

```python
# Definimos una variable numérica
numero = 5

# Estructura condicional simple
# Solo se ejecuta el bloque si la condición es verdadera
if numero > 0:
    print("El número es positivo")
`````

### 3.2. If-else[](#32-if-else "Permanent link")

**Estructura**:

```
if valor1 == valor2:
    acción1
else:
    acción2
```

**Ejemplo**:

```
# Definimos un número entero
numero = 8

# Estructura condicional doble
# Se evalúa si el número es divisible entre 2
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
```

### 3.3. If-elif-else[](#33-if-elif-else "Permanent link")

**Sintaxis**:

```
if valor1 == valor2:
    acción1
elif test:
    acción2
else:
    acción3
```

### 3.4. If-elif-elif[](#34-if-elif-elif "Permanent link")

```
if valor1 == valor2:
    acción1
elif test:
    acción2
elif test:
    acción3
```

### 3.5. Operador ternario[](#35-operador-ternario "Permanent link")

**Sintaxis**:

```
acción1 if valor1 == valor2 else acción2
```

**Ejemplo 1**: comprobando si un número es negativo.

```
# Definimos un número entero
numero = -3

# Operador ternario:
# Si numero es mayor o igual que 0, el resultado será "Positivo"
# En caso contrario, el resultado será "Negativo"
resultado = "Positivo" if numero >= 0 else "Negativo"

print(resultado)
```

**Ejemplo 2**: Comprobar nota.

```
# Definimos una nota que puede venir de una entrada externa
nota = 8.5

# Operador ternario avanzado con validación incluida:
# 1. Primero se comprueba si la nota está fuera del rango válido (0 a 10)
# 2. Si es válida, se clasifica como "Aprobado" o "Suspenso"
# 3. Todo se resuelve en una única expresión condicional
resultado = (
    "Nota no válida" if nota < 0 or nota > 10
    else "Aprobado" if nota >= 5
    else "Suspenso"
)

print(resultado)
```

### 3.6. Anidado[](#36-anidado "Permanent link")

```
# Definimos la nota de un alumno
nota = 6.5

# Primer nivel de decisión:
# Comprobamos si la nota está dentro del rango válido
if 0 <= nota <= 10:

    # Segundo nivel de decisión (if anidado):
    # Solo se evalúa si la nota es válida
    if nota >= 5:
        print("Asignatura aprobada")
    else:
        # Condición por defecto del if interno
        # Se ejecuta si la nota es menor que 5
        print("Asignatura suspendida")

else:
    # Condición por defecto del if externo
    # Se ejecuta cuando la nota no está en el rango válido
    print("Nota no válida")
```

### 3.7. Comparaciones en listas[](#37-comparaciones-en-listas "Permanent link")

*   Se distingue entre mayúsculas y minúsculas.
*   Para ignorar mayúsculas → pasamos las cadenas a minúsculas en la comparación.
*   **Múltiples condiciones:**
*   `and`
*   `or`
    
*   **Comprobar si un elemento está en una lista:**
    

`````
if valor in lista:
    acción1
else:
    acción2
````

- **Comprobar si un elemento NO está en una lista:**

```python
if valor not in lista:
    acción1
else:
    acción2
`````

- - -

## 4) Estructura de selección `match` en Python[](#4-estructura-de-seleccion-match-en-python "Permanent link")

### 4.1.  Resumen rápido de variantes[](#41-resumen-rapido-de-variantes "Permanent link")

| Variante | Descripción | Ejemplo breve |
| --- | --- | --- |
| Valor literal | Coincide con un valor exacto | `case 10:` |
| Alternativas | Varios valores posibles | `case "a" \| "b":` |
| Variable de captura | Asigna el valor a una variable | `case x:` |
| Estructura | Coincidencia con listas, tuplas, dicts, objetos | `case [a, b, c]:` |
| Comodín | Caso por defecto | `case _:` |
| Guarda | Añade condición lógica | `case n if n > 0:` |

### 4.2. Sintaxis básica[](#42-sintaxis-basica "Permanent link")

**Estructura:**

```
match variable:
    case patron1:
        # acciones si coincide con patrón1
        pass

    case patron2:
        # acciones si coincide con patrón2
        pass

    case _:
        # caso por defecto (equivalente a 'default' en switch)
        pass
```

**Ejemplo**:

```
dia = 3

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case _:
        print("Día no válido")
```

### 4.3. Tuplas[](#43-tuplas "Permanent link")

```
coordenada = (0, 5)

match coordenada:
    case (0, y):
        print(f"Está sobre el eje Y en {y}")
    case (x, 0):
        print(f"Está sobre el eje X en {x}")
    case (x, y):
        print(f"Punto general ({x}, {y})")
```

### 4.4. Listas[](#44-listas "Permanent link")

**Ejemplo 1**:

```
valores = [10, 20]

match valores:
    case [a, b]:
        print(f"La lista tiene dos elementos: {a} y {b}")
    case [a]:
        print(f"La lista tiene un solo elemento: {a}")
    case []:
        print("La lista está vacía")
    case _:
        print("La lista tiene más de dos elementos")
```

**Ejemplo 2**:

```
datos = [1, 2, 3]

match datos:
    case [a, b, c]:
        print(f"Tres elementos: {a}, {b}, {c}")
    case [a, b]:
        print(f"Dos elementos: {a}, {b}")
    case [a, *resto]:
        print(f"Empieza con {a} y el resto es {resto}")
```

**Atención**:

*   El operador \* se utiliza para capturar el resto de los elementos de una secuencia.
*   Su funcionamiento es equivalente al uso de \*args en funciones.
*   Este tipo de patrones es especialmente útil para trabajar con listas de longitud variable.

### 4.5. Diccionarios[](#45-diccionarios "Permanent link")

```
# Creamos un diccionario con información de una persona
persona = {"nombre": "Luis", "edad": 17}

# Utilizamos match para analizar la estructura del diccionario
match persona:
    # Caso 1: el diccionario tiene las claves "nombre" y "edad"
    case {"nombre": nombre, "edad": edad}:
        print(f"{nombre} tiene {edad} años")

    # Caso 2: el diccionario solo tiene la clave "nombre"
    case {"nombre": nombre}:
        print(f"Persona llamada {nombre}")

    # Caso 3: cualquier otro diccionario distinto
    case _:
        print("Información de persona no válida")
```

**Atención**:

*   No se compara el diccionario completo, sino su estructura y claves.
*   El orden de las claves no importa.
*   Cada case captura los valores y los guarda en variables.
*   case \_ garantiza que siempre habrá una salida.

### 4.6. Objetos[](#46-objetos "Permanent link")

```
# Definimos una clase llamada Punto
# Representa un punto en un plano cartesiano (x, y)
class Punto:
    def __init__(self, x, y):
        # Atributo que almacena la coordenada X
        self.x = x
        # Atributo que almacena la coordenada Y
        self.y = y

# Creamos un objeto de la clase Punto
p = Punto(3, 4)

# Utilizamos match para analizar la estructura del objeto
match p:
    # Caso 1: el punto está sobre el eje Y (x vale 0)
    case Punto(x=0, y=y):
        print(f"Sobre eje Y en {y}")

    # Caso 2: cualquier otro punto con coordenadas (x, y)
    case Punto(x=x, y=y):
        print(f"Punto en ({x}, {y})")
```

### 4.7. Condicionales[](#47-condicionales "Permanent link")

```
# Definimos una variable numérica
numero = 7

# Utilizamos match para evaluar el valor del número
match numero:
    # Caso 1: el número es menor que 0
    case n if n < 0:
        print("Negativo")

    # Caso 2: el número es exactamente 0
    case n if n == 0:
        print("Cero")

    # Caso 3: el número es mayor que 0
    case n if n > 0:
        print("Positivo")
```

**Atención**:

*   En este ejemplo, match se combina con condiciones (if), llamadas guards.
*   La variable n captura el valor de numero.
*   Cada case solo se ejecuta si:
    *   El patrón coincide, y
    *   La condición del if se cumple.
*   Este uso permite expresar decisiones de forma más clara que con múltiples if / elif.

[⬆ Ir arriba](#top)
