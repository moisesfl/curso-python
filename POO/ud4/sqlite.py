import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect(r"C:\Users\moisesfl\Downloads\bbdd_biblio.bd")
cursor = conexion.cursor()

# Leer el archivo .sql de MySQL
with open(r"C:\Users\moisesfl\Downloads\script_biblioteca.sql", "r", encoding="utf-8") as archivo:
    script_sql = archivo.read()

try:
    # Ejecutar todo el script en SQLite
    cursor.executescript(script_sql)
    conexion.commit()
    print("¡Script ejecutado con éxito!")
except sqlite3.OperationalError as e:
    print(f"Error de compatibilidad: {e}")
finally:
    conexion.close()