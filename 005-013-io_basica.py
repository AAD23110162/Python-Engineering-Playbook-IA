
"""
005-010-io_basica.py
--------------------------------
Entrada/salida básica con validación.
Pide nombre y edad al usuario e imprime un saludo.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    nombre: str = input("¿Cómo te llamas? ").strip()
    edad_str: str = input("¿Cuántos años tienes? ").strip()

    if not edad_str.isdigit():
        print("⚠️ La edad debe ser un número entero.")
        return

    edad: int = int(edad_str)
    print(f"Hola {nombre}, tienes {edad} años.")


if __name__ == "__main__":
    main()
