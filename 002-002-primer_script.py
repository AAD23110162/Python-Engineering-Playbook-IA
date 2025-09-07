
"""
002-002-primer_script.py
--------------------------------
Primer script de práctica en Python:
Solicita un nombre desde la línea de comandos y saluda al usuario.

Ejemplo:
    $ python 002-002-primer_script.py --nombre "Alejandro"
    Hola, Alejandro 👋 Bienvenido a Python!

Autor: Alejandro Aguirre Díaz
"""

import argparse


def saludar(nombre: str) -> None:
    """Imprime un saludo personalizado."""
    print(f"Hola, {nombre} 👋 Bienvenido a Python!")


def main() -> None:
    nombre = ""
    while not nombre:
        nombre = input("¿Cuál es tu nombre? ").strip()
    saludar(nombre)


if __name__ == "__main__":
    main()
