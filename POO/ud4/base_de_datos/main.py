import mysql
from data_base import *


if __name__ == "__main__":
    
    ####mysql###

    mysql_db = MySQLDatabase("root", "", "clase")
    mysql_db.connect()


    # Crear usuario
    alumno = Alumno("juanjoo", "sdf@a.com")

    #Guardar el usuario
    #mysql_db.create(alumno)
    print (mysql_db.read(1))

    mysql_db.delete(7)

    ###sqlite###

    sqlite_db = SQLiteDatabase("clase")
    sqlite_db.connect()

    cursor = sqlite_db.connection.cursor()

    #Comprobamos si exite la tabla alumnos
    cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type = 'table' AND name = 'alumnos'
    """)

    if cursor.fetchone() is None:
        print("La tabla no existe. Creando tabla...")

        cursor.execute("""
            CREATE TABLE alumnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT)
            """)

    # cursor.execute("""
    #     CREATE TABLE alumnos (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         nombre TEXT NOT NULL,
    #         departamento TEXT,
    #         salario REAL
    #     """)

    sqlite_db.create(alumno)

    print (sqlite_db.read(4))
    #print (sqlite_db.delete(3))



#SQL script to create the 'clase' table in MySQL and tables:
'''
-- Crear la base de datos 'clase' si no existe
CREATE DATABASE IF NOT EXISTS clase 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Seleccionar la base de datos 'clase'
USE clase;

-- Crear la tabla 'alumnos'
CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150)
);
'''
