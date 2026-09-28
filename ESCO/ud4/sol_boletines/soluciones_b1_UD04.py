#Ejercicio 1

def saludar_usuario(nombre, idioma="es"):
    if idioma == "es":
        print(f"¡Hola {nombre}!")
    elif idioma == "en":
        print(f"Hello {nombre}!")
    elif idioma == "fr":
        print(f"Salut {nombre}!")
    else:
        print(f"Idioma no soportado para {nombre}.")

saludar_usuario("Ana")           
saludar_usuario("John", "en")   
saludar_usuario("Pierre", "fr")

############ Otra opcion ############

def saludar_usuario(nombre, idioma="es"):
    saludos = {
        "es": "¡Hola",
        "en": "Hello",
        "fr": "Salut"
    }
    
    prefijo = saludos.get(idioma, "Hola")
    print(f"{prefijo} {nombre}!")

saludar_usuario("Ana","es")
saludar_usuario("Amalia")
saludar_usuario("Pepe","en")

############ Otra opcion ############

def saludar_usuario(nombre, idioma="es"):
    match idioma:
        case "es":
            print(f"¡Hola {nombre}!")
        case "en":
            print(f"Hello {nombre}!")
        case "fr":
            print(f"Salut {nombre}!")
        case _:
            print(f"Hola {nombre} (idioma desconocido)")

saludar_usuario("Ana","it")
saludar_usuario("Eva","fr")

############ Otra opcion ############

def obtener_saludo(nombre, idioma="es") -> str:
    if idioma == "en":
        return f"Hello {nombre}!"
    elif idioma == "fr":
        return f"Salut {nombre}!"
    return f"¡Hola {nombre}!" 

mensaje = obtener_saludo("Ana", "fr")
print(mensaje)


#Ejercicio 2

def calcular_total(precio: float, iva: int = 21) -> float:
    precio_final = precio + (precio * iva / 100)
    return precio_final

resultado = calcular_total(iva=10, precio=100.0)
print(f"Total con IVA: {resultado}€")
resultado_sin_iva = calcular_total(precio=100.0)
print(f"Total con IVA: {resultado_sin_iva}€")


#Ejercicio 3

def analizar_notas(*notas: float) -> bool:
    if not notas:
        print("Error: No se han introducido notas.")
        return False
    
    cantidad = len(notas)
    nota_max = max(notas)
    nota_min = min(notas)
    media = sum(notas) / cantidad
    
    print(f"Total de notas: {cantidad}")
    print(f"Nota más alta: {nota_max} | Nota más baja: {nota_min}")
    print(f"Nota media: {media:.2f}")
    
    return True if media >= 5 else False

aprobado = analizar_notas(4.5, 7.0, 8.5, 3.0)
print(f"¿Ha promocionado?: {aprobado}")

############ Otra opcion ############

def analizar_notas(*notas: float) -> bool:
    notas_validas = [n for n in notas if 0 <= n <= 10]
    
    if not notas_validas:
        return False
        
    cantidad = len(notas_validas)
    nota_max = max(notas_validas)
    nota_min = min(notas_validas)
    media = sum(notas_validas) / cantidad

    print(f"Total de notas: {cantidad}")
    print(f"Media de notas válidas: {media:.2f}")
    print(f"Nota más alta: {nota_max} | Nota más baja: {nota_min}")

    return media >= 5

analizar_notas(7, 8, 15, 4)

#Ejercicio 4

def crear_perfil(nombre, **datos_extra):
    print(f"--- Perfil de {nombre} ---")
    for propiedad, valor in datos_extra.items():
        print(f"{propiedad.capitalize()}: {valor}")

crear_perfil("Ana", edad=25, ciudad="Lugo", profesion="Programadora")

#Ejercicio 5

def limpiar_lista(lista_mixta: list) -> list:
    #limpia =  [x for x in lista_mixta if isinstance(x, (int, float)) and not isinstance(x, bool)]
    limpia = [x for x in lista_mixta if isinstance(x, (int, float)) and type(x) != bool]
    return limpia

mi_lista = ["hola", 10, 3.5, True, [1, 2], 20]
print(f"Lista purgada: {limpiar_lista(mi_lista)}")


############ Otra opcion ############

def limpiar_lista(lista_mixta):
    resultado = []
    for x in lista_mixta:
        if type(x) in [int, float]:
            resultado.append(x)
    return resultado

mi_lista = ["hola", 11, 3.5, True, [1, 2], 20]
print(f"Lista purgada: {limpiar_lista(mi_lista)}")


#Ejercicio 6

def gestionar_stock(producto, *ventas, stock_inicial=100, **info_extra):
    total_vendido = sum(ventas)
    stock_restante = stock_inicial - total_vendido
    
    print(f"\nRESUMEN DE STOCK: {producto}")
    print("-" * 25)

    if total_vendido > stock_inicial:
        print(f" ERROR: No se puede procesar la venta de {producto}.")
        print(f"   Pedido: {total_vendido} | Disponible: {stock_inicial}")
        return

    print(f"Stock inicial: {stock_inicial}")
    print(f"Unidades vendidas: {total_vendido}")
    print(f"Stock actual: {stock_restante}")
    
    if info_extra:
        print("Información adicional:")
        for clave, valor in info_extra.items():
            print(f" - {clave}: {valor}")

gestionar_stock("Teclado", 10, 5, 2, stock_inicial=50, proveedor="Logitech", categoria="Periféricos")
gestionar_stock("Game", 10, 5, 2, stock_inicial=10, proveedor="EA", categoria="Game sports")