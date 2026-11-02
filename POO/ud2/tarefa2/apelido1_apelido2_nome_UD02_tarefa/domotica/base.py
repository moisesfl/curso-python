"""Clase abstracta común a todos los dispositivos."""
from abc import ABC, abstractmethod
from .common import DatoInvalido, Utils


class Dispositivo(ABC):
    def __init__(self, id: str, nombre: str, fabricante: str):
        if not Utils.validar_id(id):
            raise DatoInvalido(f"ID inválido: {id!r}")
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalido("El nombre no puede estar vacío")
        if not isinstance(fabricante, str) or not fabricante.strip():
            raise DatoInvalido("El fabricante no puede estar vacío")
        self._id = id.strip()
        self._nombre = nombre.strip()
        self._fabricante = fabricante.strip()

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, valor: str) -> None:
        if not Utils.validar_id(valor):
            raise DatoInvalido(f"ID inválido: {valor!r}")
        self._id = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalido("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def fabricante(self) -> str:
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalido("El fabricante no puede estar vacío")
        self._fabricante = valor.strip()

    @abstractmethod
    def tipo(self) -> str:
        """Devuelve el tipo concreto del dispositivo."""

    def __str__(self) -> str:
        return f"[{self.tipo()}] {self.nombre} (id={self.id}, fabricante={self.fabricante})"
