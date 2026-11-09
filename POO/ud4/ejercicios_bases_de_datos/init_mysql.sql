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