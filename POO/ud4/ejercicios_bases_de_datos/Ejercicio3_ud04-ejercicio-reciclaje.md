# UD4 – Ejercicio 3: “EcoTrack” — Conexión a BD + CRUD en Terminal

---

## 1) Enunciado

Construye una aplicación de **línea de comandos** (interfaz por terminal) llamada **EcoTrack** que permita registrar cuánto material reciclado entra en los **puntos limpios** de una ciudad.

### 1.1 Menú de arranque (configuración de conexión)

Al iniciar, muestra un menú para **elegir el motor de base de datos** y, en su caso, **configurar** la conexión:

1. **Elegir backend**

   * `1) SQLite`
   * `2) MySQL`

2. **Si elige SQLite**

   * Pedir **ruta** del fichero (por ejemplo `./ecotrack.db`).
   * Si no existe, la app puede crearlo automáticamente al ejecutar el script SQL de inicialización.

3. **Si elige MySQL**

   * Pedir: **host/IP**, **puerto**, **usuario**, **contraseña**, **nombre de base de datos**.
   * Probar la conexión y mostrar un mensaje de éxito o error.
   * Guardar la configuración en `config.json`.

> Tras la configuración, la app continuará al **menú CRUD**.

### 1.2 Menú de operaciones (CRUD)

Implementa al menos estas opciones:

* **Materiales**

  * `Crear` material
  * `Listar` materiales
  * `Actualizar` material (por `id`)
  * `Eliminar` material (por `id`)
* **Puntos de reciclaje**

  * `Crear` punto
  * `Listar` puntos
  * `Actualizar` punto (por `id`)
  * `Eliminar` punto (por `id`)
* **Registros de depósito**

  * `Crear` registro (fecha, punto, material, cantidad, fuente)
  * `Listar` registros (con joins para ver nombres de material y punto)
  * `Eliminar` registro (por `id`)
* **Consultas útiles (opcional recomendado)**

  * Total reciclado por **material** en un rango de fechas.
  * Total reciclado por **punto** en un rango de fechas.

> La navegación debe ser sencilla (números + Enter) y con validación básica.
> En cada operación, informa claramente de **éxito/fracaso**.

---

## 2) Modelo de datos

### 2.1 Diagrama (ER/UML en ASCII)

```
+-------------------+           +-------------------+
|      material     | 1       n |  registro_deposito|
+-------------------+-----------+-------------------+
| id (PK)           |           | id (PK)           |
| nombre (UNIQUE)   |           | fecha             |
| categoria         |           | punto_id (FK)     |
| unidad_medida     |           | material_id (FK)  |
| reciclable (bool) |           | cantidad          |
+-------------------+           | fuente (enum)     |
                                +-------------------+
                                         ^
                                         | n
                                         |
                              1          |
+-------------------+--------------------+
|       punto       |
+-------------------+
| id (PK)           |
| nombre            |
| municipio         |
| direccion         |
| lat               |
| lon               |
+-------------------+
```

* **Relaciones**

  * `registro_deposito.material_id → material.id` (N:1)
  * `registro_deposito.punto_id → punto.id` (N:1)

### 2.2 Descripción de tablas

* **material**: tipos de residuos (papel, plástico…) y su categoría.
* **punto**: ubicaciones de los puntos limpios.
* **registro_deposito**: entradas de material en una fecha concreta, con cantidad y fuente (`domiciliario`, `empresa`, `evento`).

---

## 3) Scripts de inicialización (para contenedores)

> Usa estos scripts para **crear el esquema** y **cargar datos de ejemplo**.

### 3.1 SQLite — `init_sqlite.sql`

```sql
PRAGMA foreign_keys = ON;

-- Tablas
CREATE TABLE IF NOT EXISTS material (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL UNIQUE,
  categoria TEXT NOT NULL,
  unidad_medida TEXT NOT NULL DEFAULT 'kg',
  reciclable INTEGER NOT NULL DEFAULT 1 CHECK (reciclable IN (0,1))
);

CREATE TABLE IF NOT EXISTS punto (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  municipio TEXT NOT NULL,
  direccion TEXT,
  lat REAL,
  lon REAL
);

CREATE TABLE IF NOT EXISTS registro_deposito (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fecha TEXT NOT NULL, -- ISO8601 (YYYY-MM-DD HH:MM:SS)
  punto_id INTEGER NOT NULL,
  material_id INTEGER NOT NULL,
  cantidad REAL NOT NULL CHECK (cantidad >= 0),
  fuente TEXT NOT NULL CHECK (fuente IN ('domiciliario','empresa','evento')),
  FOREIGN KEY (punto_id) REFERENCES punto(id),
  FOREIGN KEY (material_id) REFERENCES material(id)
);

-- Datos semilla
INSERT OR IGNORE INTO material (nombre, categoria, unidad_medida, reciclable) VALUES
 ('Papel y cartón','Celulósicos','kg',1),
 ('Plástico','Polímeros','kg',1),
 ('Vidrio','Inorgánicos','kg',1),
 ('RAEE','Electrónicos','kg',1);

INSERT OR IGNORE INTO punto (nombre, municipio, direccion, lat, lon) VALUES
 ('Punto Norte','EcoCiudad','Av. Bosque 12', 40.4167, -3.7033),
 ('Punto Sur','EcoCiudad','Calle Río 45', 40.4000, -3.7100);

INSERT INTO registro_deposito (fecha, punto_id, material_id, cantidad, fuente) VALUES
 ('2025-01-15 10:00:00', 1, 1, 125.50, 'domiciliario'),
 ('2025-02-02 12:30:00', 2, 2, 200.00, 'empresa'),
 ('2025-03-20 09:10:00', 1, 3, 80.75,  'evento');
```

---

### 3.2 MySQL — `init_mysql.sql`

```sql
CREATE DATABASE IF NOT EXISTS ecotrack CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE ecotrack;

CREATE TABLE IF NOT EXISTS material (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL UNIQUE,
  categoria VARCHAR(50) NOT NULL,
  unidad_medida VARCHAR(10) NOT NULL DEFAULT 'kg',
  reciclable TINYINT(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS punto (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  municipio VARCHAR(80) NOT NULL,
  direccion VARCHAR(200),
  lat DECIMAL(9,6),
  lon DECIMAL(9,6)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS registro_deposito (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fecha DATETIME NOT NULL,
  punto_id INT NOT NULL,
  material_id INT NOT NULL,
  cantidad DECIMAL(10,2) NOT NULL CHECK (cantidad >= 0),
  fuente ENUM('domiciliario','empresa','evento') NOT NULL,
  CONSTRAINT fk_registro_punto   FOREIGN KEY (punto_id)   REFERENCES punto(id),
  CONSTRAINT fk_registro_material FOREIGN KEY (material_id) REFERENCES material(id),
  INDEX idx_registro_fecha (fecha),
  INDEX idx_registro_punto (punto_id),
  INDEX idx_registro_material (material_id)
) ENGINE=InnoDB;

INSERT IGNORE INTO material (nombre, categoria, unidad_medida, reciclable) VALUES
 ('Papel y cartón','Celulósicos','kg',1),
 ('Plástico','Polímeros','kg',1),
 ('Vidrio','Inorgánicos','kg',1),
 ('RAEE','Electrónicos','kg',1);

INSERT IGNORE INTO punto (nombre, municipio, direccion, lat, lon) VALUES
 ('Punto Norte','EcoCiudad','Av. Bosque 12', 40.416700, -3.703300),
 ('Punto Sur','EcoCiudad','Calle Río 45', 40.400000, -3.710000);

INSERT INTO registro_deposito (fecha, punto_id, material_id, cantidad, fuente) VALUES
 ('2025-01-15 10:00:00', 1, 1, 125.50, 'domiciliario'),
 ('2025-02-02 12:30:00', 2, 2, 200.00, 'empresa'),
 ('2025-03-20 09:10:00', 1, 3, 80.75,  'evento');
```

---



