
"""
011-021-oop_intro_resumen.py
----------------------------
Modo DEMO: crea un Usuario y un Pedido con ítems, paga y muestra estados.
Modo INTERACTIVO: te pide datos (usuario e ítems) y ejecuta el flujo.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    def actualizar_email(self, nuevo: str) -> None:
        if "@" not in nuevo:
            raise ValueError("Email inválido.")
        self.email = nuevo

@dataclass
class ItemPedido:
    sku: str
    cantidad: int
    precio_unitario: float
    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario

@dataclass
class Pedido:
    folio: str
    usuario: Usuario
    items: List[ItemPedido] = field(default_factory=list)
    pagado: bool = False
    def agregar_item(self, sku: str, cantidad: int, precio_unitario: float) -> None:
        if cantidad <= 0 or precio_unitario < 0:
            raise ValueError("Cantidad o precio inválido.")
        self.items.append(ItemPedido(sku, cantidad, precio_unitario))
    @property
    def total(self) -> float:
        return round(sum(i.subtotal for i in self.items), 2)
    def pagar(self) -> None:
        if not self.items:
            raise RuntimeError("No se puede pagar un pedido vacío.")
        self.pagado = True
    def resumen(self) -> str:
        estado = "PAGADO" if self.pagado else "PENDIENTE"
        return f"Pedido {self.folio} de {self.usuario.nombre} → total=${self.total} ({estado})"

# Utilidades de entrada segura
def leer_int(msg: str, minimo: Optional[int] = None) -> int:
    while True:
        s = input(msg).strip()
        try:
            v = int(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un entero válido.")

def leer_float(msg: str, minimo: Optional[float] = None) -> float:
    while True:
        s = input(msg).strip()
        try:
            v = float(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def run_demo() -> None:
    u = Usuario(1, "Alejandro", "alejandro@example.com")
    p = Pedido("A-1001", u)
    p.agregar_item("SKU-ABC", 2, 150.0)
    p.agregar_item("SKU-XYZ", 1, 299.99)
    print("Antes de pagar:", p.resumen())
    p.pagar()
    print("Después de pagar:", p.resumen())

def run_interactivo() -> None:
    print("=== Crear usuario ===")
    uid = leer_int("ID (entero): ", minimo=1)
    nombre = input("Nombre: ").strip() or "Usuario"
    email = input("Email: ").strip() or "user@example.com"
    u = Usuario(uid, nombre, email)

    folio = input("Folio del pedido (ej. P-0001): ").strip() or "P-0001"
    p = Pedido(folio, u)

    print("\n=== Agregar ítems (vacío para terminar) ===")
    while True:
        sku = input("SKU: ").strip()
        if not sku:
            break
        cantidad = leer_int("Cantidad: ", minimo=1)
        precio = leer_float("Precio unitario: ", minimo=0.0)
        try:
            p.agregar_item(sku, cantidad, precio)
        except ValueError as e:
            print(f"Error: {e}")
        print(f"Subtotal actual: ${p.total}")

    if not p.items:
        print("No agregaste ítems. Saliendo.")
        return

    print("\nResumen:", p.resumen())
    pagar = input("¿Pagar ahora? [s/N]: ").strip().lower()
    if pagar == "s":
        p.pagar()
    print("Estado final:", p.resumen())

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    if modo.startswith("i"):
        run_interactivo()
    else:
        run_demo()

if __name__ == "__main__":
    main()
