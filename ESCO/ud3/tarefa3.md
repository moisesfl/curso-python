# Ejercicio Final – UD03

## Índice de contenidos

- [Ejercicio Final – UD03](#ejercicio-final--ud03)
  - [Índice de contenidos](#índice-de-contenidos)
  - [Contexto general](#contexto-general)
  - [Datos de partida](#datos-de-partida)
  - [Requisitos funcionales (QUÉ debe hacer el programa)](#requisitos-funcionales-qué-debe-hacer-el-programa)
    - [1. Menú Principal de Gestión (`while`)](#1-menú-principal-de-gestión-while)
    - [2. Eliminación Segura (Búsqueda manual + `remove`)](#2-eliminación-segura-búsqueda-manual--remove)
    - [3. Adición de nuevos elementos (`append`)](#3-adición-de-nuevos-elementos-append)
    - [4. Ejecución Auditoría](#4-ejecución-auditoría)
      - [4.1. Filtrado y Control de Flujo (`continue` / `break`)](#41-filtrado-y-control-de-flujo-continue--break)
      - [4.2. Procesamiento de Precios Históricos (`enumerate`)](#42-procesamiento-de-precios-históricos-enumerate)
      - [4.3. Validación de Stock (Bucle `while`)](#43-validación-de-stock-bucle-while)
      - [4.4. Clasificación y Alertas (Operador Ternario)](#44-clasificación-y-alertas-operador-ternario)
    - [5. Resumen Final](#5-resumen-final)
  - [Requisitos técnicos (CÓMO debe hacerse)](#requisitos-técnicos-cómo-debe-hacerse)
  - [Entrega](#entrega)
## Contexto general 

A lo largo de esta tarea vas a desarrollar un programa que simule el proceso de auditoría de una tienda. Para ello te propongo que te imagines que estás creando una pequeña aplicación de gestión de inventario como las que se utilizan para controlar el stock de los productos.

El programa comenzará con un menú principal, desde donde el usuario interactúa con el sistema. Este menú ofrecerá cuatro opciones diferentes: añadir un artículo al inventario, lo que permitirá añadir un producto nuevo al inventario o aumentar su stock, eliminar un artículo existente, de modo que deje de existir en el inventario si, por ejemplo, caduca todo el stock y deja de venderse, ejecutar el proceso de auditoría del inventario, donde comprobará el estado en general de todo el inventario, y la opción salir de la aplicación, donde el programa terminará de ejecutarse mostrando por pantalla el listado de productos en stock y el valor total de los mismos.

Dentro del proceso de ejecución de auditoría, el sistema deberá analizar el inventario, procesando el listado de productos almacenado, comprobando si cada uno de ellos dispone de suficiente stock y detectando posibles registros incorrectos o corruptos que serán filtrados.

##  Datos de partida

Copia este bloque al inicio:

```python
inventario = [
    {"nombre": "Teclado", "precios": [20.5, 25.0, 18.0], "stock": 15},
    {"nombre": "Ratón", "precios": [10.0, 12.5], "stock": 0},
    {"nombre": "ERROR_LOG", "precios": [], "stock": -1},
    {"nombre": "Monitor", "precios": [150.0, 145.0, 160.0], "stock": 8},
    {"nombre": "Alfombrilla", "precios": [5.0], "stock": 20}
]

umbral_stock_bajo = 5
```

- Puedes añadir y eliminar los elementos que quieras al inventario para hacer pruebas sobre el programa.

##  Requisitos funcionales (QUÉ debe hacer el programa)

### 1. Menú Principal de Gestión (`while`)

El programa debe empezar mostrando un menú con 4 opciones:

1. Añadir producto (pide nombre, stock y un precio inicial).
2. Eliminar producto (pide el nombre y lo borra de la lista).
3. Ejecutar Auditoría (ejecuta todo el proceso de cálculo).
4. Salir.

### 2. Eliminación Segura (Búsqueda manual + `remove`)

Cuando el usuario quiera eliminar un producto (por ejemplo, porque está caducado):

- Primero debes buscarlo en la lista.
- Si lo encuentras, lo eliminas y muestras:

  > "Producto [nombre] eliminado correctamente."

- Si no lo encuentras tras recorrer la lista, muestra:

  > "Error: El producto no existe."

### 3. Adición de nuevos elementos (`append`)

Al añadir un producto, debes crear un diccionario nuevo con la estructura correcta:

```python
{"nombre": n, "precios": [p], "stock": s}
```

y añadirlo a la lista `inventario`.

Para los pasos 1, 2 y 3 recuerda los ejercicios hechos en el segundo y tercer tema, por ejemplo, el ejercicio de la lista de la compra.

### 4. Ejecución Auditoría

#### 4.1. Filtrado y Control de Flujo (`continue` / `break`)

- Recorre la lista `inventario` con un bucle `for`.
- Si el nombre del producto es `"ERROR_LOG"`, muestra:

  > "Saltando registro corrupto..."

  y usa `continue`.
- Si el nombre es `"STOP"`, usa `break` (puedes añadir un artículo con este nombre al final de la lista para probar la parada).

#### 4.2. Procesamiento de Precios Históricos (`enumerate`)

- Para cada producto válido, recorre su lista de precios.
- Usa `enumerate` para mostrar:

  > "Analizando precio [índice] del producto [nombre]: [valor]€".

- Calcula el precio medio de cada producto sumando sus precios y dividiendo por la cantidad de elementos.

#### 4.3. Validación de Stock (Bucle `while`)

Durante la auditoría el stock debe ser comprobado para cada producto de modo que:

- Si el stock es exactamente `0`, usa un bucle `while` para preguntar al usuario:

  > "¿Se han recibido unidades de [nombre]? (si/no)"

  - Si dice `"si"`, pide la cantidad (un número entero) y actualiza el stock.
  - Si dice `"no"`, el stock se queda en `0` y el bucle termina.
- En caso contrario continúa con el siguiente elemento del inventario.

#### 4.4. Clasificación y Alertas (Operador Ternario)

Después de validar el stock, el programa debe clasificar el estado de cada producto. Para ello:

- Crea una variable `estado_stock`.
- Usa un operador ternario para que valga `"Crítico"` si el stock es menor que `umbral_stock_bajo`, o `"Normal"` en caso contrario.

### 5. Resumen Final

Al final del programa, muestra por pantalla:

- El valor total del inventario (suma de: `precio_medio * stock` de cada producto).
- Una lista simple con los nombres de los productos que han quedado en estado `"Crítico"`.

##  Requisitos técnicos (CÓMO debe hacerse)

- Uso obligatorio de los bucles y comprehensions vistos a lo largo del tema 3, así como las estructuras vistas en temas anteriores. (No hay que forzar que haya un ejemplo de cada comprehension, simplemente es utilizarlas y mostrar que se saben utilizar).
- Aplicar correctamente:
  - El sangrado.
  - El control del flujo de ejecución.
  - La gestión de variables.
- No usar funciones (todo en un único bloque principal).
- El código debe ser legible, ordenado y comentado.

## Entrega[](#entrega "Permanent link")

- La entrega de esta tarea consistirá en un fichero .py (`apellido1_apellido2_nombre_EC_T03.py`) con el código del programa, qué deberá llevar comentarios explicativos de cada bloque. 
