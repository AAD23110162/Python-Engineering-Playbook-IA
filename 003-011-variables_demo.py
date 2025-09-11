
"""
003-011-variables_demo.py
--------------------------------
Demostración de variables en Python.
Declara distintos tipos de variables y muestra su valor y tipo.

Autor: Alejandro Aguirre Díaz
"""

def main() -> None:
    # Declaración de variables de diferentes tipos primitivos y compuestos
    entero: int = 42  # Variable entera
    decimal: float = 3.1416  # Variable de punto flotante
    texto: str = "Python"  # Variable de texto (string)
    booleano: bool = True  # Variable booleana
    lista: list[int] = [1, 2, 3]  # Lista de enteros
    tupla: tuple[str, int] = ("edad", 25)  # Tupla con un string y un entero
    diccionario: dict[str, str] = {"nombre": "Alejandro", "curso": "Python"}  
    # Diccionario con claves y valores string

    # Agrupa todas las variables en una lista para mostrarlas
    variables = [entero, decimal, texto, booleano, lista, tupla, diccionario]
    # Itera sobre cada variable y muestra su valor y tipo usando la función type()
    for var in variables:
        print(f"Valor: {var} -> Tipo: {type(var)}")


if __name__ == "__main__":
    main()
