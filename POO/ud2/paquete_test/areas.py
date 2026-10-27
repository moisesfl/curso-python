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

def area_triangulo():
    print("cáculo área triángulo")
    return