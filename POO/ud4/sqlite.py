import sqlite3

class GestorBD:
    """Clase que gestiona la conexión y operaciones CRUD de una base de datos SQLite."""

    def __init__(self, nombre_bd="empresa.db"):
        self.nombre_bd = nombre_bd
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla empleados si no existe."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            departamento TEXT,
            salario REAL
        )
        """)
        self.conexion.commit()

    def insertar_empleado(self, nombre, departamento, salario):
        """Inserta un nuevo empleado."""
        self.cursor.execute(
            "INSERT INTO empleados (nombre, departamento, salario) VALUES (?, ?, ?)",
            (nombre, departamento, salario)
        )
        self.conexion.commit()

    def listar_empleados(self):
        """Devuelve todos los empleados."""
        self.cursor.execute("SELECT * FROM empleados")
        return self.cursor.fetchall()

    def eliminar_por_salario(self, limite):
        """Elimina empleados con salario inferior al límite indicado."""
        self.cursor.execute("DELETE FROM empleados WHERE salario < ?", (limite,))
        self.conexion.commit()

    def cerrar(self):
        """Cierra la conexión."""
        self.conexion.close()




if __name__ == "__main__":
    gestor = GestorBD()

    # Insertar empleados
    gestor.insertar_empleado("Ana", "Ventas", 1800.50)
    gestor.insertar_empleado("Luis", "IT", 2200.75)
    gestor.insertar_empleado("Marta", "RRHH", 2000.00)

    print("📋 Empleados actuales:")
    for e in gestor.listar_empleados():
        print(e)

    gestor.eliminar_por_salario(2000)

    print("\n📋 Tras eliminar salarios bajos:")
    for e in gestor.listar_empleados():
        print(e)

    gestor.cerrar()




# import sqlite3

# # 1️ Conectar o crear base de datos
# conexion = sqlite3.connect("empresa.db")
# cursor = conexion.cursor()

# # 2️ Crear tabla
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS empleados (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nombre TEXT NOT NULL,
#     departamento TEXT,
#     salario REAL
# )
# """)

# # 3️ Insertar registros
# empleados = [
#     ("Ana", "Ventas", 1800.50),
#     ("Luis", "IT", 2200.75),
#     ("Marta", "RRHH", 2000.00),
#     ("Carlos", "IT", 2500.00)
# ]
# cursor.executemany("INSERT INTO empleados (nombre, departamento, salario) VALUES (?, ?, ?)", empleados)
# conexion.commit()

# # 4️ Consultar registros
# print("Lista de empleados:")
# cursor.execute("SELECT * FROM empleados")
# for fila in cursor.fetchall():
#     print(fila)

# # 5️ Eliminar empleados con salario bajo
# cursor.execute("DELETE FROM empleados WHERE salario < 2000")
# conexion.commit()

# # 6️ Mostrar datos actualizados
# print("\nEmpleados tras la eliminación:")
# cursor.execute("SELECT * FROM empleados")
# for fila in cursor.fetchall():
#     print(fila)

# # 7️ Cerrar conexión
# conexion.close()






























# import sqlite3

# # Conectar a la base de datos SQLite
# conexion = sqlite3.connect(r"C:\Users\moisesfl\Downloads\bbdd_biblio.bd")
# cursor = conexion.cursor()

# # Leer el archivo .sql de MySQL
# with open(r"C:\Users\moisesfl\Downloads\script_biblioteca.sql", "r", encoding="utf-8") as archivo:
#     script_sql = archivo.read()

# try:
#     # Ejecutar todo el script en SQLite
#     cursor.executescript(script_sql)
#     conexion.commit()
#     print("¡Script ejecutado con éxito!")
# except sqlite3.OperationalError as e:
#     print(f"Error de compatibilidad: {e}")
# finally:
#     conexion.close()