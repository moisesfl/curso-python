# __init__.py
# Propósito: definir la API pública del paquete 'geometria' para que
# los consumidores puedan importar directamente lo que necesitan.
# Ejemplo: `from geometria import area_circulo`

from .areas import area_circulo, area_rectangulo, area_triangulo

# __all__ controla qué símbolos se exportan cuando se usa `from geometria import *`.
__all__ = ["area_circulo", "area_rectangulo","area_triangulo"]