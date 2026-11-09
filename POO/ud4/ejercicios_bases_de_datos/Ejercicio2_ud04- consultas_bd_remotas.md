# UD4 – Ejercicio 2: “MiniGestor Remoto” — Consola + CRUD en **MySQL**

## Enunciado

Desarrolla **MiniGestor Remoto**, un programa de consola que:

1. **Configura** la conexión remota a **MySQL** (host/IP, puerto, usuario, contraseña, base de datos).
2. Ofrece un **menú CRUD** sobre una tabla `personas`.
3. Añade una opción para **ejecutar una sentencia SQL** introducida por el usuario (una sola sentencia cada vez).

---

## 1. Flujo de uso

1. Al iniciar:

   * Muestra un selector de motor:

     ```
     Selecciona motor:
     [1] MySQL
     ```
   * Solicita: **host**, **puerto**, **usuario**, **contraseña**, **base de datos**.
   * Leer/guardar estos datos en `config.json`.

2. **Prueba de conexión**:

   * Intenta conectar y muestra **OK** o **error** con detalle.
   * Si conecta, crea la tabla `personas` si no existe (ver esquema más abajo).

3. **Menú principal**:

   ```
   === MiniGestor Remoto ===
   [1] Crear registro
   [2] Listar registros
   [3] Buscar por ID
   [4] Actualizar registro
   [5] Eliminar registro
   [6] Ejecutar sentencia SQL personalizada
   [0] Salir
   ```

---

## 2. Modelo de datos

Tabla **personas**:

| Campo  | Tipo (MySQL)          | Notas                    |
| ------ | --------------------- | ------------------------ |
| id     | INT AUTO_INCREMENT PK | Identificador único      |
| nombre | VARCHAR(100) NOT NULL |                          |
| edad   | INT NOT NULL          | `edad >= 0` (validación) |
| email  | VARCHAR(255) UNIQUE   | Único                    |

**Script MySQL (creación si no existe):**

```sql
CREATE TABLE IF NOT EXISTS personas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  edad INT NOT NULL,
  email VARCHAR(255) UNIQUE
) ENGINE=InnoDB;
```

> Puedes ejecutar este `CREATE TABLE` desde el programa al iniciar sesión si la tabla no existe.

---

## 3. Requisitos técnicos

* **Python 3.14+**
* Conectores:

  * **MySQL:** `mysql-connector-python` (o `PyMySQL`)

* **Parámetros de conexión**:

  * MySQL: host, port (3306), user, password, database

* **Buenas prácticas**:

  * **Consultas parametrizadas** (placeholder `%s`, evita concatenar strings).
  * Manejo de excepciones con mensajes claros.
  * Validaciones (edad numérica, email no vacío, etc.).

---

## 4. Funcionalidades requeridas

### Crear registro

* Pide `nombre`, `edad`, `email`.
* Inserta en `personas`.
* Confirma con el `id` inserto.

### Listar registros

* Muestra todas las filas en formato tabular.

### Buscar por ID

* Pide `id` y muestra la fila o avisa si no existe.

### Actualizar registro

* Pide `id`, muestra valores actuales y permite introducir los nuevos.
* Actualiza solo si el `id` existe.

### Eliminar registro

* Pide `id`, solicita confirmación, elimina si existe.

### SQL personalizada (una sentencia)

* Pide una sentencia SQL completa **(una sola)**.
* Si es `SELECT`, muestra filas en tabla.
* Si es `INSERT/UPDATE/DELETE/DDL`, ejecuta y confirma filas afectadas.
* Controla errores (sintaxis, permisos, etc.).

> **Seguridad & control**:
>
> * Acepta **una** sentencia por ejecución (rechaza si detectas `;` extra).
> * No interpolar input del usuario, **no** formatees strings en la sentencia.
> * Para `SELECT`, no impongas límites, pero puedes sugerir `LIMIT`.

---

## 5. Estructura sugerida

```
minigestor_sqlite/
├── main.py           # Programa principal (menú)
├── README.md         # Instrucciones de uso
└── App/
  |─ __init__.py 
  |─ interfaz_usuario.py 
  |─ db_manager.py     # Funciones para conectar y operar con la BD. Utilizar Programación  orientada a objetos.	
  |─ config.py		   # Carga/guardado de o JSON
	

```
## 6. Ejemplo de interacción

```
Motor:
[1] MySQL
> 1

Host: db.miempresa.com
Puerto [5432]: 5432
Usuario: alumno
Contraseña: ****
Base de datos: demo

Conexión OK. Tabla personas lista.

=== MiniGestor Remoto ===
[1] Crear  [2] Listar  [3] Buscar ID  [4] Actualizar  [5] Eliminar
[6] SQL personalizada
[0] Salir
> 6

Introduce UNA sentencia SQL:
> SELECT nombre, edad FROM personas WHERE edad >= 30 ORDER BY edad DESC;

Resultados:
------------------------------------
nombre               | edad
------------------------------------
"María Pérez"        | 45
"Luis Martínez"      | 31
```

---


