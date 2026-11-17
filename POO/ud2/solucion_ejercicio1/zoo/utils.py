class ZooUtils:
    # Rangos orientativos de ejemplo (peso mínimo, peso máximo), en kg.
    # En una aplicación real deberían depender de la raza, sexo y desarrollo.
    RANGOS_PESO = {
        "perro": (5, 35),
        "aguila": (1, 12),
        "serpiente": (0.1, 5),
    }

    @staticmethod
    def es_peso_saludable(especie: str, edad: int, peso_kg: float) -> str:
        """
        Devuelve 'bajo', 'adecuado' o 'alto'.
        Los rangos son didácticos y no constituyen una valoración veterinaria.
        """
        if peso_kg <= 0 or edad < 0:
            raise ValueError("El peso debe ser positivo y la edad no negativa.")

        rango = ZooUtils.RANGOS_PESO.get(especie.lower())
        if rango is None:
            raise ValueError(f"No hay un rango definido para {especie}.")

        minimo, maximo = rango
        if peso_kg < minimo:
            return "bajo"
        if peso_kg > maximo:
            return "alto"
        return "adecuado"
