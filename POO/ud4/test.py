import mysql.connector

# 1️ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empleados"
)

# 2️ ---  CREACIÓN DEL CURSOR     ------------------------------
cursor = conexion.cursor()

# 3️ ---  OPERACIONES CRUD           ------------------------------
# Crear una TABLA
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    departamento VARCHAR(100),
                    salario DECIMAL(10, 2))'''
)

# CREATE: Insertar datos
cursor.execute("INSERT INTO empleados (nombre, departamento, salario) VALUES (%s, %s, %s)", ("Luis", "IT", 2200))
conexion.commit()

# READ: Consultar datos
cursor.execute("SELECT * FROM empleados")
for fila in cursor.fetchall():
    print(fila)  # Muestra los registros existentes

# UPDATE: Modificar un salario
cursor.execute("UPDATE empleados SET salario = %s WHERE nombre = %s", (2300, "Luis"))
conexion.commit()

# DELETE: Borrar un empleado
cursor.execute("DELETE FROM empleados WHERE nombre = %s", ("Luis",))

conexion.commit()

# 4️ --- CERRAR LA CONEXIÓN    -----------------------------------
conexion.close()  