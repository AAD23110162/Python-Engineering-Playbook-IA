
"""
001-001-diagnostico_entorno.py
--------------------------------
Este script imprime información básica del entorno de Python:
- Versión actual de Python
- Ruta del intérprete
- Disponibilidad de `pip`

Autor: Alejandro Aguirre Díaz
"""

import sys
import shutil


def diagnostico() -> None:
    """Muestra información básica del entorno de Python."""
    print("🔎 Diagnóstico del entorno Python")
    print("-" * 40)
    print(f"Versión de Python : {sys.version}")
    print(f"Ruta del intérprete: {sys.executable}")

    pip_path = shutil.which("pip")
    if pip_path:
        print(f"pip disponible en   : {pip_path}")
    else:
        print("⚠️ pip no está disponible en este entorno.")


if __name__ == "__main__":
    diagnostico()
