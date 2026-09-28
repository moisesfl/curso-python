################### Ejercicio 1

def cuenta_atras(n: int):
    if n == 0:
        print("¡Despegue!") 
    else:
        print(n)
        cuenta_atras(n - 1) 

cuenta_atras(990)

################### Ejercicio 2

def sumar_digitos(n: int) -> int:
    if n < 10: 
        return n 
    return (n % 10) + sumar_digitos(n // 10)

print(sumar_digitos(2834))

################################## Otra opcion

def sumar_digitos_texto(n: int) -> int:
    s = str(n)
    
    if len(s) == 1:
        return int(s)
    
    return int(s[0]) + sumar_digitos_texto(int(s[1:]))

print(sumar_digitos_texto(123))

################### Ejercicio 3

def contar_caracter(cadena, caracter):
    if not cadena: 
        return 0 
    
    coincide = 1 if cadena[0] == caracter else 0
    return coincide + contar_caracter(cadena[1:], caracter)

print(contar_caracter("banana", "a"))

################################## Otra opcion


def contar_caracter_split(cadena, caracter):
    if not cadena:
        return 0
    
    trozos = cadena.split(caracter)
    return len(trozos) - 1

print(contar_caracter_split("banana", "a"))

################### Ejercicio 4

def contar_numeros(lista):
    total = 0
    for elemento in lista:
        if isinstance(elemento, list):
            total += contar_numeros(elemento)
        else:
            total += 1
    return total

print(contar_numeros([1, [2, [1,3,4]], 4, [5]]))

################################## Otra opcion

def contar_recursivo_puro(lista):
    if not lista:
        return 0 
    
    primero = lista[0]
    resto = lista[1:]
    
    if isinstance(primero, list):
        return contar_recursivo_puro(primero) + contar_recursivo_puro(resto)
    else:
        return 1 + contar_recursivo_puro(resto)

print(contar_recursivo_puro([1, [2, 3], 4, [5]])) 

################################## Otra opcion

def aplanar(lista):
    resultado = []
    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(aplanar(elemento))
        else: 
            resultado.append(elemento)
    return resultado

mi_lista = [1, [2, 3], 4, [5]]
print(len(aplanar(mi_lista))) 