# Examen de estructuras de control (22/10/2026 16:50 h)
**Curso Especialización:** Desarrollo de Aplicaciones en Python  
**Duración Máxima:** 3 Horas (180 Minutos)  
**Puntuación Total:** 10.0 Puntos  

---

## 1. Instrucciones para el Alumnado

1. **Entorno de Trabajo:** Debe desarrollar el código en Python utilizando VSCode.
2. **Estructura del Proyecto:** El examen consta de **5 apartados acumulativos**. Cada apartado construye sobre los datos y estructuras procesados en la fase previa.
3. **Criterios de Estilo y Sangrado:** El sangrado (indentación) en Python es una regla sintáctica estricta. El uso inapropiado de tabuladores o sangrados incorrectos provocará errores de ejecución (`IndentationError`, `TabError`) que penalizarán la nota final.
4. **Entrega:** Se entregará un único fichero de script Python llamado `apellido_apellido_nombre_examen.py` debidamente documentado con docstrings e comentarios.

---

## 2. Contexto del Proyecto Real: "EcoCharge Networks"

**EcoCharge Networks** es una compañía que gestiona una red distribuida de puntos de carga rápida para vehículos eléctricos (EV). Cada punto de carga envía periódicamente paquetes de telemetría a un servidor central. Debido a la inestabilidad de las redes IoT y a la heterogeneidad de los cargadores, los datos recibidos contienen errores de formato, lecturas corruptas y registros fuera de rango.

Como desarrollador/a del equipo de software, se le encarga construir el **Módulo Central de Auditoría, Tarificación y Procesamiento Robusto** de las sesiones de carga.

Los datos de telemetría recibidos por el servidor se representan inicialmente como una lista de diccionarios con la siguiente estructura tipo:

```python
REGISTROS_TELEMETRIA = [
    {"id_sesion": "SES-101", "cliente": "VIP", "conector": "CCS2", "kw_h": 45.5, "duracion_min": 30, "hora": 14, "activa": True},
    {"id_sesion": "SES-102", "cliente": "ESTANDAR", "conector": "CHADEMO", "kw_h": -12.0, "duracion_min": 15, "hora": 9, "activa": False}, # Error: kw_h negativo
    {"id_sesion": "SES-103", "cliente": "FLOTA", "conector": "MENNEKES", "kw_h": 22.0, "duracion_min": 120, "hora": 23, "activa": True},
    {"id_sesion": "SES-104", "cliente": "ESTANDAR", "conector": "CCS2", "kw_h": 60.0, "duracion_min": 40, "hora": 18, "activa": True},
    {"id_sesion": "CORRUPTO", "cliente": "DESCONOCIDO"}, # Error: falta información obligatoria
    {"id_sesion": "SES-105", "cliente": "VIP", "conector": "SCHUKO", "kw_h": 11.5, "duracion_min": 90, "hora": 2, "activa": True}
]
```

---

## 3. Enunciado del Examen (5 Apartados Progresivos)

### Apartado 1: Validación de Datos y Tarificación Dinámica (1.5 Puntos)

Para garantizar la correcta tarificación de las recargas, el sistema debe evaluar el coste base por kWh consumido utilizando un algoritmo de **tarificación dinámica**.

#### Requerimientos:
1. **Función de Tarificación (`calcular_tarifa_kwh`):** Implemente una función que reciba el `conector` (cadena) y la `hora` del día (entero de 0 a 23).
   - Debe utilizar la estructura de selección múltiple **`match-case`** para clasificar según el conector:
     - Si el conector es `"CCS2"` o `"CHADEMO"` (carga ultra-rápida): tarifa base de $0.45\text{ \$/kWh}$. Si la hora está entre las 17 y las 21 (hora punta), aplique un recargo de $0.15\text{ \$/kWh}$ adicional mediante una guarda (`if`).
     - Si el conector es `"MENNEKES"` (carga semi-rápida): tarifa base de $0.25\text{ \$/kWh}$.
     - Si el conector es `"SCHUKO"` (carga lenta): tarifa base de $0.15\text{ \$/kWh}$. Si la hora está entre las 0 y las 6 (hora valle), aplique un descuento de $0.05\text{ \$/kWh}$ mediante una guarda (`if`).
     - Para cualquier otro conector no reconocido (caso por defecto `_`), devuelva `None`.
2. **Aplicación de Descuento por Cliente** (`calcular_precio_final`): Implemente una nueva función que llame a la anterior y utilice un **operador ternario** para calcular el precio final aplicable: si el tipo de cliente es `"VIP"` o `"FLOTA"`, el precio por kWh calculado tendrá un descuento del $10\%$; en caso contrario, se mantendrá el precio base.

---

### Apartado 2: Limpieza y Filtrado Masivo (2.0 Puntos)

Antes de procesar la facturación global, el lote de datos debe ser auditado para eliminar registros corruptos y extraer listas estructuradas para el departamento analítico.

#### Requerimientos:
1. **Sustitución de Bucle Ineficiente:** Un desarrollador júnior intentó validar los datos utilizando la siguiente estructura:
   ```python
   # Código defectuoso a corregir
   idx = 0
   while True:
       reg = REGISTROS_TELEMETRIA[idx]
       if reg["kw_h"] > 0:
           print("Válido")
       idx += 1
   ```
   Reescriba el bucle utilizando un bucle `for` junto con la función **`enumerate()`** para mostrar el índice de cada registro y controlar de forma segura el límite de la lista sin provocar un `IndexError`.
2. **Filtrado con List Comprehension:** Cree una nueva lista llamada `sesiones_validas` mediante una **List Comprehension** con condición simple que conserve únicamente los diccionarios que cumplan todas estas condiciones:
   - Que contengan las claves `"kw_h"` y `"activa"`.
   - Que `"kw_h"` sea un valor mayor que cero (`kw_h > 0`).
   - Que la sesión esté marcada como activa (`activa == True`).
3. **Extracción con Set y Dict Comprehensions:**
   - Genere un conjunto mediante **Set Comprehension** denominado `conectores_unicos` que contenga todos los tipos de conectores presentes en las sesiones válidas, eliminando duplicados implícitamente.
   - Genere un diccionario mediante **Dict Comprehension** denominado `resumen_kw` cuyas claves sean el `id_sesion` y cuyos valores sean los `kw_h` consumidos, incluyendo únicamente las sesiones cuyo consumo sea superior a 20 kWh.
4. Todo lo pedido en este apartado debe estar dentro de una función llamada `auditar_y_filtar_datos` que devuelva la lista, el conjunto y el diccionario creados.
---

### Apartado 3: Arquitectura Funcional Modular y Transformaciones Avanzadas (2.0 Puntos)

El sistema requiere funciones puras para agregar métricas de rendimiento y ordenar el flujo de trabajo sin alterar las estructuras de datos originales de la aplicación.

#### Requerimientos:
1. **Firma Flexible y Regla de Inmutabilidad:** Diseñe la función `generar_informe_sesiones(titulo, *sesiones, **configuraciones)`.
   - La función debe aceptar un título posicional obligatorio, un número indeterminado de sesiones de carga mediante `*args`, y parámetros de configuración opcionales mediante `**kwargs` (por ejemplo, `moneda="EUR"`, `mostrar_detalles=True`).
   - **Regla de Inmutabilidad:** La función no debe modificar la lista original recibida. Si necesita realizar ordenaciones o modificaciones, debe trabajar sobre una copia explícita de los datos.
   - La función debe devolver una cadena formateada (utilizando **f-strings**) con el total acumulado de kWh y la duración media de las sesiones recibidas.
2. **Transformaciones con Funciones Lambda (`map`, `filter`, `sorted`, `reduce`):**
   - **Filtrado con `filter`:** Obtenga una lista de sesiones correspondientes a recargas de alta potencia ($\text{kWh} \ge 30.0$) utilizando `filter()` y una expresión `lambda`.
   - **Transformación con `map`:** Convierta la lista de sesiones filtradas en una lista de valores monetarios (costo total en euros) aplicando la función de tarificación del Apartado 1 mediante `map()` y `lambda`.
   - **Ordenación Multicriterio con `sorted`:** Ordene la lista de sesiones válidas en orden descendente por energía consumida (`kw_h`) y, en caso de empate, en orden ascendente por duración (`duracion_min`), utilizando `sorted()` con una función `lambda` en el parámetro `key`.
   - **Acumulación con `reduce`:** Importe `reduce` del módulo `functools` y calcule la energía total consumida por toda la red mediante una función `lambda` acumuladora sobre la lista de consumos.

REVISAR=> quitar o de reduce?!!!!!!!!!!!!!!!!!!
---

### Apartado 4: Análisis Jerárquico/Anidado Mediante Recursividad (2.0 Puntos)

La red de EcoCharge se organiza en una **estructura jerárquica de subredes y puntos de carga**. Una subred puede contener estaciones de carga individuales o, a su vez, contener otras subredes anidadas a diferentes niveles de profundidad.

Dada la siguiente estructura de datos anidada que representa la red de distribución:

```python
RED_DISTRIBUCION = [
    15.5, # Carga directa en Hub Central
    [22.0, 45.0, [10.5, 60.0]], # Subred Norte con ramificación interna
    [30.0, [12.5, [5.0, 18.0]]], # Subred Sur con triple anidamiento
    8.0 # Carga directa en Estación Auxiliar
]
```

#### Requerimientos:
1. **Implementación Recursiva de Aplanamiento y Suma (`calcular_potencia_recursiva`):** Escriba una función recursiva que reciba la estructura anidada y devuelva la **potencia total acumulada** en toda la jerarquía de la red sin utilizar la función built-in `sum()` ni bucles `for`/`while` para recorrer la profundidad.
2. **Análisis de los Componentes Recursivos:** Identifique y comente en el código:
   - El **Caso Base:** Cuando la lista esté vacía o se evalúe un valor numérico directo.
   - El **Paso Recursivo:** Cuando un elemento sea una lista anidada (utilizando `isinstance(elemento, list)`).
   - El **Progreso hacia el caso base:** Cómo se reduce la estructura en cada llamada recursiva.
3. **Cuestión recursividad:**
   - Explique en un comentario del código qué ocurre en la pila de llamadas de Python (*call stack*) si una estructura anidada carece de caso base o supera el límite de profundidad por defecto, indicando el nombre exacto de la excepción que lanza el intérprete.

---

### Apartado 5: Gestión Jerárquica de Excepciones y código robusto (2.5 Puntos)

Para evitar que un dato malformado detenga la ejecución del servidor central en producción, debe implementar una arquitectura de código robusta mediante captura de excepciones y clases personalizadas.

#### Requerimientos:
1. **Jerarquía de Excepciones Personalizadas:** Defina la siguiente estructura de clases de excepción heredando de la clase base `Exception`:
   - `EcoChargeError(Exception)`: Excepción base para todos los errores de la plataforma.
   - `DatosCorruptosError(EcoChargeError)`: Se lanza cuando un registro carece de campos obligatorios.
   - `LecturaInvalidaError(EcoChargeError)`: Se lanza cuando los valores numéricos violan las reglas de negocio (ej. `kw_h < 0` o `duracion_min <= 0`).
2. **Procesamiento de Registros con `raise ... from ...` y `assert`:**
   - Escriba la función `procesar_registro_individual(registro)`.
   - Dentro de la función, utilice **`assert isinstance(registro, dict)`** para verificar como invariante de desarrollo que la entrada es un diccionario.
   - Si faltan claves obligatorias (`"id_sesion"`, `"kw_h"`, `"duracion_min"`), capture el `KeyError` técnico y lance un `DatosCorruptosError` utilizando la sintaxis de encadenamiento de excepciones: **`raise DatosCorruptosError(...) from err`**.
   - Si los valores numéricos son negativos, lance un **`LecturaInvalidaError`** con un mensaje explicativo.
3. **Bloque Completo `try-except-else-finally`:** Implemente la función `procesar_lote_telemetria(lote_registros)` que recorra todos los registros y contenga la estructura completa de gestión:
   - **`try`:** Llama a `procesar_registro_individual`.
   - **`except`:** Captura de forma jerárquica las excepciones específicas (`DatosCorruptosError`, `LecturaInvalidaError`) mostrando el detalle y la causa original (`__cause__`), seguida de un bloque `except EcoChargeError` como último recurso de la aplicación.
   - **`else`:** Se ejecuta cuando el registro es completamente válido e incrementa el contador de registros procesados con éxito.
   - **`finally`:** Se ejecuta en cada iteración garantizando la escritura de un mensaje de log o cierre de auditoría.

---

## 4. Anexo Docente: Solucionario Oficial y Guía de Corrección

### Solucionario Integrado en Python (`ecocharge_sistema.py`)

```python
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

    # # 4. Reduce: Suma acumulada de kWh consumidos
    # consumos = [s["kw_h"] for s in sesiones_validas]
    # total_acumulado = reduce(lambda acc, x: acc + x, consumos, 0.0)

    return altas_cargas, costos, ordenadas#, total_acumulado

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
            if err.__cause__:
                print(f"  [CAUSA TÉCNICA ORIGINAL] {type(err.__cause__).__name__}: {err.__cause__}")
        except EcoChargeError as err:
            # Captura general del dominio
            print(f"  [ERROR GENÉRICO ECOCHARGE] {err}")
        except Exception as err:
            # Captura de último recurso
            print(f"  [ERROR INESPERADO] {type(err).__name__}: {err}")
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
    
    informe = generar_informe_sesiones("INFORME DIARIO DE RECARGAS", *sesiones_v, moneda="EUR")
    print(f"\n{informe}")

    potencia_red = calcular_potencia_recursiva(RED_DISTRIBUCION)
    print(f"\nPotencia Acumulada en Red Jerárquica: {potencia_red:.2f} kWh")

    procesar_lote_telemetria(REGISTROS_TELEMETRIA)
```

---

### Mapeo Normativo BOE (Módulo 5099) y Unidades Didácticas

| Apartado | Unidad Didáctica | Resultados de Aprendizaje (BOE) | Criterios de Evaluación Evaluados |
| :--- | :--- | :--- | :--- |
| **Apartado 1** | UD1 (Fundamentos) + UD2 (Condicionales) | RA1, RA2 | Representación en diagramas de flujo, sangrado explícito, sentencias `if-elif-else`, `match-case` con guards y operador ternario. |
| **Apartado 2** | UD3 (Bucles y Comprensiones) | RA3 | Comparación `while True` vs `for`, iteración con `enumerate()`, List/Set/Dict Comprehensions con filtrado. |
| **Apartado 3** | UD4 (Funciones y Lambdas) | RA4 | Firmas flexibles (`*args`, `**kwargs`), inmutabilidad, uso de `map`, `filter`, `sorted` (multicriterio) y `reduce`. |
| **Apartado 4** | UD4 (Recursividad) | RA4 | Diseño recursivo (caso base y recursivo), traza de ejecución, manejo de estructuras anidadas y prevención de `RecursionError`. |
| **Apartado 5** | UD5 (Gestión de Excepciones) | RA5 | Jerarquía de excepciones personalizadas, encadenamiento con `raise ... from ...`, uso de `assert` y bloque completo `try-except-else-finally`. |

---

### Rúbrica Analítica de Calificación (10.0 Puntos)

```
+---------------------------------------------------------------------------------------------------+
| APARTADO 1: Tarificación Dinámica y Diagrama de Flujo (1.5 Puntos)                                 |
+---------------------------------------------------------------------------------------------------+
| • Correcta simbología y lógica en el Diagrama de Flujo (0.4 pts)                                  |
| • Implementación de match-case con guardas para hora punta/valle (0.6 pts)                        |
| • Aplicación correcta del operador ternario para el descuento de cliente (0.3 pts)               |
| • Sintaxis y sangrado PEP 8 sin errores (0.2 pts)                                                 |
+---------------------------------------------------------------------------------------------------+
| APARTADO 2: Limpieza, Iteración e Identificación con Comprensiones (2.0 Puntos)                   |
+---------------------------------------------------------------------------------------------------+
| • Justificación técnica de las deficiencias de while True y reescritura con enumerate() (0.5 pts) |
| • List Comprehension correcta con filtrado booleano y comprobación de claves (0.5 pts)            |
| • Set Comprehension sin duplicados (0.5 pts)                                                      |
| • Dict Comprehension con filtro numérico (> 20 kWh) (0.5 pts)                                     |
+---------------------------------------------------------------------------------------------------+
| APARTADO 3: Arquitectura Funcional y Operaciones Lambda (2.0 Puntos)                              |
+---------------------------------------------------------------------------------------------------+
| • Firma con *args y **kwargs, formato f-string e inmutabilidad garantizada (0.6 pts)              |
| • Uso de filter() y map() con lambdas simples y legibles (0.5 pts)                                |
| • Ordenación multicriterio con sorted(..., key=lambda) (0.5 pts)                                  |
| • Acumulación correcta mediante reduce() (0.4 pts)                                                |
+---------------------------------------------------------------------------------------------------+
| APARTADO 4: Algoritmo Recursivo e Inspección de Pila (2.0 Puntos)                                 |
+---------------------------------------------------------------------------------------------------+
| • Definición correcta del Caso Base y Paso Recursivo sobre listas anidadas (0.8 pts)             |
| • Cálculo exacto de potencia sin usar sum() ni bucles iterativos (0.5 pts)                         |
| • Detalle escrito de la traza de llamadas (0.4 pts)                                               |
| • Explicación del call stack y RecursionError (0.3 pts)                                           |
+---------------------------------------------------------------------------------------------------+
| APARTADO 5: Pipeline Robusto y Excepciones Personalizadas (2.5 Puntos)                            |
+---------------------------------------------------------------------------------------------------+
| • Jerarquía de excepciones personalizadas (EcoChargeError, DatosCorruptosError, etc.) (0.5 pts)   |
| • Uso de assert para invariante y encadenamiento raise ... from ... (0.6 pts)                     |
| • Implementación pulcra de try, except específicos, else y finally (1.0 pts)                      |
| • Impresión de diagnósticos y causa original (__cause__) (0.4 pts)                                |
+---------------------------------------------------------------------------------------------------+
```

#### Penalizaciones Frecuentes:
- **-1.0 Punto:** Presencia de `IndentationError` o `TabError` que impida la ejecución del script.
- **-0.5 Puntos:** Modificación de estructuras mutables globales dentro de funciones (violación de la regla de inmutabilidad).
- **-0.5 Puntos:** Uso de `except Exception:` a ciegas como primera rama de captura (captura no jerárquica).
- **-0.3 Puntos:** Creación de bucles infinitos con `while True` no controlados.
