from .base import Animal


class Perro(Animal):
    def __init__(self, nombre: str, peso_kg: float, edad: int, raza: str):
        super().__init__(nombre, "Perro", peso_kg, edad)
        self.raza = raza

    def moverse(self) -> None:
        print("...corre... ...salta... ...mueve la cola...")

    def getTipo(self) -> str:
        return self.raza

    def hacerSonido(self) -> None:
        print("¡GUAU GUAU!")

    @staticmethod
    def parir(nombre: str) -> "Perro":
        return Perro(nombre, peso_kg=2.0, edad=0, raza="Bichón Maltés")

    def __str__(self) -> str:
        return f"{super().__str__()}, raza {self.raza}"


class Aguila(Animal):
    def __init__(self, nombre: str, peso_kg: float, edad: int,
                 subespecie: str, envergadura_cm: float):
        super().__init__(nombre, "Aguila", peso_kg, edad)
        self.subespecie = subespecie
        self.envergadura_cm = envergadura_cm

    def moverse(self) -> None:
        print("...bate las alas... ...asciende... ...planea alto...")

    def getTipo(self) -> str:
        return self.subespecie

    def volar(self) -> None:
        print(f"{self.nombre} está volando.")

    def hacerSonido(self) -> None:
        print("¡IIIIIIIIHHHHH!")

    @staticmethod
    def parir(nombre: str) -> "Aguila":
        return Aguila(nombre, peso_kg=2.0, edad=0,
                      subespecie="Calva", envergadura_cm=15.0)

    def __str__(self) -> str:
        return f"{super().__str__()}, envergadura {self.envergadura_cm} cm"


class Serpiente(Animal):
    def __init__(self, nombre: str, peso_kg: float, edad: int,
                 subespecie: str, venenosa: bool):
        super().__init__(nombre, "Serpiente", peso_kg, edad)
        self.subespecie = subespecie
        self.venenosa = venenosa

    def moverse(self) -> None:
        print("...se desliza... ...repta entre las rocas... ...saca la lengua...")

    def getTipo(self) -> str:
        return self.subespecie

    def hacerSonido(self) -> None:
        print("SSSSSSS!")

    @staticmethod
    def parir(nombre: str) -> "Serpiente":
        return Serpiente(nombre, peso_kg=0.2, edad=0,
                         subespecie="Culebra", venenosa=False)

    def __str__(self) -> str:
        return f"{super().__str__()}, venenosa {self.venenosa}"
