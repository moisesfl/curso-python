"""Dispositivos concretos del sistema."""
from .base import Dispositivo
from .common import DatoInvalido, Utils


class SensorTemperatura(Dispositivo):
    def __init__(self, id: str, nombre: str, fabricante: str, celsius: float):
        super().__init__(id, nombre, fabricante)
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise DatoInvalido("La temperatura debe ser numérica")
        self._celsius = float(valor)

    def leer_valor(self) -> float:
        return self._celsius

    def calibrar(self, offset: float) -> None:
        if isinstance(offset, bool) or not isinstance(offset, (int, float)):
            raise DatoInvalido("El offset debe ser numérico")
        self._celsius += float(offset)

    def tipo(self) -> str:
        return "SensorTemperatura"

    def __str__(self) -> str:
        return f"{super().__str__()[:-1]}, {self.celsius:.1f} ºC)"


class BombillaInteligente(Dispositivo):
    def __init__(self, id: str, nombre: str, fabricante: str,
                 brillo: int = 100, encendida: bool = False):
        super().__init__(id, nombre, fabricante)
        self.brillo = brillo
        if not isinstance(encendida, bool):
            raise DatoInvalido("encendida debe ser bool")
        self._encendida = encendida
        self._firmware = "1.0.0"

    @property
    def brillo(self) -> int:
        return self._brillo

    @brillo.setter
    def brillo(self, valor: int) -> None:
        if isinstance(valor, bool) or not isinstance(valor, int) or not 0 <= valor <= 100:
            raise DatoInvalido("El brillo debe ser un entero entre 0 y 100")
        self._brillo = valor

    @property
    def encendida(self) -> bool:
        return self._encendida

    def encender(self) -> None:
        self._encendida = True

    def apagar(self) -> None:
        self._encendida = False

    def actualizar_firmware(self, version: str) -> None:
        if not Utils.validar_version(version):
            raise DatoInvalido("Versión inválida (formato esperado X.Y.Z)")
        self._firmware = version.strip()

    def tipo(self) -> str:
        return "BombillaInteligente"

    def __str__(self) -> str:
        estado = "encendida" if self.encendida else "apagada"
        return f"{super().__str__()[:-1]}, brillo={self.brillo}, {estado})"


class CerraduraInteligente(Dispositivo):
    def __init__(self, id: str, nombre: str, fabricante: str, bloqueada: bool = True):
        super().__init__(id, nombre, fabricante)
        if not isinstance(bloqueada, bool):
            raise DatoInvalido("bloqueada debe ser bool")
        self._bloqueada = bloqueada

    @property
    def bloqueada(self) -> bool:
        return self._bloqueada

    def bloquear(self) -> None:
        self._bloqueada = True

    def desbloquear(self) -> None:
        self._bloqueada = False

    # Adaptación semántica del protocolo Conmutable para operaciones comunes del Hub.
    def encender(self) -> None:
        self.bloquear()

    def apagar(self) -> None:
        self.desbloquear()

    def tipo(self) -> str:
        return "CerraduraInteligente"

    def __str__(self) -> str:
        estado = "bloqueada" if self.bloqueada else "desbloqueada"
        return f"{super().__str__()[:-1]}, {estado})"
