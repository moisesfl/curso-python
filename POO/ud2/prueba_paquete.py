# Importación directa desde el paquete (gracias a __init__.py)
#from paquete_test import area_circulo, area_rectangulo, area_triangulo
from paquete_test import *


def main() -> None:
    """
    Punto de entrada de la aplicación.
    """

    print("=== DEMOSTRACIÓN DEL PAQUETE 'geometria' ===\n")

    area_t = area_triangulo()

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