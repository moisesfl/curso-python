# Examen de estructuras de control (22/10/2026 16:50 h)
**Curso Especialización:** Desarrollo de Aplicaciones en Python  
**Duración Máxima:** 3 Horas (180 Minutos)  
**Puntuación Total:** 10.0 Puntos  

---

## 1. Instrucciones para el Alumnado

1. **Entorno de Trabajo:** Debe desarrollar el código en Python utilizando VSCode.
2. **Estructura del Proyecto:** El examen consta de **5 apartados**.
3. **Criterios de Estilo y Sangrado:** El sangrado (indentación) en Python es una regla sintáctica estricta. El uso inapropiado de tabuladores o sangrados incorrectos provocará errores de ejecución (`IndentationError`, `TabError`) que penalizarán la nota final.
4. **Entrega:** Se entregará un único fichero de Python llamado `apellido_apellido_nombre_examen.py` debidamente documentado con docstrings e comentarios.

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

## 3. Enunciado del Examen (5 Apartados)

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

### Apartado 3: Función con número variable de argumentos y Transformaciones Avanzadas (2.0 Puntos)

El sistema requiere funciones puras para agregar métricas de rendimiento y ordenar el flujo de trabajo sin alterar las estructuras de datos originales de la aplicación.

#### Requerimientos:
1. **Diseñe la función `generar_informe_sesiones(titulo, *sesiones, **configuraciones)`.**
   - La función debe aceptar un título posicional obligatorio, un número indeterminado de sesiones de carga (válidas) mediante `*args` y parámetros de configuración opcionales mediante `**kwargs` (por ejemplo, `moneda="EUR"`, `pais="España"`).
   - **Regla de Inmutabilidad:** La función no debe modificar la lista original recibida
   - La función debe devolver una cadena formateada (utilizando **f-strings**) con el número de sesiones procesadas, el total acumulado de kWh, la duración media de las sesiones recibidas y los parámetros de configuración opcionales.
2. **Cree una función que utilice funciones Lambda** (`map`, `filter`, `sorted`, `reduce`), tenga como parámetro `sesiones_validas` y haga lo siguiente:
   - **Filtrado con `filter`:** Obtenga una lista de sesiones correspondientes a recargas de alta potencia ($\text{kWh} \ge 30.0$) utilizando `filter()` y una expresión `lambda`.
   - **Transformación con `map`:** Convierta la lista de sesiones filtradas en una lista de valores monetarios (costo total en euros) aplicando la función de tarificación del Apartado 1 mediante `map()` y `lambda`.
   - **Ordenación Multicriterio con `sorted`:** Ordene la lista de sesiones válidas en orden descendente por energía consumida (`kw_h`) y, en caso de empate, en orden ascendente por duración (`duracion_min`), utilizando `sorted()` con una función `lambda` en el parámetro `key`.
   - **Acumulación con `reduce`:** Importe `reduce` del módulo `functools` y calcule la energía total consumida por toda la red mediante una función `lambda` acumuladora sobre la lista de consumos.

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
   - El **Paso Recursivo:** Cuando un elemento sea una lista anidada.

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