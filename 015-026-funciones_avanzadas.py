
"""
015-026-funciones_avanzadas.py
------------------------------
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
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = (time.perf_counter() - t0) * 1000
            print(f"[timeit] {fn.__name__} tomó {dt:.2f} ms")
    return wrapper

def retry(n: int = 3, delay: float = 0.1) -> Callable:
    def deco(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last: Optional[Exception] = None
            for _ in range(n):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    time.sleep(delay)
            raise last  # type: ignore[misc]
        return wrapper
    return deco

@timeit
@retry(n=5, delay=0.05)
def tarea_inestable(p_fallo: float = 0.5) -> int:
    """Falla con probabilidad p_fallo y retorna 42 si logra pasar."""
    if random.random() < p_fallo:
        raise RuntimeError("Fallo aleatorio")
    # Trabajo simulado
    time.sleep(0.02)
    return 42

def fibonacci(n: int) -> Iterator[int]:
    """Generador de los primeros n números de Fibonacci."""
    if n < 0:
        raise ValueError("n debe ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def leer_entero(msg: str, minimo: int | None = None) -> int:
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
    print("▶ DEMO tarea_inestable (p_fallo=0.5)")
    try:
        print("Resultado:", tarea_inestable(0.5))
    except Exception as e:
        print("Falló tras reintentos:", e)

    print("\n▶ DEMO fibonacci(10)")
    print(list(fibonacci(10)))

def interactivo() -> None:
    print("1) Ejecutar tarea_inestable")
    print("2) Generar fibonacci(n)")
    op = input("Elige opción: ").strip()
    if op == "1":
        p = leer_float("Probabilidad de fallo (0–1): ", 0.0)
        if p > 1.0:
            print("⚠️ Debe ser ≤ 1.0. Se usará 0.5")
            p = 0.5
        try:
            print("Resultado:", tarea_inestable(p))
        except Exception as e:
            print("Falló tras reintentos:", e)
    elif op == "2":
        n = leer_entero("n (≥ 0): ", 0)
        try:
            print(list(fibonacci(n)))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida.")

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    if modo.startswith("i"):
        interactivo()
    else:
        demo()

if __name__ == "__main__":
    main()
