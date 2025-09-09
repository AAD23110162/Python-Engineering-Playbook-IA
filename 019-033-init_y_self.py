
"""
019-033-init_y_self.py
----------------------
Clase Producto con atributos obligatorios definidos en __init__:
- nombre, precio_base, iva (porcentaje p.ej. 16), descuento (porcentaje p.ej. 10)
Método:
- precio_final(): aplica IVA y luego descuento → total = base*(1+iva/100)*(1-desc/100)

Modos:
  DEMO: crea productos y muestra su precio final.
  INTERACTIVO: captura datos por teclado y calcula.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio_base: float
    iva: float       # porcentaje (ej. 16 para 16%)
    descuento: float # porcentaje (ej. 10 para 10%)

    def __post_init__(self) -> None:
        if self.precio_base < 0: raise ValueError("precio_base no puede ser negativo.")
        if self.iva < 0: raise ValueError("iva no puede ser negativo.")
        if not (0 <= self.descuento <= 100): raise ValueError("descuento debe estar entre 0 y 100.")

    def precio_final(self) -> float:
        total = self.precio_base * (1 + self.iva / 100.0)
        total *= (1 - self.descuento / 100.0)
        return round(total, 2)

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
    p1 = Producto("Baguette", 80.0, iva=16.0, descuento=0.0)
    p2 = Producto("Café Latte", 50.0, iva=16.0, descuento=10.0)
    print(f"{p1.nombre}: base={p1.precio_base} → final={p1.precio_final()}")
    print(f"{p2.nombre}: base={p2.precio_base} → final={p2.precio_final()}")

def interactivo() -> None:
    nombre = input("Nombre del producto: ").strip() or "Producto"
    base = leer_float("Precio base: ", minimo=0.0)
    iva = leer_float("IVA (%) ej. 16: ", minimo=0.0)
    desc = leer_float("Descuento (%) 0–100: ", minimo=0.0)
    try:
        p = Producto(nombre, base, iva, desc)
        print(f"Precio final de {p.nombre}: {p.precio_final()}")
    except ValueError as e:
        print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
