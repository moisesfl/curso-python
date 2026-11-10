
import mysql.connector
import sqlite3
from base import Database


class MySQLDatabase(Database):

    def __init__(self, user, password, database, host="localhost"):
        super().__init__(database)

        self.host = host
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):

        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database_name
        )

        return self.connection

    def create(self, data):

        cursor = self.connection.cursor()

        sql = """
            INSERT INTO usuarios (nombre, email)
            VALUES (%s, %s)
        """

        cursor.execute(sql, (data["nombre"], data["email"]))

        self.connection.commit()

        return cursor.lastrowid

    def read(self, record_id):

        cursor = self.connection.cursor(dictionary=True)

        sql = "SELECT * FROM usuarios WHERE id = %s"

        cursor.execute(sql, (record_id,))

        return cursor.fetchone()

    def update(self, record_id, data):

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

    def delete(self, record_id):

        cursor = self.connection.cursor()

        sql = "DELETE FROM usuarios WHERE id = %s"

        cursor.execute(sql, (record_id,))

        self.connection.commit()

        return cursor.rowcount






class SQLiteDatabase(Database):

    def __init__(self, database_name):
        super().__init__(database_name)

        self.connection = None

    def connect(self):

        self.connection = sqlite3.connect(self.database_name)

        # Permite recuperar los registros como diccionarios
        self.connection.row_factory = sqlite3.Row

        return self.connection

    def create(self, data):

        cursor = self.connection.cursor()

        sql = """
            INSERT INTO usuarios (nombre, email)
            VALUES (?, ?)
        """

        cursor.execute(sql, (data["nombre"], data["email"]))

        self.connection.commit()

        return cursor.lastrowid

    def read(self, record_id):

        cursor = self.connection.cursor()

        sql = "SELECT * FROM usuarios WHERE id = ?"

        cursor.execute(sql, (record_id,))

        resultado = cursor.fetchone()

        return dict(resultado) if resultado else None

    def update(self, record_id, data):

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

    def delete(self, record_id):

        cursor = self.connection.cursor()

        sql = "DELETE FROM usuarios WHERE id = ?"

        cursor.execute(sql, (record_id,))

        self.connection.commit()

        return cursor.rowcount
