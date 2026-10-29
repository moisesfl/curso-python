# UD2 — Tarea entregable - Sistema de Domótica

- - -

# Entrega

## Cómo entregar

*   Proyecto en Github.
    *   El proyecto deberá tener un README.MD con una breve explicación del mismo.
    *   Se deberá crear en modo público para que pueda acceder.
    *   Crear un fichero de texto .txt con el enlace al proyecto de GitHub.
*   Fichero zip con el proyecto.
    *   El formato del nombre del fichero zip será el siguiente: `apelido1_apelido2_nome_UD02_tarefa.zip`.

- - -

# Enunciado general

Desarrolla una **aplicación modular en Python** que simule un **sistema de domótica** donde diferentes dispositivos (sensores, bombillas, cerraduras, etc.) se gestionan desde un **Hub central**.

El objetivo es aplicar **Programación Orientada a Objetos (POO)** para organizar el código de forma estructurada, reutilizable y extensible, poniendo en práctica:

*   Clases, objetos y herencia.
*   Encapsulación.
*   Polimorfismo mediante clases abstractas y Protocols.
*   Métodos estáticos y de clase.
*   Estructuras de control y datos: bucles, condicionales, listas, diccionarios.
*   Manejo de excepciones propias.

- - -

# Estructura del proyecto

```
mi_proyecto_domotica/
│
├─ domotica/                      # Paquete principal
│  ├─ __init__.py                 # Expone las clases principales del paquete
│  ├─ base.py                     # Clase abstracta base Dispositivo
│  ├─ dispositivos.py             # Subclases: SensorTemperatura, BombillaInteligente, CerraduraInteligente
│  ├─ hub.py                      # Clase Hub: registro y operaciones polimórficas
│  ├─ interfaces.py               # Protocols: Medible, Conmutable, Actualizable
│  ├─ common.py                   # Utilidades (validaciones, factorías, excepciones)
│
└─ main.py                        # Programa principal de demostración
```

- - -

# Requisitos funcionales y técnicos

## 1. Clase base (abstracta) `Dispositivo` (`base.py`)

Define la estructura común de todos los dispositivos.

*   Atributos protegidos:
    
    *   `_id: str`
    *   `_nombre: str`
    *   `_fabricante: str`
*   Métodos:
    
    *   `__init__`: constructor con validaciones.
    *   Métodos _setters_ y _getters_ para los atributos.
    *   `__str__`: representación legible del objeto.
    *   `tipo()`: método abstracto que devuelva el tipo de dispositivo.

## 2. Subclases (`dispositivos.py`)

Implementa tres clases derivadas de `Dispositivo`, cada una con atributos y métodos propios:

### `SensorTemperatura`

*   Atributo adicional:
    
    *   `_celsius: float`
*   Métodos:
    
    *   `leer_valor()`: devuelve la temperatura actual.
    *   `tipo()`: devuelve `"SensorTemperatura"`.

### `BombillaInteligente`

*   Atributos adicionales:
    
    *   `_brillo: int` (0–100)
    *   `_encendida: bool`
*   Métodos:
    
    *   `encender()`, `apagar()`
    *   `tipo()`: `"BombillaInteligente"`

### `CerraduraInteligente`

*   Atributos adicionales:
    
    *   `_bloqueada: bool`
*   Métodos:
    
    *   `bloquear()`, `desbloquear()`
    *   `tipo()`: `"CerraduraInteligente"`

- - -

## 3. Protocols (`interfaces.py`)

Define las capacidades que un dispositivo puede tener, sin obligar a una jerarquía rígida.

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Medible(Protocol):
    def leer_valor(self) -> float: ...

@runtime_checkable
class Conmutable(Protocol):
	""" Adaptar a cada tipo de dispositivo para que se puedan activar/desactivar utilizando polimorfismo llamando al metodo correspondiente si  ya lo integran """
    def encender(self) -> None: ...
    def apagar(self) -> None: ...

@runtime_checkable
class Actualizable(Protocol):
    def actualizar_firmware(self, version: str) -> None: ...
```

- - -

## 4. Clase `Hub` (`hub.py`)

Gestiona los dispositivos registrados y realiza operaciones comunes.

*   **Atributos**:
    
    *   `_dispositivos: dict[str, Dispositivo]` :
        *   Diccionario donde se almacenan los dispositivos con clave ID y objeto.
        *   Formato del ID:
            *   Formato bombillas: "B001", "B002", ...
            *   Formato sensores: "S001", "S002", ...
            *   Formato cerradura: "C001", "C002", ...
*   **Métodos**:
    
    *   `registrar(disp: Dispositivo)`: añade dispositivos evitando duplicados.
        
    *   `listar()`: devuelve todos los dispositivos.
        
    *   `operar_todos()`: Recorre la colección de dispositivos:
        
        *   Si es `Medible`, muestra su lectura.
        *   Si es `Conmutable`, alterna encendido/apagado.
    *   `estadisticas()`: devuelve un diccionario con el número de dispositivos por tipo.
        

- - -

## 5. Módulo común (`common.py`)

El módulo common.py centraliza utilidades transversales y excepciones de dominio para el sistema de domótica. Debe ser independiente del resto de módulos (no debe importar Dispositivo ni subclases), para evitar dependencias circulares y permitir pruebas unitarias aisladas.

#### Excepciones:

| Clase | Hereda de | ¿Cuándo lanzarla? | Ejemplo de mensaje |
| --- | --- | --- | --- |
| `DatoInvalido` | `ValueError` | Un dato no cumple el formato o las reglas de negocio | `"ID generado inválido: 'B00-'"` |
| `Duplicado` | `Exception` | Se intenta registrar/insertar un elemento con clave ya existente (validado en `Hub`) | `"El ID 'B001' ya existe"` |
| `NoEncontrado` | `Exception` | No existe un elemento solicitado por su identificador | `"No existe el dispositivo 'X999'"` |

#### Clase Utils

*   Clase `Utils` con:
    
    *   `validar_id(texto: str) -> bool`
    *   `fabricar_id(prefijo: str, n: int) -> str`
    *   `validar_version(version: str) -> bool`

#### Función validar_id

*   Valida el formato de identificador de un dispositivo.
*   Reglas de validación (todas obligatorias):
    *   Texto debe ser str y no vacío (tras strip()).
    *   Debe comenzar por letra \[A-Za-z\].
    *   Por convención en la unidad: B (bombilla), S (sensor), C (cerradura)… pero no limitar solo a estas.
    *   El resto de caracteres deben ser alfanuméricos o guiones: \[A-Za-z0-9-\].
    *   No se permiten espacios internos.

#### Función fabricar_id

Genera un nuevo ID canonizado para dispositivos, con el formato:

```
<PREFIJO><NNN>
```

donde es una letra (o varias letras) en mayúsculas y es un entero con 3 dígitos (con cero a la izquierda si procede).

**Reglas**:

*   prefijo debe ser str, no vacío; se normaliza a mayúsculas (upper()).
*   n debe ser int positivo (>= 1).
*   El id\_candidato debe superar validar\_id(...); en caso contrario, lanzar DatoInvalido con mensaje:
    *   "ID generado inválido: ''".

Ejemplos:

*   fabricar\_id("b", 1) → "B001"
*   fabricar\_id("S", 12) → "S012"
*   fabricar\_id("Hub", 7) → "HUB007"

Casos que deben lanzar DatoInvalido:

*   fabricar\_id("", 1) → prefijo vacío
*   fabricar\_id("B", 0) → n no positivo
*   fabricar\_id("X\_", 5) → guion bajo no permitido por validar\_id

Notas:

*   No comprueba colisiones (IDs ya usados); eso corresponde a Hub.

- - -

## 6. Programa principal (`main.py`)

Demostración completa del funcionamiento.

*   Crear una lista de dispositivos de distintos tipos.
*   Registrarlos en el `Hub`.
*   Mostrar su información y estadísticas.
*   Utilizar bucles, condicionales, listas y diccionarios.
*   Mostrar manejo de excepciones controladas.

### Presentación e inicio

1.  Mostrar un encabezado breve indicando que comienza la demo del sistema de domótica.
2.  Crear una instancia del `Hub` (registro interno vacío).

### Preparación de datos (entrada)

3.  Preparar una **lista de diccionarios** con la definición de dispositivos a crear.
    
    *   Cada elemento define: `id`, `tipo` (sensor/bombilla/cerradura), `nombre`, `fabricante` y los parámetros específicos:
        
        *   `SensorTemperatura`: `celsius` inicial.
        *   `BombillaInteligente`: `brillo` inicial (0–100).
        *   `CerraduraInteligente`: estado inicial (bloqueada por defecto, opcional).
    
    *   Incluir **al menos dos dispositivos por tipo** para que las estadísticas sean significativas.
        
    *   Incluir **casos problemáticos** para probar validaciones:
        
        *   Un `id` inválido (por ejemplo, que no empiece por letra).
        *   Un `id` duplicado (repetir uno existente).

### Creación e inyección en el `Hub`

4.  Recorrer con un **bucle** la lista de definiciones:
    
    *   Según el `tipo`, **instanciar** la subclase correspondiente:
        
        *   `SensorTemperatura(...)`
        *   `BombillaInteligente(...)`
        *   `CerraduraInteligente(...)`
    *   Validar previamente el `id` con `Utils.validar_id`; si es inválido, **avisar** y **saltar** ese elemento.
        
5.  Registrar cada dispositivo en el `Hub` con `hub.registrar(disp)`:
    
    *   Si el `id` **ya existe**, capturar `Duplicado` y mostrar un mensaje indicando el fallo.
    *   Si algún dato fuese inválido en el constructor, capturar `DatoInvalido` y continuar con el siguiente.

### Listado y representación

6.  Imprimir un **listado de todos los dispositivos** registrados, recorriendo `hub.listar()`:
    
    *   Mostrar la representación legible (`__str__`) de cada objeto.
    *   Comprobar que los estados iniciales (`online`, brillo, bloqueada, etc.) se muestran correctamente.

### Capacidades por dispositivo (duck typing con Protocols)

7.  Para cada dispositivo registrado:
    
    *   Comprobar **dinámicamente** si implementa `Medible` (`isinstance(d, Medible)`):
        
        *   Si sí, imprimir “Medible”.
    *   Comprobar si implementa `Conmutable`:
        
        *   Si sí, imprimir “Conmutable”.
    *   Comprobar si implementa `Actualizable`:
        
        *   Si sí, imprimir “Actualizable”.
    *   Construir un **resumen de capacidades** por cada dispositivo.
        

### Operaciones polimórficas masivas

8.  Llamar a `hub.operar_todos()` (recorre todos los dispositivos):
    
    *   Para cada **Medible**: llamar a `leer_valor()` y mostrar la lectura.
    *   Para cada **Conmutable**: ejecutar `encender()` y luego `apagar()`; mostrar mensajes de acción (o estado resultante).

### Acciones específicas por tipo

9.  Localizar una `BombillaInteligente` y:
    
    *   Cambiar su **brillo** (p. ej., 50 → 90) y mostrar el nuevo valor.
        
    *   Ejecutar una **actualización de firmware** con `Actualizable.actualizar_firmware("1.2.3")`, validando versión con `Utils.validar_version`.
        
        *   Si la versión es inválida, capturar `DatoInvalido` y mostrar mensaje.
10.  Localizar una `CerraduraInteligente` y:
    
    *   Mostrar su estado (bloqueada/desbloqueada).
    *   Llamar a `bloquear()` y luego a `desbloquear()` (y viceversa) para evidenciar la **conmutación**.

## Estadísticas y resúmenes

11.  Obtener `hub.estadisticas()` y mostrar el **diccionario** con recuento por tipo (p. ej., `{'SensorTemperatura': 2, 'BombillaInteligente': 2, 'CerraduraInteligente': 1}`).
    
12.  Mostrar un **resumen final**: total de dispositivos, cuántos son medibles, cuántos conmutables y cuántos actualizables (se puede calcular sobre `hub.listar()` con contadores).
    

## Manejo de errores y casos límite (demostración explícita)

13.  Intentar registrar de nuevo un `id` existente para mostrar el mensaje de `Duplicado`.
14.  Probar a validar una **versión incorrecta** (por ejemplo `"1.0"`) para evidenciar `validar_version == False` y el lanzamiento de `DatoInvalido` si se intenta actualizar con ella.
15.  Intentar consultar un dispositivo inexistente para ilustrar `NoEncontrado`.

## Cierre

16.  Mostrar un mensaje de **fin de la demostración**.

- - -

# Ejemplo de salida (output) del programa

\=== DEMO DOMÓTICA — INICIO ===

Creando Hub… OK Cargando definiciones de dispositivos (lista de diccionarios)…

Validando e instanciando:

*   OK: S001 (sensor) → SensorTemperatura "Sensor Cocina" (Acme, 22.5 ºC)
*   OK: B001 (bombilla) → BombillaInteligente "Bombilla Salón" (Lumen, brillo=80)
*   OK: C001 (cerradura) → CerraduraInteligente "Puerta Principal" (SafeCo, bloqueada)
*   OK: S002 (sensor) → SensorTemperatura "Sensor Dormitorio" (Acme, 19.3 ºC)
*   OK: B002 (bombilla) → BombillaInteligente "Bombilla Pasillo" (Lumen, brillo=50)
*   ERROR: id "001" inválido → se omite
*   ERROR: Duplicado "B001" ya existe → se omite

Registro en Hub completado: 5 dispositivos.

Listado de dispositivos:

*   \[SensorTemperatura\] Sensor Cocina (id=S001, fabricante=Acme)
*   \[BombillaInteligente\] Bombilla Salón (id=B001, fabricante=Lumen)
*   \[CerraduraInteligente\] Puerta Principal (id=C001, fabricante=SafeCo)
*   \[SensorTemperatura\] Sensor Dormitorio (id=S002, fabricante=Acme)
*   \[BombillaInteligente\] Bombilla Pasillo (id=B002, fabricante=Lumen)

Capacidades detectadas:

*   S001 → Medible
*   B001 → Conmutable, Actualizable
*   C001 → Conmutable
*   S002 → Medible
*   B002 → Conmutable, Actualizable

Operar todos (polimorfismo):

*   S001 → lectura = 22.50 ºC
*   B001 → encender() → OK; apagar() → OK
*   C001 → encender() (bloquear) → OK; apagar() (desbloquear) → OK
*   S002 → lectura = 19.30 ºC
*   B002 → encender() → OK; apagar() → OK

Acciones específicas:

*   Calibrar S001 con offset +0.70 → nueva lectura = 23.20 ºC
*   B001: brillo previo = 80 → brillo nuevo = 90
*   B001: actualizar\_firmware("1.2.3") → OK
*   B002: actualizar\_firmware("1.0") → ERROR: versión inválida (formato esperado X.Y.Z)
*   C001: estado → bloqueada; desbloquear() → OK; bloquear() → OK

Estadísticas por tipo:

*   SensorTemperatura: 2
*   BombillaInteligente: 2
*   CerraduraInteligente: 1 Total dispositivos: 5

Resumen de capacidades:

*   Medibles: 2
*   Conmutables: 3
*   Actualizables: 2

Pruebas de errores controlados:

*   Registrar de nuevo B001 → ERROR: Duplicado (el ID ya existe)
*   Validar id "A\_01" → False (carácter '\_' no permitido)
*   Actualizar firmware B002 a "v1.2.3" → ERROR: versión inválida
*   Obtener "X999" → ERROR: NoEncontrado (no existe)

\=== DEMO DOMÓTICA — FIN ===

- - -

# 📐 UML de clases (ASCII)

```
+-----------------------------------+
|        <<abstract>>               |
|            Dispositivo            |
+-----------------------------------+
| - _id: str                        |
| - _nombre: str                    |
| - _fabricante: str                |                   
+-----------------------------------+
| + __init__()                      |
| + __str__()                       |
| + tipo(): str {abstract}          |          
| + propiedades (get/set)           |
+-----------------^-----------------+
                  |
  +---------------+---------------+----------------+
  |               |               |                |
+----------------+ +----------------+ +----------------+
|SensorTemperatura| |BombillaInteligente| |CerraduraInteligente|
+----------------+ +----------------+ +----------------+
| - _celsius     | | - _brillo      | | - _bloqueada   |
| + leer_valor() | | - _encendida   | | + bloquear()   |
| + tipo()       | | + encender()   | | + desbloquear()|
|                | | + apagar()     | | + tipo()       |
+----------------+ +----------------+ +----------------+
```