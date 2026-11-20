from ast import Delete

import mysql
from data_base import *


if __name__ == "__main__":
    
    #mysql

    mysql_db = MySQLDatabase("root", "", "clase")
    mysql_db.connect()


    # Crear usuario
    alumno = Alumno("juan", "sdf@a.com")

    #Guardar el usuario
    #mysql_db.create(alumno)
    print (mysql_db.read(1))

    mysql_db.delete(7)

    #sqlite
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





    # # Leer usuario
    # resultado = db.read(nuevo_id)

    # print("Usuario:", resultado)

    # # Actualizar usuario
    # usuario["nombre"] = "Ana García"

    # db.update(nuevo_id, usuario)

    # print("Usuario actualizado:", db.read(nuevo_id))

    # # Eliminar usuario
    # db.delete(nuevo_id)

    # print("Usuario eliminado:", db.read(nuevo_id))


    # # Utilizar SQLite
    # db = SQLiteDatabase("usuarios.db")
    # db.connect()

    # gestionar_usuarios(db)

    # db.connection.close()