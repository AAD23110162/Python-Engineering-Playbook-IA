
"""
017-031-intro_poo.py
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
        # Desplaza el punto sumando dx y dy a las coordenadas actuales
        self.x += dx
        self.y += dy

    def distancia(self, otro: "Punto2D") -> float:
        # Calcula la distancia euclidiana entre este punto y otro
        return math.hypot(self.x - otro.x, self.y - otro.y)

def leer_float(msg: str) -> float:
    # Solicita un número flotante al usuario y valida la entrada
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    # Modo demostración: crea dos puntos, los mueve y calcula distancias
    a = Punto2D(0, 0)
    b = Punto2D(3, 4)
    print(f"A={a}  B={b}  dist(A,B)={a.distancia(b):.2f}")
    a.mover(1, -2)
    print(f"Mover A por (1,-2) → A={a}, dist(A,B)={a.distancia(b):.2f}")

def interactivo() -> None:
    # Modo interactivo: permite al usuario crear y manipular dos puntos
    print("=== Crear puntos ===")
    ax, ay = leer_float("A.x: "), leer_float("A.y: ")
    bx, by = leer_float("B.x: "), leer_float("B.y: ")
    a, b = Punto2D(ax, ay), Punto2D(bx, by)

    while True:
        print("\n1) Mover A   2) Mover B   3) Distancia A-B   4) Salir")
        op = input("Opción: ").strip()
        if op == "1":
                # Solicita los valores dx y dy para mover A
            a.mover(leer_float("dx: "), leer_float("dy: "))
            print("A →", a)
        elif op == "2":
                # Solicita los valores dx y dy para mover B
            b.mover(leer_float("dx: "), leer_float("dy: "))
            print("B →", b)
        elif op == "3":
                # Calcula la distancia actual entre A y B
            print(f"dist(A,B) = {a.distancia(b):.3f}")
        elif op == "4":
                # Sale del ciclo interactivo
            break
        else:
                # Si la opción no es válida, muestra mensaje
            print("Opción no válida.")

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    # Si el modo empieza con 'i', activa el modo interactivo; si no, ejecuta demo
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
