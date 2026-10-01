# ==========================================
# EXCEPCIONES PERSONALIZADAS
# ==========================================

class BancoError(Exception):
    """Base para todas las excepciones del banco."""
    pass


class SaldoInsuficienteError(BancoError):
    """La cuenta no tiene fondos suficientes."""
    pass


class CuentaInvalidaError(BancoError):
    """La cuenta o el titular no son válidos."""
    pass


# ==========================================
# CONSTANTE
# ==========================================

SALDO_DISPONIBLE = 500


# ==========================================
# FUNCIÓN PRINCIPAL
# ==========================================

def procesar_transferencia(cuenta_origen, monto):
    """
    Valida y procesa una transferencia bancaria.
    """

    # 1. Validación de tipo
    assert isinstance(monto, (int, float)), \
        "El monto debe ser un número"

    # 2. Validación del monto
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que 0")

    # Límite diario del banco
    if monto > 1000:
        raise CuentaInvalidaError(
            "Límite de transferencia diaria excedido"
        )

    # 3. Comprobación del saldo
    if monto > SALDO_DISPONIBLE:
        raise SaldoInsuficienteError(
            "Saldo insuficiente para realizar la transferencia"
        )

    # 4. Validación de la cuenta
    try:
        cuenta = cuenta_origen.upper()

        #Nunca saltará la excepción ya que la varible cuenta simpre será un string porque viene de input()
    except (AttributeError, TypeError) as error:
        # Encadenamiento de excepciones
        raise CuentaInvalidaError(
            "El nombre de la cuenta no es válido"
        ) from error

    # Si todo es correcto
    return f"Transferencia de {monto:.2f} € realizada correctamente desde {cuenta}"
    

# ==========================================
# BLOQUE DE CONTROL
# ==========================================

while True:

    try:
        # Pedimos los datos al usuario
        cuenta = input("Nombre del titular: ")

        cantidad = input("Cantidad a enviar: ")

        # Convertimos el texto a número
        monto = float(cantidad)

        # Procesamos la transferencia
        resultado = procesar_transferencia(cuenta, monto)

    except SaldoInsuficienteError as error:

        print(f"❌ {error}")

    except CuentaInvalidaError as error:

        print(f"❌ {error}")

    # Se puede añadir as error para ver el mensaje concreto donde ha saltado el raise
    except ValueError:

        print("❌ La cantidad debe ser un número válido.")
        #print (error)

    else:

        # Solo se ejecuta si NO ha habido ninguna excepción
        print(f"✅ {resultado}")

    finally:

        print("Cierre de sesión seguro en la pasarela de pagos")
        print("-" * 50)