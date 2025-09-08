
"""
007-015-listas_tuplas_sets_dicts.py
-----------------------------------
Pide una lista de elementos separados por comas y:
- La muestra como lista (normalizada/strip)
- La convierte a tupla
- Obtiene el conjunto (únicos)
- Calcula un diccionario de frecuencias

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations
from collections import Counter


def normaliza(items: list[str]) -> list[str]:
    return [x.strip() for x in items if x.strip()]


def main() -> None:
    entrada = input("Ingresa elementos separados por comas: ").strip()
    lista = normaliza(entrada.split(",")) if entrada else []
    tupla = tuple(lista)
    conjunto = set(lista)
    frec: dict[str, int] = dict(Counter(lista))

    print("\nResultados")
    print("-" * 30)
    print(f"Lista     : {lista}")
    print(f"Tupla     : {tupla}")
    print(f"Set       : {conjunto}")
    print(f"Frecuencias: {frec}")


if __name__ == "__main__":
    main()
