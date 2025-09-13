
"""
015-026-funciones_avanzadas.py
------------------------------
Un decorador en Python es una función que recibe otra función y devuelve 
una nueva función que extiende o modifica su comportamiento.
Los decoradores se aplican usando el símbolo @ antes de la definición de 
la función objetivo.

Incluye:
  - Decorador @timeit (mide tiempo)
  - Decorador @retry(n) (reintentos)
  - Generador fibonacci(n)

Modo DEMO:
  - Ejecuta tarea_inestable con @retry y @timeit
  - Genera 10 números de Fibonacci

Modo INTERACTIVO:
  - Menú para ejecutar tarea_inestable (con prob. fallo) o fibonacci(n)

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
import time
import functools
import random
from typing import Callable, Iterator, Optional

def timeit(fn: Callable) -> Callable:
    # Decorador que mide el tiempo de ejecución de una función y lo imprime
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()  # Marca el tiempo inicial
        try:
            return fn(*args, **kwargs)  # Ejecuta la función decorada
        finally:
            dt = (time.perf_counter() - t0) * 1000  # Calcula el tiempo transcurrido en ms
            print(f"[timeit] {fn.__name__} tomó {dt:.2f} ms")
    return wrapper

def retry(n: int = 3, delay: float = 0.1) -> Callable:
    # Decorador parametrizable que reintenta la ejecución de una función n veces si falla
    def deco(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last: Optional[Exception] = None
            for _ in range(n):
                try:
                    return fn(*args, **kwargs)  # Intenta ejecutar la función
                except Exception as e:
                    last = e  # Guarda la última excepción
                    time.sleep(delay)  # Espera antes de reintentar
            raise last  # Si falla todas las veces, lanza la última excepción
        return wrapper
    return deco

@timeit
@retry(n=5, delay=0.05)
def tarea_inestable(p_fallo: float = 0.5) -> int:
    """Falla con probabilidad p_fallo y retorna 42 si logra pasar."""
    # Genera un número aleatorio y falla si está por debajo de p_fallo
    if random.random() < p_fallo:
        raise RuntimeError("Fallo aleatorio")
    # Simula trabajo con una pequeña espera
    time.sleep(0.02)
    return 42  # Retorna 42 si no falla

def fibonacci(n: int) -> Iterator[int]:
    """Generador de los primeros n números de Fibonacci."""
    # Valida que n sea no negativo
    if n < 0:
        raise ValueError("n debe ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        yield a  # Devuelve el siguiente número de la secuencia
        a, b = b, a + b  # Actualiza los valores para el siguiente ciclo

def leer_entero(msg: str, minimo: int | None = None) -> int:
    # Solicita un entero al usuario y valida el mínimo si se indica
    while True:
        s = input(msg).strip()
        try:
            v = int(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un entero válido")

def leer_float(msg: str, minimo: float | None = None) -> float:
    # Solicita un número flotante al usuario y valida el mínimo si se indica
    while True:
        s = input(msg).strip()
        try:
            v = float(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un número válido (float)")

def demo() -> None:
    # Modo demostración: ejecuta tarea_inestable y muestra la secuencia de Fibonacci
    print("▶ DEMO tarea_inestable (p_fallo=0.5)")
    try:
        print("Resultado:", tarea_inestable(0.5))
    except Exception as e:
        print("Falló tras reintentos:", e)

    print("\n▶ DEMO fibonacci(10)")
    print(list(fibonacci(10)))

def interactivo() -> None:
    # Modo interactivo: menú para ejecutar tarea_inestable o generar Fibonacci
    print("1) Ejecutar tarea_inestable")
    print("2) Generar fibonacci(n)")
    op = input("Elige opción: ").strip()
    if op == "1":
        # Solicita la probabilidad de fallo y ejecuta la tarea
        p = leer_float("Probabilidad de fallo (0–1): ", 0.0)
        if p > 1.0:
            print("⚠️ Debe ser ≤ 1.0. Se usará 0.5")
            p = 0.5
        try:
            print("Resultado:", tarea_inestable(p))
        except Exception as e:
            print("Falló tras reintentos:", e)
    elif op == "2":
        # Solicita n y genera la secuencia de Fibonacci
        n = leer_entero("n (≥ 0): ", 0)
        try:
            print(list(fibonacci(n)))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida.")

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    # Basta con poner 'i' para modo interactivo o 'd' para demo (no es necesario escribir la palabra completa)
    # Esto funciona porque usamos 'modo.startswith("i")', así que cualquier texto que empiece con 'i' activa el modo interactivo
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    if modo.startswith("i"):
        interactivo()
    else:
        demo()

if __name__ == "__main__":
    main()
