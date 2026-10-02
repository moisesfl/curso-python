import mysql.connector



# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="proba"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("¡Conexión exitosa a MySQL!")

# 2. Crear el cursor
cursor = conexion.cursor()

# 3. Ejecutar la consulta para ver los registros de la tabla
cursor.execute("SELECT * FROM trabajador")

# 4. Obtener y mostrar todos los resultados
resultados = cursor.fetchall()
for fila in resultados:
  print(fila)

# 5. Cerrar la conexión
cursor.close()

# Cerrar la conexión al terminar
conexion.close()

