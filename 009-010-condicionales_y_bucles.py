
"""
009-010-condicionales_y_bucles.py
----------------------------------
Juego "Adivina el número":
- El programa elige un número entre 1 y 100.
- Tienes 7 intentos.
- Indica "más alto" o "más bajo" según el caso.
- Valida entradas y controla errores.

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations
import random


def pedir_entero(msg: str) -> int | None:
    s = input(msg).strip()
    if not s.isdigit():
        return None
    return int(s)


def main() -> None:
    objetivo = random.randint(1, 100)
    intentos = 7
    print("🎯 Adivina el número (1-100). Tienes 7 intentos.")

    for intento in range(1, intentos + 1):
        n = pedir_entero(f"Intento {intento}/{intentos}: ")
        if n is None:
            print("⚠️ Ingresa un entero válido.")
            continue

        if n == objetivo:
            print(f"✅ ¡Correcto! El número era {objetivo}.")
            break
        elif n < objetivo:
            print("🔼 Más alto.")
        else:
            print("🔽 Más bajo.")
    else:
        print(f"❌ Se acabaron los intentos. El número era {objetivo}.")


if __name__ == "__main__":
    main()
