################################ Ejercicio 1

try:
    edad = int(input("Por favor, introduce tu edad: "))

except ValueError:
    print("Error: Debes introducir un número entero válido.")

else:
    if edad >= 18:
        print("¡Bienvenido! Puedes pasar.")
    else:
        print("Acceso denegado.")
finally:
    print("Fin del proceso de control.")


################################ Ejercicio 2

def obtener_producto(inventario, categoria, posicion):
    try:
        producto = inventario[categoria][posicion]
        return f"Producto encontrado: {producto}"

    except (KeyError, IndexError) as e:
        nombre_error = type(e).__name__
        return f"Error de acceso: Categoría o posición no válida ({nombre_error})"

    except Exception as e:
        return f"Error inesperado: {type(e).__name__} - {e}"

stock = {
    "móviles": ["iPhone 15", "Samsung S23", "Pixel 8"],
    "portátiles": ["MacBook Air", "Dell XPS"]
}

print(obtener_producto(stock, "móviles", 1))      
print(obtener_producto(stock, "consolas", 0))     
print(obtener_producto(stock, "móviles", 10))     
print(obtener_producto("no_soy_un_dict", "x", 0)) 

################################ Ejercicio 3

def retirar_dinero(saldo, cantidad):
    if cantidad < 0:
        raise ValueError("No se pueden retirar cantidades negativas.")
    
    if cantidad > saldo:
        raise ValueError(f"Fondos insuficientes para retirar {cantidad}€.")
    
    return saldo - cantidad

try:
    mi_saldo = 100
    print(f"Saldo restante: {retirar_dinero(mi_saldo, 150)}€")
except ValueError as e:
    print(f" Operación cancelada: {e}")

################################ Ejercicio 4

class ErrorConexionServidor(Exception):
    pass

def conectar_db(puerto):
    try:
        puerto_int = int(puerto)
        print(f"Conectando al puerto {puerto_int}...")
    except ValueError as e:
        raise ErrorConexionServidor("Fallo crítico de configuración") from e

try:
    conectar_db(900)
    conectar_db("ochenta")
except ErrorConexionServidor as err:
    print(f"Mensaje: {err}")
    print(f"Causa original: {err.__cause__}") 

################################ Ejercicio 5

def crear_producto(nombre, precio):
    assert precio > 0, f"El precio de {nombre} debe ser positivo"
    return {"nombre": nombre, "precio": precio}

print(crear_producto("Monitor", 150))  
print(crear_producto("Cable", -5))   

################################ Ejercicio 6

class VueloError(Exception):
    """Base para todas las excepciones del sistema de vuelos."""
    pass

class OverbookingError(VueloError):
    """Lanzada cuando no hay asientos disponibles."""
    pass

class VueloCanceladoError(VueloError):
    """Lanzada cuando el número de asientos es incoherente (negativo)."""
    pass

def reservar_asiento(asientos_libres):
    if asientos_libres == 0:
        raise OverbookingError("No quedan asientos libres en este vuelo.")
    if asientos_libres < 0:
        raise VueloCanceladoError("El vuelo ha sido cancelado o los datos son erróneos.")
    print("Asiento reservado con éxito.")

pruebas = [0, -1, 1]

for valor in pruebas:
    try:
        reservar_asiento(valor)
    except OverbookingError as e:
        print(f"Atención específica: {e}")
    except VueloError as e:
        print(f"Error general de vuelo: {e}")