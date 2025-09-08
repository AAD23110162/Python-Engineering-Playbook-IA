
"""
008-010-conversiones_y_booleanos.py
-----------------------------------
Convierte cadenas a int/float/bool de forma segura y demuestra
operadores lógicos (and/or/not) y "truthiness" en Python.

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations


def to_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


def to_float(s: str) -> float | None:
    try:
        return float(s)
    except ValueError:
        return None


def to_bool(s: str) -> bool | None:
    mapa = {"true": True, "false": False, "1": True, "0": False, "sí": True, "si": True, "no": False}
    v = s.strip().lower()
    return mapa.get(v, None)


def truthiness_demo(values: list[object]) -> None:
    for v in values:
        print(f"{repr(v):>12} -> bool(): {bool(v)}")


def main() -> None:
    s_int = input("Cadena para convertir a int: ")
    s_float = input("Cadena para convertir a float: ")
    s_bool = input("Cadena para convertir a bool (true/false/1/0/sí/no): ")

    print("\nConversiones")
    print("-" * 30)
    print("int   :", to_int(s_int))
    print("float :", to_float(s_float))
    print("bool  :", to_bool(s_bool))

    # Operadores lógicos
    a = bool(to_bool(s_bool))  # si es None -> False
    b = to_int(s_int) is not None
    c = to_float(s_float) is not None

    print("\nOperadores lógicos")
    print("-" * 30)
    print(f"a and b -> {a and b}")
    print(f"a or  c -> {a or c}")
    print(f"not a   -> {not a}")

    print("\nTruthiness común")
    print("-" * 30)
    truthiness_demo([0, 1, "", "hola", [], [1], {}, {"k": 1}, None])


if __name__ == "__main__":
    main()
