
"""
013-020-modulos_y_paquetes.py
-----------------------------
Ejemplo práctico de módulos y paquetes *sin crear subcarpetas permanentes*:
- Crea un paquete temporal en disco: `tmp_pkg_demo/`
- Escribe `__init__.py` y `utilidades.py`
- Lo importa dinámicamente y lo usa
- (Opcional) elimina los archivos al final

Autor: Alejandro Aguirre Díaz
"""

from __future__ import annotations
import sys
import tempfile
import textwrap
import importlib
import importlib.util
import os
from pathlib import Path


def crear_paquete_temporal(base: Path) -> Path:
    pkg_dir = base / "tmp_pkg_demo"
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # __init__.py – expone una versión
    (pkg_dir / "__init__.py").write_text(
        '"""Paquete temporal de demostración."""\n__all__ = ["utilidades", "VERSION"]\nVERSION = "0.1.0"\n',
        encoding="utf-8",
    )

    # utilidades.py – funciones de ejemplo
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


def demo_imports(pkg_dir: Path) -> None:
    # Añadimos el directorio padre del paquete a sys.path para importarlo de forma normal
    sys.path.insert(0, str(pkg_dir.parent))

    try:
        # Importar el paquete y el submódulo
        pkg = importlib.import_module("tmp_pkg_demo")
        util = importlib.import_module("tmp_pkg_demo.utilidades")

        print(f"Paquete tmp_pkg_demo VERSION={getattr(pkg, 'VERSION', 'desconocida')}")
        print("es_par(10) =", util.es_par(10))
        print("fibonacci(10) =", util.fibonacci(10))

    finally:
        # Limpiar sys.path (buena práctica)
        if sys.path and sys.path[0] == str(pkg_dir.parent):
            sys.path.pop(0)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        pkg_dir = crear_paquete_temporal(base)
        demo_imports(pkg_dir)

        # (Opcional) mostrar dónde se creó el paquete temporal
        print("\nPaquete temporal en:", pkg_dir)


if __name__ == "__main__":
    main()
