
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
    # Elimina espacios en blanco de cada elemento y descarta los vacíos
    return [x.strip() for x in items if x.strip()]


def main() -> None:
    # Solicita al usuario una cadena de elementos separados por comas
    entrada = input("Ingresa elementos separados por comas: ").strip()
    # Convierte la entrada en una lista normalizada (sin espacios y sin elementos vacíos)
    lista = normaliza(entrada.split(",")) if entrada else []
    # Convierte la lista a tupla (inmutable)
    tupla = tuple(lista)
    # Convierte la lista a conjunto para obtener elementos únicos
    conjunto = set(lista)
    # Calcula un diccionario de frecuencias usando Counter
    frec: dict[str, int] = dict(Counter(lista))

    # Muestra los resultados de las conversiones y el análisis
    print("\nResultados")
    print("-" * 30)
    print(f"Lista     : {lista}")
    print(f"Tupla     : {tupla}")
    print(f"Set       : {conjunto}")
    print(f"Frecuencias: {frec}")


if __name__ == "__main__":
    main()
