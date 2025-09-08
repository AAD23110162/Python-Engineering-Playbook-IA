
"""
016-027-programacion_defensiva.py
---------------------------------
Buenas prácticas de programación defensiva:
  - Validación de entradas
  - Excepciones personalizadas
  - Logging de errores

Incluye dos utilidades:
  1) dividir(a, b)  -> CeroDivisionError y validaciones
  2) validar_email(s) -> EmailInvalidoError si no cumple formato básico

Modos:
  DEMO: ejecuta casos de prueba
  INTERACTIVO: menú para usar dividir() o validar_email()

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
import logging
import re
from typing import Optional

# Configuración simple de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)
log = logging.getLogger("defensiva")

class EmailInvalidoError(ValueError):
    """Se lanza cuando un email no cumple un formato mínimo."""

def dividir(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a y b deben ser numéricos")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

def validar_email(s: str) -> str:
    if not isinstance(s, str):
        raise TypeError("El email debe ser una cadena")
    s = s.strip()
    if not s:
        raise EmailInvalidoError("El email está vacío")
    if not EMAIL_RE.match(s):
        raise EmailInvalidoError("Formato de email inválido")
    return s

def leer_float(msg: str) -> float:
    while True:
        s = input(msg).strip()
        try:
            return float(s)
        except ValueError:
            print("⚠️ Ingresa un número (float) válido.")

def demo() -> None:
    print("▶ DEMO dividir")
    casos = [(10, 2), (5, 0), ("a", 3)]
    for a, b in casos:
        try:
            print(f"dividir({a},{b}) =", dividir(a, b))  # type: ignore[arg-type]
        except Exception as e:
            log.error("Error en dividir(%r,%r): %s", a, b, e)

    print("\n▶ DEMO validar_email")
    emails = ["user@example.com", "mal@", "", 123]
    for s in emails:
        try:
            print(f"validar_email({s!r}) =", validar_email(s))  # type: ignore[arg-type]
        except Exception as e:
            log.warning("Email inválido (%r): %s", s, e)

def interactivo() -> None:
    print("1) Dividir a/b")
    print("2) Validar email")
    op = input("Elige opción: ").strip()
    if op == "1":
        a = leer_float("a: ")
        b = leer_float("b: ")
        try:
            print("Resultado:", dividir(a, b))
        except Exception as e:
            log.error("Error en dividir: %s", e)
            print("Error:", e)
    elif op == "2":
        s = input("Email: ").strip()
        try:
            print("OK:", validar_email(s))
        except Exception as e:
            log.warning("Email inválido: %s", e)
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
