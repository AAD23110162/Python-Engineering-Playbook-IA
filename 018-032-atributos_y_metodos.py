
"""
018-032-atributos_y_metodos.py
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
        # Constructor: inicializa el titular y el saldo
        if saldo_inicial < 0:
            raise ValueError("Saldo inicial no puede ser negativo.")
        self.titular = titular
        self._saldo = float(saldo_inicial)

    @property
    def saldo(self) -> float:
        # Propiedad de solo lectura para consultar el saldo actual
        return self._saldo

    def depositar(self, monto: float) -> None:
        # Suma el monto al saldo si es válido
        if monto <= 0:
            raise ValueError("El depósito debe ser > 0.")
        self._saldo += monto

    def retirar(self, monto: float) -> None:
        # Resta el monto al saldo si es válido y hay fondos suficientes
        if monto <= 0:
            raise ValueError("El retiro debe ser > 0.")
        if monto > self._saldo:
            raise ValueError("Fondos insuficientes.")
        self._saldo -= monto

    def transferir(self, otra: "CuentaBancaria", monto: float) -> None:
        # Transfiere el monto a otra cuenta usando retirar y depositar
        self.retirar(monto)
        otra.depositar(monto)

    def __repr__(self) -> str:
        # Representación legible de la cuenta bancaria
        return f"CuentaBancaria(titular={self.titular!r}, saldo={self._saldo:.2f})"

def leer_float(msg: str) -> float:
    # Solicita un número flotante al usuario y valida la entrada
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    # Modo demostración: muestra operaciones típicas entre dos cuentas
    a = CuentaBancaria("Ana", 100)
    b = CuentaBancaria("Ben", 50)
    print(a, b)
    a.depositar(25); print("Ana deposita 25 →", a)
    a.transferir(b, 60); print("Ana transfiere 60 a Ben →", a, b)
    # Prueba un retiro inválido (fondos insuficientes)
    try:
        b.retirar(1000)
    except ValueError as e:
        print("Retiro inválido:", e)

def interactivo() -> None:
    # Modo interactivo: permite al usuario operar dos cuentas bancarias
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
                # Deposita en la cuenta A
                a.depositar(leer_float("Monto: ")); print(a)
            elif op == "2":
                # Retira de la cuenta A
                a.retirar(leer_float("Monto: ")); print(a)
            elif op == "3":
                # Transfiere de A a B
                a.transferir(b, leer_float("Monto: ")); print(a, b)
            elif op == "4":
                # Deposita en la cuenta B
                b.depositar(leer_float("Monto: ")); print(b)
            elif op == "5":
                # Retira de la cuenta B
                b.retirar(leer_float("Monto: ")); print(b)
            elif op == "6":
                # Transfiere de B a A
                b.transferir(a, leer_float("Monto: ")); print(a, b)
            elif op == "7":
                # Muestra el estado actual de ambas cuentas
                print(a, b)
            elif op == "8":
                # Sale del menú interactivo
                break
            else:
                # Opción no reconocida
                print("Opción no válida.")
        except ValueError as e:
            # Muestra el error si ocurre una excepción en la operación
            print("Error:", e)

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    # Si el modo empieza con 'i', activa el modo interactivo; si no, ejecuta demo
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
