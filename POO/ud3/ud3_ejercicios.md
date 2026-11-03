
# UD3 – Boletín de ejercicios (POO + Ficheros en Python)

> Recomendación general para todos: usa `pathlib.Path`, apertura segura con `with`, `encoding="utf-8"`, y captura de errores (`FileNotFoundError`, `PermissionError`, `json.JSONDecodeError`, etc.).

# Índice

1.  [Cifrado César con menú de consola](#1-cifrado-c%C3%A9sar-con-men%C3%BA-de-consola)
2.  [Codificador Base64](#2-codificador-base64)
3.  [Utilidades de texto por consola](#3-utilidades-de-texto-por-consola)
4.  [Gestión de instituto (JSON)](#4-gesti%C3%B3n-de-instituto-json)

- - -

# 1) Cifrado César con menú de consola

**Descripción.**

Aplicación de consola que cifra o descifra un fichero de texto mediante **Cifrado César**.

*   Más información: [Wikipedia - Cifrado César](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar)
*   Ayuda: [Geeksforgeeks](https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/)

**Requisitos.**

*   Menú que ve el usuario:
    1.  Cifrar
    2.  Descifrar
    3.  Salir
*   Al cifrar/descifrar, leer el fichero de entrada y **generar un fichero nuevo** con el resultado añadiendo al nombre "_cifrado" o "_descifrado".
*   Debe permitir al usuario elegir el desplazamiento.
*   Gestión de errores:
    *   Gestionar los posibles errores que pueda dar el programa si el fichero no existe, etc.
    *   En caso de que haya un error, el programa mostrará cual es el error y volverá al menú principal.
*   El programa mostrará un banner de inicio con el nombre de la aplicación y los datos del estudiante, y un banner de cierre de la aplicación.

**Estructura.**

*   `main.py`
*   `__init__.py`
*   `interfaz_usuario.py` -> clase con el menú y banners
*   `cript_cesar.py` -> clase con las funcionalidades para cifrar/descifrar.
*   `ficheros.py` -> clase con las funcionalidades para trabajar con ficheros

- - -

# 2) Codificador Base64

**Descripción.**

Aplicación de consola que codifica o decodifica ficheros mediante **Base64**.

*   Más información: [Wikipedia base64](https://es.wikipedia.org/wiki/Base64).
*   Ayuda: [GeeksforGeeks - base64](https://www.geeksforgeeks.org/python/encoding-and-decoding-base64-strings-in-python/)

**Requisitos.**

*   Menú que ve el usuario:
    1.  Codificar
    2.  Descodificar
    3.  Salir
*   El programa debe permitir la codificación y descodificación de ficheros binarios.
*   Al codificar/descodificar, leer el fichero de entrada y **generar un fichero nuevo** con el resultado añadiendo al nombre "\_b64" o "\_decoded".
*   Generar un log en la carpeta en que se ejecuta el programa. Se almacenara en cada línea la fecha/hora, la tarea ejecutada y el usuario que la ejecutó. También se mostrarán los errores.
*   Gestión de errores:
    *   Gestionar los posibles errores que pueda dar el programa si el fichero no existe, etc.
    *   En caso de que haya un error, el programa mostrará cual es el error y volverá al menú principal.
*   El programa mostrará un banner de inicio con el nombre de la aplicación y los datos del estudiante, y un banner de cierre de la aplicación.

**Estructura.**

*   `main.py`
*   `__init__.py`
*   `interfaz_usuario.py` -> clase con el menú y banners.
*   `registrar.py` -> clase con las funciones para generar logs.
*   `b64_io.py` → clase con las funcionalidades para codificar/decodificar.
*   `ficheros.py` → clase con las funcionalidades para trabajar con ficheros.

- - -

# 3) Utilidades de texto por consola

**Descripción.** Programa con interfaz de consola para operar sobre un fichero de texto.

**Requisitos:** El programa permitirá al usuario:

*   **Visualizar** todo el contenido.
*   Mostrar las **palabras con una letra** indicada por el usuario (insensible a mayúsculas).
*   Mostrar la **cantidad de apariciones** de una **palabra** (insensible a mayúsculas).
*   Mostrar la **cantidad de apariciones** de una **letra**.
*   **Sustituir** una palabra por otra y **guardar** en un fichero nuevo con el nombre del original añadiendo "\_mod" al nombre.

**Estructura.**

*   `main.py`
*   `__init__.py`
*   `interfaz_usuario.py` -> clase con el menú y banners.
*   `ficheros.py` → clase con las funcionalidades para trabajar con ficheros.
*   `text_parser.py` → clase con las funcionalidades para realizar las operaciones pedidas.

- - -

# 4) Gestión de Instituto (JSON)

**Descripción:** Aplicación con interfaz por consola que permite gestionar los estudiantes y profesores de un centro de formación profesional de informática mediante el almacenamiento de datos en un fichero json básico para estudiantes y otro para profesores.

*   Más información: [Wikipedia JSON](https://es.wikipedia.org/wiki/JSON)

**Requisitos:**

*   **Menú de usuario**:
    
    1.  listar estudiantes.
    2.  listar profesores.
    3.  Crear estudiante.
    4.  Eliminar estudiante.
    5.  Crear profesor.
    6.  Eliminar profesor.
    7.  Modificar datos estudiante.
    8.  Modificar datos de profesor.
    9.  Buscar datos de estudiantee.
    10.  Buscar datos de profesor.
    11.  Salir.
*   **Datos de estudiantes**:
    
    *   DNI -> clave que identifica cada registro. str.
    *   Nombre -> str.
    *   Apellidos -> str.
    *   Ciclo -> siglas (ASIR, DAM, etc). str.
    *   Curso -> int.
*   **Datos profesores**:
    
    *   DNI -> clave que identificaa cada registro. str.
    *   Nombre -> str.
    *   Apellidos -> str.
    *   Especialidad. -> _Informática, Sistemas y Aplicaciones informáticas, Formación y Orientación Laboral_
    *   Ciclos -> siglas (ASIR, DAM, etc). str.
    *   Módulos -> siglas (SRI, PSP, SAD, AD, PAR, ...). str.
*   **Gestión de errores**:
    
    *   Gestionar los posibles errores que pueda dar el programa si el fichero no existe, etc.
    *   En caso de que haya un error, el programa mostrará cual es el error y volverá al menú principal.
*   Generar un **log** en la carpeta en que se ejecuta el programa. Se almacenara en cada línea la fecha/hora, la tarea ejecutada y el usuario que la ejecutó. También se mostrarán los errores.
    

**Estructura:**

*   `main.py`
*   app
    *   `__init__.py`
        
    *   `interfaz_usuario.py` -> clase con el menú y banners.
        
    *   `ficheros.py` → clase con las funcionalidades para trabajar con ficheros.
        
    *   `gestion_instituto.py` → clase con las funcionalidades para gestionar estudiantes y profesores que usa las clases respectivas.
        
    *   `estudiante` -> clase con funcionalidades específicas para gestionar a los estudiantes y que usa las funcionalidades de "ficheros.py".
        
    *   `docente.py` -> clase con funcionalidades específicas para gestionar a los docentes y que usa las funcionalidades de "ficheros.py".
        
    *   `registrar.py` -> clase con las funciones para generar logs.
        
*   datos
    *   `docentes.json`
    *   `estudiantes.json`

- - -