
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
    # Calcula el número total de caracteres en el texto
    num_caracteres = len(texto)
    # Cuenta cuántos caracteres son mayúsculas
    num_mayusculas = sum(1 for c in texto if c.isupper())
    # Cuenta cuántos caracteres son minúsculas
    num_minusculas = sum(1 for c in texto if c.islower())
    # Separa el texto en palabras usando espacios como separador
    palabras = texto.split()
    # Encuentra la palabra más larga usando la función max y la longitud como clave
    palabra_larga = max(palabras, key=len) if palabras else ""

    # Muestra los resultados del análisis
    print(f"Texto analizado: {texto}")
    print(f"Caracteres totales : {num_caracteres}")
    print(f"Mayúsculas         : {num_mayusculas}")
    print(f"Minúsculas         : {num_minusculas}")
    print(f"Palabra más larga  : '{palabra_larga}'")


def main() -> None:
    # Solicita al usuario que escriba un texto y elimina espacios al inicio y final
    texto_usuario: str = input("Escribe un texto: ").strip()
    # Llama a la función para analizar el texto ingresado
    analizar_texto(texto_usuario)


if __name__ == "__main__":
    main()
