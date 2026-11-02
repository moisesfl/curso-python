"""Hub central: registro y operaciones polimórficas."""
from .base import Dispositivo
from .common import Duplicado, NoEncontrado
from .interfaces import Medible, Conmutable


class Hub:
    def __init__(self):
        self._dispositivos: dict[str, Dispositivo] = {}

    def registrar(self, disp: Dispositivo) -> None:
        if disp.id in self._dispositivos:
            raise Duplicado(f"El ID '{disp.id}' ya existe")
        self._dispositivos[disp.id] = disp

    def listar(self) -> list[Dispositivo]:
        return list(self._dispositivos.values())

    def obtener(self, id: str) -> Dispositivo:
        try:
            return self._dispositivos[id]
        except KeyError:
            raise NoEncontrado(f"No existe el dispositivo '{id}'") from None

    def operar_todos(self) -> None:
        for disp in self.listar():
            if isinstance(disp, Medible):
                print(f"* {disp.id} → lectura = {disp.leer_valor():.2f}")
            if isinstance(disp, Conmutable):
                disp.encender()
                print(f"* {disp.id} → encender() → OK")
                disp.apagar()
                print(f"  {disp.id} → apagar() → OK")

    def estadisticas(self) -> dict[str, int]:
        resultado: dict[str, int] = {}
        for disp in self._dispositivos.values():
            resultado[disp.tipo()] = resultado.get(disp.tipo(), 0) + 1
        return resultado
