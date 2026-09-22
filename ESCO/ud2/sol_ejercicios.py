#EJERCICIO MIXTO 2

# 1. Creamos un diccionario vacío
compras = {"Fruta":["Manzana"], "Lácteos":["Leche"]}
# 2. Pedimos una acción
accion = input("Acción (agregar, eliminar, ver): ").lower()

# 3. Comprobamos la acción
if accion == "agregar":

    categoria = input("Categoría: ")
    articulo = input("Artículo: ")

    # Operador ternario
    compras[categoria] = compras[categoria] if categoria in compras else []

    ##Comprobación de si el artículo ya existe en la categoría
    # Añadimos el artículo
    compras[categoria].append(articulo)

elif accion == "eliminar":

    categoria = input("Categoría: ")
    articulo = input("Artículo: ")

    # Comprobamos que existe la categoría
    if categoria in compras:

        # Comprobamos que existe el artículo
        if articulo in compras[categoria]:
            compras[categoria].remove(articulo)
        else:
            print("El artículo no existe.")

    else:
        print("La categoría no existe.")

elif accion == "ver":

    # Mostramos el diccionario
    print(compras)

else:
    print("Acción no válida.")


## Comprobamos si el artículo ya existe
# if articulo in compras[categoria]:
#     print("El artículo ya está en la lista.")
# else:
#     compras[categoria].append(articulo)
#     print("Artículo añadido.")