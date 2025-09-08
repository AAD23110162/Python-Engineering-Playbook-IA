
"""
018-030-atributos_y_metodos.py
------------------------------
Clase CuentaBancaria con:
- depositar(monto)
- retirar(monto)
- transferir(otra, monto)
- saldo (property de solo lectura)
- __repr__

Modos:
  DEMO: muestra operaciones típicas.
  INTERACTIVO: crea cuentas y ofrece un mini-menú.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations

class CuentaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0) -> None:
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial no puede ser negativo.")
        self.titular = titular
        self._saldo = float(saldo_inicial)

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El depósito debe ser > 0.")
        self._saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El retiro debe ser > 0.")
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes.")
        self._saldo -= monto

    def transferir(self, otra: "CuentaBancaria", monto: float) -> None:
        self.retirar(monto)
        otra.depositar(monto)

    def __repr__(self) -> str:
        return f"CuentaBancaria(titular={self.titular!r}, saldo={self._saldo:.2f})"

def leer_float(msg: str) -> float:
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    a = CuentaBancaria("Ana", 100)
    b = CuentaBancaria("Ben", 50)
    print(a, b)
    a.depositar(25); print("Ana deposita 25 →", a)
    a.transferir(b, 60); print("Ana transfiere 60 a Ben →", a, b)
    try:
        b.retirar(1000)
    except ValueError as e:
        print("Retiro inválido:", e)

def interactivo() -> None:
    print("=== Crear dos cuentas ===")
    a = CuentaBancaria(input("Titular A: ").strip() or "A", leer_float("Saldo A: "))
    b = CuentaBancaria(input("Titular B: ").strip() or "B", leer_float("Saldo B: "))
    while True:
        print("\n1) Depositar en A  2) Retirar de A  3) Transferir A→B")
        print("4) Depositar en B  5) Retirar de B  6) Transferir B→A")
        print("7) Ver estados     8) Salir")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                a.depositar(leer_float("Monto: ")); print(a)
            elif op == "2":
                a.retirar(leer_float("Monto: ")); print(a)
            elif op == "3":
                a.transferir(b, leer_float("Monto: ")); print(a, b)
            elif op == "4":
                b.depositar(leer_float("Monto: ")); print(b)
            elif op == "5":
                b.retirar(leer_float("Monto: ")); print(b)
            elif op == "6":
                b.transferir(a, leer_float("Monto: ")); print(a, b)
            elif op == "7":
                print(a, b)
            elif op == "8":
                break
            else:
                print("Opción no válida.")
        except ValueError as e:
            print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
