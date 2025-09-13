
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
    # Excepción personalizada para errores de formato de email

def dividir(a: float, b: float) -> float:
    # Realiza la división entre a y b con validaciones de tipo y cero
    # Verifica que ambos argumentos sean numéricos
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a y b deben ser numéricos")
    # Verifica que el divisor no sea cero
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    # Si todo es correcto, realiza la división
    return a / b

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")  # Expresión regular básica para validar emails

def validar_email(s: str) -> str:
    # Valida que el email sea una cadena, no esté vacío y cumpla el formato básico
    # Verifica que el argumento sea tipo str
    if not isinstance(s, str):
        raise TypeError("El email debe ser una cadena")
    # Elimina espacios en blanco al inicio y final
    s = s.strip()
    # Verifica que el email no esté vacío
    if not s:
        raise EmailInvalidoError("El email está vacío")
    # Verifica que el email cumpla el patrón básico
    if not EMAIL_RE.match(s):
        raise EmailInvalidoError("Formato de email inválido")
    # Si todo es correcto, retorna el email validado
    return s

def leer_float(msg: str) -> float:
    # Solicita un número flotante al usuario y valida la entrada
    while True:
        s = input(msg).strip()
        # Intenta convertir la entrada a float
        try:
            return float(s)
        except ValueError:
            # Si falla la conversión, muestra mensaje y repite
            print("⚠️ Ingresa un número (float) válido.")

def demo() -> None:
    # Modo demostración: ejecuta casos de prueba para dividir y validar_email
    print("▶ DEMO dividir")
    casos = [(10, 2), (5, 0), ("a", 3)]  # Incluye casos válidos y errores
    for a, b in casos:
        # Prueba la función dividir con diferentes entradas
        try:
            print(f"dividir({a},{b}) =", dividir(a, b))  # type: ignore[arg-type]
        except Exception as e:
            # Loguea el error si ocurre una excepción
            log.error("Error en dividir(%r,%r): %s", a, b, e)

    print("\n▶ DEMO validar_email")
    emails = ["user@example.com", "mal@", "", 123]  # Incluye emails válidos y errores
    for s in emails:
        # Prueba la función validar_email con diferentes entradas
        try:
            print(f"validar_email({s!r}) =", validar_email(s))  # type: ignore[arg-type]
        except Exception as e:
            # Loguea el error si ocurre una excepción
            log.warning("Email inválido (%r): %s", s, e)

def interactivo() -> None:
    # Modo interactivo: menú para usar dividir() o validar_email()
    print("1) Dividir a/b")
    print("2) Validar email")
    op = input("Elige opción: ").strip()
    # Verifica la opción elegida por el usuario
    if op == "1":
        # Solicita los valores para la división
        a = leer_float("a: ")
        b = leer_float("b: ")
        try:
            print("Resultado:", dividir(a, b))
        except Exception as e:
            # Loguea y muestra el error si ocurre una excepción
            log.error("Error en dividir: %s", e)
            print("Error:", e)
    elif op == "2":
        # Solicita el email para validar
        s = input("Email: ").strip()
        try:
            print("OK:", validar_email(s))
        except Exception as e:
            # Loguea y muestra el error si ocurre una excepción
            log.warning("Email inválido: %s", e)
            print("Error:", e)
    else:
        # Opción no reconocida
        print("Opción no válida.")

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    # Si el modo empieza con 'i', activa el modo interactivo
    if modo.startswith("i"):
        interactivo()
    else:
        # Si no, ejecuta el modo demo
        demo()

if __name__ == "__main__":
    main()
