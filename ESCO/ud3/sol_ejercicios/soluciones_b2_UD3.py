##########################################
#Ejercicio1

numeros = [10, 25, 43, 12, 5, 88, 30]
objetivo = int(input("Introduce el número a buscar: "))
encontrado = False

#Puede usarse enumerate(numeros) para saber posicion y valor
for i in range(len(numeros)):
    if numeros[i] == objetivo:
        print(f"Número encontrado en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print("Número no encontrado")


##########################################
#Ejercicio2

lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] 
objetivo = int(input("Número a buscar (binaria): "))

bajo = 0
alto = len(lista) - 1
encontrado = False

while bajo <= alto:
    medio = (bajo + alto) // 2 
    
    if lista[medio] == objetivo:
        print(f"Número encontrado en la posición {medio}")
        encontrado = True
        break
    elif lista[medio] < objetivo:
        bajo = medio + 1  
    else:
        alto = medio - 1 

if not encontrado:
    print("Número no encontrado")


##########################################
#Ejercicio3

numeros = [2, 7, 11, 15]
objetivo = 9
hallado = False

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] + numeros[j] == objetivo:
            print(f"Índices: {i} y {j}")
            hallado = True
            break 
    if hallado: 
        break

if not hallado:
    print("No existen dos números que sumen el objetivo")

##########################################
#Ejercicio4

cadena = "{[()]}"
pila = []
balanceados = True

parejas = {')': '(', ']': '[', '}': '{'}

for caracter in cadena:
    if caracter in "([{":  
        pila.append(caracter)
    elif caracter in ")]}":
        if not pila or pila.pop() != parejas[caracter]:
            balanceados = False
            break

if balanceados and len(pila) == 0:
    print("Paréntesis balanceados")
else:
    print("Paréntesis no balanceados")

##########################################
#Ejercicio5

texto = "hola mundo entero"
patron = "mundo"

t_len = len(texto)
p_len = len(patron)
encontrado_en = -1

for i in range(t_len - p_len + 1):
    coincide = True
    for j in range(p_len):
        if texto[i + j] != patron[j]:
            coincide = False
            break
    
    if coincide:
        encontrado_en = i
        break

if encontrado_en != -1:
    print(f"Patrón encontrado en la posición {encontrado_en}")
else:
    print("Patrón no encontrado")