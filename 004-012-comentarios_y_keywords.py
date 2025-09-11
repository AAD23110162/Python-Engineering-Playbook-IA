
"""
004-012-comentarios_y_keywords.py
--------------------------------
Ejemplo de uso de comentarios y palabras reservadas (keywords).
Se muestran 5 keywords con ejemplos sencillos.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    # Comentario de una línea: sirve para explicar una instrucción o bloque de código
    """
    Comentario multilínea:
    Se puede usar para documentar funciones, clases o explicar bloques grandes de código.
    Este script muestra cómo funcionan algunas palabras reservadas.
    """

    print("Ejemplos de 5 keywords en Python:\n")

    # 1. if / else: permiten tomar decisiones según una condición
    numero: int = 5  # Variable de ejemplo
    if numero > 0:
        print("if/else -> El número es positivo")
    else:
        print("if/else -> El número es negativo")

    # 2. for: permite iterar sobre una secuencia (lista, tupla, etc.)
    print("for -> Recorriendo lista:")
    for i in [1, 2, 3]:  # Itera sobre los elementos de la lista
        print(i)

    # 3. def: se usa para definir funciones
    def cuadrado(x: int) -> int:
        # return: devuelve el resultado de la función
        return x * x
    print(f"def -> cuadrado(4) = {cuadrado(4)}")

    # 4. return: ya se usó en la función cuadrado para devolver un valor

    # 5. import: permite importar módulos externos o estándar de Python
    import math  # Importa el módulo math para usar funciones matemáticas
    print(f"import -> math.sqrt(16) = {math.sqrt(16)}")


if __name__ == "__main__":
    main()
