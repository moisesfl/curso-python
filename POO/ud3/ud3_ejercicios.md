
# UD3 – Boletín de ejercicios (POO + Ficheros en Python)

> Recomendación general para todos: usa `pathlib.Path`, apertura segura con `with`, `encoding="utf-8"`, y captura de errores (`FileNotFoundError`, `PermissionError`, `json.JSONDecodeError`, etc.).

# Índice

1.  [Cifrado César con menú de consola](#1-cifrado-c%C3%A9sar-con-men%C3%BA-de-consola)
2.  [Utilidades de texto por consola](#2-utilidades-de-texto-por-consola)
3.  [Gestión de un taller de reparación informática (JSON)](#taller-json)

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
*   Generar un log en la carpeta en que se ejecuta el programa. Se almacenara en cada línea la fecha y hora, la tarea ejecutada y el usuario que la ejecutó. También se mostrarán los errores.

*   Gestión de errores:
    *   Gestionar los posibles errores que pueda dar el programa si el fichero no existe, etc.
    *   En caso de que haya un error, el programa mostrará cual es el error y volverá al menú principal.
*   El programa mostrará un banner de inicio con el nombre de la aplicación y los datos del estudiante, y un banner de cierre de la aplicación.

**Estructura.**

*   `main.py`
*   `__init__.py`
*   `interfaz_usuario.py` -> clase con el menú y banners
*   `script_cesar.py` -> clase con las funcionalidades para cifrar/descifrar.
*   `ficheros.py` -> clase con las funcionalidades para trabajar con ficheros

- - -

# 2) Utilidades de texto por consola

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
*   `ficheros.py` -> clase con las funcionalidades para trabajar con ficheros.
*   `text_parser.py` -> clase con las funcionalidades para realizar las operaciones pedidas.

- - -

#  <a id="taller-json"></a>3) Gestión de un taller de reparación informática (JSON)

## Descripción

Desarrollar una aplicación con interfaz por consola que permita gestionar los equipos informáticos de un taller de reparación mediante el almacenamiento de datos en ficheros JSON.

La aplicación permitirá registrar equipos, consultar su información, modificar sus datos y gestionar las intervenciones técnicas realizadas.

## Requisitos

*   **Menú de usuario**:

    1. Listar equipos.
    2. Registrar un equipo.
    3. Eliminar un equipo.
    4. Modificar datos de un equipo.
    5. Buscar un equipo por número de serie.
    6. Registrar una intervención técnica.
    7. Listar las intervenciones de un equipo.
    8. Salir.


*   **Datos de los equipos**:

    Cada equipo se identificará mediante su número de serie, que será la clave del registro.

    - **Número de serie:** `str`
    - **Cliente:** `str`
    - **Tipo de equipo:** `str` (PC, portátil, impresora, etc.).
    - **Marca:** `str`
    - **Modelo:** `str`
    - **Avería:** `str`
    - **Estado:** `str` (RECIBIDO, EN_REPARACION, REPARADO).

*   **Datos de las intervenciones**:

    Cada intervención tendrá un identificador único.

    - **ID de intervención:** `str`
    - **Número de serie del equipo:** `str`
    - **Técnico:** `str`
    - **Descripción del trabajo:** `str`
    - **Horas dedicadas:** `float`

    Un equipo podrá tener varias intervenciones técnicas.


*   **Los datos se almacenarán en dos ficheros JSON**:

    -   `equipos.json`
    -   `intervenciones.json`

    La aplicación deberá guardar los cambios realizados para que los datos se mantengan al cerrar y volver a ejecutar el programa.


*   **Gestión de errores**:

    El programa deberá gestionar, al menos, los siguientes errores:

    - Ficheros inexistentes o con formato JSON incorrecto.
    - Errores de lectura y escritura.
    - Equipos duplicados o inexistentes.
    - Intervenciones asociadas a equipos inexistentes.

    En caso de error, se mostrará un mensaje al usuario y se volverá al menú principal cuando sea posible.


*   **Registro de actividad (log)**:

    El programa generará un fichero `taller.log` en el que se registrará:

    - Fecha y hora.
    - Operación realizada.
    - Errores producidos.


*   **Estructura**:

    - `main.py`
    - `app/`
        - `__init__.py`
        - `interfaz_usuario.py` -> Menú y presentación de información.
        - `ficheros.py` -> Lectura y escritura de ficheros JSON.
        - `gestion_taller.py` -> Coordinación de las operaciones.
        - `equipo.py` -> Gestión de equipos.
        - `intervencion.py` -> Gestión de intervenciones.
        - `registrar.py` -> Registro de actividad y errores.
    - `datos/`
        - `equipos.json`
        - `intervenciones.json`

*   **Consideraciones**:

    - No se permitirá registrar dos equipos con el mismo número de serie.
    - No se permitirá registrar intervenciones para equipos inexistentes.
    - No se permitirá eliminar un equipo que tenga intervenciones registradas.
    - Los datos deberán validarse antes de guardarse.
    - Se utilizará programación orientada a objetos y código modular.
