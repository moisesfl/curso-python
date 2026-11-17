from typing import Protocol, runtime_checkable


@runtime_checkable
class Sonoro(Protocol):
    def hacerSonido(self) -> None:
        ...


@runtime_checkable
class Alimentable(Protocol):
    def alimentar(self, kg: float) -> None:
        ...
