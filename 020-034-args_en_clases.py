
"""
020-034-args_en_clases.py
-------------------------
Clase Paquete que acepta items por *args en el constructor.
Cada item es una tupla (nombre, peso_kg, volumen_l).

Modos:
  DEMO: crea un paquete con algunos items y muestra totales.
  INTERACTIVO: permite capturar items por teclado.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Tuple, List

Item = Tuple[str, float, float]  # (nombre, peso_kg, volumen_l)

@dataclass
class Paquete:
    items: List[Item]

    def __init__(self, *items: Item) -> None:
        self.items = []
        for it in items:
            self.agregar(it)

    def agregar(self, item: Item) -> None:
        nombre, peso, vol = item
        if not nombre.strip():
            raise ValueError("El nombre del item no puede estar vacío.")
        if peso <= 0 or vol < 0:
            raise ValueError("Peso debe ser > 0 y volumen ≥ 0.")
        self.items.append((nombre.strip(), float(peso), float(vol)))

    @property
    def peso_total(self) -> float:
        return round(sum(p for _, p, _ in self.items), 3)

    @property
    def volumen_total(self) -> float:
        return round(sum(v for _, _, v in self.items), 3)

    def resumen(self) -> str:
        return f"Items={len(self.items)} | peso_total={self.peso_total} kg | volumen_total={self.volumen_total} L"

def leer_float(msg: str, minimo: float | None = None) -> float:
    while True:
        s = input(msg).strip()
        try:
            v = float(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    p = Paquete(("Baguette", 0.25, 1.2), ("Café Latte", 0.35, 0.5), ("Té Verde", 0.20, 0.4))
    print(p.resumen())
    for it in p.items:
        print(" -", it)

def interactivo() -> None:
    print("=== Crear paquete (enter en nombre para terminar) ===")
    paquete = Paquete()
    while True:
        nombre = input("Nombre del item: ").strip()
        if not nombre:
            break
        peso = leer_float("Peso (kg)  ≥ 0.001: ", minimo=0.001)
        vol = leer_float("Volumen (L) ≥ 0.0  : ", minimo=0.0)
        try:
            paquete.agregar((nombre, peso, vol))
        except ValueError as e:
            print("Error:", e)
    print("\nResumen:", paquete.resumen())
    for it in paquete.items:
        print(" -", it)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
