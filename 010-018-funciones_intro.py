
"""
010-018-funciones_intro.py
--------------------------
Calculadora con dos modos:
1) CLI con flags: --op {suma,resta,mul,div} --a <num> --b <num>
2) Interactivo (si no pasas flags): te pide op, a y b por teclado.

"""

from __future__ import annotations
import argparse
import sys
from typing import Callable, Dict

def suma(a: float, b: float) -> float: return a + b
def resta(a: float, b: float) -> float: return a - b
def mul(a: float, b: float) -> float: return a * b
def div(a: float, b: float) -> float:
    # Verifica que el divisor no sea cero para evitar error
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

OPS: Dict[str, Callable[[float, float], float]] = {
    # Diccionario que asocia el nombre de la operación con la función correspondiente
    "suma": suma,
    "resta": resta,
    "mul": mul,
    "div": div,
}

def parse_args() -> argparse.Namespace:
    # Configura el parser de argumentos para modo CLI
    p = argparse.ArgumentParser(description="Calculadora básica con funciones")
    p.add_argument("--op", choices=OPS.keys(), help="Operación a realizar")
    p.add_argument("--a", type=float, help="Operando A")
    p.add_argument("--b", type=float, help="Operando B")
    return p.parse_args()

def leer_float(prompt: str) -> float:
    # Solicita al usuario un número flotante y valida la entrada
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido.")

def interactivo() -> None:
    # Modo interactivo: solicita operación y operandos por teclado
    print("Modo interactivo. Operaciones disponibles:", ", ".join(OPS.keys()))
    while True:
        op = input("Operación [suma/resta/mul/div]: ").strip().lower()
        if op in OPS:
            break
        print("⚠️ Operación no válida.")
    # Solicita los operandos y realiza la operación
    a = leer_float("Valor de a: ")
    b = leer_float("Valor de b: ")
    try:
        print(OPS[op](a, b))
    except ZeroDivisionError as e:
        print(f"Error: {e}")

def main() -> None:
    # Si no hay argumentos en la línea de comandos, entra en modo interactivo
    if len(sys.argv) == 1:
        interactivo()
        return

    # Modo CLI: procesa los argumentos
    args = parse_args()
    # Verifica que todos los argumentos requeridos estén presentes
    if args.op is None or args.a is None or args.b is None:
        print("Uso: --op {suma,resta,mul,div} --a <num> --b <num>")
        print("O ejecuta sin flags para modo interactivo.")
        sys.exit(2)

    # Realiza la operación seleccionada y maneja división por cero
    try:
        print(OPS[args.op](args.a, args.b))  # type: ignore[arg-type]
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
