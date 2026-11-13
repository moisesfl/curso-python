import re

import mysql.connector
import sqlite3
from data_base import Database
from dataclasses import dataclass


@dataclass
class Alumno:
  nombre: str
  email: str

class MySQLDatabase(Database):

    def __init__(self, user, password, database, host="localhost"):
        super().__init__(database)

        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    #Crear previamente en MYSQL server la base de datos
    def connect(self):

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            print("Conexión MySQL establecida correctamente.")
            return self.connection

        except mysql.connector.Error as error:
            print(f"Error al conectar con MySQL: {error}")
            self.connection = None
            return None

        except Exception as error:
            print(f"Error inesperado al conectar con MySQL: {error}")
            return None

    def create(self, data: Alumno):

        try:
            if not isinstance(data, Alumno):
                raise ValueError ("Dato no válido")
            
            if self.connection is None:
                raise RuntimeError("No existe una conexión con MySQL.")

            cursor = self.connection.cursor()

            sql = """
                INSERT INTO alumnos (nombre, email)
                VALUES (%s, %s)
            """

            cursor.execute(sql, (data.nombre, data.email))

            self.connection.commit()

            print("Insertado correctamente")

            return cursor.lastrowid

        except mysql.connector.Error as error:
            print(f"Error al insertar el usuario en MySQL: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al insertar el usuario: {error}")
            return None



    def read(self, record_id):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con MySQL.")

            cursor = self.connection.cursor(dictionary=True)

            sql = "SELECT * FROM alumnos WHERE id = %s"

            cursor.execute(sql, (record_id,))

            return cursor.fetchone()

        except mysql.connector.Error as error:
            print(f"Error al consultar el usuario en MySQL: {error}")
            return None

        except Exception as error:
            print(f"Error inesperado al consultar el usuario: {error}")
            return None

    def update(self, record_id, data):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con MySQL.")

            cursor = self.connection.cursor()

            sql = """
                UPDATE usuarios
                SET nombre = %s, email = %s
                WHERE id = %s
            """

            cursor.execute(
                sql,
                (data["nombre"], data["email"], record_id)
            )

            self.connection.commit()

            return cursor.rowcount

        except mysql.connector.Error as error:
            print(f"Error al actualizar el usuario en MySQL: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al actualizar el usuario: {error}")
            return None

    def delete(self, record_id):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con MySQL.")

            cursor = self.connection.cursor()

            sql = "DELETE FROM usuarios WHERE id = %s"

            cursor.execute(sql, (record_id,))

            self.connection.commit()

            return cursor.rowcount

        except mysql.connector.Error as error:
            print(f"Error al eliminar el usuario en MySQL: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al eliminar el usuario: {error}")
            return None


class SQLiteDatabase(Database):

    def __init__(self, database_name):
        super().__init__(database_name)

        self.connection = None

    def connect(self):

        try:
            self.connection = sqlite3.connect(self.database_name)

            # Permite recuperar los registros como diccionarios
            self.connection.row_factory = sqlite3.Row

            print("Conexión SQLite establecida correctamente.")
            return self.connection

        except sqlite3.Error as error:
            print(f"Error al conectar con SQLite: {error}")
            self.connection = None
            return None

        except Exception as error:
            print(f"Error inesperado al conectar con SQLite: {error}")
            return None

    def create(self, data):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con SQLite.")

            cursor = self.connection.cursor()

            sql = """
                INSERT INTO usuarios (nombre, email)
                VALUES (?, ?)
            """

            cursor.execute(sql, (data["nombre"], data["email"]))

            self.connection.commit()

            return cursor.lastrowid

        except sqlite3.Error as error:
            print(f"Error al insertar el usuario en SQLite: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al insertar el usuario: {error}")
            return None

    def read(self, record_id):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con SQLite.")

            cursor = self.connection.cursor()

            sql = "SELECT * FROM usuarios WHERE id = ?"

            cursor.execute(sql, (record_id,))

            resultado = cursor.fetchone()

            return dict(resultado) if resultado else None

        except sqlite3.Error as error:
            print(f"Error al consultar el usuario en SQLite: {error}")
            return None

        except Exception as error:
            print(f"Error inesperado al consultar el usuario: {error}")
            return None

    def update(self, record_id, data):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con SQLite.")

            cursor = self.connection.cursor()

            sql = """
                UPDATE usuarios
                SET nombre = ?, email = ?
                WHERE id = ?
            """

            cursor.execute(
                sql,
                (data["nombre"], data["email"], record_id)
            )

            self.connection.commit()

            return cursor.rowcount

        except sqlite3.Error as error:
            print(f"Error al actualizar el usuario en SQLite: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al actualizar el usuario: {error}")
            return None

    def delete(self, record_id):

        try:
            if self.connection is None:
                raise RuntimeError("No existe una conexión con SQLite.")

            cursor = self.connection.cursor()

            sql = "DELETE FROM usuarios WHERE id = ?"

            cursor.execute(sql, (record_id,))

            self.connection.commit()

            return cursor.rowcount

        except sqlite3.Error as error:
            print(f"Error al eliminar el usuario en SQLite: {error}")
            self.connection.rollback()
            return None

        except Exception as error:
            print(f"Error inesperado al eliminar el usuario: {error}")
            return None