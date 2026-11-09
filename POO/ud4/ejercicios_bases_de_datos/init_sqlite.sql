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
