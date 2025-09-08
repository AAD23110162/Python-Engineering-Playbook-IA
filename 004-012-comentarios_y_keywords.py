
"""
004-010-comentarios_y_keywords.py
--------------------------------
Ejemplo de uso de comentarios y palabras reservadas (keywords).
Se muestran 5 keywords con ejemplos sencillos.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    # Comentario de una línea
    """
    Comentario multilínea:
    Este script muestra cómo funcionan algunas palabras reservadas.
    """

    print("Ejemplos de 5 keywords en Python:\n")

    # 1. if / else
    numero: int = 5
    if numero > 0:
        print("if/else -> El número es positivo")
    else:
        print("if/else -> El número es negativo")

    # 2. for
    print("for -> Recorriendo lista:")
    for i in [1, 2, 3]:
        print(i)

    # 3. def
    def cuadrado(x: int) -> int:
        return x * x
    print(f"def -> cuadrado(4) = {cuadrado(4)}")

    # 4. return
    # (Ya se usó en cuadrado)

    # 5. import
    import math
    print(f"import -> math.sqrt(16) = {math.sqrt(16)}")


if __name__ == "__main__":
    main()
