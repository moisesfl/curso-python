#Ejercicio 1

intentos_invalidos = 0

while True:
    edad = input("Introduce tu edad: ")

    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("Edad no válida")
        intentos_invalidos += 1

if edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")

print("Intentos inválidos:", intentos_invalidos)


################################################
#Opción sin while true

edad = input("Introduce tu edad: ")
intentos_invalidos = 0

while not edad.isdigit():
    print("Edad no válida")
    intentos_invalidos += 1
    edad = input("Introduce tu edad: ")

edad = int(edad)

if edad < 18:
    print("Menor de edad")
else:
    print("Mayor de edad")

print("Intentos inválidos:", intentos_invalidos)


################################################
#Ejercicio 2

frase = input("Introduce una frase: ").lower()

vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

for letra in frase:
    if letra in vocales:
        vocales[letra] += 1

print("Diccionario:", vocales)

maximo = max(vocales.values())

mas_frecuentes = [v for v, c in vocales.items() if c == maximo]

print("Vocal(es) más frecuente(s):", mas_frecuentes)


################################################
#Otra opción

frase = input("Introduce una frase: ").lower()

#vocales = {v: frase.count(v) for v in "aeiou"}
vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}

for letra in frase:
    if letra in vocales:
        vocales[letra] += 1

print(vocales)

maximo = max(vocales.values())

for v, c in vocales.items():
    if c == maximo:
        print("Vocal más frecuente:", v)


################################################
#Ejercicio 3

datos = ["  Ana ", "luis", "MARIA", "   PeDro", "" , "  "]

nombres = [nombre.strip().capitalize() for nombre in datos if nombre.strip()]

print(nombres)


################################################
#Ejercicio 4

notas = [2, 10, 5, 4, 7, 3, 9]

estado = ["apto" if n >= 5 else "no apto" for n in notas]

print(estado)


################################################
#Ejercicio 5

valores = [3, 3, 5, 2, 2, 9, 1, 5, 7]

unicos = {v for v in valores}

lista = sorted(list(unicos))

for n in lista:
    print(n, "-> cuadrado:", n**2)


################################################
#Ejercicio 6

cuadrados = {n: n**2 for n in range(1,21) if n % 3 == 0}

print(cuadrados)


################################################
#Ejercicio 7

inventario = {"pan":10, "leche":5, "huevos":12}

while True:

    producto = input("Producto (salir para terminar): ")

    if producto == "salir":
        break

    cantidad = int(input("Cantidad: "))

    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

print("Inventario final:", inventario)

total = sum(inventario.values())
print("Total unidades:", total)

producto_max = max(inventario, key=inventario.get)
print("Producto con más unidades:", producto_max)

################################################
#Otra opcion sin while true

inventario = {"pan":10, "leche":5, "huevos":12}
producto = input("Producto (salir para terminar): ").lower()

while producto!="salir":

    cantidad = int(input("Cantidad: "))

    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    
    producto = input("Producto (salir para terminar): ").lower()

print("Inventario final:", inventario)

total = sum(inventario.values())
print("Total unidades:", total)

producto_max = max(inventario, key=inventario.get)
print("Producto con más unidades:", producto_max)


################################################
#Ejercicio 8

nombres = ["Ana", "Luis", "Maria", "Pedro", "Lucia"]

objetivo = input("Nombre a buscar: ")

encontrado = False

for i in range(len(nombres)):

    if nombres[i] == objetivo:
        print("Encontrado en índice:", i)
        encontrado = True
        break

if not encontrado:
    print("No encontrado")


################################################
#Otra opcion

nombres = ["Ana", "Luis", "Maria", "Pepe", "Lucia"]
objetivo = input("Nombre a buscar: ").lower()
encontrado = False

for i, nombre in enumerate(nombres):
    if nombre.lower() == objetivo:
        print(f"Encontrado en el índice: {i}")
        encontrado = True
        break

if not encontrado:
    print("No se encuentra en la lista.")

################################################
#Ejercicio 9

palabras = []
descartadas = 0

for i in range(10):

    palabra = input("Introduce palabra: ")

    if len(palabra) < 3:
        descartadas += 1
        continue

    palabras.append(palabra.lower())

print("Lista final:", palabras)
print("Descartadas:", descartadas)


################################################
#Ejercicio 10

for i in range(1,11):

    if i % 2 == 0:
        continue

    for j in range(1,11):

        if j % 3 == 0:
            continue

        print(i, "x", j, "=", i*j)


################################################
#Ejercicio 11

generador = (n**2 for n in range(1,101))

contador = 0

for valor in generador:

    print(valor)

    contador += 1

    if contador == 10:
        break


################################################
#Ejercicio 12

entradas = ["10", " 20", "30 ", "x", "40.5", "50", "-7", "  "]

numeros = []
descartados = 0

for e in entradas:

    e = e.strip()

    if e == "":
        descartados += 1
        continue

    if e.lstrip("-").isdigit():
        numeros.append(int(e))
    else:
        descartados += 1

print("Lista:", numeros)
print("Suma:", sum(numeros))
print("Descartados:", descartados)

################################################
#Otra opción con dict

entradas = ["10", " 20", "30 ", "x", "40.5", "50", "-7", "  "]

enteros_validos = [int(e) for e in entradas if e.strip().lstrip('-').isdigit() and "." not in e]

descartados = len(entradas) - len(enteros_validos)

print("Lista:", enteros_validos)
print("Suma:", sum(enteros_validos))
print("Descartados:", descartados)


################################################
#Ejercicio 13

numeros = []

for i in range(8):
    n = int(input("Número: "))
    numeros.append(n)

minimo = min(numeros)
maximo = max(numeros)

pares = 0
impares = 0

#pares = len([n for n in numeros if n % 2 == 0])
#impares = 8 - pares

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Mínimo:", minimo)
print("Máximo:", maximo)
print(f"Media: {sum(numeros) / len(numeros):.2f}")
print("Pares:", pares)
print("Impares:", impares)


################################################
#Ejercicio 14

notas = {"Ana": "7", "Luis": "4", "Maria": "10", "Pepe": "5"}

transformado = {nombre.upper(): int(nota) for nombre, nota in notas.items()}

aprobados = {nombre: nota for nombre, nota in transformado.items() if nota >= 5}

print(transformado)
print(aprobados)


################################################
#Ejercicio 15

carrito = {}
errores = 0

entrada = input("Compra (producto,cantidad,precio) o 'fin': ")


while entrada.lower() != "fin":
    
    partes = entrada.split(",")
    
    if len(partes) != 3:
        print("Error: Formato incorrecto (falta una coma o sobran datos).")
        errores += 1
        entrada = input("Compra (producto,cantidad,precio) o 'fin': ")
        continue
        
    nombre, cant, precio = partes
    nombre = nombre.strip()
    cant = cant.strip()
    precio = precio.strip()

    if not nombre:
        print("Error: El nombre del producto no puede estar vacío.")
        errores += 1
        entrada = input("Compra (producto,cantidad,precio) o 'fin': ")
        continue

    if not cant.isdigit() or int(cant) <= 0:
        print("Error: La cantidad debe ser un número entero mayor que 0.")
        errores += 1
        entrada = input("Compra (producto,cantidad,precio) o 'fin': ")
        continue

    precio_limpio = precio.replace(".", "", 1) 
    if not precio_limpio.isdigit() or float(precio) <= 0:
        print("Error: El precio debe ser un número positivo.")
        errores += 1
        entrada = input("Compra (producto,cantidad,precio) o 'fin': ")
        continue

    cant = int(cant)
    precio = float(precio)
    coste_total = cant * precio

    if nombre in carrito:
        carrito[nombre]['cantidad'] += cant
        carrito[nombre]['coste'] += coste_total
    else:
        carrito[nombre] = {'cantidad': cant, 'coste': coste_total}
    
    entrada = input("Compra (producto,cantidad,precio) o 'fin': ")


total_gastado = sum(datos['coste'] for datos in carrito.values())
productos_ordenados = sorted(carrito, key=lambda x: carrito[x]['coste'], reverse=True)

print(f"\nTotal gastado: {total_gastado:.2f}€")
print(f"Líneas descartadas: {errores}")
print(f"Detalle: {carrito}")
print("Productos ordenados por gasto:", productos_ordenados)



#####################################################
#Otra opción

compras = {}
errores = 0

while True:

    linea = input("Introduce compra (producto,cantidad,precio) o fin: ")

    if linea == "fin":
        break

    partes = linea.split(",")

    if len(partes) != 3:
        errores += 1
        continue

    producto, cantidad, precio = partes

    producto = producto.strip()

    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except:
        errores += 1
        continue

    if producto == "" or cantidad <= 0 or precio <= 0:
        errores += 1
        continue

    coste = cantidad * precio

    if producto in compras:
        compras[producto]["cantidad"] += cantidad
        compras[producto]["coste"] += coste
    else:
        compras[producto] = {"cantidad": cantidad, "coste": coste}

total = sum(v["coste"] for v in compras.values())

ordenados = sorted(compras.items(), key=lambda x: x[1]["coste"], reverse=True)

print("Total gastado:", total)
print("Resumen:", compras)
print("Ordenados por coste:", ordenados)
print("Errores:", errores)