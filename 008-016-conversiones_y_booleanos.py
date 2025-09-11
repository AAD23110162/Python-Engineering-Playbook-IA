
"""
008-016-conversiones_y_booleanos.py
-----------------------------------
Convierte cadenas a int/float/bool de forma segura y demuestra
operadores lógicos (and/or/not) y "truthiness" en Python.

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations


def to_int(s: str) -> int | None:
    # Intenta convertir la cadena a entero
    try:
        return int(s)
    except ValueError:
        # Si falla la conversión, retorna None
        return None


def to_float(s: str) -> float | None:
    # Intenta convertir la cadena a flotante
    try:
        return float(s)
    except ValueError:
        # Si falla la conversión, retorna None
        return None


def to_bool(s: str) -> bool | None:
    # Diccionario de equivalencias para valores booleanos comunes
    mapa = {"true": True, "false": False, "1": True, "0": False, "sí": True, "si": True, "no": False}
    # Normaliza la cadena (sin espacios y en minúsculas)
    v = s.strip().lower()
    # Retorna el valor booleano correspondiente o None si no es válido
    return mapa.get(v, None)


def truthiness_demo(values: list[object]) -> None:
    # Muestra cómo Python evalúa la "veracidad" (truthiness) de distintos valores
    for v in values:
        print(f"{repr(v):>12} -> bool(): {bool(v)}")


def main() -> None:
    # Solicita al usuario tres cadenas para convertir
    s_int = input("Cadena para convertir a int: ")
    s_float = input("Cadena para convertir a float: ")
    s_bool = input("Cadena para convertir a bool (true/false/1/0/sí/no): ")

    # Muestra los resultados de las conversiones
    print("\nConversiones")
    print("-" * 30)
    print("int   :", to_int(s_int))
    print("float :", to_float(s_float))
    print("bool  :", to_bool(s_bool))

    # Demostración de operadores lógicos con los valores convertidos
    a = bool(to_bool(s_bool))  # Si es None, bool(None) es False
    b = to_int(s_int) is not None  # True si la conversión fue exitosa
    c = to_float(s_float) is not None  # True si la conversión fue exitosa

    print("\nOperadores lógicos")
    print("-" * 30)
    print(f"a and b -> {a and b}")  # AND lógico
    print(f"a or  c -> {a or c}")   # OR lógico
    print(f"not a   -> {not a}")    # Negación lógica

    # Demostración de "truthiness" en Python con valores comunes
    print("\nTruthiness común")
    print("-" * 30)
    truthiness_demo([0, 1, "", "hola", [], [1], {}, {"k": 1}, None])


if __name__ == "__main__":
    main()
