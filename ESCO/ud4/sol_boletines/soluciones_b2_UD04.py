################# Ejercicio 1

productos = [("Teclado", 25), ("Ratón", 12), ("Monitor", 150), ("Alfombrilla", 5)]

ordenados = sorted(productos, key=lambda x: x[1], reverse=True)
print(f"Productos de caro a barato: {ordenados}")

################# Ejercicio 2

from functools import reduce

gastos = [12.50, 4.20, 33.0, 9.15, 11.0]

total = reduce(lambda acc, x: acc + x, gastos)

maximo = reduce(lambda acc, x: x if x > acc else acc, gastos)

print(f"Total: {total}€ | Máximo: {maximo}€")

###################################### Otra opcion - no valida

gastos = [12.50, 4.20, 33.0, 9.15, 11.0]

total = 0
for gasto in gastos:
    total += gasto

maximo = gastos[0] 
for gasto in gastos:
    if gasto > maximo:
        maximo = gasto

print(f"Total: {total} | Máximo: {maximo}")

##########################################################

gastos = [12.50, 4.20, 33.0, 9.15, 11.0]

total = sum(gastos)
maximo = max(gastos)

print(f"Total: {total} | Máximo: {maximo}")

################# Ejercicio 3

usuarios = ["  ana  ", "pepe ", "  MARIA", " jUan "]

limpios = list(map(lambda s: s.strip().capitalize(), usuarios))
print(f"Usuarios corregidos: {limpios}")

################# Ejercicio 4

datos = ["ana@gmail.com", "usuario123", "contacto@tienda.es", "info_sin_arroba", "pedro@yahoo.com"]

correos = list(filter(lambda s: "@" in s, datos))
print(f"Correos encontrados: {correos}")

#correos = list(filter(lambda s: s.count("@") == 1, datos))

#correos = list(filter(lambda s: s.find("@") != -1, datos))

################# Ejercicio 5

precios = [100, 250, 50, 15, 400]

finales = list(map(lambda p: p - (p*20/100) if p > 200 else p - (p*5/100), precios))

#finales = list(map(lambda p: p * 0.8 if p > 200 else p * 0.95, precios))
print(f"Precios con descuento: {finales}")

###################################### Otra opcion

precios = [100, 250, 50, 15, 400]

def aplicar_politica_descuento(precio):
    if precio > 200:
        return precio * 0.8
    return precio * 0.95

finales = list(map(aplicar_politica_descuento, precios))
print(finales)

################# Ejercicio 6

alumnos = [{"n": "Ana", "nota": 8}, {"n": "Zoe", "nota": 8}, {"n": "Luis", "nota": 10}, {"n": "Pepe", "nota": 5}]

ranking = sorted(alumnos, key=lambda x: (-x['nota'], x['n']))
print(f"Ranking: {ranking}")

###################################### Otra opcion

alumnos = [{"n": "Ana", "nota": 8}, {"n": "Zoe", "nota": 8}, {"n": "Luis", "nota": 10}, {"n": "Pepe", "nota": 5}]

alumnos_por_nombre = sorted(alumnos, key=lambda x: x['n'])

resultado_final = sorted(alumnos_por_nombre, key=lambda x: x['nota'], reverse=True)

print(resultado_final)

################# Ejercicio 7

emails = ["admin@google.com", "ventas@empresa.es", "soporte@proton.me"]


dominios = list(map(lambda e: e.split("@")[1].split(".")[0], emails))
print(f"Dominios: {dominios}")

###################################### Otra opcion

emails = ["admin@google.com", "ventas@empresa.es", "soporte@proton.me"]

def extraer(email):
    inicio = email.find("@") + 1
    fin = email.find(".", inicio) 
    return email[inicio:fin]

dominios = list(map(extraer, emails))

################# Ejercicio 8

claves = ["123", "Abcdefg1", "password", "Holi12345", "A1"]

seguras = list(filter(lambda s: len(s) > 7 and any(c.isdigit() for c in s), claves))
print(f"Claves seguras: {seguras}")

###################################### Otra opcion

def es_segura(clave):
    if len(clave) <= 7:
        return False
    
    tiene_numero = False
    for caracter in clave:
        if caracter.isdigit():
            tiene_numero = True
            break

    return tiene_numero

claves = ["123", "Abcdefg1", "password", "Holi12345", "A1"]
seguras = list(filter(es_segura, claves))
print(seguras)

################# Ejercicio 9

from functools import reduce

precios = [10.5, 40.0, 100.0, 5.25]

total_carrito = reduce(lambda acc, x: acc + (x - 10 if x > 50 else x), precios, 0)
print(f"Total carrito (con promociones): {total_carrito}€")

################# Ejercicio 10

comentario = "Este servicio es una estafa y una basura total"
prohibidas = ["estafa", "basura", "horrible"]

es_toxico = any(map(lambda p: p in prohibidas, comentario.split()))

print(f"¿Es el comentario tóxico?: {es_toxico}")