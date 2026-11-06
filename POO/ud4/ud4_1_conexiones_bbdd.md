# UD4 - 1. Conexión con Bases de Datos en Python

## Índice de contenidos

*   [CRUD - Conceptos básicos de conexión a bases de datos](#crud-conceptos-basicos-de-conexion-a-bases-de-datos)
    *   [🔹 Definición](#definicion)
    *   [🔹 Ejemplo visual del ciclo CRUD](#ejemplo-visual-del-ciclo-crud)
*   [1. Librerías necesarias](#1-librerias-necesarias)
    *   [Documentación](#documentacion)
        *   [SQLite](#sqlite)
        *   [MySQL](#mysql)
        *   [PostGreSQL](#postgresql)
        *   [MongoDB](#mongodb)
*   [2.Uso de las librerías para gestión de conexión y operaciones CRUD](#2uso-de-las-librerias-para-gestion-de-conexion-y-operaciones-crud)
    *   [Pasos generales](#pasos-generales)
    *   [Cuestiones de seguridad](#cuestiones-de-seguridad)
        *   [¿Qué es el sql injection?](#que-es-el-sql-injection)
        *   [¿Cómo evitamos sql injection?](#como-evitamos-sql-injection)
    *   [🔸 SQLite](#sqlite_1)
    *   [🔸 MySQL](#mysql_1)
    *   [🔸 PostgreSQL](#postgresql_1)
    *   [🔸 MongoDB (NoSQL)](#mongodb-nosql)
*   [3. Comparativa general de las operaciones CRUD](#3-comparativa-general-de-las-operaciones-crud)
*   [4. Prueba simple de instrucciones](#4-prueba-simple-de-instrucciones)
*   [5. Ejemplo de Aplicación](#5-ejemplo-de-aplicacion)
    *   [Clase GestorBD](#clase-gestorbd)
    *   [Ejemplo de uso de la clase](#ejemplo-de-uso-de-la-clase)
*   [Conclusiones](#conclusiones)

_ _ _

# CRUD - Conceptos básicos de conexión a bases de datos[](#crud-conceptos-basicos-de-conexion-a-bases-de-datos "Permanent link")

## 🔹 Definición[](#definicion "Permanent link")

El término **CRUD** proviene del acrónimo inglés de las cuatro operaciones básicas que se pueden realizar sobre una base de datos:

| Letra | Operación | Significado | Ejemplo en SQL |
| --- | --- | --- | --- |
| **C** | **Create** | Crear o insertar datos nuevos | `INSERT INTO ...` |
| **R** | **Read** | Leer o consultar datos existentes | `SELECT ... FROM ...` |
| **U** | **Update** | Actualizar o modificar datos existentes | `UPDATE ... SET ...` |
| **D** | **Delete** | Eliminar datos | `DELETE FROM ...` |

Estas operaciones son comunes a todas las bases de datos, ya sean relacionales (como SQLite, MySQL, PostgreSQL) o NoSQL (como MongoDB).

## 🔹 Ejemplo visual del ciclo CRUD[](#ejemplo-visual-del-ciclo-crud "Permanent link")

```
┌────────────┐
│   CREATE   │  ➜ Inserta nuevos datos
└──────┬─────┘
       │
       ▼
┌────────────┐
│    READ    │  ➜ Consulta y muestra información
└──────┬─────┘
       │
       ▼
┌────────────┐
│   UPDATE   │  ➜ Modifica registros existentes
└──────┬─────┘
       │
       ▼
┌────────────┐
│   DELETE   │  ➜ Elimina registros
└────────────┘
```

![CRUD](https://files.realpython.com/media/What-Are-CRUD-Operations_Watermarked.b243ab2b79cb.jpg)

- - -

# 1. Librerías necesarias[](#1-librerias-necesarias "Permanent link")

| Motor | Librería Python | Instalación |
| --- | --- | --- |
| SQLite | `sqlite3` |  Incluida en Python |
| MySQL | `mysql.connector` | `pip install mysql-connector-python` |
| PostgreSQL | `psycopg2` | `pip install psycopg2` |
| MongoDB | `pymongo` | `pip install pymongo` |



## Documentación[](#documentacion "Permanent link")

### SQLite[](#sqlite "Permanent link")

- Documentación SQLite: [https://sqlite.org](url) 
- Documentación API Python SQLite3: [https://docs.python.org/3/library/sqlite3.html](url)

### MySQL[](#mysql "Permanent link")

- Documentación MySQL: [https://dev.mysql.com/doc/refman/8.4/en/](url) 
- Tutorial guía W3Schools: [https://www.w3schools.com/python/python_mysql_getstarted.asp](url)

### PostGreSQL[](#postgresql "Permanent link")

- Documentación PostgreSQL: [https://www.postgresql.org/docs/](url) 
- Documentación Psycopg (Python postgresql adapter): [https://www.psycopg.org/docs/](url)

### MongoDB[](#mongodb "Permanent link")

- Documentación MongoDB: [https://www.mongodb.com/es/docs/?msockid=325001c78bee654a109816118a966489](url)
- Tutorial guía W3Schools: [https://www.w3schools.com/python/python\_mongodb\_getstarted.asp](url)

- - -

# 2.Uso de las librerías para gestión de conexión y operaciones CRUD[](#2uso-de-las-librerias-para-gestion-de-conexion-y-operaciones-crud "Permanent link")

## Pasos generales[](#pasos-generales "Permanent link")

1) Contectar con la base de datos. 
2) Crear el objeto _cursor_. Representa un objeto de control de operaciones que: 
    - Ejecuta sentencias SQL (cursor.execute(...)) 
    - Recupera resultados (cursor.fetchone(), cursor.fetchall()) 
    - Gestiona parámetros de las consultas. 
3) Crear la query SQL. 
4) Hacer commit (ejecutar la sentencia SQL). 
5) Cerrar la conexión.

## Cuestiones de seguridad[](#cuestiones-de-seguridad "Permanent link")

### ¿Qué es el sql injection?[🔗](#que-es-el-sql-injection "Permanent link")

Consiste en utilizar vulnerabilidades en las páginas web, y otras aplicaciones que interactúan con bases de datos, para introducir instrucciones SQL y así **poder saltarse los controles de autenticación y realizar acciones no autorizadas en el sistema**.

**Ocurre normalmente cuando** se pide al usuario por un input, como su nombre, y el usuario, en lugar de su nombre de usuario, introduce una sentencia SQL que será ejecutada en la base de datos sin ser tenida en cuenta a la hora de programar la web, lo que puede dar lugar a ejecuciones de código SQL no deseadas.

En la siguiente página se puede llevar a cabo a modo de práctica un ataque SQL Injection: [hacksplaining - sql-injection](https://www.hacksplaining.com/exercises/sql-injection#/)

Herramienta online para analizar sitios web en búsqueda de vulnerabilidades de este tipo: [pentest tools - sql injection scanner](https://pentest-tools.com/website-vulnerability-scanning/sql-injection-scanner-online)

Aquí tienes **4 ejemplos claros y didácticos de SQL Injection**, cada uno con **sentencia, explicación y por qué es peligroso**. Están diseñados para que puedas usarlos directamente en apuntes o ejercicios.

- - -

#### 🔥 **1\. Ejemplo clásico: evasión de login**[🔗](#1-ejemplo-clasico-evasion-de-login "Permanent link")

💉 _Inyección en un campo de usuario para saltarse la autenticación_

**Entrada del atacante (campo “usuario”):**

```
' OR '1'='1
```

**Consulta SQL vulnerable:**

```
SELECT * FROM usuarios
WHERE usuario = '' OR '1'='1' AND password = '';
```

##### 🧠 Explicación[🔗](#explicacion "Permanent link")

*   `'1'='1'` es siempre verdadero.
*   La condición completa del `WHERE` se convierte en verdadera para **todas las filas**.
*   El atacante entra sin conocer contraseña.

##### ⚠️ Consecuencia[🔗](#consecuencia "Permanent link")

Acceso total sin credenciales.

- - -

#### 🔥 **2\. Eliminación masiva de datos**[🔗](#2-eliminacion-masiva-de-datos "Permanent link")

💉 _Ataque para borrar contenido completo de una tabla_

**Entrada del atacante (por ejemplo, en un formulario de “nombre”):**

```
'; DROP TABLE empleados; --
```

**SQL final ejecutado en un sistema vulnerable:**

```
SELECT * FROM empleados WHERE nombre = '';
DROP TABLE empleados;
-- ';
```

##### 🧠 Explicación[🔗](#explicacion_1 "Permanent link")

*   El atacante **cierra la consulta legítima** con `';`
*   Inserta una instrucción destructiva: `DROP TABLE empleados;`
*   `--` comenta el resto para evitar errores sintácticos.

##### ⚠️ Consecuencia[🔗](#consecuencia_1 "Permanent link")

La tabla `empleados` desaparece por completo.

- - -

#### 🔥 **3\. Extracción de datos sensibles ignorando filtros**[🔗](#3-extraccion-de-datos-sensibles-ignorando-filtros "Permanent link")

💉 _Ataque para ver toda la tabla saltándose restricciones_

**Entrada del atacante (parámetro “id”):**

```
1 OR 1=1
```

**Consulta vulnerable:**

```
SELECT * FROM cuentas WHERE id = 1 OR 1=1;
```

##### 🧠 Explicación[🔗](#explicacion_2 "Permanent link")

*   El filtro por ID queda inutilizado.
*   `1 OR 1=1` devuelve **todas** las filas de la tabla.

##### ⚠️ Consecuencia[🔗](#consecuencia_2 "Permanent link")

El atacante obtiene la lista completa de cuentas, sueldos, correos, etc.

- - -

#### 🔥 **4\. Ataque UNION para robar otra tabla**[🔗](#4-ataque-union-para-robar-otra-tabla "Permanent link")

💉 _Inyección que combina resultados con tablas sensibles (por ejemplo, contraseñas)_

**Entrada del atacante (campo “nombre”):**

```
' UNION SELECT usuario, password FROM admin; --
```

**SQL resultante:**

```
SELECT nombre, salario FROM empleados
WHERE nombre = ''
UNION
SELECT usuario, password FROM admin;
-- ';
```

##### 🧠 Explicación[🔗](#explicacion_3 "Permanent link")

*   `UNION` permite devolver datos de una segunda consulta.
*   El atacante mezcla la tabla original con `admin`.
*   Los resultados muestran **usuarios y contraseñas** junto a los empleados.

##### ⚠️ Consecuencia[🔗](#consecuencia_3 "Permanent link")

Filtración directa de credenciales.

- - -

### ¿Cómo evitamos sql injection?[🔗](#como-evitamos-sql-injection "Permanent link")

Los ataques de SQL Injection se producen cuando el atacante consigue que la aplicación mezcle datos y código SQL, permitiéndole modificar o ejecutar instrucciones maliciosas. En Python, la protección es sencilla si se siguen cuatro principios fundamentales.

#### ✅ 1. Usar siempre consultas parametrizadas (NUNCA concatenar strings)[🔗](#1-usar-siempre-consultas-parametrizadas-nunca-concatenar-strings "Permanent link")

Este es el método más importante y eficaz.

❌ **Vulnerable**

```
sql = f"SELECT * FROM usuarios WHERE nombre = '{usuario}'"
cursor.execute(sql)
```

✅ **Seguro**

```
cursor.execute(
    "SELECT * FROM usuarios WHERE nombre = ?",
    (usuario,)
)   # SQLite

cursor.execute(
    "SELECT * FROM usuarios WHERE nombre = %s",
    (usuario,)
)   # MySQL / PostgreSQL
```

🧠 **Por qué funciona**

*   Cuando se usa ? o %s, el driver:
*   Escapa caracteres peligrosos.
*   Trata la entrada como dato, no como código.

#### ✅ 2. No interpolar identificadores: usar “listas blancas” (whitelists)[🔗](#2-no-interpolar-identificadores-usar-listas-blancas-whitelists "Permanent link")

Los placeholders no sirven para nombres de columnas o tablas, solo para valores.

❌ Vulnerable

```
cursor.execute(f"SELECT {columna} FROM empleados")
```

✅ Seguro

```
permitidas = {"id", "nombre", "salario"}
if columna in permitidas:
    cursor.execute(f"SELECT {columna} FROM empleados")
```

#### ✅ 3. Validar y sanear todas las entradas del usuario[🔗](#3-validar-y-sanear-todas-las-entradas-del-usuario "Permanent link")

**Comprobar**: - Tipo de dato (int, float, str…) - Longitud (ej. máximo 50 caracteres) - Formatos esperados (ej. email) - Rangos numéricos

**Ejemplo**:

```
def validar_id(x):
    if not str(x).isdigit():
        raise ValueError("ID inválido")
    return int(x)
```

La validación evita valores maliciosos antes de llegar al SQL.

#### ✅ 4. Usar transacciones y manejar errores correctamente[🔗](#4-usar-transacciones-y-manejar-errores-correctamente "Permanent link")

Evita quedar en estados inconsistentes si un ataque intenta romper la consulta.

```
try:
    conn.execute("BEGIN")
    cursor.execute(...)   # operaciones SQL
    conn.commit()
except:
    conn.rollback()
```

- - -

## 🔸 SQLite[](#sqlite_1 "Permanent link")

```
import sqlite3

# 1️ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
      #(si no existe, se crea automáticamente)
conexion = sqlite3.connect("empresa.db")

# 2️ ---  CREACIÓN DEL CURSOR     ------------------------------
cursor = conexion.cursor()

# 3️ ---  OPERACIONES CRUD           ------------------------------

# Crear una TABLA
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    departamento TEXT,
                    salario REAL)''')
conexion.commit()

# CREATE: Insertar un nuevo registro
cursor.execute("INSERT INTO empleados (nombre, departamento, salario) VALUES (?, ?, ?)", ("Ana", "Ventas", 1800))
conexion.commit()

# READ: Consultar registros
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)  # Muestra cada fila de la tabla empleados

# UPDATE: Actualizar un registro
cursor.execute("UPDATE empleados SET salario = ? WHERE nombre = ?", (1900, "Ana"))
conexion.commit()

# DELETE: Eliminar un registro
cursor.execute("DELETE FROM empleados WHERE nombre = ?", ("Ana",))
conexion.commit()

# 4️ --- CERRAR LA CONEXIÓN    -----------------------------------
conexion.close() 
```

- - -

## 🔸 MySQL[](#mysql_1 "Permanent link")

```
import mysql.connector

# 1️ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empleados"
)

# 2️ ---  CREACIÓN DEL CURSOR     ------------------------------
cursor = conexion.cursor()

# 3️ ---  OPERACIONES CRUD           ------------------------------
# Crear una TABLA
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    departamento VARCHAR(100),
                    salario DECIMAL(10, 2))'''
)

# CREATE: Insertar datos
cursor.execute("INSERT INTO empleados (nombre, departamento, salario) VALUES (%s, %s, %s)", ("Luis", "IT", 2200))
conexion.commit()

# READ: Consultar datos
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)  # Muestra los registros existentes

# UPDATE: Modificar un salario
cursor.execute("UPDATE empleados SET salario = %s WHERE nombre = %s", (2300, "Luis"))
conexion.commit()

# DELETE: Borrar un empleado
cursor.execute("DELETE FROM empleados WHERE nombre = %s", ("Luis",))

conexion.commit()

# 4️ --- CERRAR LA CONEXIÓN    -----------------------------------
conexion.close() 
```

- - -

## 🔸 PostgreSQL[](#postgresql_1 "Permanent link")

```
import psycopg2

# 1️ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
conexion = psycopg2.connect(
    host="localhost/IP/url",
    user="postgres",
    password="1234",
    dbname="empresa"
)
# 2️ ---  CREACIÓN DEL CURSOR     ------------------------------
cursor = conexion.cursor()

# 3️ ---  OPERACIONES CRUD           ------------------------------
# CREATE: Insertar un registro
cursor.execute("INSERT INTO empleados (nombre, departamento, salario) VALUES (%s, %s, %s)", ("Marta", "RRHH", 2000))
conexion.commit()

# READ: Consultar registros
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)

# UPDATE: Actualizar un registro
cursor.execute("UPDATE empleados SET salario = %s WHERE nombre = %s", (2100, "Marta"))
conexion.commit()

# DELETE: Eliminar un registro
cursor.execute("DELETE FROM empleados WHERE nombre = %s", ("Marta",))
conexion.commit()

# 4️ --- CERRAR LA CONEXIÓN    -----------------------------------
conexion.close()  
```

- - -

## 🔸 MongoDB (NoSQL)[](#mongodb-nosql "Permanent link")

```
from pymongo import MongoClient

# 1️ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
    #(por defecto puerto 27017)
cliente = MongoClient("mongodb://localhost_o_IP_o_URL:27017/")

# 2️ ---  OPERACIONES CRUD           ------------------------------

#  Crear base de datos y colección
db = cliente["empresa"]
coleccion = db["empleados"]

# CREATE: Insertar un documento
empleado = {"nombre": "Carlos", "departamento": "IT", "salario": 2500}
coleccion.insert_one(empleado)

# READ: Consultar documentos
for doc in coleccion.find():
    print(doc)  # Muestra todos los documentos almacenados

# UPDATE: Actualizar un documento
coleccion.update_one({"nombre": "Carlos"}, {"$set": {"salario": 2700}})

# DELETE: Eliminar documentos
coleccion.delete_one({"nombre": "Carlos"})

# 3 --- CERRAR LA CONEXIÓN    -----------------------------------
cliente.close()  
```

- - -

# 3. Comparativa general de las operaciones CRUD[](#3-comparativa-general-de-las-operaciones-crud "Permanent link")

| Operación | SQLite | MySQL | PostgreSQL | MongoDB |
| --- | --- | --- | --- | --- |
| **Create** | `INSERT INTO ... VALUES (?, ?, ?)` | `INSERT INTO ... VALUES (%s, %s, %s)` | `INSERT INTO ... VALUES (%s, %s, %s)` | `insert_one({})` |
| **Read** | `SELECT * FROM tabla` | `SELECT * FROM tabla` | `SELECT * FROM tabla` | `find({})` |
| **Update** | `UPDATE tabla SET campo=? WHERE id=?` | `UPDATE tabla SET campo=%s WHERE id=%s` | `UPDATE tabla SET campo=%s WHERE id=%s` | `update_one({}, {"$set":{}})` |
| **Delete** | `DELETE FROM tabla WHERE id=?` | `DELETE FROM tabla WHERE id=%s` | `DELETE FROM tabla WHERE id=%s` | `delete_one({})` |

- - -

# 4. Prueba simple de instrucciones[](#4-prueba-simple-de-instrucciones "Permanent link")

Aplicación simple para hacer la prueba de instrucciones básicas de lo que sería la interacción con una base de datos de empleados embebida (sqlite).

```
import sqlite3

# 1️ Conectar o crear base de datos
conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

# 2️ Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    departamento TEXT,
    salario REAL
)
""")

# 3️ Insertar registros
empleados = [
    ("Ana", "Ventas", 1800.50),
    ("Luis", "IT", 2200.75),
    ("Marta", "RRHH", 2000.00),
    ("Carlos", "IT", 2500.00)
]
cursor.executemany("INSERT INTO empleados (nombre, departamento, salario) VALUES (?, ?, ?)", empleados)
conexion.commit()

# 4️ Consultar registros
print("Lista de empleados:")
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)

# 5️ Eliminar empleados con salario bajo
cursor.execute("DELETE FROM empleados WHERE salario < 2000")
conexion.commit()

# 6️ Mostrar datos actualizados
print("\nEmpleados tras la eliminación:")
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)

# 7️ Cerrar conexión
conexion.close()
```

**Output esperado:**

```
Lista de empleados:
(1, 'Ana', 'Ventas', 1800.5)
(2, 'Luis', 'IT', 2200.75)
(3, 'Marta', 'RRHH', 2000.0)
(4, 'Carlos', 'IT', 2500.0)

Empleados tras la eliminación:
(2, 'Luis', 'IT', 2200.75)
(3, 'Marta', 'RRHH', 2000.0)
(4, 'Carlos', 'IT', 2500.0)
```

- - -

# 5. Ejemplo de Aplicación[](#5-ejemplo-de-aplicacion "Permanent link")

A continuación, se encapsula toda la funcionalidad en una clase `GestorBD` que implementa las operaciones CRUD (**Create**, **Read**, **Update**, **Delete**) mediante funciones.

### 🧩 Clase `GestorBD`[🔗](#clase-gestorbd "Permanent link")

```
import sqlite3

class GestorBD:
    """Clase que gestiona la conexión y operaciones CRUD de una base de datos SQLite."""

    def __init__(self, nombre_bd="empresa.db"):
        self.nombre_bd = nombre_bd
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla empleados si no existe."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT,
            salario REAL
        )
        """)
        self.conexion.commit()

    def insertar_empleado(self, nombre, departamento, salario):
        """Inserta un nuevo empleado."""
        self.cursor.execute(
            "INSERT INTO empleados (nombre, departamento, salario) VALUES (?, ?, ?)",
            (nombre, departamento, salario)
        )
        self.conexion.commit()

    def listar_empleados(self):
        """Devuelve todos los empleados."""
        self.cursor.execute("SELECT * FROM empleados")
        return self.cursor.fetchall()

    def eliminar_por_salario(self, limite):
        """Elimina empleados con salario inferior al límite indicado."""
        self.cursor.execute("DELETE FROM empleados WHERE salario < ?", (limite,))
        self.conexion.commit()

    def cerrar(self):
        """Cierra la conexión."""
        self.conexion.close()
```

- - -

### 🧪 Ejemplo de uso de la clase[🔗](#ejemplo-de-uso-de-la-clase "Permanent link")

```
if __name__ == "__main__":
    gestor = GestorBD()

    # Insertar empleados
    gestor.insertar_empleado("Ana", "Ventas", 1800.50)
    gestor.insertar_empleado("Luis", "IT", 2200.75)
    gestor.insertar_empleado("Marta", "RRHH", 2000.00)

    print("📋 Empleados actuales:")
    for e in gestor.listar_empleados():
        print(e)

    gestor.eliminar_por_salario(2000)

    print("\n📋 Tras eliminar salarios bajos:")
    for e in gestor.listar_empleados():
        print(e)

    gestor.cerrar()
```

**🧾 Output esperado:**

```
📋 Empleados actuales:
(1, 'Ana', 'Ventas', 1800.5)
(2, 'Luis', 'IT', 2200.75)
(3, 'Marta', 'RRHH', 2000.0)

📋 Tras eliminar salarios bajos:
(2, 'Luis', 'IT', 2200.75)
(3, 'Marta', 'RRHH', 2000.0)
```

- - -

# 🧠 Conclusiones[🔗](#conclusiones "Permanent link")

*   Todas las bases de datos comparten las operaciones CRUD.
*   En motores relacionales, se usa SQL; en MongoDB, se trabaja con documentos JSON.

[⬆ Ir arriba](#top)