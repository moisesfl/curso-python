# ==============================================================================
# TAREA ENTREGABLE – UD04: SISTEMA INTELIGENTE DE GESTIÓN "STREAMIFY PRO"
# ==============================================================================

from functools import reduce

# DATOS DE PARTIDA
usuarios = [
    {"email": "juan@gmail.com", "plan": "estándar", "precio": 9.99, "meses": 12},
    {"email": "marta@yahoo.es", "plan": "premium", "precio": 15.99, "meses": 5},
    {"email": "pedro_sin_arroba", "plan": "estándar", "precio": 9.99, "meses": 2},
    {"email": "ana@gmail.com", "plan": "premium", "precio": 15.99, "meses": 24},
    {"email": "info@empresa.com", "plan": "básico", "precio": 5.99, "meses": 1}
]

DESCUENTO_FIDELIDAD = 0.20

# Nota: Adaptado para coincidir con la lógica y ejemplo de la práctica (packs y servicios)
servicios_adicionales = ["Cloud-Storage", ["Music-Pass", "Video-4K"], "Gaming-Hub", ["VPN", "Secure-Login"]]


# ==============================================================================
# 2. SANEAMIENTO DE DATOS (filter + lambda)
# ==============================================================================
def sanear_usuarios(lista_usuarios):
    """
    Filtra los usuarios eliminando aquellos cuyo email no contenga '@'.
    
    Parámetros:
        lista_usuarios (list): Lista de diccionarios con la información de los usuarios.
        
    Devuelve:
        tuple: (usuarios_validos [list], eliminados [int])
    """
    print("\n[EJECUTANDO FILTRADO...]")
    
    # Identificar y mostrar los eliminados para cumplir con la salida esperada
    eliminados = list(filter(lambda u: "@" not in u["email"], lista_usuarios))
    for elim in eliminados:
        print(f"- Registro eliminado: '{elim['email']}' (Email inválido)")
        
    # Filtrar usuarios válidos usando filter y una función lambda
    usuarios_validos = list(filter(lambda u: "@" in u["email"], lista_usuarios))
    
    print("Saneamiento completado:")
    print(f"- Usuarios originales: {len(lista_usuarios)}")
    print(f"- Usuarios válidos: {len(usuarios_validos)}")
    
    print("\nLista de emails listos:")
    for i, user in enumerate(usuarios_validos, 1):
        print(f"{i}. {user['email']}")
        
    return usuarios_validos, len(eliminados)


# ==============================================================================
# 3. AUDITORÍA DE INGRESOS Y SERVICIOS (reduce + recursividad)
# ==============================================================================
def calcular_precio_usuario(usuario):
    """Calcula el precio final aplicando descuento si lleva más de 10 meses."""
    if usuario["meses"] > 10:
        return usuario["precio"] * (1 - DESCUENTO_FIDELIDAD)
    return usuario["precio"]


def auditar_ingresos_servicios(lista_usuarios, servicios):
    """
    Calcula los ingresos mensuales y anuales usando reduce y lambdas, 
    y cuenta de forma recursiva los servicios individuales (incluyendo anidados).
    
    Parámetros:
        lista_usuarios (list): Lista de usuarios válidos.
        servicios (list): Lista de servicios y packs de servicios.
        
    Devuelve:
        None (Muestra directamente el informe por pantalla).
    """
    print("\n[GENERANDO INFORME DE AUDITORÍA...]")
    
    # Calcular ingresos mensuales reales aplicando descuento mediante map + reduce y lambda
    precios_finales = list(map(lambda u: calcular_precio_usuario(u), lista_usuarios))
    #ingresos_mensuales = reduce(lambda acc, precio: acc + precio, precios_finales, 0)
    ingresos_mensuales = sum(precios_finales)
    ingresos_anuales = ingresos_mensuales * 12

    # Función recursiva interna para aplanar y contar servicios
    def aplanar_y_contar(lista_servs):
        """Función recursiva para recorrer listas anidadas de servicios."""
        contador = 0
        elementos_planos = []
        for item in lista_servs:
            if isinstance(item, list):
                sub_cont, sub_elems = aplanar_y_contar(item)
                contador += sub_cont
                elementos_planos.extend(sub_elems)
            else:
                contador += 1
                elementos_planos.append(item)
        return contador, elementos_planos

    total_servicios, lista_plana = aplanar_y_contar(servicios)

    print("\nRESUMEN FINANCIERO (Precios con Dto.):")
    print(f"- Ingresos Mensuales Reales: {ingresos_mensuales:.2f}€")
    print(f"- Proyección Ingresos Anuales: {ingresos_anuales:.2f}€")

    print("\nANÁLISIS TÉCNICO DE SERVICIOS:")
    print(f"- Se han detectado {total_servicios} servicios individuales en los packs activos.")
    print(f"(Desglose: {', '.join(lista_plana)})")
    print("\nEstado de la auditoría: COMPLETA")


# ==============================================================================
# 4. CLASIFICACIÓN (sorted + tuplas)
# ==============================================================================
def clasificar_usuarios(lista_usuarios):
    """
    Ordena jerárquicamente a los usuarios primero por plan (A-Z) 
    y en caso de empate por antigüedad (meses) de mayor a menor.
    
    Parámetros:
        lista_usuarios (list): Lista de usuarios válidos.
        
    Devuelve:
        list: Lista ordenada de usuarios.
    """
    print("\n[GENERANDO CLASIFICACIÓN POR PRIORIDAD...]")
    
    # Ordenación utilizando sorted con una clave basada en tuplas:
    # 1. plan (ascendente, de la A a la Z)
    # 2. meses (descendente, usando -u["meses"])
    usuarios_ordenados = sorted(
        lista_usuarios, 
        key=lambda u: (u["plan"], -u["meses"])
    )
    
    print("\nLISTA DE CLIENTES ORDENADA:")
    for i, user in enumerate(usuarios_ordenados, 1):
        # Capitalizamos el plan para que estético coincida con el ejemplo
        plan_formateado = user["plan"].capitalize()
        print(f"{i}. [{plan_formateado}] - {user['email']} ({user['meses']} meses)")
        
    print("\nLista clasificada por Plan y Antigüedad (Descendente).")
    return usuarios_ordenados


# ==============================================================================
# 5. ENVIAR FACTURAS (recursividad)
# ==============================================================================
def enviar_avisos(lista_clientes_procesados):
    """
    Función recursiva que procesa el envío de facturas notificando 
    el precio cobrado y el ahorro por fidelidad de cada cliente.
    
    Parámetros:
        lista_clientes_procesados (list): Lista de clientes a notificar.
    """
    # Condición base de la recursividad: si la lista está vacía, termina
    if not lista_clientes_procesados:
        print("\nProceso de envío finalizado con éxito. ------------------------------------------")
        return

    # Extraer el primer cliente de la lista
    cliente = lista_clientes_procesados[0]
    
    # Calcular precio final y ahorro
    if cliente["meses"] > 10:
        precio_final = cliente["precio"] * (1 - DESCUENTO_FIDELIDAD)
        ahorro = cliente["precio"] * DESCUENTO_FIDELIDAD
        detalle_descuento = f"(Ahorro: {ahorro:.2f}€ por fidelidad)"
    else:
        precio_final = cliente["precio"]
        detalle_descuento = "(Sin descuento aplicado)"

    print(f">> Factura enviada a: {cliente['email']} Cobrado: {precio_final:.2f}€ | {detalle_descuento}")

    # Llamada recursiva con el resto de la lista (excluyendo el primero)
    enviar_avisos(lista_clientes_procesados[1:])


# ==============================================================================
# 1. MENÚ DE CONTROL (while + match-case)
# ==============================================================================
def main():
    """Función principal que controla el flujo de ejecución mediante un menú interactivo."""
    usuarios_validos = list(filter(lambda u: "@" in u["email"], usuarios)) # Estado inicial válido por defecto para las opciones
    
    while True:
        print("\n==========================================")
        print("     SISTEMA DE GESTIÓN STREAMIFY PRO     ")
        print("==========================================")
        print("1. Saneamiento de datos")
        print("2. Auditoría de Ingresos y Servicios")
        print("3. Clasificación")
        print("4. Enviar Facturas")
        print("5. Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        match opcion:
            case "1":
                usuarios_validos, _ = sanear_usuarios(usuarios)
            case "2":
                auditar_ingresos_servicios(usuarios_validos, servicios_adicionales)
            case "3":
                clasificar_usuarios(usuarios_validos)
            case "4":
                print("\n[INICIANDO ENVÍO RECURSIVO DE FACTURAS...]")
                enviar_avisos(usuarios_validos)
            case "5":
                print("\nCerrando sistema... ¡Gracias por usar Streamify Pro!")
                break
            case _:
                print("\n❌ Opción no válida. Por favor, introduzca un número del 1 al 5.")


if __name__ == "__main__":
    main()