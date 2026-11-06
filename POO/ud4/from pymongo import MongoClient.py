from pymongo import MongoClient

# 1️⃣ ---  CONEXIÓN CON LA BASE DE DATOS ------------------------
    #(por defecto puerto 27017)
cliente = MongoClient("mongodb://localhost_o_IP_o_URL:27017/")

# 2️⃣ ---  OPERACIONES CRUD           ------------------------------

#  Crear base de datos y colección
db = cliente["empresa"]
coleccion = db["empleados"]

# CREATE: Insertar un documento
empleado = {"nombre": "Carlos", "departamento": "IT", "salario": 2500}
coleccion.insert_one(empleado)

# READ: Consultar documentos
for doc in coleccion.find():
    print(doc)  # Muestra todos los documentos almacenados

# UPDATE: Actualizar un documento
coleccion.update_one({"nombre": "Carlos"}, {"$set": {"salario": 2700}})

# DELETE: Eliminar documentos
coleccion.delete_one({"nombre": "Carlos"})

# 4️⃣ --- CERRAR LA CONEXIÓN    -----------------------------------
cliente.close()  
