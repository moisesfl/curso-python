# UD3 – Tratamiento de ficheros con Python

## Índice

1.  Conceptos.
2.  Apertura y lectura de ficheros.
3.  Escritura, punteros y control de flujo.
4.  Ficheros JSON.
5.  Gestión de errores con ficheros. Logging.

# 1️. Conceptos

*   **Tipos de rutas**:
    
    *   **Absolutas**: indican la localización completa del archivo desde la raíz del sistema de archivos. No dependen del directorio de trabajo actual.  
        Ejemplo: `/home/usuario/documentos/datos.txt` o `C:\\Users\\usuario\\datos.txt`.
    *   **Relativas**: se definen respecto al directorio de trabajo actual del programa.  
        Ejemplo: `datos/alumnos.txt` o `../config/config.json`.
*   **Manejo de rutas**: se utiliza el módulo `pathlib`, que proporciona la clase `Path` para manipular rutas de forma más segura, legible y multiplataforma.  
    Permite operaciones como: comprobar existencia (`Path.exists()`), crear carpetas (`Path.mkdir()`), cambiar nombres (`Path.rename()`), o concatenar rutas mediante el operador `/`.
    
*   **Modos de apertura**:
    
    *   `"r"` → **Solo lectura**. Lanza error si el archivo no existe.
    *   `"w"` → **Solo escritura**. Crea el archivo si no existe o sobrescribe su contenido si ya existe.
    *   `"a"` → **Añadir (append)**. Abre el archivo y sitúa el puntero al final; si no existe, lo crea.
    *   `"x"` → **Creación exclusiva**. Crea un archivo nuevo y genera error si ya existe.
    *   `"b"` → **Modo binario**. Se utiliza junto con los anteriores (`"rb"`, `"wb"`, etc.) para leer o escribir datos binarios (imágenes, audio, etc.).
    *   `encoding` → Define la codificación del texto. Por defecto suele ser `"utf-8"`, y debe especificarse para evitar errores con caracteres especiales.
*   **Uso de `with` (context manager)**:  
    Se utiliza el bloque `with open(...) as f:` para **abrir el fichero de forma segura**, garantizando su cierre automático incluso si ocurre un error durante la ejecución.  
    Evita tener que llamar manualmente a `f.close()` y mejora la gestión de recursos.
    
*   **Métodos de lectura**:
    
    *   `.read()` → Lee **todo el contenido del fichero** y lo devuelve como una cadena.  
        Ideal para archivos pequeños o cuando se necesita el contenido completo de una vez.
        
    *   `.readline()` → Lee **una única línea** del fichero, manteniendo el puntero en la siguiente posición.  
        Útil para procesar línea a línea de forma controlada.
        
    *   `.readlines()` → Devuelve **una lista de todas las líneas** del fichero.  
        No recomendable para archivos muy grandes, ya que carga todo en memoria.
        
    *   **Iteración línea a línea** → Permite recorrer el archivo de forma eficiente:  
        Esta forma es **la más eficiente y recomendada** para leer archivos de texto grandes.
        
        ```python
        with open("datos.txt", "r", encoding="utf-8") as f:
            for linea in f:
                print(linea.strip())
        ```
        

## Propiedades y métodos del objeto `File`

El objeto `File`, obtenido al abrir un fichero mediante la función `open()` o el método `Path.open()`, dispone de diversas **propiedades y métodos** que permiten conocer su estado y comportamiento durante la lectura o escritura.

A continuación se describen las más importantes:

### Propiedades básicas

*   **`f.name`** → Devuelve el **nombre y ruta** del archivo asociado al objeto.  
    Ejemplo: `print(f.name)` puede devolver `"datos/alumnos.txt"`.
    
*   **`f.mode`** → Indica el **modo de apertura** del fichero (`"r"`, `"w"`, `"a"`, `"rb"`, etc.).  
    Útil para comprobar si el archivo fue abierto en modo lectura, escritura o binario.
    
*   **`f.closed`** → Es un valor booleano (`True` o `False`) que indica si el archivo **ya ha sido cerrado**.  
    Puede consultarse tras el bloque `with` o después de ejecutar `f.close()`.
    
*   **`f.encoding`** → Muestra la **codificación de caracteres** utilizada al leer o escribir el archivo (por ejemplo, `"UTF-8"`).  
    Permite verificar que la codificación sea la esperada, especialmente en sistemas con configuraciones locales distintas.
    

### Métodos de comprobación de capacidades

*   **`f.readable()`** → Devuelve `True` si el archivo **permite lectura**, es decir, si fue abierto en modo `"r"` o similar.  
    Útil para condicionar operaciones según la capacidad del archivo.
    
*   **`f.writable()`** → Devuelve `True` si el archivo **permite escritura**, como ocurre en los modos `"w"`, `"a"`, `"x"`, o `"r+"`.  
    Permite validar si se puede escribir antes de llamar a `.write()`.
    
*   **`f.seekable()`** → Devuelve `True` si el archivo **permite mover el puntero** mediante el método `.seek()`.  
    Los archivos de texto suelen ser _seekable_, pero algunos flujos (por ejemplo, sockets o pipes) no lo son.
    

- - -

# 2️ – Apertura y lectura de ficheros de texto

*   Un **fichero de texto** almacena en memoria persistente información codificada en caracteres legibles (por ejemplo, UTF-8).
*   Al abrirlo, Python crea en la memoria RAM un **objeto `File`**, que representa el flujo de datos entre el programa y el archivo físico.
*   Este objeto permite leer, escribir y consultar información del fichero, así como conocer su estado.

## Sintaxis básica de apertura

```python
with open("ruta/al/archivo.txt", mode="r", encoding="utf-8") as f:
    # Operaciones de lectura o escritura
    contenido = f.read()
```

* El bloque `with` garantiza el cierre automático del fichero, incluso si ocurre un error.

* El parámetro `mode` indica el modo de apertura (`"r"`, `"w"`, `"a"`, etc.).

* El parámetro `encoding` define la codificación del texto, habitualmente `"utf-8"`.

Es recomendable utilizar **`pathlib.Path`** para manejar rutas de forma más clara y portable:

```python
from pathlib import Path

ruta = Path("datos/alumnos.txt")
with ruta.open("r", encoding="utf-8") as f:
    contenido = f.read()
```

## Ejemplo 1 – Inspección de propiedades del objeto `File`

El siguiente ejemplo muestra cómo acceder a las **propiedades y métodos** más importantes del objeto `File`:

```python
from pathlib import Path

ruta = Path("datos/alumnos.txt")

with ruta.open("r", encoding="utf-8") as f:
    print("Nombre del fichero:", f.name)
    print("Modo de apertura:", f.mode)
    print("Codificación:", f.encoding)
    print("¿Permite lectura?:", f.readable())
    print("¿Permite escritura?:", f.writable())
    print("¿Permite mover el puntero?:", f.seekable())

print("Archivo cerrado:", f.closed)
```

Este ejemplo ilustra cómo consultar el estado del archivo y comprobar sus capacidades antes de operar sobre él.

## Ejemplo 2 – Lectura completa del fichero (`.read()`)

El método `.read()` lee **todo el contenido del fichero** y lo devuelve como una cadena.

```python
with open("datos/alumnos.txt", "r", encoding="utf-8") as f:
    texto = f.read()
    print("Contenido completo del archivo:\n")
    print(texto)
```

Se recomienda solo para ficheros pequeños, ya que carga todo el contenido en memoria.

## Ejemplo 3 – Lectura línea a línea (`.readline()`)

El método `.readline()` devuelve una **única línea** del fichero cada vez que se llama.

```python
with open("datos/alumnos.txt", "r", encoding="utf-8") as f:
    linea1 = f.readline()
    linea2 = f.readline()
    print("Primera línea:", linea1.strip())
    print("Segunda línea:", linea2.strip())
```

Útil cuando se desea procesar las líneas de manera controlada o cuando solo se necesitan unas pocas líneas del inicio.

## Ejemplo 4 – Lectura como lista (`.readlines()`)

El método `.readlines()` devuelve una lista donde cada elemento corresponde a una línea del fichero.

```python
with open("datos/alumnos.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    print("Número de líneas:", len(lineas))
    print("Tercera línea:", lineas[2].strip())
```

Como `.read()`, también carga todo el contenido en memoria, por lo que no es adecuado para ficheros grandes.

## Ejemplo 5 – Iteración línea a línea (forma recomendada)

Es la **forma más eficiente y legible** de leer ficheros grandes, ya que procesa una línea cada vez y libera memoria progresivamente.

Python permite recorrer directamente el archivo como si fuera una secuencia iterable:

```python
from pathlib import Path

# Definir la ruta del archivo
ruta = Path("datos/alumnos.txt")

# Apertura segura con codificación UTF-8
with ruta.open("r", encoding="utf-8") as f:
    # Lectura línea a línea (forma eficiente y legible)
    for linea in f:
        print(linea.strip())
```

Otra forma de implementarla pero mostrando el número línea:

```python
from pathlib import Path

ruta = Path("datos/alumnos.txt")

with ruta.open("r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        print(f"{numero:02d}: {linea.strip()}")
```

## Buenas prácticas a aplicar

*   Utilizar siempre `with open(...)` o `Path.open()` para garantizar el cierre.
*   Especificar `encoding="utf-8"`.
*   Evitar usar `read()` o `readlines()` con ficheros grandes.
*   Validar la existencia de la ruta antes de abrir el archivo.
*   Manejar las excepciones comunes del sistema de archivos.
*   Formatear la salida de forma clara y legible para el usuario.

- - -

# 3️ – Escritura, punteros y control del flujo

## Conceptos básicos

### Modos de escritura de archivos

Los ficheros se pueden abrir en diferentes **modos de escritura**:

| Modo | Descripción |
| --- | --- |
| `"w"` | Escribe un archivo nuevo. Si ya existe, **sobrescribe** su contenido. |
| `"a"` | Añade nuevo contenido **al final** del archivo existente (modo _append_). |
| `"x"` | Crea un archivo nuevo; da error si ya existe. |
| `"wb"` / `"ab"` | Versiones en **modo binario** (útiles para imágenes o bytes). |

> Siempre que se abra un archivo para escribir, es recomendable especificar el parámetro `encoding="utf-8"` para evitar errores con acentos o caracteres especiales.

### Puntero del archivo

Cada fichero tiene un **puntero interno** que indica la posición actual de lectura o escritura.

*   **`f.tell()`** → Devuelve la posición actual (en bytes) del puntero.
*   **`f.seek(offset, whence)`** → Mueve el puntero:
    *   `offset`: desplazamiento en bytes.
    *   `whence` (opcional):
        *   `0`: desde el inicio (por defecto)
        *   `1`: desde la posición actual
        *   `2`: desde el final del archivo

> Ejemplo: `f.seek(0)` vuelve al inicio del fichero.

### Control del búfer

Python no escribe inmediatamente en disco: los datos se almacenan en un **búfer temporal**.

*   **`f.flush()`** → Fuerza el vaciado del búfer y escribe los datos en disco de inmediato.
*   El archivo también se vacía automáticamente al cerrarse (`f.close()` o al salir del bloque `with`).

## Ejemplo 1 – Escritura básica

```python
# Importamos Path para manejar rutas de forma moderna y multiplataforma
from pathlib import Path  
# Definimos la ruta del archivo de salida
ruta = Path("datos/saludo.txt")

# Creamos la carpeta 'datos' si no existe (evita errores de ruta)
ruta.parent.mkdir(parents=True, exist_ok=True)

# Abrimos el archivo en modo escritura ('w') con codificación UTF-8
with ruta.open("w", encoding="utf-8") as f:
    f.write("Hola, mundo!\n")  # Escribimos la primera línea
    f.write("Este es mi primer archivo escrito con Python.\n")  # Escribimos otra línea

# Al salir del bloque 'with', el archivo se cierra automáticamente
print("Archivo creado correctamente.")
```

**Claves**:

*   El archivo se crea (o sobrescribe si ya existía).
*   Cada llamada a .write() añade texto donde está el puntero.
*   Se recomienda usar UTF-8 para evitar errores con tildes o eñes.

## Ejemplo 2 – Añadir información y consultar el puntero

```python
from pathlib import Path  # Importamos Path

log = Path("logs/registro.log")  # Definimos la ruta del archivo de log
log.parent.mkdir(parents=True, exist_ok=True)  # Creamos la carpeta si no existe

# Abrimos el archivo en modo 'a' (append) para añadir texto al final
with log.open("a", encoding="utf-8") as f:
    f.write("Inicio de la sesión.\n")  # Añadimos una línea de texto
    print("Puntero actual:", f.tell())  # Mostramos la posición actual del puntero en bytes
    f.write("Nueva entrada registrada correctamente.\n")  # Añadimos otra línea
    f.flush()  # Forzamos el guardado inmediato de los datos en disco

# El archivo se cierra automáticamente al salir del bloque
print("Datos añadidos al log.")
```

## Ejemplo 3 – Uso de `.seek()` y lectura parcial

```python
from pathlib import Path  # Importamos Path para manejar la ruta del archivo

archivo = Path("datos/demo_seek.txt")  # Definimos la ruta del archivo

# Abrimos en modo 'w+' para escribir y leer en el mismo archivo
with archivo.open("w+", encoding="utf-8") as f:
    f.write("Python permite mover el puntero en archivos de texto.\n")  # Escribimos una línea
    f.write("Esta línea se añadirá después.\n")  # Añadimos otra línea

    f.seek(0)  # Movemos el puntero al inicio del archivo (posición 0)
    print("Puntero movido al inicio:", f.tell())  # Confirmamos la nueva posición

    inicio = f.read(20)  # Leemos los primeros 20 caracteres
    print("Primeros 20 caracteres:", inicio)  # Mostramos el texto leído
```

**Claves**:

*   El modo "w+" permite leer y escribir.
*   `.seek(0)` reposiciona el puntero al inicio.
*   `.read(20)` lee solo los primeros 20 caracteres, no todo el archivo.

## Ejemplo 4 – Escritura con listas y `.writelines()`

```python
from pathlib import Path  # Importamos Path para manejar rutas

ruta = Path("datos/alumnos.txt")  # Definimos la ruta del archivo
alumnos = ["Ana López\n", "Luis García\n", "María Torres\n"]  # Lista con las líneas a escribir

# Abrimos el archivo en modo escritura ('w')
with ruta.open("w", encoding="utf-8") as f:
    f.writelines(alumnos)  # Escribimos todas las líneas de la lista en una sola operación

# Cierre automático del archivo al salir del bloque
print("Archivo 'alumnos.txt' creado con varias líneas.")
```

**Claves**:

*   .writelines() escribe una secuencia de cadenas (lista o tupla).
*   No añade saltos de línea automáticamente, cada cadena debe incluir \\n.
*   Es más eficiente que varias llamadas a .write() cuando hay muchas líneas.

## Ejemplo 5 – Registro de operaciones con timestamp

```python
from pathlib import Path  # Módulo moderno para rutas
from datetime import datetime  # Para registrar la fecha y hora

ruta_log = Path("logs/operaciones.log")  # Definimos la ruta del log
ruta_log.parent.mkdir(parents=True, exist_ok=True)  # Creamos la carpeta si no existe

# Abrimos el archivo en modo append
with ruta_log.open("a", encoding="utf-8") as f:
    # Obtenemos la fecha y hora actuales formateadas
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Escribimos una línea con la marca temporal
    f.write(f"[{timestamp}] Inicio de la operación\n")

    # Consultamos la posición del puntero tras escribir
    pos = f.tell()
    f.write(f"[{timestamp}] Puntero tras escribir: {pos}\n")

    # Vaciamos el búfer para asegurar que se escriba de inmediato
    f.flush()

    # Movemos el puntero al inicio y leemos el contenido para mostrarlo
    f.seek(0)
    print("Contenido actual del log:\n")
    print(f.read())  # Leemos todo el contenido del archivo
```

**Claves**:

*   Uso de datetime para generar marcas temporales precisas.
*   Control completo del flujo: escribir, mover puntero y leer.
*   Ideal para logs de auditoría.

## Buenas prácticas a aplicar

*   Siempre usar `with open(...)` o `Path.open()` para garantizar cierre automático.
*   Especificar la codificación `utf-8`.
*   Forzar escritura inmediata con `.flush()` en procesos críticos.
*   Reposicionar el puntero antes de leer (`f.seek(0)` o similar).
*   Incluir marcas temporales o separadores al registrar logs.
*   Manejar excepciones (`FileNotFoundError`, `PermissionError`) al abrir ficheros.

- - -

# 4️ – Tratamiento de ficheros JSON

## Conceptos

Los ficheros **JSON (JavaScript Object Notation)** se utilizan para **intercambiar y persistir datos estructurados** de forma **ligera, legible y multiplataforma**. Son el formato de facto para **APIs web**, **configuraciones de aplicaciones**, **exportación/importación de datos** y **registro de eventos**.

**¿Para qué se utilizan?** 

*   **Configuración de aplicaciones**: `config.json` con parámetros de ejecución (puertos, rutas, credenciales de prueba).
*   **Intercambio de datos por APIs**: respuestas REST/GraphQL (`users`, `orders`, `metrics`).
*   **Datasets ligeros**: listas de objetos (alumnos, productos, sensores).
*   **Logs estructurados**: eventos con `timestamp`, `level` y `message`.
*   **Persistencia rápida**: guardar el estado de un programa o un resultado intermedio de cálculo.

## Referencias

*   W3Schools: [https://www.w3schools.com/python/python_json.asp](url)
*   Wikipedia: [https://es.wikipedia.org/wiki/JSON](url)
*   Validador de formato: [https://jsonlint.com](url)
*   JSON web tokens: [https://www.jwt.io](url)

## Información de librería

*   **Módulo estándar `json`**: no requiere instalación. Proporciona funciones para **serializar** (Python → JSON) y **deserializar** (JSON → Python).
*   **Funciones principales**:
    *   `json.load(f)` / `json.dump(obj, f, ...)` → trabajar directamente con **ficheros**.
    *   `json.loads(s)` / `json.dumps(obj, ...)` → trabajar con **cadenas** en memoria.
*   **Parámetros útiles al serializar (Guardar en JSON)**:
    *   `indent=int` → sangría legible (p. ej., `indent=2`). Si no aparece todo en una sola línea.
    *   `ensure_ascii=bool` → si `False`, permite **tildes y eñes** directamente (UTF-8), si no en el fichero aparecen los códigos ASCII.
    *   `sort_keys=bool` → ordena claves para salidas **deterministas** y comparables.
    *   `separators=(',', ':')` → controla separadores para reducir tamaño.
    *   `default=callable` → conversor para **tipos no JSON** (p. ej., `datetime`).
*   **Parámetros útiles al deserializar (Leer JSON)**:
    *   `parse_float`, `parse_int`, `parse_constant` → parseo especializado.
    *   `object_hook` / `object_pairs_hook` → **post-procesado** de dicts al cargar.
*   **Tipos compatibles (JSON ↔ Python)**:
    *   `object` ↔ `dict`, `array` ↔ `list`, `string` ↔ `str`, `number` ↔ `int/float`, `true/false` ↔ `bool`, `null` ↔ `None`.
*   **Manejo de errores**: `json.JSONDecodeError` (formato inválido); capturar y notificar con mensajes claros.
*   **Validación de estructura**: comprobación de **claves requeridas**, tipos y rangos; para validaciones formales, puede emplearse `jsonschema` (opcional, no estándar).
*   **Buenas prácticas**: abrir con `encoding="utf-8"`, usar `with` para cierre automático, mantener claves estables y documentadas.

## Ejemplo de fichero json

```json
[
  {
    "isbn": "978-84-376-0494-7",
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año_publicacion": 1967,
    "género": "Realismo mágico",
    "disponible": true
  },
  {
    "isbn": "978-84-339-7135-6",
    "título": "La sombra del viento",
    "autor": "Carlos Ruiz Zafón",
    "año_publicacion": 2001,
    "género": "Misterio",
    "disponible": false
  },
  {
    "isbn": "978-84-670-6046-5",
    "título": "Don Quijote de la Mancha",
    "autor": "Miguel de Cervantes",
    "año_publicacion": 1605,
    "género": "Aventura",
    "disponible": true
  }
]
```

## Escribir en un fichero JSON

Ahora vamos a crear el fichero anterior:

```python
import json
from pathlib import Path

def crearFicheroBiblioteca(ruta_fichero: str) -> None:
    """
    Crea un fichero JSON con información de libros de una biblioteca.
    Si el fichero ya existe, lo sobrescribe.
    """

    # Datos iniciales (lista de diccionarios)
    libros = [
        {
            "isbn": "978-84-376-0494-7",
            "título": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "año_publicación": 1967,
            "género": "Realismo mágico",
            "disponible": True
        },
        {
            "isbn": "978-84-339-7135-6",
            "título": "La sombra del viento",
            "autor": "Carlos Ruiz Zafón",
            "año_publicación": 2001,
            "género": "Misterio",
            "disponible": False
        },
        {
            "isbn": "978-84-670-6046-5",
            "título": "Don Quijote de la Mancha",
            "autor": "Miguel de Cervantes",
            "año_publicación": 1605,
            "género": "Aventura",
            "disponible": True
        }
    ]

    ruta = Path(ruta_fichero)
    ruta.parent.mkdir(parents=True, exist_ok=True)  # crea carpeta si no existe

    # Escribimos el JSON en UTF-8 y con formato legible
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=2)

    print(f"Fichero '{ruta.name}' creado correctamente con {len(libros)} libros.")


```

## Leer un fichero JSON

Leemos los contenidos del fichero anterior y los mostramos por pantalla:

```python
import json
from pathlib import Path

def mostrarLibros(ruta_fichero: str) -> None:
    """
    Lee el fichero JSON con información de libros y muestra su contenido
    recorriendo las claves y valores de cada diccionario (libro).
    """

    ruta = Path(ruta_fichero)

    # Comprobamos si el fichero existe
    if not ruta.exists():
        print(f"El fichero '{ruta_fichero}' no existe.")
        return

    # Leemos el contenido del JSON
    with open(ruta, "r", encoding="utf-8") as f:
        libros = json.load(f)

    # Si no hay libros, avisamos
    if not libros:
        print("No hay libros en la biblioteca.")
        return

    print("\n *** LISTADO DE LIBROS ***")
    print("-" * 40)

    # Recorremos cada libro (cada diccionario dentro de la lista)
    for i, libro in enumerate(libros, start=1):
        print(f"Libro {i}:")
        # Recorremos las claves y valores del diccionario
        for clave, valor in libro.items():
            print(f"   {clave}: {valor}")
        print("-" * 40)

```

## Añadir una entrada en un fichero JSON

Ahora añadimos un libro al fichero:

```python
import json
from pathlib import Path

def agregarLibro(ruta_fichero: str, nuevo_libro: dict) -> None:
    """
    Añade un nuevo libro al fichero JSON de la biblioteca.

    Parámetros:
        ruta_fichero (str): ruta del fichero JSON.
        nuevo_libro (dict): diccionario con los datos del libro.
    """

    ruta = Path(ruta_fichero)

    # Si el fichero no existe, creamos una lista vacía
    if not ruta.exists():
        libros = []
    else:
        # Leemos el JSON actual
        with open(ruta, "r", encoding="utf-8") as f:
            try:
                libros = json.load(f)
            except json.JSONDecodeError:
                libros = []

    # Añadimos el nuevo libro a la lista
    libros.append(nuevo_libro)

    # Guardamos de nuevo el fichero
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=2)

    print(f"Libro '{nuevo_libro.get('titulo', 'Sin título')}' añadido correctamente.")

```

## Eliminar una entrada en un fichero JSON

Ahora vamos a liminar uno de los libros del fichero:

```Python
import json
from pathlib import Path

def eliminarLibro(ruta_fichero: str, isbn: str) -> None:
    """
    Elimina un libro del fichero JSON en función de su ISBN.

    Parámetros:
        ruta_fichero (str): ruta al fichero JSON.
        isbn (str): código ISBN del libro a eliminar.
    """

    ruta = Path(ruta_fichero)

    # 1️ Comprobar que el fichero existe
    if not ruta.exists():
        print(f"El fichero '{ruta_fichero}' no existe.")
        return

    # 2️ Leer el fichero JSON
    with open(ruta, "r", encoding="utf-8") as f:
        try:
            libros = json.load(f)
        except json.JSONDecodeError:
            print("❌ Error: el fichero JSON está corrupto o vacío.")
            return

    # 3️ Buscar el libro por ISBN
    isbn = isbn.strip()
    libro_encontrado = False

    nuevos_libros = []
    for libro in libros:
        if str(libro.get("isbn", "")).strip() != isbn:
            nuevos_libros.append(libro)
        else:
            libro_encontrado = True

    # 4️ Verificar si se encontró
    if not libro_encontrado:
        print(f"No se encontró ningún libro con ISBN {isbn}.")
        return

    # 5️ Guardar el fichero actualizado
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(nuevos_libros, f, ensure_ascii=False, indent=2)

    print(f"Libro con ISBN {isbn} eliminado correctamente.")


```

## Modificar una entrada en un fichero JSON

```python
import json
from pathlib import Path

def modificarLibro(ruta_fichero: str, isbn: str, campo: str, nuevo_valor) -> None:
    """
    Modifica un dato de un libro en el fichero JSON según su ISBN.

    Parámetros:
        ruta_fichero (str): ruta al fichero JSON.
        isbn (str): ISBN del libro a modificar.
        campo (str): nombre de la clave que se quiere cambiar.
        nuevo_valor: valor nuevo para ese campo (puede ser str, int, bool...).
    """

    ruta = Path(ruta_fichero)

    # 1️ Verificar existencia del fichero
    if not ruta.exists():
        print(f"El fichero '{ruta_fichero}' no existe.")
        return

    # 2️ Leer el JSON
    with open(ruta, "r", encoding="utf-8") as f:
        try:
            libros = json.load(f)
        except json.JSONDecodeError:
            print("Error: el fichero JSON está corrupto o vacío.")
            return

    # 3️ Buscar el libro y modificar el campo
    isbn = isbn.strip()
    modificado = False

    for libro in libros:
        if str(libro.get("isbn", "")).strip() == isbn:
            if campo not in libro:
                print(f"El campo '{campo}' no existe en el libro.")
                return
            libro[campo] = nuevo_valor
            modificado = True
            break

    # 4️ Comprobar si se encontró y guardarlo
    if not modificado:
        print(f"No se encontró ningún libro con ISBN {isbn}.")
        return

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(libros, f, ensure_ascii=False, indent=2)

    print(f"Campo '{campo}' del libro con ISBN {isbn} actualizado correctamente.")


```

- - -

# 6️ Gestión de errores con ficheros

Trabajar con ficheros implica posibles **errores en tiempo de ejecución**: rutas inexistentes, permisos insuficientes o contenidos corruptos.  
Una buena gestión de errores mantiene el programa **estable**, informa al usuario y evita **pérdidas de datos**.

## Contenidos desarrollados

*   **Errores comunes al trabajar con ficheros:**
    *   `FileNotFoundError` → el archivo no existe.
    *   `PermissionError` → permisos insuficientes de lectura/escritura.
    *   `IsADirectoryError` → se intenta abrir una carpeta como archivo.
    *   `IOError` / `OSError` → errores generales de E/S.
    *   `json.JSONDecodeError` → JSON inválido.
*   **Estructura de manejo de errores:**
    *   Bloques `try` / `except` / `else` / `finally`.
    *   Validación previa con `Path.exists()` y `Path.is_file()`.
    *   Registro de errores mediante `logging` (ficheros `.log`).
*   **Buenas prácticas:**
    *   No asumir existencia de archivos: comprobar y crear si procede.
    *   Mensajes de error claros y accionables.
    *   Usar `raise` o terminar el programa si no se puede continuar.
    *   Cerrar ficheros siempre (preferiblemente con `with`).

## Ejemplo 1 – Control básico al abrir un fichero

```python
from pathlib import Path  # Path ofrece manejo de rutas multiplataforma

ruta = Path("datos/alumnos.txt")  # Ruta al fichero de entrada

try:
    # Abrimos el archivo en modo lectura con codificación UTF-8
    with ruta.open("r", encoding="utf-8") as f:
        contenido = f.read()  # Leemos todo el contenido
        print("Contenido del archivo:")
        print(contenido)      # Mostramos el resultado por consola

# El archivo no existe o la ruta es incorrecta
except FileNotFoundError:
    print("Error: el archivo no existe. Verifica la ruta y el nombre.")

# El usuario no tiene permisos para leer el recurso
except PermissionError:
    print("Error: no dispones de permisos para acceder al archivo.")

# Cualquier otro error no previsto (con el tipo y el detalle)
except Exception as e:
    print(f"Error inesperado: {type(e).__name__} → {e}")

# Se ejecuta solo si no saltó ninguna excepción en el bloque try
else:
    print("Lectura completada sin errores.")

# Se ejecuta SIEMPRE: haya error o no (útil para liberar recursos, logs, etc.)
finally:
    print("Fin del proceso de lectura.")
```

## Ejemplo 2 – Validación previa con `pathlib`

```python
from pathlib import Path  # Importamos Path para manejar rutas

ruta = Path("datos/notas.csv")  # Definimos la ruta del CSV

# Comprobamos si el archivo existe antes de abrirlo
if not ruta.exists():
    print("El archivo no existe. Creándolo con encabezado por defecto...")
    ruta.parent.mkdir(parents=True, exist_ok=True)    # Creamos la carpeta si no existe
    ruta.write_text("nombre,nota\n", encoding="utf-8")  # Creamos el archivo con cabecera
else:
    print("Archivo encontrado:", ruta.name)

# Intentamos abrir el archivo en modo lectura
try:
    with ruta.open("r", encoding="utf-8") as f:
        for linea in f:                 # Recorremos el archivo línea a línea (eficiente)
            print("→", linea.strip())   # strip() elimina saltos de línea finales
# OSError agrupa varios errores de entrada/salida (p. ej., dispositivo no disponible)
except OSError as e:
    print(f"Error de acceso al archivo: {e}")
```

- - -

## Ejemplo 3 – Captura de errores al procesar JSON

```python
import json              # Módulo estándar para JSON
from pathlib import Path # Manejo de rutas

ruta = Path("datos/config.json")  # Ruta del archivo JSON

try:
    # Abrimos y cargamos el JSON (puede fallar si el formato es inválido)
    with ruta.open("r", encoding="utf-8") as f:
        datos = json.load(f)  # Convierte el JSON a dict/list de Python
    print("Archivo JSON cargado correctamente.")

# Archivo no encontrado
except FileNotFoundError:
    print("No se encontró el archivo de configuración.")

# JSON mal formado: proporciona línea y columna del error
except json.JSONDecodeError as e:
    print(f"Error de formato JSON: línea {e.lineno}, columna {e.colno} → {e.msg}")

# Cualquier otro error
except Exception as e:
    print(f"Error inesperado: {e}")

# Si todo fue bien, mostramos un resumen de claves
else:
    # list(datos.keys()) asume que 'datos' es un dict;
    # si no lo fuera, se puede comprobar con isinstance(datos, dict)
    if isinstance(datos, dict):
        print("Claves del JSON:", list(datos.keys()))
    else:
        print("El JSON cargado no es un objeto (dict), es de tipo:", type(datos).__name__)

# Bloque que siempre se ejecuta (útil para cerrar recursos extra o trazar finalización)
finally:
    print("Fin del proceso de carga de configuración.")
```

- - -

## Ejemplo 4 – Registro de errores a fichero con `logging`

```python
import logging           # Módulo estándar para registro de eventos
from pathlib import Path # Manejo de rutas

# Configuramos el logger para escribir en un archivo .log
ruta_log = Path("logs/errores.log")
ruta_log.parent.mkdir(parents=True, exist_ok=True)  # Creamos la carpeta 'logs' si no existe

logging.basicConfig(
    filename=ruta_log,                     # Archivo donde se guardarán los logs
    level=logging.ERROR,                   # Nivel mínimo: solo errores o más graves
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato con fecha y nivel
)

ruta = Path("datos/inexistente.txt")  # Archivo que no existe (forzará FileNotFoundError)

try:
    with ruta.open("r", encoding="utf-8") as f:
        contenido = f.read()  # Intentamos leer (no llegaremos aquí si falla)
except FileNotFoundError as e:
    # Registramos el error en el fichero .log con el detalle de la excepción
    logging.error("Archivo no encontrado: %s", e)
    print("Se ha registrado el error en el log:", ruta_log)
except Exception as e:
    # Registramos cualquier otro error no esperado
    logging.exception("Error inesperado accediendo al archivo")  # incluye traceback
    print("Error inesperado registrado en el log.")
```

- - -

# Buenas prácticas recomendadas

*   Usar siempre `with open(...)` para garantizar el cierre automático.
*   Especificar `encoding="utf-8"` en los ficheros de texto.
*   Verificar la existencia de rutas con `Path.exists()`.
*   Manejar excepciones comunes:
    *   `FileNotFoundError`
    *   `PermissionError`
    *   `JSONDecodeError`
*   Evitar `readlines()` en ficheros grandes, mejor iterar línea a línea.
*   No mezclar lectura y escritura sin reposicionar el puntero.
