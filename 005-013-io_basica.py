
"""
005-013-io_basica.py
--------------------------------
Entrada/salida básica con validación.
Pide nombre y edad al usuario e imprime un saludo.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    # Solicita el nombre al usuario y elimina espacios al inicio y final
    nombre: str = input("¿Cómo te llamas? ").strip()
    # Solicita la edad como texto y elimina espacios
    edad_str: str = input("¿Cuántos años tienes? ").strip()

    # Verifica que la edad ingresada sea un número entero
    if not edad_str.isdigit():
        print("⚠️ La edad debe ser un número entero.")
        return  # Termina la función si la edad no es válida

    # Convierte la edad de texto a entero
    edad: int = int(edad_str)
    # Imprime el saludo con el nombre y la edad
    print(f"Hola {nombre}, tienes {edad} años.")


if __name__ == "__main__":
    main()
