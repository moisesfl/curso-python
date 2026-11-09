
# UD4 – Ejercicio: “MiniGestor SQLite” — CRUD + SQL libre por Consola

## Enunciado

Vas a desarrollar una pequeña **aplicación de consola** en Python llamada **MiniGestor SQLite**.
El programa permitirá al usuario **conectarse a una base de datos SQLite** y realizar operaciones CRUD sobre una tabla de personas, además de **introducir cualquier sentencia SQL manualmente**.

---

## 1. Descripción general

1. Al iniciar el programa, el usuario debe indicar el **nombre del fichero de base de datos** (por ejemplo, `datos.db`).

   * Si el fichero no existe, el programa lo **creará automáticamente** y generará la tabla necesaria.

2. Una vez establecida la conexión, se mostrará un **menú principal** con las operaciones disponibles:

   ```
   === MiniGestor SQLite ===
   [1] Crear registro
   [2] Listar registros
   [3] Buscar por ID
   [4] Actualizar registro
   [5] Eliminar registro
   [6] Ejecutar sentencia SQL personalizada
   [0] Salir
   ```

3. El usuario podrá elegir libremente qué acción ejecutar hasta que decida salir.

---

## 2. Modelo de datos

El programa gestionará una tabla llamada `personas` con los siguientes campos:

| Campo    | Tipo       | Descripción                        |
| -------- | ---------- | ---------------------------------- |
| `id`     | INTEGER PK | Identificador único (autonumérico) |
| `nombre` | TEXT       | Nombre de la persona               |
| `edad`   | INTEGER    | Edad en años                       |
| `email`  | TEXT       | Correo electrónico (único)         |

Ejemplo de creación de tabla (el programa debe ejecutarlo si no existe):

```sql
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    email TEXT UNIQUE
);
```

---

## 3. Funcionalidades requeridas

### Crear registro

* Solicita `nombre`, `edad` y `email`.
* Inserta el registro y confirma al usuario.

### Listar registros

* Muestra todos los registros existentes en formato tabulado.

### Buscar por ID

* Solicita un ID y muestra los datos correspondientes.

### Actualizar registro

* Permite modificar un registro existente, seleccionando por ID.

### Eliminar registro

* Pide el ID a eliminar y solicita confirmación antes de borrarlo.

### Ejecutar sentencia SQL personalizada

* Permite al usuario introducir **una sentencia SQL completa** y ejecutarla directamente.
* Debe permitir tanto consultas (`SELECT`) como instrucciones (`INSERT`, `UPDATE`, `DELETE`, `CREATE`, etc.).
* Si la sentencia devuelve resultados (por ejemplo, en un `SELECT`), se deben mostrar en pantalla en formato de tabla.
* Si la sentencia no devuelve filas, debe informar de que se ha ejecutado correctamente.

> **Importante:**
>
> * Implementa **control de errores** (por ejemplo, si la sentencia está mal escrita).
> * No permitas más de una sentencia a la vez (por seguridad).

Ejemplo:

```
Selecciona una opción: 6
Introduce tu sentencia SQL:
> SELECT nombre, edad FROM personas WHERE edad > 25;

Resultados:
-------------------------------------
Nombre           | Edad
-------------------------------------
Luis Martínez     | 31
María Pérez       | 45
```

---

## 4. Estructura sugerida

```
minigestor_sqlite/
├── main.py           # Programa principal (menú)
├── README.md         # Instrucciones de uso
└── App/
  |─ __init__.py 
  |─ interfaz_usuario.py 
  |─ db_manager.py     # Funciones para conectar y operar con la BD. Utilizar Programación orientada a objetos.	
  |─ Data/
	|─ datos.db		# Fichero de la base de datos sqlite

```

---

## 5. Ejemplo de ejecución

```
Introduce el nombre del fichero de base de datos: datos.db
Conectado correctamente a datos.db

=== MiniGestor SQLite ===
[1] Crear registro
[2] Listar registros
[3] Buscar por ID
[4] Actualizar registro
[5] Eliminar registro
[6] Ejecutar sentencia SQL personalizada
[0] Salir
--------------------------------
Selecciona una opción: 6

Introduce tu sentencia SQL:
> SELECT COUNT(*) AS total FROM personas;

Resultados:
-------------------------------------
total
-------------------------------------
3
```

---
