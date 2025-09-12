
"""
014-024-fechas_y_math.py
------------------------
Modo DEMO:
  - Calcula días entre 2024-01-01 y 2025-09-07
  - Muestra operaciones de math: sqrt, sin, cos, factorial
Modo INTERACTIVO:
  - Pide dos fechas (YYYY-MM-DD) y calcula días entre ellas
  - Pide un número y aplica operaciones de math

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
from datetime import date
import math

def leer_fecha(prompt: str) -> date:
    # Solicita una fecha al usuario en formato YYYY-MM-DD y valida la entrada
    while True:
        s = input(prompt).strip()
        try:
            y, m, d = (int(x) for x in s.split("-"))
            return date(y, m, d)
        except Exception:
            print("⚠️ Formato inválido. Usa YYYY-MM-DD, ej. 2025-09-07")

def leer_float(prompt: str) -> float:
    # Solicita un número flotante al usuario y valida la entrada
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número válido (float)")

def leer_entero_no_neg(prompt: str) -> int:
    # Solicita un entero no negativo al usuario y valida la entrada
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if v < 0:
                print("⚠️ Debe ser ≥ 0")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un entero válido")

def dias_entre(a: date, b: date) -> int:
    # Calcula el número absoluto de días entre dos fechas
    return abs((b - a).days)

def demo() -> None:
    # Modo demostración: calcula días entre dos fechas fijas y muestra operaciones matemáticas
    a = date(2024, 1, 1)
    b = date(2025, 9, 7)
    print(f"🗓️ Días entre {a} y {b}: {dias_entre(a, b)}")

    x = 9.0
    n = 6
    print("\n🔢 Operaciones math (x=9.0, n=6)")
    print("sqrt(x)  =", math.sqrt(x))  # Raíz cuadrada
    print("sin(x)   =", math.sin(x))   # Seno
    print("cos(x)   =", math.cos(x))   # Coseno
    print("factorial(n) =", math.factorial(n))  # Factorial

def interactivo() -> None:
    # Modo interactivo: solicita fechas y números al usuario y muestra resultados
    print("=== Fechas ===")
    a = leer_fecha("Fecha A (YYYY-MM-DD): ")
    b = leer_fecha("Fecha B (YYYY-MM-DD): ")
    print(f"Días entre {a} y {b}: {dias_entre(a, b)}")

    print("\n=== Operaciones matemáticas ===")
    x = leer_float("x para sqrt/sin/cos: ")
    n = leer_entero_no_neg("n para factorial (entero ≥ 0): ")
    try:
        print("sqrt(x)  =", math.sqrt(x))
    except ValueError as e:
        print("sqrt(x)  -> Error:", e)
    print("sin(x)   =", math.sin(x))
    print("cos(x)   =", math.cos(x))
    try:
        print("factorial(n) =", math.factorial(n))
    except ValueError as e:
        print("factorial(n) -> Error:", e)

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    # Basta con poner 'i' para modo interactivo o 'd' para demo (no es necesario escribir la palabra completa)
    # Esto funciona porque usamos 'modo.startswith("i")', así que cualquier texto que empiece con 'i' activa el modo interactivo
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    if modo.startswith("i"):
        interactivo()
    else:
        demo()

if __name__ == "__main__":
    main()
