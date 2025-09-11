
"""
002-002-primer_script.py
--------------------------------
Primer script de práctica en Python:
Solicita un nombre desde la línea de comandos y saluda al usuario.

Autor: Alejandro Aguirre Díaz
"""
import argparse
# Importamos argparse para mostrar cómo se puede usar en scripts, aunque en este ejemplo no se utiliza.

def saludar(nombre: str) -> None:
    """Imprime un saludo personalizado."""
    # Utiliza una f-string para mostrar el saludo con el nombre proporcionado
    print(f"Hola, {nombre} 👋 Bienvenido a Python!")

def main() -> None:
    # Inicializa la variable nombre como cadena vacía
    nombre = ""
    # Bucle que solicita el nombre hasta que el usuario ingrese un valor no vacío
    while not nombre:
        # Solicita el nombre al usuario y elimina espacios al inicio y final
        nombre = input("¿Cuál es tu nombre? ").strip()
    # Llama a la función saludar con el nombre ingresado
    saludar(nombre)

if __name__ == "__main__":
    # Ejecuta la función principal solo si el script se ejecuta directamente
    main()
