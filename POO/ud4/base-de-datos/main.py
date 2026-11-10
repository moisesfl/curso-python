if if __name__ == "__main__":

    # Crear usuario
    usuario = {
        "nombre": "Ana",
        "email": "ana@ejemplo.com"
    }

    nuevo_id = db.create(usuario)

    print("Usuario creado:", nuevo_id)

    # Leer usuario
    resultado = db.read(nuevo_id)

    print("Usuario:", resultado)

    # Actualizar usuario
    usuario["nombre"] = "Ana García"

    db.update(nuevo_id, usuario)

    print("Usuario actualizado:", db.read(nuevo_id))

    # Eliminar usuario
    db.delete(nuevo_id)

    print("Usuario eliminado:", db.read(nuevo_id))


    # Utilizar SQLite
    db = SQLiteDatabase("usuarios.db")
    db.connect()

    gestionar_usuarios(db)

    db.connection.close()