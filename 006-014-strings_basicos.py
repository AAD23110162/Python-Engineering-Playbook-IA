
"""
006-014-strings_basicos.py
--------------------------------
Análisis de cadenas:
- Número de caracteres
- Número de mayúsculas
- Número de minúsculas
- Palabra más larga

Autor: Alejandro Aguirre Díaz
"""

def analizar_texto(texto: str) -> None:
    """Analiza un texto y muestra métricas básicas."""
    num_caracteres = len(texto)
    num_mayusculas = sum(1 for c in texto if c.isupper())
    num_minusculas = sum(1 for c in texto if c.islower())
    palabras = texto.split()
    palabra_larga = max(palabras, key=len) if palabras else ""

    print(f"Texto analizado: {texto}")
    print(f"Caracteres totales : {num_caracteres}")
    print(f"Mayúsculas         : {num_mayusculas}")
    print(f"Minúsculas         : {num_minusculas}")
    print(f"Palabra más larga  : '{palabra_larga}'")


def main() -> None:
    texto_usuario: str = input("Escribe un texto: ").strip()
    analizar_texto(texto_usuario)


if __name__ == "__main__":
    main()
