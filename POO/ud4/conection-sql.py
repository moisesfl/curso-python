
import mysql.connector

class GestorBD:
    """Clase que gestiona una base de datos MySQL."""

    def __init__(self, nombre_bd="empresa"):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=nombre_bd
        )

        self.cursor = self.conexion.cursor()

        self.crear_tabla()

    def crear_tabla(self):
        """Crea la tabla empleados si no existe."""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            departamento VARCHAR(50),
            salario DECIMAL(10,2)
        )
        """)

    def insertar_empleado(self, nombre, departamento, salario):
        """Inserta un nuevo empleado."""

        self.cursor.execute(
            "INSERT INTO empleados (nombre, departamento, salario) VALUES (%s, %s, %s)",
            (nombre, departamento, salario)
        )

        self.conexion.commit()

    def listar_empleados(self):
        """Devuelve todos los empleados."""

        self.cursor.execute("SELECT * FROM empleados")

        return self.cursor.fetchall()

    def eliminar_por_salario(self, limite):
        """Elimina empleados con salario inferior al límite."""

        self.cursor.execute(
            "DELETE FROM empleados WHERE salario < %s",
            (limite,)
        )

        self.conexion.commit()

    def cerrar(self):
        """Cierra la conexión."""

        self.cursor.close()
        self.conexion.close()








if __name__ == "__main__":

    gestor = GestorBD()

    # Insertar empleados
    gestor.insertar_empleado("Ana", "Ventas", 1800.50)
    gestor.insertar_empleado("Luis", "IT", 2200.75)
    gestor.insertar_empleado("Marta", "RRHH", 2000.00)

    print("Empleados actuales:")

    for empleado in gestor.listar_empleados():
        print(empleado)

    # Eliminar empleados con salario inferior a 2000
    gestor.eliminar_por_salario(2000)

    print("\nTras eliminar salarios bajos:")

    for empleado in gestor.listar_empleados():
        print(empleado)

    # Cerrar conexión
    gestor.cerrar()





# import mysql.connector

# # 1. Conectar con la base de datos
# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="empresa"
# )

# cursor = conexion.cursor()

# # 2. Crear tabla
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS empleados (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nombre VARCHAR(50) NOT NULL,
#     departamento VARCHAR(50),
#     salario DECIMAL(10,2)
# )
# """)

# # 3. Insertar registros
# empleados = [
#     ("Ana", "Ventas", 1800.50),
#     ("Luis", "IT", 2200.75),
#     ("Marta", "RRHH", 2000.00),
#     ("Carlos", "IT", 2500.00)
# ]

# cursor.executemany(
#     "INSERT INTO empleados (nombre, departamento, salario) VALUES (%s, %s, %s)",
#     empleados
# )

# conexion.commit()

# # 4. Consultar registros
# print("Lista de empleados:")
# cursor.execute("SELECT * FROM empleados")

# for fila in cursor.fetchall():
#     print(fila)

# # 5. Eliminar empleados con salario bajo
# cursor.execute(
#     "DELETE FROM empleados WHERE salario < %s",
#     (2000,)
# )

# conexion.commit()

# # 6. Mostrar datos actualizados
# print("\nEmpleados tras la eliminación:")
# cursor.execute("SELECT * FROM empleados")

# for fila in cursor.fetchall():
#     print(fila)

# # 7. Cerrar conexión
# cursor.close()
# conexion.close()


















# # import mysql.connector

# # # Establecer la conexión
# # conexion = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="",
# #     database="proba"
# # )

# # # Verificar si la conexión fue exitosa
# # if conexion.is_connected():
# #     print("¡Conexión exitosa a MySQL!")

# # # 2. Crear el cursor
# # cursor = conexion.cursor()

# # # 3. Ejecutar la consulta para ver los registros de la tabla
# # cursor.execute("SELECT * FROM trabajador")

# # # 4. Obtener y mostrar todos los resultados
# # resultados = cursor.fetchall()
# # for fila in resultados:
# #   print(fila)

# # # 5. Cerrar la conexión
# # cursor.close()

# # # Cerrar la conexión al terminar
# # conexion.close()

