"""Protocols para detectar capacidades sin exigir una jerarquía rígida."""
from typing import Protocol, runtime_checkable


@runtime_checkable
class Medible(Protocol):
    def leer_valor(self) -> float: ...


@runtime_checkable
class Conmutable(Protocol):
    """Capacidad de activar y desactivar un dispositivo."""
    def encender(self) -> None: ...
    def apagar(self) -> None: ...


@runtime_checkable
class Actualizable(Protocol):
    def actualizar_firmware(self, version: str) -> None: ...
