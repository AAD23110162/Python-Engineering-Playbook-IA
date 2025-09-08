
"""
013-023-modulos_y_paquetes.py
-----------------------------
Crea un paquete temporal (tmp_pkg_demo) y lo importa dinámicamente.

Modo DEMO:
  - Importa y usa utilidades: es_par(10), fibonacci(10)

Modo INTERACTIVO:
  - Te pide un número para es_par()
  - Te pide n para fibonacci(n)

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
import sys
import tempfile
import textwrap
import importlib
from pathlib import Path

PKG_NAME = "tmp_pkg_demo"

def crear_paquete_temporal(base: Path) -> Path:
    pkg_dir = base / PKG_NAME
    pkg_dir.mkdir(parents=True, exist_ok=True)
    (pkg_dir / "__init__.py").write_text(
        '"""Paquete temporal de demostración."""\n__all__ = ["utilidades", "VERSION"]\nVERSION = "0.1.0"\n',
        encoding="utf-8",
    )
    (pkg_dir / "utilidades.py").write_text(
        textwrap.dedent(
            """
            from __future__ import annotations

            def es_par(n: int) -> bool:
                return n % 2 == 0

            def fibonacci(n: int) -> list[int]:
                if n < 0:
                    raise ValueError("n debe ser >= 0")
                a, b = 0, 1
                out: list[int] = []
                for _ in range(n):
                    out.append(a)
                    a, b = b, a + b
                return out
            """
        ),
        encoding="utf-8",
    )
    return pkg_dir

def cargar_utilidades(pkg_parent: Path):
    sys.path.insert(0, str(pkg_parent))
    try:
        pkg = importlib.import_module(PKG_NAME)
        util = importlib.import_module(f"{PKG_NAME}.utilidades")
        return pkg, util
    finally:
        # Mantén el path temporal durante la ejecución; se limpia al salir del with
        pass

def leer_int(msg: str, minimo: int | None = None) -> int:
    while True:
        s = input(msg).strip()
        try:
            v = int(s)
            if minimo is not None and v < minimo:
                print(f"⚠️ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("⚠️ Ingresa un entero válido.")

def run_demo(pkg, util) -> None:
    print(f"Paquete {PKG_NAME} VERSION={getattr(pkg, 'VERSION', 'desconocida')}")
    print("es_par(10)      =", util.es_par(10))
    print("fibonacci(10)   =", util.fibonacci(10))

def run_interactivo(util) -> None:
    n_par = leer_int("Número para es_par(n): ")
    print("Resultado es_par:", util.es_par(n_par))
    n_fib = leer_int("n para fibonacci(n): ", minimo=0)
    try:
        print("Resultado fibonacci:", util.fibonacci(n_fib))
    except ValueError as e:
        print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        pkg_dir = crear_paquete_temporal(base)
        pkg, util = cargar_utilidades(pkg_dir.parent)

        if modo.startswith("i"):
            run_interactivo(util)
        else:
            run_demo(pkg, util)

        print("\nPaquete temporal creado en:", pkg_dir)

if __name__ == "__main__":
    main()
