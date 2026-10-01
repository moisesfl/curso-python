# Tarea entregable UD05: Sistema de Validación Bancaria "SafeBank"

##  Índice de contenidos

- [ Contexto general](#-contexto-general)
- [ Datos de partida](#-datos-de-partida)
- [ Requisitos funcionales (QUÉ debe hacer el programa](#-requisitos-funcionales-qué-debe-hacer-el-programa)
  - [1. Función `procesar_transferencia(cuenta_origen, montante)`](#1-función-procesar_transferenciacuenta_origen-montante)
  - [2. El Bloque de Control (Menú Interactivo)](#2-el-bloque-de-control-menú-interactivo)
- [ Requisitos técnicos (CÓMO debe hacerse)](#-requisitos-técnicos-cómo-debe-hacerse)
- [ Criterios de evaluación cubiertos](#-criterios-de-evaluación-cubiertos)

---

##  Contexto general

Vas a desarrollar el módulo de seguridad de una aplicación bancaria. El sistema debe procesar transferencias entre cuentas, validando que los datos sean correctos, que haya saldo suficiente y que el sistema no sufra errores de coherencia interna.

##  Datos de partida

Copia estas excepciones personalizadas al inicio de tu código (puedes cambiar el mensaje de error):

```python
class BancoError(Exception):
    """Base para todas las excepciones del banco."""
    pass


class SaldoInsuficienteError(BancoError):
    """Lanzada cuando la cuenta origen no tiene fondos suficientes."""
    pass


class CuentaInvalidaError(BancoError):
    """Lanzada cuando el formato de la cuenta o el titular no es correcto."""
    pass
```

##  Requisitos funcionales (QUÉ debe hacer el programa)

### 1. Función `procesar_transferencia(cuenta_origen, montante)`

Esta función debe orquestar la seguridad del proceso:

1. **Validación de Tipo:** Usa un `assert` para comprobar que el montante es un número (`int` o `float`). Si falla, significa que hay un bug en el código que llamó a la función.

2. **Validación de Negocio:**
   - Si el montante es menor o igual a 0, lanza un `ValueError` con un mensaje descriptivo.
   - Si el montante es mayor a 1000€ (límite del banco), lanza una `CuentaInvalidaError` con el mensaje `"Límite de transferencia diaria excedido"`.

3. **Encadenamiento de Excepciones:**
   - Simula un saldo fijo de 500€ (con una constante). Si el montante supera los 500€, lanza un `SaldoInsuficienteError`.
   - Dentro de un bloque `try-except`, intenta convertir el nombre de la `cuenta_origen` a mayúsculas. Si te pasan un valor `None` o un número en lugar de un `string`, captura el `AttributeError` o `TypeError` y lanza un `CuentaInvalidaError` `from` el error original (encadenamiento).

### 2. El Bloque de Control (Menú Interactivo)

Crea un bucle `while` que pida al usuario el nombre del titular y la cantidad a enviar.

- **Captura Específica:** Maneja `SaldoInsuficienteError` y `CuentaInvalidaError` mostrando mensajes amigables al cliente.
- **Captura de Datos:** Maneja el `ValueError` si el usuario introduce letras en la cantidad de dinero.
- **Bloque Finally:** Independientemente de si la transferencia se hizo o falló, debe imprimir: `"Cierre de sesión seguro en la pasarela de pagos"`.

##  Requisitos técnicos (CÓMO debe hacerse)

- **Excepciones:** Debes utilizar correctamente las excepciones, tanto su lanzamiento como su captura de los modos vistos en la unidad 5 (`raise`, captura múltiple, bloques `try - except - else - finally`,...).
- **Aplicar correctamente:**
  - El sangrado
  - El control del flujo de ejecución
  - La gestión de variables
- El código debe ser legible, ordenado y comentado.

