"""
SOLUCIONARIO OFICIAL EXAMEN CASO PRÁCTICO: ECOCHARGE NETWORKS
Módulo Profesional: Estructuras de Control en Python (Código BOE: 5099)
"""

from functools import reduce

# ==============================================================================
# DATOS DE ENTRADA (CONTEXTO DEL SISTEMA)
# ==============================================================================
REGISTROS_TELEMETRIA = [
    {"id_sesion": "SES-101", "cliente": "VIP", "conector": "CCS2", "kw_h": 45.5, "duracion_min": 30, "hora": 14, "activa": True},
    {"id_sesion": "SES-102", "cliente": "ESTANDAR", "conector": "CHADEMO", "kw_h": -12.0, "duracion_min": 15, "hora": 9, "activa": False},
    {"id_sesion": "SES-103", "cliente": "FLOTA", "conector": "MENNEKES", "kw_h": 22.0, "duracion_min": 120, "hora": 23, "activa": True},
    {"id_sesion": "SES-104", "cliente": "ESTANDAR", "conector": "CCS2", "kw_h": 60.0, "duracion_min": 40, "hora": 18, "activa": True},
    {"id_sesion": "CORRUPTO", "cliente": "DESCONOCIDO"},
    {"id_sesion": "SES-105", "cliente": "VIP", "conector": "SCHUKO", "kw_h": 11.5, "duracion_min": 90, "hora": 2, "activa": True}
]

# ==============================================================================
# APARTADO 1: TARIFICACIÓN DINÁMICA (MATCH-CASE Y TERNARIO)
# ==============================================================================
def calcular_tarifa_kwh(conector: str, hora: int) -> float | None:
    """Calcula la tarifa base por kWh según el conector y la hora empleando match-case."""
    match conector:
        case "CCS2" | "CHADEMO" if 17 <= hora <= 21:
            return 0.45 + 0.15  # Recargo hora punta
        case "CCS2" | "CHADEMO":
            return 0.45
        case "MENNEKES":
            return 0.25
        case "SCHUKO" if 0 <= hora <= 6:
            return max(0.0, 0.15 - 0.05)  # Descuento hora valle
        case "SCHUKO":
            return 0.15
        case _:
            return None

def calcular_precio_final(conector: str, hora: int, tipo_cliente: str) -> float | None:
    """Aplica el descuento por cliente mediante operador ternario sobre la tarifa base."""
    tarifa_base = calcular_tarifa_kwh(conector, hora)
    if tarifa_base is None:
        return None
    
    # Operador ternario: 10% de descuento para clientes VIP o FLOTA
    precio_final = tarifa_base * 0.90 if tipo_cliente in ("VIP", "FLOTA") else tarifa_base
    return round(precio_final, 4)

# ==============================================================================
# APARTADO 2: LIMPIEZA Y COMPRENSIONES (LIST, SET, DICT COMPREHENSIONS)
# ==============================================================================
def auditar_y_filtrar_datos(lote: list[dict]):
    """Demuestra la iteración segura con enumerate() y filtrado con comprensiones."""
    print("--- 1. Recorrido Seguro con enumerate() ---")
    for idx, reg in enumerate(lote):
        # Validación segura evitando IndexError y while True infinito
        id_ses = reg.get("id_sesion", "DESCONOCIDO")
        print(f"Registro [{idx}]: ID={id_ses}")

    # List Comprehension con condición de filtrado
    sesiones_validas = [
        reg for reg in lote
        if "kw_h" in reg and "activa" in reg and reg["kw_h"] > 0 and reg["activa"] is True
    ]

    # Set Comprehension para obtener conectores únicos
    conectores_unicos = {reg["conector"] for reg in sesiones_validas if "conector" in reg}

    # Dict Comprehension para resumen de sesiones de alto consumo (> 20 kWh)
    resumen_kw = {reg["id_sesion"]: reg["kw_h"] for reg in sesiones_validas if reg["kw_h"] > 20.0}

    return sesiones_validas, conectores_unicos, resumen_kw

# ==============================================================================
# APARTADO 3: ARQUITECTURA FUNCIONAL Y TRANSFORMACIONES LAMBDA
# ==============================================================================
def generar_informe_sesiones(titulo: str, *sesiones, **configuraciones) -> str:
    """Genera un informe con firma flexible (*args, **kwargs) respetando la inmutabilidad."""
    moneda = configuraciones.get("moneda", "EUR")
    
    if not sesiones:
        return f"=== {titulo} ===\nNo hay sesiones registradas."

    # Inmutabilidad: Se trabaja con las estructuras recibidas sin modificarlas
    total_kwh = sum(s["kw_h"] for s in sesiones)
    media_duracion = sum(s["duracion_min"] for s in sesiones) / len(sesiones)

    return (f"=== {titulo} ===\n"
            f"Sesiones Procesadas: {len(sesiones)}\n"
            f"Energía Total: {total_kwh:.2f} kWh\n"
            f"Duración Media: {media_duracion:.1f} min\n"
            f"Moneda de Facturación: {moneda}")

def ejecutar_transformaciones_lambda(sesiones_validas: list[dict]):
    """Demuestra el uso de filter, map, sorted y reduce con funciones lambda."""
    # 1. Filter: Cargas de alta potencia (>= 30 kWh)
    altas_cargas = list(filter(lambda s: s["kw_h"] >= 30.0, sesiones_validas))

    # 2. Map: Cálculo del costo total por sesión
    costos = list(map(
        lambda s: round(s["kw_h"] * (calcular_precio_final(s["conector"], s["hora"], s["cliente"]) or 0.0), 2),
        sesiones_validas
    ))

    # 3. Sorted: Ordenación multicriterio (-kw_h, +duracion_min)
    ordenadas = sorted(sesiones_validas, key=lambda s: (-s["kw_h"], s["duracion_min"]))

    # 4. Reduce: Suma acumulada de kWh consumidos
    consumos = [s["kw_h"] for s in sesiones_validas]
    total_acumulado = reduce(lambda acc, x: acc + x, consumos, 0.0)

    return altas_cargas, costos, ordenadas, total_acumulado

# ==============================================================================
# APARTADO 4: ALGORITMO RECURSIVO DE POTENCIA
# ==============================================================================
RED_DISTRIBUCION = [
    15.5,
    [22.0, 45.0, [10.5, 60.0]],
    [30.0, [12.5, [5.0, 18.0]]],
    8.0
]

def calcular_potencia_recursiva(red: list | float | int) -> float:
    """Calcula la potencia acumulada en una red jerárquica anidada de forma recursiva."""
    # CASO BASE 1: Si se recibe un número directo (hoja del árbol)
    if isinstance(red, (int, float)):
        return float(red)
    
    # CASO BASE 2: Lista vacía
    if not red:
        return 0.0

    # PASO RECURSIVO: Procesar el primer elemento y sumar recursivamente el resto
    primer_elemento = red[0]
    resto_lista = red[1:]

    return calcular_potencia_recursiva(primer_elemento) + calcular_potencia_recursiva(resto_lista)

"""
TRAZA MANUAL DE LLAMADAS PARA LA SUBLISTA [10.5, 60.0]:
1. calcular_potencia_recursiva([10.5, 60.0])
   -> primer_elemento = 10.5, resto = [60.0]
   -> Llama a calcular_potencia_recursiva(10.5) + calcular_potencia_recursiva([60.0])
2. calcular_potencia_recursiva(10.5) -> CASO BASE -> Retorna 10.5
3. calcular_potencia_recursiva([60.0])
   -> primer_elemento = 60.0, resto = []
   -> Llama a calcular_potencia_recursiva(60.0) + calcular_potencia_recursiva([])
4. calcular_potencia_recursiva(60.0) -> CASO BASE -> Retorna 60.0
5. calcular_potencia_recursiva([]) -> CASO BASE -> Retorna 0.0
Resultado final: 10.5 + (60.0 + 0.0) = 70.5
"""

# ==============================================================================
# APARTADO 5: EXCEPCIONES PERSONALIZADAS Y PIPELINE ROBUSTO
# ==============================================================================
class EcoChargeError(Exception):
    """Excepción base para el dominio de EcoCharge Networks."""
    pass

class DatosCorruptosError(EcoChargeError):
    """Lanzada cuando faltan campos requeridos en la telemetría."""
    pass

class LecturaInvalidaError(EcoChargeError):
    """Lanzada cuando los datos numéricos no cumplen las reglas de negocio."""
    pass

def procesar_registro_individual(registro: dict) -> float:
    """Procesa un registro aplicando aserciones, validaciones y encadenamiento de excepciones."""
    # Aserción para desarrollo/depuración (comprueba invariante interno)
    assert isinstance(registro, dict), "Invariante roto: 'registro' debe ser un diccionario"

    try:
        # Validación de presencia de campos (puede lanzar KeyError)
        id_sesion = registro["id_sesion"]
        kw_h = registro["kw_h"]
        duracion = registro["duracion_min"]
    except KeyError as err:
        # Encadenamiento de excepciones (raise ... from ...)
        raise DatosCorruptosError(f"Registro incompleto. Falta la clave obligatoria {err}") from err

    # Validación de reglas de negocio
    if kw_h <= 0 or duracion <= 0:
        raise LecturaInvalidaError(f"Valores no válidos en sesión '{id_sesion}': kWh={kw_h}, Duración={duracion}")

    return float(kw_h)

def procesar_lote_telemetria(lote: list[dict]):
    """Pipeline principal de ejecución con estructura try-except-else-finally completa."""
    registros_exitosos = 0
    print("\n=== INICIANDO PIPELINE DE PROCESAMIENTO ROBUSTO ===")

    for idx, registro in enumerate(lote):
        print(f"\nProcesando Registro #{idx + 1}...")
        try:
            kw_procesados = procesar_registro_individual(registro)
        except (DatosCorruptosError, LecturaInvalidaError) as err:
            # Captura de excepciones específicas del dominio
            print(f"  [ERROR DOMINIO] {type(err).__name__}: {err}")
            print("___")
            if err.__cause__:
                print(f"  [CAUSA TÉCNICA ORIGINAL] {type(err.__cause__).__name__}: {err.__cause__}")
        except EcoChargeError as err:
            # Captura general del dominio
            print(f"  [ERROR GENÉRICO ECOCHARGE] {err}")
        else:
            # Se ejecuta solo si NO hubo excepciones
            registros_exitosos += 1
            print(f"  [ÉXITO] Registro procesado correctamente: {kw_procesados} kWh")
        finally:
            # Se ejecuta SIEMPRE
            print(f"  [AUDITORÍA] Fin de verificación registro #{idx + 1}")

    print(f"\nPipeline Finalizado. Total Registros Válidos: {registros_exitosos}/{len(lote)}")

# ==============================================================================
# BLOQUE PRINCIPAL DE EJECUCIÓN (PRUEBA INTEGRAL)
# ==============================================================================
if __name__ == "__main__":
    # Ejecución de demostración
    sesiones_v, conectores_u, resumen = auditar_y_filtrar_datos(REGISTROS_TELEMETRIA)
    
    informe = generar_informe_sesiones("INFORME DIARIO DE RECARGAS", *sesiones_v, moneda="EUR", país="España")
    print(f"\n{informe}")

    potencia_red = calcular_potencia_recursiva(RED_DISTRIBUCION)
    print(f"\nPotencia Acumulada en Red Jerárquica: {potencia_red:.2f} kWh")

    procesar_lote_telemetria(REGISTROS_TELEMETRIA)