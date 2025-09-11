
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

# Importamos el módulo sys para obtener información del sistema y el intérprete de Python
# Importamos shutil para buscar la ruta de 'pip' en el sistema

def diagnostico() -> None:
    """Muestra información básica del entorno de Python."""
    # Imprime el encabezado del diagnóstico
    print("🔎 Diagnóstico del entorno Python")
    print("-" * 40)
    # Muestra la versión de Python en uso
    print(f"Versión de Python : {sys.version}")
    # Muestra la ruta absoluta del intérprete de Python
    print(f"Ruta del intérprete: {sys.executable}")

    # Busca la ruta del ejecutable 'pip' en el sistema
    pip_path = shutil.which("pip")
    if pip_path:
        # Si se encuentra 'pip', muestra su ruta
        print(f"pip disponible en   : {pip_path}")
    else:
        # Si no se encuentra 'pip', muestra una advertencia
        print("⚠️ pip no está disponible en este entorno.")


if __name__ == "__main__":
    # Ejecuta la función de diagnóstico solo si el script se ejecuta directamente
    diagnostico()