import mysql
from data_base import *


if __name__ == "__main__":

    mysql_db = MySQLDatabase("root", "", "clase")
    mysql_db.connect()



    # Crear usuario
    alumno = Alumno("juan", "sdf@a.com")


    #Guardar el usuario
    #mysql_db.create(alumno)
    print (mysql_db.read(1))




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