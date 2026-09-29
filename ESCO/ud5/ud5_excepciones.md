# UD05-excepciones-python

## Índice de contenidos

*   [ UD05 Gestión de excepciones en Python](#ud05-gesetion-de-excepciones-en-python)
    *   [ Índice](#indice)
    *   [1\. ¿Qué es una excepción?](#1-que-es-una-excepcion)
        *   [Excepciones comunes](#excepciones-comunes)
    *   [2\. Bloques try, except, else, finally](#2-bloques-try-except-else-finally)
    *   [3\. Captura múltiple y jerárquica](#3-captura-multiple-y-jerarquica)
    *   [4\. raise lanzar excepciones manualmente](#4-raise-lanzar-excepciones-manualmente)
        *   [¿Qué aporta raise que no se pueda hacer con try-except?](#que-aporta-raise-que-no-se-pueda-hacer-con-try-except)
        *   [raise ... from ... Encadenamiento de excepciones](#raise-from-encadenamiento-de-excepciones)
    *   [5\. assert: comprobaciones para desarrollo](#5-assert-comprobaciones-para-desarrollo)
        *   [¿Qué es assert y para qué sirve?](#que-es-assert-y-para-que-sirve)
        *   [Sintaxis genérica](#sintaxis-generica)
        *   [Ejemplo de uso](#ejemplo-de-uso)
    *   [6\. Excepciones personalizadas](#6-excepciones-personalizadas)
        *   [¿Qué son y qué utilidad tienen?](#que-son-y-que-utilidad-tienen)
        *   [Sintaxis](#sintaxis)
        *   [Ejemplo](#ejemplo)

#  UD05 Gesetión de excepciones en Python[](#ud05-gesetion-de-excepciones-en-python "Permanent link")

- - -

##  Índice[](#indice "Permanent link")

```
1. ¿Qué es una excepción?.
2. Bloques `try`, `except`, `else`, `finally` .
3. Captura múltiple y jerárquica.
4. `raise` lanzar excepciones manualmente.
5. `assert`: comprobaciones para desarrollo.
6. Excepciones personalizadas.
```

- - -

## 1\. ¿Qué es una excepción?[](#1-que-es-una-excepcion "Permanent link")

Una **excepción** es un evento que **interrumpe** el flujo normal del programa cuando ocurre un **error** (p. ej., dividir entre cero, acceder a un índice inexistente).  
Python **lanza** una excepción y, si no se **maneja**, el programa se detiene mostrando un _traceback_.

```
# Ejemplo simple: provoca ZeroDivisionError
def dividir(a, b):
    return a / b  # Si b == 0 -> ZeroDivisionError

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Lanza excepción si no se maneja
```

### Excepciones comunes[](#excepciones-comunes "Permanent link")

| Excepción | ¿Cuándo ocurre? | Ejemplo |
| --- | --- | --- |
| `ValueError` | Valor con formato incorrecto | `int("abc")` |
| `TypeError` | Tipo no compatible | `len(10)` |
| `KeyError` | Clave inexistente en dict | `d["x"]` sin `"x"` |
| `IndexError` | Índice fuera de rango | `[1,2][5]` |
| `ZeroDivisionError` | División por cero | `1/0` |
| `FileNotFoundError` | Archivo no existe | `open("no.txt")` |
| `PermissionError` | Permisos insuficientes | `open("/root/x", "w")` |
| `TimeoutError` | Operación tardó demasiado | sockets/procesos |
| `OSError` | Errores del sistema/IO | rutas, E/S, etc. |

- - -

## 2\. Bloques `try`, `except`, `else`, `finally`[](#2-bloques-try-except-else-finally "Permanent link")

Estructura básica para **intentar** una operación que tenga el riesgo de terminar en error de ejecución, **manejar** el error, ejecutar código si **no hubo errores**, y ejecutar código **siempre** independientemente de que haya habido un error de ejecución.

*   **try**: dentro del bloque `try` introducimos el código que puede dar lugar al error de ejecución.
    
*   **except**: bloque que captura la excepción y que edevuelve al usuario el error que se ha producido.
    
*   **else**: bloque con el código que se ejecutará solamente si no se produce el error.
    
*   **finally**: bloque con código que se ejecuta siempre haya o no error de ejecución.
    

**Ejemplo para una calculadora de divisiones**:

A continuación se muestra el código para una calculadora sencilla que realiza divisiones:

```
    try:
        # 1️ Entrada de datos (pueden provocar ValueError)
        a = float(input("Introduce el numerador: "))
        b = float(input("Introduce el denominador: "))

        # 2️ Operación peligrosa (puede provocar ZeroDivisionError)
        resultado = a / b

    except ValueError:
        #  Error si el usuario introduce algo que no es un número
        print(" Error: Debes introducir valores numéricos.")

    except ZeroDivisionError:
        #  Error específico al dividir entre cero
        print(" Error: No se puede dividir entre cero.")

    else:
        #  Solo se ejecuta si NO ha ocurrido ninguna excepción
        print(f" Resultado de la división: {resultado}")

    finally:
        #  Se ejecuta siempre, haya error o no
        print(" Operación finalizada.\n")
```

- - -

## 3\. Captura múltiple y jerárquica[](#3-captura-multiple-y-jerarquica "Permanent link")

Puedes capturar **varios tipos** de excepciones a la vez y respetar la **jerarquía** (_de más específica a más general_).

```
def convertir_a_int(x):
    try:
        return int(x)
    except (ValueError, TypeError) as e:
        #  Captura múltiple: datos inválidos o tipo incorrecto
        print(f"No se pudo convertir a int: {e}")
        return None
    except Exception as e:
        #  Último recurso (muy general). Úsalo con moderación.
        print(f"Error inesperado: {e}")
        return None
```

> **Orden correcto:** primero las excepciones **específicas**, luego las **generales**. Si pones `except Exception` antes, “tapará” las específicas.

- - -

## 4\. `raise` lanzar excepciones manualmente[](#4-raise-lanzar-excepciones-manualmente "Permanent link")

`raise` se utiliza para lanzar excepciones manualmente en tu código. Es decir, cuando detectas una condición de error que Python no detectaría por sí mismo, puedes crear y lanzar una excepción para indicar que algo ha salido mal.

**Sintaxis**:

```
raise ValueError("Mensaje descriptivo del error")
```

**Ejemplo** de uso para la división por cero:

```
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
```

> **Mensaje útil:** Incluye datos que ayuden a **diagnosticar** (no pongas información sensible).

### ¿Qué aporta raise que no se pueda hacer con try-except?[](#que-aporta-raise-que-no-se-pueda-hacer-con-try-except "Permanent link")

*   **Control proactivo**: Con raise puedes crear excepciones personalizadas en situaciones que Python no detecta automáticamente (ej: validación de datos, reglas de negocio).
*   **Comunicación clara**: Permite indicar errores específicos con mensajes descriptivos, mejorando la depuración y el mantenimiento del código.
*   **Jerarquía de excepciones**: Puedes definir tus propias excepciones (heredando de Exception) y lanzarlas cuando sea necesario.

**Ejemplo**:

```
def procesar_edad(valor):
    """
    Convierte 'valor' a entero y valida que sea una edad razonable (0..120).
    Demuestra:
    - Captura múltiple: (TypeError, ValueError)
    - Captura jerárquica: ValueError específico vs Exception general
    """
    try:
        # 1) Puede lanzar TypeError si valor es None u objeto no convertible,
        #    o ValueError si es una cadena no numérica ("hola").
        edad = int(valor)

        # 2) Validación lógica: decidimos lanzar *nuestra propia* excepción.
        #    Ojo: aquí lanzamos ValueError a propósito para reutilizar la misma rama específica.
        if edad < 0 or edad > 120:
            raise ValueError(f"edad fuera de rango: {edad} (debe estar entre 0 y 120)")

        return edad

    except (TypeError, ValueError) as e:
        #  CAPTURA MÚLTIPLE (y además específica)
        # - TypeError: int(None), int(objeto_raro)...
        # - ValueError: int("hola"), o nuestro raise ValueError(...) de arriba
        print(f" Entrada inválida para edad → {valor!r}. Detalle: {type(e).__name__}: {e}")
        return None

    except Exception as e:
        #  CAPTURA GENERAL (último recurso)
        # Aquí caerían errores inesperados que no sean TypeError/ValueError.
        print(f" Error inesperado → {type(e).__name__}: {e}")
        return None


# ---------------------------
# Casos de prueba (muy didácticos)
# ---------------------------
pruebas = [
    "25",        #  OK
    "hola",      #  ValueError (int("hola"))
    None,        #  TypeError (int(None))
    "-3",        #  ValueError (por validación: fuera de rango)
    "200",       #  ValueError (por validación: fuera de rango)
]

for p in pruebas:
    resultado = procesar_edad(p)
    print(f"Resultado final para {p!r}: {resultado}")
    print("-" * 45)
```

### `raise ... from ...` Encadenamiento de excepciones[🔗](#raise-from-encadenamiento-de-excepciones "Permanent link")

Conserva el **contexto** cuando conviertes excepciones de bajo nivel en una de **dominio**.

*   **Mantiene la trazabilidad**: ves la excepción final (la que te interesa para tu programa) y también la causa real (lo que ocurrió por debajo).
*   **Mejora el diagnóstico**: el traceback mostrará algo del estilo: “The above exception was the direct cause of the following exception” (la excepción anterior fue la causa directa…)
*   **Evita perder contexto**: si lanzas una excepción nueva sin from, el motivo original puede quedar oculto o menos claro.

```
class EdadInvalidaError(Exception):
    """Error del dominio: la edad recibida no es válida."""
    pass


def leer_edad(texto):
    """
    Intenta convertir 'texto' a int.
    Si falla la conversión, lanza EdadInvalidaError conservando la causa original
    mediante 'raise ... from ...'.
    """
    try:
        return int(texto)
    except (ValueError, TypeError) as e:
        #  Aquí traducimos un error "técnico" (ValueError/TypeError)
        #  a un error "de dominio" (EdadInvalidaError), SIN perder la causa.
        raise EdadInvalidaError(f"No se pudo interpretar la edad a partir de {texto!r}") from e


# ---------------------------
# Pruebas didácticas
# ---------------------------
entradas = ["25", "hola", None]

for x in entradas:
    try:
        edad = leer_edad(x)
        print(f"Entrada {x!r} → edad = {edad}")
    except EdadInvalidaError as err:
        print(f" Entrada {x!r} → {type(err).__name__}: {err}")

        # La excepción original queda accesible en __cause__
        causa = err.__cause__
        print(f"   ↳ Causa original: {type(causa).__name__}: {causa}")
    print("-" * 50)
```

**ATENCIÓN**:

`{x!r}` en un f-string significa: “formatea este valor x usando repr()” (representación “literal/de depuración”), en lugar de usar str().

Diferencia rápida: str() vs repr() - str(x) → pensado para usuarios (más “bonito”). - repr(x) → pensado para depurar (más “exacto” y normalmente muestra comillas, escapes, etc.).

Ejemplo:

```
x = "hola"
print(f"{x}")    # hola
print(f"{x!r}")  # 'hola'   ← aparecen comillas
```

- - -

## 5\. `assert`: comprobaciones para desarrollo[](#5-assert-comprobaciones-para-desarrollo "Permanent link")

### ¿Qué es assert y para qué sirve?[](#que-es-assert-y-para-que-sirve "Permanent link")

`assert` es una sentencia de comprobación (“afirmación”) que verifica que una condición sea verdadera durante la ejecución.

*   Si la condición es True → el programa continúa normal.
*   Si la condición es False → Python lanza una excepción AssertionError (con un mensaje opcional).

**Uso típico** (muy importante):

*   Se usa como herramienta de depuración para detectar errores de lógica y violaciones de invariantes (condiciones que “deberían cumplirse siempre” si el programa está bien).
*   No está pensada para validar entradas de usuario “normales”. Para eso suele ser mejor if ...: raise ValueError(...), etc.

**Relación con la gestión de excepciones**:

*   assert lanza una excepción (concretamente AssertionError), así que se puede:
    
    *   dejar que “explote” (útil en desarrollo/depuración),
    *   o capturarla con try/except si se desea gestionar.
*   En producción, es frecuente no capturar AssertionError, porque suele indicar un bug del programador, no un error recuperable.
    

**Nota práctica**: si Python se ejecuta con optimización (python -O), las aserciones pueden desactivarse. Por eso no deben usarse para validaciones críticas de negocio o seguridad.

### Sintaxis genérica[](#sintaxis-generica "Permanent link")

La estructura básica es:

```
assert condicion
assert condicion, "mensaje explicativo"
```

### Ejemplo de uso[](#ejemplo-de-uso "Permanent link")

Este ejemplo integra: - `assert` para comprobar un invariante interno (algo que “debe ser cierto” tras convertir). - `raise ... from ...` para transformar errores “técnicos” en un error “de dominio” manteniendo la causa.

```
class EdadInvalidaError(Exception):
    """Error del dominio: la edad recibida no es válida."""
    pass


def leer_edad(texto):
    """
    Convierte 'texto' a int y devuelve la edad.
    - Usa 'assert' para comprobar un supuesto interno (invariante) durante depuración.
    - Usa 'raise ... from ...' para encadenar la excepción original si la conversión falla.
    """
    try:
        edad = int(texto)  # Puede lanzar ValueError (cadena no numérica) o TypeError (None, etc.)

        # ASSERT (depuración): tras int(...), 'edad' *debe* ser un entero.
        # Esto NO valida al usuario: es un "chequeo de coherencia" del programa.
        # Si fallara, sería indicio de un bug o de un cambio inesperado en el código.
        assert isinstance(edad, int), "Invariante roto: 'edad' debería ser int tras int(texto)"

        # (Aquí podrías seguir con validaciones de negocio usando if/raise, si procede)
        return edad

    except (ValueError, TypeError) as e:
        # Traducimos el error técnico a un error de dominio y ENCADENAMOS la causa.
        raise EdadInvalidaError(f"No se pudo interpretar la edad a partir de {texto!r}") from e


# ---------------------------
# Pruebas didácticas
# ---------------------------
entradas = ["25", "hola", None]

for x in entradas:
    try:
        resultado = leer_edad(x)
        print(f"Entrada {x!r} → edad = {resultado}")

    except EdadInvalidaError as err:
        print(f"Entrada {x!r} → {type(err).__name__}: {err}")

        # La excepción original se conserva en __cause__ gracias a "raise ... from ..."
        print(f"   ↳ Causa original: {type(err.__cause__).__name__}: {err.__cause__}")

    except AssertionError as aerr:
        # En la práctica, este bloque suele indicar un bug interno, no una entrada inválida.
        print(f"Fallo de aserción (bug probable) → {aerr}")

    print("-" * 55)
```

- - -

## 6\. Excepciones personalizadas[](#6-excepciones-personalizadas "Permanent link")

### ¿Qué son y qué utilidad tienen?[](#que-son-y-que-utilidad-tienen "Permanent link")

Las excepciones personalizadas son **clases propias** (normalmente _**heredadas de**_ `Exception`) que te permiten representar errores de tu dominio (tu programa, tu aplicación) con nombres claros y tratarlos de forma específica.

**¿Por qué usarlas?**

*   **Claridad semántica**: no es lo mismo “ValueError genérico” que "EdadInvalidaError". El nombre ya explica el problema.
*   **Manejo más fino**: puedes capturar solo tus errores de negocio sin atrapar errores técnicos.
*   **Arquitectura por capas**: en capas externas (UI/API) puedes exponer un error “amigable” y por dentro encadenar la causa real con raise ... from ....
*   **Extensibilidad**: puedes crear una jerarquía de errores para categorías (validación, acceso a datos, permisos, etc.).

### Sintaxis[](#sintaxis "Permanent link")

La estructura típica es:

1.  Excepción mínima (la más común)

```
class MiError(Exception):
    pass
```

1.  Con mensaje y/o datos extra (opcional)

```
class MiError(Exception):
    def __init__(self, mensaje, codigo=None):
        super().__init__(mensaje)
        self.codigo = codigo
```

### Ejemplo[](#ejemplo "Permanent link")

```
# 1) Jerarquía de excepciones del dominio
class AppError(Exception):
    """Base para todos los errores de la aplicación."""
    pass

class ValidacionError(AppError):
    """Errores de validación de datos de entrada."""
    pass

class EdadInvalidaError(ValidacionError):
    """La edad no se pudo interpretar o no cumple el formato esperado."""
    pass


def leer_edad(texto):
    """
    Convierte 'texto' a int.
    - Si falla la conversión, lanzamos un error de dominio (EdadInvalidaError)
      encadenando la causa original (ValueError/TypeError).
    """
    try:
        edad = int(texto)
        return edad
    except (ValueError, TypeError) as e:
        # Traducimos el error técnico → error del dominio, conservando la causa.
        raise EdadInvalidaError(f"No se pudo interpretar la edad a partir de {texto!r}") from e


# ---------------------------
# Pruebas didácticas
# ---------------------------
entradas = ["30", "hola", None]

for x in entradas:
    try:
        print(f"{x!r} → {leer_edad(x)}")

    except EdadInvalidaError as err:
        # Captura específica: solo el caso "edad inválida"
        print(f"EdadInvalidaError: {err}")
        print(f"   ↳ Causa: {type(err.__cause__).__name__}: {err.__cause__}")

    except ValidacionError as err:
        # Captura más general dentro del dominio de validación
        print(f"ValidacionError: {err}")

    except AppError as err:
        # Captura aún más general: cualquier error propio de la app
        print(f"AppError: {err}")

    except Exception as e:
        # Último recurso: errores no contemplados (bugs, fallos del sistema, etc.)
        print(f"Error inesperado: {type(e).__name__}: {e}")
```

> **Ventaja:** Al capturar `AppError` atrapas **toda tu familia** de errores.

[⬆ Ir arriba](#top)

