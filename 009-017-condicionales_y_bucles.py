
"""
009-017-condicionales_y_bucles.py
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
    # Solicita al usuario un valor y elimina espacios
    s = input(msg).strip()
    # Verifica si la entrada es un número entero positivo
    if not s.isdigit():
        return None  # Retorna None si la entrada no es válida
    return int(s)  # Convierte la entrada a entero y la retorna


def main() -> None:
    # Genera un número aleatorio entre 1 y 100 como objetivo
    objetivo = random.randint(1, 100)
    # Define el número máximo de intentos permitidos
    intentos = 7
    print("🎯 Adivina el número (1-100). Tienes 7 intentos.")

    # Bucle principal del juego: hasta 7 intentos
    for intento in range(1, intentos + 1):
        # Solicita al usuario un número entero
        n = pedir_entero(f"Intento {intento}/{intentos}: ")
        if n is None:
            # Si la entrada no es válida, muestra advertencia y repite el intento
            print("⚠️ Ingresa un entero válido.")
            continue

        # Compara el número ingresado con el objetivo
        if n == objetivo:
            print(f"✅ ¡Correcto! El número era {objetivo}.")
            break  # Termina el juego si adivinó
        elif n < objetivo:
            print("🔼 Más alto.")  # Indica que el número es mayor
        else:
            print("🔽 Más bajo.")  # Indica que el número es menor
    else:
        # Si se acaban los intentos sin adivinar, muestra el número correcto
        print(f"❌ Se acabaron los intentos. El número era {objetivo}.")


if __name__ == "__main__":
    main()
