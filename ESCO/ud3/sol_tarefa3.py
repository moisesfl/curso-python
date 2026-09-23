#SOLUCION TAREFA 3

from time import perf_counter


inventario = [
 {"nombre": "Teclado", "precios": [20.5, 25.0, 18.0], "stock": 15},
 {"nombre": "Ratón", "precios": [10.0, 12.5], "stock": 0},
 {"nombre": "ERROR_LOG", "precios": [], "stock": -1},
 {"nombre": "Monitor", "precios": [150.0, 145.0, 160.0], "stock": 8},
 {"nombre": "Alfombrilla", "precios": [5.0], "stock": 20}
]
umbral_stock_bajo = 5

texto_menu = '''\nMENÚ PRINCIPAL\n1. Añadir producto\n2. Eliminar producto
3. Ejecutar audotoría\n4. Salir\n'''

while True:


    opcion = int(input(texto_menu + "\nIndique el número de la opción: "))

    match opcion:

        # 1. AÑADIR PRODUCTO

        case 1:
            nombre = input("Nombre del producto: ")
            #precios = list(map(float, input("Precios (separados por comas): ").split(',')))
            precios = [float(x) for x in input("Precios (separados por comas): ").split(',')]
            stock = int(input("Stock: "))

            #Comprobamos si el producto ya existe
            producto_existente = False

            for producto in inventario:
                if producto["nombre"].lower() == nombre.lower():
                    producto["stock"] += stock
                    producto["precios"].extend(precios)
                    producto_existente = True
                    print(f"Producto {nombre} ya existe. Se ha actualizado su stock y precios.")
                    break

            if not producto_existente:
                nuevo_producto = {
                    "nombre": nombre,
                    "precios": precios,
                    "stock": stock
                }

                inventario.append(nuevo_producto)
                
                print(f"Producto {nombre} añadido al inventario.")

        # 2. ELIMINAR PRODUCTO

        case 2:
            nombre_a_eliminar = input("Nombre del producto a eliminar: ")

            producto_encontrado = None

            for producto in inventario:
                if producto["nombre"].lower() == nombre.lower():
                    ptoducto_encontrado = producto
                    break

            if producto_encontrado: 
                inventario.remove(producto_encontrado)
                print(f"Producto {nombre_a_eliminar} eliminado del inventario.")
                
            else:
                print(f"Error: producto {nombre_a_eliminar} no encontrado en el inventario.")

        # 3. EJECUTAR AUDITORÍA

        case 3:
            print("Ejecutando auditoría...\n")

            valor_total = 0
            productos_criticos = []

            #Recorrido principal del inventario
    
            for producto in inventario:

                if producto["nombre"] == "ERROR_LOG":
                    print("Saltando registro corrupto.")
                    continue

                if producto["nombre"] == "STOP":
                    print("Registro STOP encontrado. Finalizando auditoría.")
                    break

                # PROCESAMIENTO DE PRECIOS CON ENUMERATE

                if not producto["precios"]:
                    print (f'Error, el producto {producto['nombre']} no tiene precios registrados.')
                    continue
                
                suma = 0

                for i, precio in enumerate(producto["precios"]):
                    print(f"Analizando precio {i} del producto {producto["nombre"]}: {precio} €")
                    suma += precio
                    
                precio_medio = suma / len(producto["precios"])
                print(f"Precio medio del producto {producto["nombre"]}: {precio_medio:.2f} €")

                # VALIDACIÓN DE STOCK CON WHILE

                while producto["stock"] == 0:
                    respuesta = input(f"¿Se han recibido unidade de {producto['nombre']}? (s/n): ").lower()

                    if respuesta == "si":
                        cantidad = int(input("¿Cuántas unidades se han recibido?"))
                        if cantidad > 0:
                            producto ["stock"] += cantidad
                            print (f"stok actualizado"
                                   f"Nuevo stock: {producto["stock"]}")
                        else:
                            print("La cantidad debe se mayor que 0")

                    elif respuesta == "no":

                        print(f"el stock de {producto["nombre"]} se mantiene en 0")
                        break

                    else:
                        print("Respuesta no válida.")
                        
                        
                # CLASIFICACIÓN MEDIANTE OPERADOR TERNARIO

                estado_stock = (
                    "Crítico"
                    if producto["stock"] < umbral_stock_bajo
                    else "Normal"
                )

                print(f"Estado del stock: {estado_stock}")

                # Si es crítico, lo añadimos a la lista
                if estado_stock == "Crítico":
                    productos_criticos.append(producto["nombre"])

                # Calculamos el valor del producto
                valor_producto = precio_medio * producto["stock"]

                valor_total += valor_producto

                print(f"Valor del stock de {producto["nombre"]}: {valor_producto:.2f}€")

        # SALIR

        case 4:
            print("Saliendo del programa.\n")

            

            # Calculamos el valor actual del inventario
            valor_salida = 0

            for producto in inventario:

                # Ignoramos registros sin precios
                if len(producto["precios"]) > 0:

                    precio_medio = (
                        sum(producto["precios"]) / len(producto["precios"])
                    )

                    valor_salida += precio_medio * producto["stock"]

            # Comprensión de listas:
            # obtenemos solamente los nombres de los productos
            nombres_productos = [
                producto["nombre"] for producto in inventario
            ]

            print(f"\nValor total del inventario: {valor_salida:.2f}€")


            nombres_estado_critico = [producto["nombre"] 
                                      for producto in inventario
                                      if producto["stock"] < umbral_stock_bajo]

            print ("\nLista de productos en stock crítico:")
            for i, producto_critico in enumerate(nombres_estado_critico):
                print (f"{i}. {producto_critico}")

            print("Programa finalizado.")

            break

        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")






'''


# ============================================================
# EJERCICIO FINAL - UD03
# Gestión y auditoría de inventario
# ============================================================

# -----------------------------
# DATOS DE PARTIDA
# -----------------------------

inventario = [
    {"nombre": "Teclado", "precios": [20.5, 25.0, 18.0], "stock": 15},
    {"nombre": "Ratón", "precios": [10.0, 12.5], "stock": 0},
    {"nombre": "ERROR_LOG", "precios": [], "stock": -1},
    {"nombre": "Monitor", "precios": [150.0, 145.0, 160.0], "stock": 8},
    {"nombre": "Alfombrilla", "precios": [5.0], "stock": 20}
]

umbral_stock_bajo = 5


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

while True:

    print("\n==============================")
    print("     GESTIÓN DE INVENTARIO")
    print("==============================")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ejecutar auditoría")
    print("4. Salir")
    print("==============================")

    opcion = input("Selecciona una opción: ")

    # --------------------------------------------------------
    # 1. AÑADIR PRODUCTO
    # --------------------------------------------------------

    if opcion == "1":

        nombre = input("Introduce el nombre del producto: ")
        stock = int(input("Introduce el stock inicial: "))
        precio = float(input("Introduce el precio inicial: "))

        # Comprobamos si el producto ya existe
        producto_existente = False

        for producto in inventario:
            if producto["nombre"].lower() == nombre.lower():
                producto["stock"] += stock
                producto["precios"].append(precio)
                producto_existente = True
                print("Producto existente. Se ha actualizado su stock y precio.")
                break

        # Si no existe, creamos un nuevo diccionario
        if not producto_existente:
            nuevo_producto = {
                "nombre": nombre,
                "precios": [precio],
                "stock": stock
            }

            inventario.append(nuevo_producto)

            print("Producto añadido correctamente.")

    # --------------------------------------------------------
    # 2. ELIMINAR PRODUCTO
    # --------------------------------------------------------

    elif opcion == "2":

        nombre_eliminar = input("Introduce el nombre del producto que quieres eliminar: ")

        producto_encontrado = None

        # Búsqueda manual del producto
        for producto in inventario:
            if producto["nombre"].lower() == nombre_eliminar.lower():
                producto_encontrado = producto
                break

        # Si se encuentra, se elimina usando remove
        if producto_encontrado is not None:
            inventario.remove(producto_encontrado)
            print(f"Producto {nombre_eliminar} eliminado correctamente.")
        else:
            print("Error: El producto no existe.")

    # --------------------------------------------------------
    # 3. EJECUTAR AUDITORÍA
    # --------------------------------------------------------

    elif opcion == "3":

        print("\n================================")
        print("       INICIO DE AUDITORÍA")
        print("================================")

        valor_total = 0
        productos_criticos = []

        # ----------------------------------------------------
        # Recorrido principal del inventario
        # ----------------------------------------------------

        for producto in inventario:

            nombre = producto["nombre"]

            # Si encontramos un registro corrupto, lo ignoramos
            if nombre == "ERROR_LOG":
                print("⚠ Saltando registro corrupto...")
                continue

            # Si encontramos STOP, detenemos la auditoría
            if nombre == "STOP":
                print("⛔ Registro STOP encontrado. Finalizando auditoría.")
                break

            print(f"\n--- Analizando {nombre} ---")

            # ------------------------------------------------
            # PROCESAMIENTO DE PRECIOS CON ENUMERATE
            # ------------------------------------------------

            precios = producto["precios"]

            # Comprobamos que el producto tenga precios
            if len(precios) == 0:
                print("Error: el producto no tiene precios.")
                continue

            suma_precios = 0

            for indice, precio in enumerate(precios):
                print(
                    f"Analizando precio {indice} del producto "
                    f"{nombre}: {precio}€"
                )

                suma_precios += precio

            # Calculamos el precio medio
            precio_medio = suma_precios / len(precios)

            print(f"Precio medio de {nombre}: {precio_medio:.2f}€")

            # ------------------------------------------------
            # VALIDACIÓN DE STOCK CON WHILE
            # ------------------------------------------------

            while producto["stock"] == 0:

                respuesta = input(
                    f"¿Se han recibido unidades de {nombre}? (si/no): "
                ).lower()

                if respuesta == "si":

                    cantidad = int(
                        input("¿Cuántas unidades se han recibido?: ")
                    )

                    if cantidad > 0:
                        producto["stock"] += cantidad
                        print(
                            f"Stock actualizado. "
                            f"Nuevo stock: {producto['stock']}"
                        )
                    else:
                        print("La cantidad debe ser mayor que 0.")

                elif respuesta == "no":

                    print(f"El stock de {nombre} se mantiene en 0.")
                    break

                else:
                    print("Respuesta no válida. Escribe 'si' o 'no'.")

            # ------------------------------------------------
            # CLASIFICACIÓN MEDIANTE OPERADOR TERNARIO
            # ------------------------------------------------

            estado_stock = (
                "Crítico"
                if producto["stock"] < umbral_stock_bajo
                else "Normal"
            )

            print(f"Estado del stock: {estado_stock}")

            # Si es crítico, lo añadimos a la lista
            if estado_stock == "Crítico":
                productos_criticos.append(nombre)

            # Calculamos el valor del producto
            valor_producto = precio_medio * producto["stock"]

            valor_total += valor_producto

            print(f"Valor del stock de {nombre}: {valor_producto:.2f}€")

        # ----------------------------------------------------
        # RESUMEN DE LA AUDITORÍA
        # ----------------------------------------------------

        print("\n================================")
        print("       RESUMEN DE AUDITORÍA")
        print("================================")

        print(f"Valor total del inventario: {valor_total:.2f}€")

        print("\nProductos en estado Crítico:")

        if len(productos_criticos) > 0:
            for nombre in productos_criticos:
                print(f"- {nombre}")
        else:
            print("- Ninguno")

    # --------------------------------------------------------
    # 4. SALIR
    # --------------------------------------------------------

    elif opcion == "4":

        print("\n================================")
        print("       SALIDA DEL PROGRAMA")
        print("================================")

        # Calculamos el valor actual del inventario
        valor_salida = 0

        for producto in inventario:

            # Ignoramos registros sin precios
            if len(producto["precios"]) > 0:

                precio_medio = (
                    sum(producto["precios"]) / len(producto["precios"])
                )

                valor_salida += precio_medio * producto["stock"]

        # Comprensión de listas:
        # obtenemos solamente los nombres de los productos
        nombres_productos = [
            producto["nombre"] for producto in inventario
        ]

        print("\nProductos en el inventario:")

        for nombre in nombres_productos:
            print(f"- {nombre}")

        print(f"\nValor total del inventario: {valor_salida:.2f}€")
        print("Programa finalizado.")

        break

    # --------------------------------------------------------
    # OPCIÓN NO VÁLIDA
    # --------------------------------------------------------

    else:
        print("Error: opción no válida. Introduce un número del 1 al 4.")
'''