############
###SQLITE###
############

##Ejecutar fichero SQL para crear la base de datos 
import sqlite3

# Conectar (si el archivo no existe, lo crea automáticamente)
conexion = sqlite3.connect("reciclaje.db")
cursor = conexion.cursor()

# Leer y ejecutar el archivo SQL
with open("init_sqlite.sql", "r", encoding="utf-8") as archivo_sql:
    script_sql = archivo_sql.read()

cursor.executescript(script_sql)

# Guardar cambios y cerrar
conexion.commit()
conexion.close()
print("Base de datos creada exitosamente desde el script.")



# Conectar a la base de datos
conexion = sqlite3.connect("reciclaje.db")

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute("SELECT direccion FROM punto;")

# Mostrar las tablas en la base de datos
print(cursor.fetchall())

# Cerrar la conexión
conexion.close()

#Ejecutar en la terminal el siguiente comando:
#sqlite3 reciclaje.db < init_sqlite.sql



############
###MYSQL####
############

##Ejecutar fichero SQL para crear la base de datos 
import mysql.connector

# 1. Conectarse al servidor MySQL (sin especificar base de datos)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""  
)

cursor = conexion.cursor()

# 2. Leer el archivo SQL
with open("init_mysql.sql", "r", encoding="utf-8") as archivo:
    script_sql = archivo.read()

# 3. Dividir el script por punto y coma (;) para ejecutar las sentencias una a una
sentencias = script_sql.split(";")

for sentencia in sentencias:
    # Ignorar espacios en blanco o saltos de línea vacíos
    if sentencia.strip():
        cursor.execute(sentencia)

# 4. Guardar cambios y cerrar conexión
conexion.commit()
cursor.close()
conexion.close()

print("¡Script ejecutado con éxito!")


#Ejecutar en la terminal el siguiente comando:
#mysql -u root -p < init_mysql.sql