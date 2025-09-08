
"""
003-011-variables_demo.py
--------------------------------
Demostración de variables en Python.
Declara distintos tipos de variables y muestra su valor y tipo.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    # Variables de diferentes tipos
    entero: int = 42
    decimal: float = 3.1416
    texto: str = "Python"
    booleano: bool = True
    lista: list[int] = [1, 2, 3]
    tupla: tuple[str, int] = ("edad", 25)
    diccionario: dict[str, str] = {"nombre": "Alejandro", "curso": "Python"}

    # Mostrar valores y tipos
    variables = [entero, decimal, texto, booleano, lista, tupla, diccionario]
    for var in variables:
        print(f"Valor: {var} -> Tipo: {type(var)}")


if __name__ == "__main__":
    main()
