
"""
012-022-pilares_oop.py
----------------------
Modo DEMO: crea un Rectangulo y un Circulo y muestra área/perímetro.
Modo INTERACTIVO: permite elegir figura y capturar dimensiones.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def perimetro(self) -> float: ...
    def resumen(self) -> str:
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimetro={self.perimetro():.2f}"

class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float) -> None:
        self.ancho = ancho; self.alto = alto
    @property
    def ancho(self) -> float: return self._ancho
    @ancho.setter
    def ancho(self, v: float) -> None:
        if v <= 0: raise ValueError("El ancho debe ser positivo.")
        self._ancho = float(v)
    @property
    def alto(self) -> float: return self._alto
    @alto.setter
    def alto(self, v: float) -> None:
        if v <= 0: raise ValueError("El alto debe ser positivo.")
        self._alto = float(v)
    def area(self) -> float: return self.ancho * self.alto
    def perimetro(self) -> float: return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio
    @property
    def radio(self) -> float: return self._radio
    @radio.setter
    def radio(self, v: float) -> None:
        if v <= 0: raise ValueError("El radio debe ser positivo.")
        self._radio = float(v)
    def area(self) -> float: return math.pi * self.radio**2
    def perimetro(self) -> float: return 2 * math.pi * self.radio

def leer_float(msg: str, minimo: float = 0.0) -> float:
    while True:
        s = input(msg).strip()
        try:
            v = float(s)
            if v <= minimo:
                print(f"⚠️ Debe ser > {minimo}.")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def run_demo() -> None:
    figuras: list[Figura] = [Rectangulo(3, 4), Circulo(2.5)]
    for f in figuras:
        print(f.resumen())

def run_interactivo() -> None:
    print("Elige figura: [1] Rectangulo  [2] Circulo")
    op = input("Opción: ").strip()
    try:
        if op == "1":
            a = leer_float("Ancho: ", 0.0)
            h = leer_float("Alto: ", 0.0)
            fig = Rectangulo(a, h)
        elif op == "2":
            r = leer_float("Radio: ", 0.0)
            fig = Circulo(r)
        else:
            print("Opción no válida. Saliendo.")
            return
        print(fig.resumen())
    except ValueError as e:
        print(f"Error: {e}")

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    if modo.startswith("i"):
        run_interactivo()
    else:
        run_demo()

if __name__ == "__main__":
    main()
