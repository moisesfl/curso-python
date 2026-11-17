from abc import ABC, abstractmethod
from .excepciones import PesoInvalido, EdadInvalida, AlimentacionInvalida


class Animal(ABC):
    total_animales = 0

    def __init__(self, nombre: str, especie: str, peso_kg: float, edad: int):
        self._nombre = nombre
        self._especie = especie
        self.peso_kg = peso_kg
        self.edad = edad
        Animal.total_animales += 1

    # UTILIZACIÓN DE MÉTODOS GETTERS Y SETTERS 

    #     # Utilizamos los setters para validar los valores iniciales
    #     self.setNombre(nombre)
    #     self.setEspecie(especie)
    #     self.setPeso(peso_kg)
    #     self.setEdad(edad)

    # # -------------------------
    # # Getters y setters
    # # -------------------------

    # def getNombre(self) -> str:
    #     return self._nombre

    # def setNombre(self, nombre: str) -> None:
    #     if not isinstance(nombre, str) or not nombre.strip():
    #         raise ValueError("El nombre no puede estar vacío.")
    #     self._nombre = nombre

    # def getEspecie(self) -> str:
    #     return self._especie

    # def setEspecie(self, especie: str) -> None:
    #     if not isinstance(especie, str) or not especie.strip():
    #         raise ValueError("La especie no puede estar vacía.")
    #     self._especie = especie

    # def getPeso(self) -> float:
    #     return self._peso_kg

    # def setPeso(self, peso: float) -> None:
    #     if not isinstance(peso, (int, float)) or peso <= 0:
    #         raise PesoInvalido("El peso debe ser un número mayor que cero.")
    #     self._peso_kg = float(peso)

    # def getEdad(self) -> int:
    #     return self._edad

    # def setEdad(self, edad: int) -> None:
    #     if not isinstance(edad, int) or edad < 0:
    #         raise EdadInvalida("La edad debe ser un entero mayor o igual que cero.")
    #     self._edad = edad



    #UTILIZACIÓN DE @PROPERTY
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def especie(self) -> str:
        return self._especie

    @especie.setter
    def especie(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La especie no puede estar vacía.")
        self._especie = valor

    @property
    def peso_kg(self) -> float:
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise PesoInvalido("El peso debe ser un número mayor que cero.")
        self._peso_kg = float(valor)

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise EdadInvalida("La edad debe ser un entero mayor o igual que cero.")
        self._edad = valor

    @abstractmethod
    def moverse(self) -> None:
        """Describe cómo se mueve el animal."""
        raise NotImplementedError

    @abstractmethod
    def getTipo(self) -> str:
        """Devuelve la raza o variedad del animal."""
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def parir(nombre: str) -> "Animal":
        """Crea y devuelve un nuevo animal de la subclase correspondiente."""
        raise NotImplementedError

    def alimentar(self, kg: float) -> None:
        if not isinstance(kg, (int, float)) or kg <= 0:
            raise AlimentacionInvalida("La cantidad de alimento debe ser mayor que cero.")
        self._peso_kg += float(kg)
        print(f"{self.nombre} ha comido {kg} kg. Nuevo peso: {self.peso_kg:.2f} kg")

    def __str__(self) -> str:
        return (
            f"Clase {self.__class__}: nombre {self.nombre}, especie {self.especie}, "
            f"peso {self.peso_kg:.1f} kg, edad {self.edad} años"
        )
