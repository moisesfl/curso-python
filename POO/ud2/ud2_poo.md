# UD2 – Programación Orientada a Objetos con Python

##  Índice de contenidos

- [UD2 – Programación Orientada a Objetos con Python](#ud2--programación-orientada-a-objetos-con-python)
  - [Índice de contenidos](#índice-de-contenidos)
- [1. Módulos y Paquetes](#1-módulos-y-paquetes)
  - [1.1. ¿Qué es un módulo?](#11-qué-es-un-módulo)
    - [**Cómo se importa:**](#cómo-se-importa)
    - [1.2. Ejemplo de desarrollo y utilización de un módulo](#12-ejemplo-de-desarrollo-y-utilización-de-un-módulo)
    - [1.3. Fichero principal de la aplicación  `if __name__ == __main__`](#13-fichero-principal-de-la-aplicación--if-__name__--__main__)
    - [1.4. ¿Qué es un paquete y cómo se estructura un proyecto?](#14-qué-es-un-paquete-y-cómo-se-estructura-un-proyecto)
    - [1.5. Actividad práctica](#15-actividad-práctica)
- [2. Clases en Python](#2-clases-en-python)
  - [2.1. Conceptos de la estructura de una clase](#21-conceptos-de-la-estructura-de-una-clase)
    - [Ejemplo de clase](#ejemplo-de-clase)
    - [Actividad propuesta](#actividad-propuesta)
  - [2.3. Decoradores:](#23-decoradores)
    - [Conceptos](#conceptos)
    - [Decoradores en la definición de clases](#decoradores-en-la-definición-de-clases)
      - [`@staticmethod`](#staticmethod)
    - [`@classmethod`](#classmethod)
- [3. Herencia](#3-herencia)
  - [3.1. Características específicas de la herencia en Python](#31-características-específicas-de-la-herencia-en-python)
  - [3.2. El constructor y `super()`](#32-el-constructor-y-super)
  - [3.3. Sobrescritura de métodos (overriding)](#33-sobrescritura-de-métodos-overriding)
  - [3.4. Herencia múltiple](#34-herencia-múltiple)
  - [3.5. Herencia jerárquica y en cadena](#35-herencia-jerárquica-y-en-cadena)
  - [3.6. Uso de `isinstance()` y `issubclass()`](#36-uso-de-isinstance-y-issubclass)
  - [3.7. Ejemplo de uso de las clases creadas](#37-ejemplo-de-uso-de-las-clases-creadas)
- [4. Polimorfismo](#4-polimorfismo)
  - [4.1. Polimorfismo en Python](#41-polimorfismo-en-python)
  - [4.2. Polimorfismo mediante herencia](#42-polimorfismo-mediante-herencia)
    - [Uso polimórfico](#uso-polimórfico)
  - [4.3. Polimorfismo con métodos redefinidos (`__str__`)](#43-polimorfismo-con-métodos-redefinidos-__str__)
  - [4.4. Polimorfismo sin herencia (duck typing)](#44-polimorfismo-sin-herencia-duck-typing)
  - [Este comportamiento se conoce como **polimorfismo dinámico**.](#este-comportamiento-se-conoce-como-polimorfismo-dinámico)
- [5. Abstracción en Python](#5-abstracción-en-python)
  - [5.1. Introducción teórica](#51-introducción-teórica)
    - [Relación con el Principio de Inversión de Dependencias (D de SOLID)](#relación-con-el-principio-de-inversión-de-dependencias-d-de-solid)
  - [5.2. Clases abstractas](#52-clases-abstractas)
    - [Ejemplo técnico](#ejemplo-técnico)
  - [5.3. Implementación de subclases concretas](#53-implementación-de-subclases-concretas)
- [6. Interfaces en Python (Protocol)](#6-interfaces-en-python-protocol)
  - [6.1. Conceptos](#61-conceptos)
  - [6.2. Contruyendo una interfaz](#62-contruyendo-una-interfaz)
  - [6.3. Combinación de abstracción e interfaz](#63-combinación-de-abstracción-e-interfaz)
  - [6.4 Ejemplo completo y output](#64-ejemplo-completo-y-output)
    - [Estructura del proyecto](#estructura-del-proyecto)
    - [Fichero `vehiculos/base.py`](#fichero-vehiculosbasepy)
    - [Fichero `vehiculos/clases.py`](#fichero-vehiculosclasespy)
    - [Fichero `vehiculos/interfaces.py`](#fichero-vehiculosinterfacespy)
    - [Fichero `vehiculos/__init__.py`](#fichero-vehiculos__init__py)
    - [Fichero `main.py`](#fichero-mainpy)
    - [Explicación](#explicación)
    - [Ejecución y salida esperada](#ejecución-y-salida-esperada)

# 1. Módulos y Paquetes

## 1.1. ¿Qué es un módulo?

Un **módulo** es un archivo de código Python (`.py`) que agrupa definiciones reutilizables: funciones, clases, constantes y variables.

Se carga una única vez por proceso (gracias al _module cache_ en `sys.modules`) y expone un **espacio de nombres** propio, evitando colisiones.

El **nombre de módulo** se determina por su ruta de importación (p. ej., `app.modelos`), no por el título del archivo en sí.

### **Cómo se importa:**

```python
import math                # módulo completo
from math import sqrt      # sólo lo que necesitas
import math as m           # con alias
```

**Idempotencia al importar**  
Una segunda importación del mismo módulo no vuelve a ejecutar su código _top-level_; Python reutiliza el objeto ya cargado en `sys.modules`.

### 1.2. Ejemplo de desarrollo y utilización de un módulo

**Estructura mínima**:

```
mi_proyecto_calculadora/
│
├─ calculadora.py        # Módulo con funciones y constantes matemáticas
└─ main.py               # Programa principal que importa y usa el módulo

```

**Fichero `calculadora.py` con operaciones matemáticas** :

Este es el fichero en el que se encuentra lo que queremos importar para ser utilizado en la aplicación desde el fichero principal.

```python
"""
Módulo: calculadora.py
Este archivo contiene funciones matemáticas básicas y algunas constantes útiles.
Puede ser importado por cualquier otro script de Python (por ejemplo, main.py).
"""

# Constantes matemáticas (podrían venir también de math, pero aquí las definimos nosotros)
PI = 3.14159
E = 2.71828

# --- FUNCIONES MATEMÁTICAS BÁSICAS ---

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def restar(a, b):
    """Devuelve la resta (a - b)."""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b

def dividir(a, b):
    """
    Devuelve el cociente (a / b).
    Lanza un ValueError si se intenta dividir entre cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def area_circulo(radio):
    """Calcula el área de un círculo usando la constante PI."""
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return PI * (radio ** 2)

def exponencial(base, exponente):
    """Calcula base^exponente utilizando una función simple."""
    return base ** exponente

```

**Fichero principal de la aplicación** `main.py`:

```python
# Importamos el módulo completo (recomendado cuando queremos usar varios elementos)
import calculadora

# También podemos importar elementos específicos (para acortar el código)
from calculadora import dividir, area_circulo

print("=== DEMOSTRACIÓN DEL MÓDULO CALCULADORA ===\n")

# Uso de funciones del módulo importado completo
a, b = 10, 5
print(f"Suma ({a} + {b}):", calculadora.sumar(a, b))
print(f"Resta ({a} - {b}):", calculadora.restar(a, b))
print(f"Multiplicación ({a} × {b}):", calculadora.multiplicar(a, b))

# Uso de función importada directamente
print(f"División ({a} ÷ {b}):", dividir(a, b))

# Cálculo del área de un círculo
radio = 3
print(f"\nÁrea de un círculo de radio {radio}: {area_circulo(radio):.2f}")

```

### 1.3. Fichero principal de la aplicación  `if __name__ == __main__`

En Python, cada archivo .py tiene un atributo especial llamado `__name__` que indica cómo se está ejecutando el archivo:

*   Si el archivo se ejecuta directamente, Python asigna `__name__ = "__main__"`.
*   Si el archivo se importa como módulo, `__name__` toma el nombre del módulo (por ejemplo, "calculadora" o "geometria.areas").

El bloque:

```python
if "__name__" == "__main__":
    main()
```

es una convención estándar que permite distinguir si el archivo se está ejecutando directamente o si ha sido importado por otro. Esto evita que el código dentro del bloque se ejecute automáticamente al importar el módulo.

 **En resumen**:

*   Protege el código de ejecución (por ejemplo, pruebas o demostraciones).
*   Permite reutilizar el módulo sin ejecutar la parte principal.
*   Mejora la legibilidad y sigue una práctica universal en Python.

### 1.4. ¿Qué es un paquete y cómo se estructura un proyecto?

Un **paquete** es un directorio que contiene un archivo `__init__.py`. Este archivo marca el directorio como paquete y puede definir la API pública mediante `__all__`. Sirve para **organizar** módulos bajo el mismo apellido (prefijo) y decidir qué partes expones como API pública.

**Ventajas**

*   Encapsulación de submódulos bajo un prefijo común.
*   Importaciones explícitas y rutas estables.
*   Inicialización controlada en `__init__.py`.

**Estructura típica**

```
mi_proyecto/
│
├─ app/
│  ├─ __init__.py
│  ├─ modelos.py
│  └─ servicios.py
└─ main.py
```

**Tips rápidos:**

*   Usa `__init__.py` para “re-exportar” lo más importante (p. ej. `from .modelos import Usuario`).
*   Nombres claros: `modelos.py` para entidades, `servicios.py` para la lógica.

### 1.5. Actividad práctica

**Enunciado.** Crea un paquete `geometria` con:

*   `__init__.py` exponiendo `area_circulo` y `area_rectangulo`.
*   `areas.py` con ambas funciones (validando parámetros).
*   `constantes.py` con `PI = 3.14159`. Escribe `demo.py` que importe desde `geometria` y calcule áreas.

**Solución orientativa.**

Estructura del proyecto:

```
mi_proyecto_geometria/
│
├─ geometria/                 # Paquete: agrupa lógica de áreas y constantes
│  ├─ __init__.py             # Expone la API pública del paquete
│  ├─ areas.py                # Funciones de cálculo de áreas (con validación)
│  └─ constantes.py           # Constantes matemáticas (p. ej. PI)
│
└─ demo.py                    # Aplicación: ejemplos de uso del paquete 'geometria'
```

Fichero `constantes.py`:

```python
# constantes.py
# Propósito: centralizar constantes matemáticas reutilizables en el paquete.

PI: float = 3.14159  # Aproximación de π utilizada en los cálculos de área

```

Fichero `areas.py`:

```
# areas.py
# Propósito: funciones puras para calcular áreas de figuras planas.
# Incluye validación de parámetros para evitar estados/entradas inválidas.

from .constantes import PI

def area_circulo(r: float) -> float:
    """
    Calcula el área de un círculo.
    """
    if r < 0:
        raise ValueError("El radio no puede ser negativo (r >= 0).")
    return PI * (r ** 2)


def area_rectangulo(a: float, b: float) -> float:
    """
    Calcula el área de un rectángulo.
    """
    if a < 0 or b < 0:
        raise ValueError("Los lados del rectángulo deben ser no negativos (a, b >= 0).")
    return a * b

```

Fichero `__init__.py`:

```
# __init__.py
# Propósito: definir la API pública del paquete 'geometria' para que
# los consumidores puedan importar directamente lo que necesitan.
# Ejemplo: `from geometria import area_circulo`

from .areas import area_circulo, area_rectangulo

# __all__ controla qué símbolos se exportan cuando se usa `from geometria import *`.
__all__ = ["area_circulo", "area_rectangulo"]

```

Fichero `demo.py`:

```
# Importación directa desde el paquete (gracias a __init__.py)
from geometria import area_circulo, area_rectangulo

def main() -> None:
    """
    Punto de entrada de la aplicación.
    """

    print("=== DEMOSTRACIÓN DEL PAQUETE 'geometria' ===\n")

    # Ejemplo 1: área de un círculo de radio 3
    r = 3.0
    area_c = area_circulo(r)
    print(f"[Ejemplo 1] Área de círculo (r = {r}): {area_c:.2f}")

    # Ejemplo 2: área de un rectángulo 2 x 5
    a, b = 2.0, 5.0
    area_r = area_rectangulo(a, b)
    print(f"[Ejemplo 2] Área de rectángulo ({a} x {b}): {area_r:.2f}")

    # Ejemplo 3: demostración de validación y manejo de errores
    print("\n[Ejemplo 3] Validación y manejo de errores:")
    try:
        area_circulo(-1)  # Radio negativo -> debe disparar ValueError
    except ValueError as e:
        print(f"   Error controlado al calcular área de círculo: {e}")

    try:
        area_rectangulo(3, -4)  # Lado negativo -> debe disparar ValueError
    except ValueError as e:
        print(f"   Error controlado al calcular área de rectángulo: {e}")

    print("\nFin de la demostración.")

# Convención estándar: sólo ejecuta main() si el archivo se ejecuta directamente.
# Si se importa (por ejemplo, desde tests), no se ejecuta el bloque siguiente.

if __name__ == "__main__":
    main()

```

- - -

# 2. Clases en Python

## 2.1. Conceptos de la estructura de una clase

Una **clase** define un tipo; sus **instancias** poseen estado (atributos) y comportamiento (métodos).

*   **Constructor**: `__init__(self, ...)` inicializa el estado del objeto ya creado por `__new__`.
*   **Destructore**: `__del__` no se recomienda; libera recursos con `with` o `try/finally`.
*   **Representador del objeto**: el método `__str__` controla lo que debe ser mostrado cuando se quiere representar el objeto como una cadena.
*   **Parámetro `self`**:
    *   referencia a la instancia actual de la clase
    *   pasada implícitamente en la llamada.
    *   realmente lo podemos llamar como queramos pero por convenio se le llama "self".
*   **Sentencia `pass`**: permite tener una clase sin definición.

Para más información sobre cláses en Python consultar: [Clases en W3schools](https://www.w3schools.com/python/python_classes.asp)

### Ejemplo de clase

```python
"""
Clase base: Vehiculo
--------------------
Representa un vehículo genérico. 
Más adelante se usará como clase padre de Coche, Autobus, Camion y Moto.
"""

class Vehiculo:
    # Atributo de clase (compartido por todas las instancias)
    total_vehiculos = 0

    def __init__(self, marca, modelo, color, velocidad_maxima):
        """
        Método constructor (__init__):
        Se ejecuta automáticamente al crear un nuevo objeto Vehiculo.
        Define los atributos básicos del vehículo.
        """
        self._marca = marca                # atributo protegido (convención: _nombre)
        self._modelo = modelo
        self._color = color
        self._velocidad_maxima = velocidad_maxima
        self._encendido = False            # estado inicial: apagado

        # Cada vez que se crea un vehículo, se incrementa el contador de clase
        Vehiculo.total_vehiculos += 1

    # ========================
    #   MÉTODOS GETTER / SETTER
    # ========================

    def get_marca(self):
        """Devuelve la marca del vehículo."""
        return self._marca

    def set_marca(self, nueva_marca):
        """Cambia la marca del vehículo."""
        if not nueva_marca:
            raise ValueError("La marca no puede estar vacía.")
        self._marca = nueva_marca

    def get_color(self):
        """Devuelve el color actual del vehículo."""
        return self._color

    def set_color(self, nuevo_color):
        """Permite cambiar el color del vehículo."""
        if not isinstance(nuevo_color, str):
            raise ValueError("El color debe ser una cadena de texto.")
        self._color = nuevo_color

    def get_velocidad_maxima(self):
        """Devuelve la velocidad máxima."""
        return self._velocidad_maxima

    def set_velocidad_maxima(self, nueva_velocidad):
        """Cambia la velocidad máxima, con validación."""
        if nueva_velocidad <= 0:
            raise ValueError("La velocidad máxima debe ser positiva.")
        self._velocidad_maxima = nueva_velocidad

    # ========================
    #   MÉTODOS DE INSTANCIA
    # ========================

    def encender(self):
        """Cambia el estado del vehículo a encendido."""
        if self._encendido:
            print("El vehículo ya está encendido.")
        else:
            self._encendido = True
            print("Vehículo encendido.")

    def apagar(self):
        """Cambia el estado del vehículo a apagado."""
        if not self._encendido:
            print("El vehículo ya está apagado.")
        else:
            self._encendido = False
            print("Vehículo apagado.")

    # ========================
    #   MÉTODO ESTÁTICO
    # ========================

    @staticmethod
    def es_vehiculo_pesado(peso):
        """
        Determina si un vehículo se considera 'pesado'.
        No depende de ninguna instancia, por eso es estático.
        """
        return peso > 3500  # kg

    # ========================
    #   MÉTODO DE CLASE
    # ========================

    @classmethod
    def mostrar_total_vehiculos(cls):
        """
        Método de clase:
        Permite acceder o modificar atributos de clase.
        En este caso, muestra cuántos vehículos se han creado.
        """
        print(f"Actualmente existen {cls.total_vehiculos} vehículos registrados.")

    # ========================
    #   REPRESENTACIÓN DEL OBJETO
    # ========================

    def __str__(self):
        """
        Representación legible del objeto.
        Se ejecuta al usar print() o str() sobre una instancia.
        """
        estado = "Encendido" if self._encendido else "Apagado"
        return (f"[Vehículo] Marca: {self._marca} | Modelo: {self._modelo} | "
                f"Color: {self._color} | Velocidad Máxima: {self._velocidad_maxima} km/h | Estado: {estado}")
    

# ========================
#   BLOQUE DE PRUEBA (solo se ejecuta si el archivo se ejecuta directamente)
# ========================
if __name__ == "__main__":
    # Crear varios vehículos
    v1 = Vehiculo("Toyota", "Corolla", "Rojo", 180)
    v2 = Vehiculo("Mercedes", "Actros", "Blanco", 120)

    # Usar getters y setters
    print(v1.get_marca(), "-", v1.get_color())
    v1.set_color("Negro")
    print("Nuevo color:", v1.get_color())

    # Probar métodos de instancia
    v1.encender()
    print(v1)
    v1.apagar()

    # Método estático: comprobar si un vehículo es pesado
    print("¿El camión es pesado?", Vehiculo.es_vehiculo_pesado(8000))

    # Método de clase: mostrar cuántos vehículos se han creado
    Vehiculo.mostrar_total_vehiculos()

```

### Actividad propuesta

Crea la clase `Animal`, la cual deberá constar de:

*   Constructor.
*   Atributo de clase.
*   Atributos de instancia.
*   Setters
*   Getters
*   Al menos un método estático.
*   Al menos un método de clase.
*   Método `__str__`

Adicionalmente deberás crear una aplicación que utilice dicha clase.

## 2.3. Decoradores:

### Conceptos

*   Los **[decoradores](https://www.w3schools.com/python/python_decorators.asp)** son una característica avanzada del lenguaje Python que permiten **modificar o ampliar el comportamiento de funciones, métodos o clases** sin alterar su código fuente directamente.
    
*   En la práctica, un decorador es **una función que recibe otra función (o clase)** y devuelve una versión modificada de la misma.
    

Definición de un decorador:

```python
def amayusculas(a):
  def interior():
    return a().upper()
  return interior
```

Cómo usar un decorador:

```python
@amayusculas
def saludar():
    print("Hola mundo!")

print(saludar)
```

Esto devolverá: `HOLA MUNDO!`

### Decoradores en la definición de clases

#### `@staticmethod`

Convierte una función definida dentro de la clase en un **método estático**: no recibe `self` ni `cls`.

```python
# Método de la clase vehículo vista previamente
    @staticmethod
    def es_vehiculo_pesado(peso):
        """
        Determina si un vehículo se considera 'pesado'.
        No depende de ninguna instancia, por eso es estático.
        """
        return peso > 3500  # kg
```

### `@classmethod`

Declara un **método de clase**: recibe `cls` (la propia clase) en lugar de `self`.

```python
# Método de la clase vehículo
    @classmethod
    def mostrar_total_vehiculos(cls):
        """
        Método de clase:
        Permite acceder o modificar atributos de clase.
        En este caso, muestra cuántos vehículos se han creado.
        """
        print(f"Actualmente existen {cls.total_vehiculos} vehículos registrados.")
```

**Cuándo usarlo**: **fábricas**, constructores alternativos, acceso/edición de **estado global** de la clase.

- - -

# 3. Herencia

## 3.1. Características específicas de la herencia en Python

*   Puede ser **simple o múltiple** (cuando mezclas varios padres).
*   `super()` llama ordenadamente a los métodos del padre según el **MRO** (Orden de Resolución de Métodos).
*   Usa **mixins** para añadir “superpoderes” pequeños a varias clases.
*   **Principios SOLID**: En el contexto de buenas prácticas de diseño, los principios SOLID sirven como guía para escribir software mantenible y escalable. En particular, el **Principio de Sustitución de Liskov (LSP)** establece que: _si S es una subclase de T, entonces los objetos de tipo T pueden ser reemplazados por objetos de tipo S sin alterar las propiedades deseables del programa_.

## 3.2. El constructor y `super()`

Las subclases deben invocar el constructor de la superclase para **inicializar correctamente** el estado heredado. En Python, se utiliza `super()`:

```python
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, puertas):
        # Inicializa atributos heredados
        super().__init__(marca, modelo, color, velocidad_maxima)
        # Inicializa atributos propios
        self._puertas = puertas
```

**Comentario técnico:** `super()` devuelve un objeto proxy que delega llamadas a la superclase según el **Method Resolution Order (MRO)**. Esto permite herencia múltiple cooperativa cuando se siguen firmas compatibles.

## 3.3. Sobrescritura de métodos (overriding)

Una subclase puede **redefinir** métodos de la superclase para **especializar** su comportamiento, manteniendo el contrato (LSP).

Ejemplo sobrescribiendo el método `__str__`:

```python
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, puertas):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self._puertas = puertas

    def __str__(self):
        # Reutiliza la representación base y la amplía
        return super().__str__() + f" | Puertas: {self._puertas}"

class Autobus(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima, plazas):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self._plazas = plazas

    def __str__(self):
        return super().__str__() + f" | Plazas: {self._plazas}"
```

## 3.4. Herencia múltiple

Python permite heredar de **múltiples superclases**. Cuando las superclases cooperan mediante `super()`, la inicialización y la resolución de métodos siguen el **MRO**.

```python
# Clase que va a ser utilizada para herencia
class Registrable:
    def registrar(self):
        print("Registro en DGT completado.")

# Clase que va a ser utilizada para herencia
class MantenimientoProgramado:
    def programar_revision(self, km):
        print(f"Revisión programada a los {km} km.")

# Clase que hereda
class Camion(Vehiculo, Registrable, MantenimientoProgramado):
    def __init__(self, marca, modelo, color, velocidad_maxima, carga_maxima):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self._carga_maxima = carga_maxima

    def __str__(self):
        return super().__str__() + f" | Carga máxima: {self._carga_maxima} kg"
```

**Comentario técnico:** el orden `Camion(Vehiculo, Registrable, MantenimientoProgramado)` determina el MRO. Puede consultarse con `Camion.__mro__`.

## 3.5. Herencia jerárquica y en cadena

Es común definir jerarquías donde una subclase actúa a su vez como superclase de una especialización posterior.

```python
class Moto(Vehiculo):
    def hacer_caballito(self):
        print(f"La moto {self.get_marca()} está haciendo un caballito.")

class MotoDeportiva(Moto):
    def __init__(self, marca, modelo, color, velocidad_maxima, electronica_avanzada=True):
        super().__init__(marca, modelo, color, velocidad_maxima)
        self._electronica_avanzada = electronica_avanzada

    def __str__(self):
        return super().__str__() + (" | Electrónica avanzada" if self._electronica_avanzada else "")
```

## 3.6. Uso de `isinstance()` y `issubclass()`

Estas funciones permiten **verificar relaciones de herencia** en tiempo de ejecución:

```python
c = Coche("Seat", "Ibiza", "Azul", 180, 5)
print(isinstance(c, Vehiculo))   # True: instancia perteneciente a una subclase de Vehiculo
print(issubclass(Coche, Vehiculo))  # True: Coche es una subclase de Vehiculo
```

Estas comprobaciones son útiles para validaciones, _type checks_ dinámicos y composición de algoritmos polimórficos.

## 3.7. Ejemplo de uso de las clases creadas

El siguiente ejemplo integra creación de instancias, herencia simple y múltiple, sobrescritura de métodos y uso de métodos estáticos y de clase.

```python
def demo():
    coche = Coche("Seat", "Ibiza", "Azul", 180, 5)
    bus = Autobus("Mercedes", "Citaro", "Amarillo", 100, 50)
    camion = Camion("Volvo", "FH16", "Blanco", 120, 25000)
    moto = Moto("Yamaha", "MT-07", "Negro", 200)

    coche.encender()
    print(coche)           # __str__ sobrescrito
    bus.encender()
    print(bus)             # __str__ sobrescrito
    print(camion)          # herencia múltiple + __str__
    moto.hacer_caballito() # método propio de Moto

    # Métodos heredados de clase/estáticos
    Vehiculo.mostrar_total_vehiculos()
    print("¿El camión es pesado?", Vehiculo.es_vehiculo_pesado(8000))

if __name__ == "__main__":
    demo()
```

**Salida esperada (resumen, puede variar en detalles):**

```
Vehículo encendido.
[Vehículo] Marca: Seat | Modelo: Ibiza | Color: Azul | Velocidad Máxima: 180 km/h | Estado: Encendido | Puertas: 5
Vehículo encendido.
[Vehículo] Marca: Mercedes | Modelo: Citaro | Color: Amarillo | Velocidad Máxima: 100 km/h | Estado: Encendido | Plazas: 50
[Vehículo] Marca: Volvo | Modelo: FH16 | Color: Blanco | Velocidad Máxima: 120 km/h | Estado: Apagado | Carga máxima: 25000 kg
La moto Yamaha está haciendo un caballito.
Actualmente existen 4 vehículos registrados.
¿El camión es pesado? True
```

- - -

# 4. Polimorfismo

## 4.1. Polimorfismo en Python

Python implementa el polimorfismo de forma **dinámica**, lo que se conoce como _duck typing_.  
No importa el tipo de la clase concreta, sino que el objeto tenga los **métodos esperados**.

> “Si camina como un pato y suena como un pato, probablemente sea un pato.”

## 4.2. Polimorfismo mediante herencia

En el ejemplo de jerarquía de clases, todas las subclases (`Coche`, `Autobus`, `Camion`, `Moto`) heredan de `Vehiculo` y redefinen algunos métodos.  
Esto permite enviar el mismo mensaje (`arrancar()`, `__str__()`, etc.) a diferentes objetos y obtener resultados distintos según la clase.

```python
class Vehiculo:
    def arrancar(self):
        print("El vehículo ha arrancado.")

class Coche(Vehiculo):
    def arrancar(self):
        print("El coche ha arrancado silenciosamente.")

class Autobus(Vehiculo):
    def arrancar(self):
        print("El autobús ha arrancado y comienza su ruta.")

class Moto(Vehiculo):
    def arrancar(self):
        print("La moto ruge al arrancar.")
```

### Uso polimórfico

```python
def iniciar_vehiculo(vehiculo):
    # Puede recibir cualquier objeto que tenga el método arrancar()
    vehiculo.arrancar()
```

```python
# Instancias de distintas clases
v = Vehiculo()
c = Coche()
a = Autobus()
m = Moto()

for objeto in (v, c, a, m):
    iniciar_vehiculo(objeto)
```

**Salida:**

```
El vehículo ha arrancado.
El coche ha arrancado silenciosamente.
El autobús ha arrancado y comienza su ruta.
La moto ruge al arrancar.
```

## 4.3. Polimorfismo con métodos redefinidos (`__str__`)

El método `__str__()` redefinido en las subclases permite mostrar información adaptada al tipo de vehículo:

```python
vehiculos = [
    Coche("Seat", "Ibiza", "Azul", 180, 5),
    Autobus("Mercedes", "Citaro", "Amarillo", 100, 50),
    Camion("Volvo", "FH16", "Blanco", 120, 25000),
    Moto("Yamaha", "MT-07", "Negro", 200)
]

for v in vehiculos:
    print(v)
```

**Salida:**

```
[Vehículo] Marca: Seat | Modelo: Ibiza | Color: Azul | Velocidad Máxima: 180 km/h | Estado: Apagado | Puertas: 5
[Vehículo] Marca: Mercedes | Modelo: Citaro | Color: Amarillo | Velocidad Máxima: 100 km/h | Estado: Apagado | Plazas: 50
[Vehículo] Marca: Volvo | Modelo: FH16 | Color: Blanco | Velocidad Máxima: 120 km/h | Estado: Apagado | Carga máxima: 25000 kg
[Vehículo] Marca: Yamaha | Modelo: MT-07 | Color: Negro | Velocidad Máxima: 200 km/h | Estado: Apagado
```

## 4.4. Polimorfismo sin herencia (duck typing)

Python no requiere herencia formal. Cualquier objeto que implemente los métodos esperados puede participar en operaciones polimórficas.

```python
class Bicicleta:
    def arrancar(self):
        print("La bicicleta comienza a pedalear.")

class PatineteElectrico:
    def arrancar(self):
        print("El patinete eléctrico acelera suavemente.")
```

```python
def probar_arranque(vehiculo):
    vehiculo.arrancar()
```

```python
for obj in (Coche(), Bicicleta(), PatineteElectrico()):
    probar_arranque(obj)
```

**Salida:**

```
El coche ha arrancado silenciosamente.
La bicicleta comienza a pedalear.
El patinete eléctrico acelera suavemente.
```

## Este comportamiento se conoce como **polimorfismo dinámico**.

# 5. Abstracción en Python

## 5.1. Introducción teórica 

La **abstracción** es uno de los cuatro pilares de la Programación Orientada a Objetos (POO), junto con la encapsulación, la herencia y el polimorfismo.

En el diseño de software, la abstracción permite centrarse en **qué hace** un objeto, sin preocuparse por **cómo lo hace**.

### Relación con el Principio de Inversión de Dependencias (D de SOLID)

El principio de **Inversión de Dependencias** establece que:

> “Los módulos de alto nivel no deben depender de módulos de bajo nivel, ambos deben depender de abstracciones.”

Esto implica que las clases no deben depender de implementaciones concretas, sino de **interfaces o clases abstractas**. De este modo, se logra un **bajo acoplamiento** y una **alta cohesión**, facilitando la mantenibilidad y extensibilidad del sistema.

## 5.2. Clases abstractas

Se utiliza para declarar métodos que las clases derivadas **deben implementar obligatoriamente**.

En Python se definen con el módulo `abc` (**Abstract Base Classes**), el decorador `@abstractmethod` y como contenido del método utilizamos la keyword `pass`.

### Ejemplo técnico

Clase abstracta que define la estructura básica de un vehículo. _**No puede instanciarse directamente**_.

```python
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase abstracta que define la estructura básica de un vehículo.
    No puede instanciarse directamente.
    """
    def __init__(self, marca, modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    @abstractmethod
    def arrancar(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

    @abstractmethod
    def detener(self):
        """Método abstracto que debe ser implementado por las subclases."""
        pass

    def __str__(self):
        return f"[Vehículo] {self._marca} {self._modelo} ({self._color})"
```

Intentar crear una instancia directa de `Vehiculo` producirá un error:

```python
v = Vehiculo("Marca", "Modelo", "Color")  # TypeError
```

**Salida:**

```
TypeError: Can't instantiate abstract class Vehiculo with abstract methods arrancar, detener
```

## 5.3. Implementación de subclases concretas

Las subclases deben **heredar de `Vehiculo`** e implementar todos los métodos abstractos para ser instanciables.

```python
class Coche(Vehiculo):
    def arrancar(self):
        print(f"El coche {self._marca} arranca suavemente.")

    def detener(self):
        print(f"El coche {self._marca} se detiene con el freno de mano.")

class Moto(Vehiculo):
    def arrancar(self):
        print(f"La moto {self._marca} ruge al arrancar.")

    def detener(self):
        print(f"La moto {self._marca} se detiene gradualmente.")

class Camion(Vehiculo):
    def arrancar(self):
        print(f"El camión {self._marca} enciende su motor diésel.")

    def detener(self):
        print(f"El camión {self._marca} utiliza el freno de aire para detenerse.")
```

- - -

# 6. Interfaces en Python (Protocol)

## 6.1. Conceptos

La abstracción y las interfaces son herramientas fundamentales para diseñar software **modular, extensible y desacoplado**.

En Python:

*   Las **clases abstractas** permiten definir la **estructura común** de una jerarquía de clases.
*   Las **interfaces (Protocol)** proporcionan un mecanismo para declarar **capacidades compartidas** entre clases dispares.

Python no tiene interfaces como tal (como Java o C#), pero puede emularlas con `Protocol` del módulo `typing`.

*   `Protocol` define un **contrato de comportamiento** que cualquier clase puede cumplir si implementa los métodos declarados.
*   `@runtime_checkable`: sin el decorador _@runtime\_checkable_, esta comprobación solo ocurre en tiempo de análisis estático, no en ejecución.

## 6.2. Contruyendo una interfaz

A continuación **creamos una interfaz** para implementar en las clases derivadas de "Vehiculo" para añadir la funcionalidad de repostaje:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Repostable(Protocol):
    """
    Interfaz que define la capacidad de repostar.
    Cualquier clase que implemente 'repostar()' se considera Repostable.
    """
    def repostar(self, litros: float) -> None:
        ...
```

## 6.3. Combinación de abstracción e interfaz

Las clases concretas pueden **heredar de la clase abstracta `Vehiculo`** e implementar la interfaz `Repostable`. De esta forma, definen tanto la estructura común como un comportamiento adicional opcional.

```python
class CocheRepostable(Coche, Repostable):
    def repostar(self, litros: float) -> None:
        print(f"El coche {self._marca} ha repostado {litros} litros de combustible.")

class CamionRepostable(Camion, Repostable):
    def repostar(self, litros: float) -> None:
        print(f"El camión {self._marca} ha repostado {litros} litros de diésel.")
```

## 6.4 Ejemplo completo y output

A continuación creamos una clase principal que utiliza las clases creadas y muestra el output

###  Estructura del proyecto

```
mi_proyecto_vehiculos/
│
├─ vehiculos/                       # Paquete principal
│  ├─ __init__.py                   # Expone la API pública
│  ├─ base.py                       # Clase abstracta Vehiculo
│  ├─ clases.py                     # Subclases concretas: Coche, Moto, Camion
│  └─ interfaces.py                 # Interfaz Repostable (Protocol)
│
└─ main.py                          # Programa principal que utiliza el paquete
```

###  Fichero `vehiculos/base.py`

```python
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    """
    Clase abstracta que define la estructura base de un vehículo.
    Incluye métodos que deberán implementarse en las subclases.
    """
    def __init__(self, marca: str, modelo: str, color: str):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    @abstractmethod
    def arrancar(self):
        """Método abstracto que debe implementar cada tipo de vehículo."""
        pass

    @abstractmethod
    def detener(self):
        """Método abstracto que debe implementar cada tipo de vehículo."""
        pass

    def __str__(self):
        return f"[Vehículo] {self._marca} {self._modelo} ({self._color})"
```

###  Fichero `vehiculos/clases.py`

```python
from .base import Vehiculo

class Coche(Vehiculo):
    def arrancar(self):
        print(f"El coche {self._marca} arranca suavemente.")

    def detener(self):
        print(f"El coche {self._marca} se detiene con el freno de mano.")

class Moto(Vehiculo):
    def arrancar(self):
        print(f"La moto {self._marca} ruge al arrancar.")

    def detener(self):
        print(f"La moto {self._marca} se detiene gradualmente.")

class Camion(Vehiculo):
    def arrancar(self):
        print(f"El camión {self._marca} enciende su motor diésel.")

    def detener(self):
        print(f"El camión {self._marca} utiliza el freno de aire para detenerse.")
```

###  Fichero `vehiculos/interfaces.py`

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Repostable(Protocol):
    """
    Interfaz que define la capacidad de repostar combustible.
    Cualquier clase que implemente este método se considera Repostable.
    """
    def repostar(self, litros: float) -> None:
        ...
```

###  Fichero `vehiculos/__init__.py`

```python
# __init__.py
# Expone los elementos principales del paquete para su uso externo.

from .base import Vehiculo
from .clases import Coche, Moto, Camion
from .interfaces import Repostable

__all__ = ["Vehiculo", "Coche", "Moto", "Camion", "Repostable"]
```

###  Fichero `main.py`

Este script ejecuta el programa demostrativo, integrando herencia, polimorfismo, abstracción e interfaces.

```python
from vehiculos import Coche, Moto, Camion, Repostable

# Extensiones con la interfaz Repostable
class CocheRepostable(Coche, Repostable):
    def repostar(self, litros: float):
        print(f"El coche {self._marca} ha repostado {litros} litros de gasolina.")

class CamionRepostable(Camion, Repostable):
    def repostar(self, litros: float):
        print(f"El camión {self._marca} ha repostado {litros} litros de diésel.")

def main():
    vehiculos = [
        CocheRepostable("Seat", "Ibiza", "Azul"),
        Moto("Yamaha", "MT-07", "Negra"),
        CamionRepostable("Volvo", "FH16", "Blanco")
    ]

    print("=== DEMOSTRACIÓN DE LA APLICACIÓN DE VEHÍCULOS ===\n")

    for v in vehiculos:
        print(v)
        v.arrancar()
        v.detener()
        # Comprobación polimórfica de interfaz
        if isinstance(v, Repostable):
            v.repostar(50)
        print("-" * 60)

if __name__ == "__main__":
    main()
```

###  Explicación

Este proyecto integra los principales conceptos de la Programación Orientada a Objetos en Python:

| Concepto | Ejemplo | Descripción |
| --- | --- | --- |
| **Abstracción** | `Vehiculo` (clase abstracta) | Define los métodos esenciales comunes a todos los vehículos. |
| **Herencia** | `Coche`, `Moto`, `Camion` | Reutilizan la estructura base y especializan el comportamiento. |
| **Polimorfismo** | `v.arrancar()` y `v.detener()` | Cada subclase redefine el método adaptándolo a su tipo. |
| **Interfaces (`Protocol`)** | `Repostable` | Define un contrato estructural sin herencia explícita. |
| **Encapsulación** | Atributos `_marca`, `_modelo`, `_color` | Protegen los datos internos de acceso directo externo. |

- - -

###  Ejecución y salida esperada

Al ejecutar `python main.py` en el directorio raíz del proyecto:

**Salida esperada:**

```
=== DEMOSTRACIÓN DE LA APLICACIÓN DE VEHÍCULOS ===

[Vehículo] Seat Ibiza (Azul)
El coche Seat arranca suavemente.
El coche Seat se detiene con el freno de mano.
El coche Seat ha repostado 50 litros de gasolina.
------------------------------------------------------------
[Vehículo] Yamaha MT-07 (Negra)
La moto Yamaha ruge al arrancar.
La moto Yamaha se detiene gradualmente.
------------------------------------------------------------
[Vehículo] Volvo FH16 (Blanco)
El camión Volvo enciende su motor diésel.
El camión Volvo utiliza el freno de aire para detenerse.
El camión Volvo ha repostado 50 litros de diésel.
------------------------------------------------------------
```

- - -

