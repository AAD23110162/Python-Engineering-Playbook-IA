#!/usr/bin/env python3
"""
012-020-pilares_oop.py
----------------------
Demostración de los pilares OOP:
- Abstracción: clase abstracta `Figura` (interface de `area()` y `perimetro()`).
- Herencia y polimorfismo: `Rectangulo`, `Circulo` implementan la interfaz.
- Encapsulamiento: validación y propiedades controladas.

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import math


class Figura(ABC):
    """Interfaz de figuras geométricas."""

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimetro(self) -> float: ...

    def resumen(self) -> str:
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimetro={self.perimetro():.2f}"


class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float) -> None:
        self.ancho = ancho
        self.alto = alto

    # Encapsulamiento con property (validación)
    @property
    def ancho(self) -> float:
        return self._ancho

    @ancho.setter
    def ancho(self, v: float) -> None:
        if v <= 0:
            raise ValueError("El ancho debe ser positivo.")
        self._ancho = float(v)

    @property
    def alto(self) -> float:
        return self._alto

    @alto.setter
    def alto(self, v: float) -> None:
        if v <= 0:
            raise ValueError("El alto debe ser positivo.")
        self._alto = float(v)

    # Implementaciones concretas (polimorfismo)
    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)


class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio

    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, v: float) -> None:
        if v <= 0:
            raise ValueError("El radio debe ser positivo.")
        self._radio = float(v)

    def area(self) -> float:
        return math.pi * self.radio**2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


def demo() -> None:
    figuras: list[Figura] = [Rectangulo(3, 4), Circulo(2.5)]
    for f in figuras:
        print(f.resumen())


if __name__ == "__main__":
    demo()
