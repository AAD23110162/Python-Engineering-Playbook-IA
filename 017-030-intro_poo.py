
"""
017-030-intro_poo.py
--------------------
Clase Punto2D con:
- mover(dx, dy)
- distancia(otro)

Modos:
  DEMO: crea puntos, los mueve y calcula distancias.
  INTERACTIVO: captura coordenadas y operaciones por teclado.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
import math
from dataclasses import dataclass

@dataclass
class Punto2D:
    x: float
    y: float

    def mover(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def distancia(self, otro: "Punto2D") -> float:
        return math.hypot(self.x - otro.x, self.y - otro.y)

def leer_float(msg: str) -> float:
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    a = Punto2D(0, 0)
    b = Punto2D(3, 4)
    print(f"A={a}  B={b}  dist(A,B)={a.distancia(b):.2f}")
    a.mover(1, -2)
    print(f"Mover A por (1,-2) → A={a}, dist(A,B)={a.distancia(b):.2f}")

def interactivo() -> None:
    print("=== Crear puntos ===")
    ax, ay = leer_float("A.x: "), leer_float("A.y: ")
    bx, by = leer_float("B.x: "), leer_float("B.y: ")
    a, b = Punto2D(ax, ay), Punto2D(bx, by)

    while True:
        print("\n1) Mover A   2) Mover B   3) Distancia A-B   4) Salir")
        op = input("Opción: ").strip()
        if op == "1":
            a.mover(leer_float("dx: "), leer_float("dy: "))
            print("A →", a)
        elif op == "2":
            b.mover(leer_float("dx: "), leer_float("dy: "))
            print("B →", b)
        elif op == "3":
            print(f"dist(A,B) = {a.distancia(b):.3f}")
        elif op == "4":
            break
        else:
            print("Opción no válida.")

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
