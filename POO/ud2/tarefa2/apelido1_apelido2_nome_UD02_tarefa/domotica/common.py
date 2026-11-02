"""Utilidades y excepciones independientes de las clases de dispositivos."""
import re


class DatoInvalido(ValueError):
    """Un dato no cumple el formato o las reglas de negocio."""


class Duplicado(Exception):
    """Se intenta insertar una clave que ya existe."""


class NoEncontrado(Exception):
    """No existe el elemento solicitado."""


class Utils:
    @staticmethod
    def validar_id(texto: str) -> bool:
        """ID no vacío, comienza por letra y continúa con letras, números o guiones."""
        return (
            isinstance(texto, str)
            and bool(texto.strip())
            and re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*", texto.strip()) is not None
        )

    @staticmethod
    def fabricar_id(prefijo: str, n: int) -> str:
        if not isinstance(prefijo, str) or not prefijo.strip():
            raise DatoInvalido("El prefijo debe ser un texto no vacío")
        if isinstance(n, bool) or not isinstance(n, int) or n < 1:
            raise DatoInvalido("n debe ser un entero positivo (>= 1)")
        candidato = f"{prefijo.strip().upper()}{n:03d}"
        if not Utils.validar_id(candidato):
            raise DatoInvalido(f"ID generado inválido: '{candidato}'")
        return candidato

    @staticmethod
    def validar_version(version: str) -> bool:
        return (
            isinstance(version, str)
            and re.fullmatch(r"\d+\.\d+\.\d+", version.strip()) is not None
        )
