
"""
023-030-encapsulamiento.py
--------------------------
Clase Usuario con atributos "privados":
- _password_hash (solo lectura pública)
- email con validación @property

Métodos:
- set_password(plain) -> guarda hash SHA-256
- check_password(plain) -> bool

Modos:
  DEMO: crea usuario, setea password y valida.
  INTERACTIVO: captura datos por teclado.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations
import hashlib
import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Usuario:
    def __init__(self, nombre: str, email: str) -> None:
        self.nombre = nombre.strip() or "Usuario"
        self._email = ""
        self.email = email  # usa setter para validar
        self._password_hash = ""  # encapsulado

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        v = value.strip()
        if not EMAIL_RE.match(v):
            raise ValueError("Email inválido.")
        self._email = v

    @property
    def password_hash(self) -> str:
        """Exposición de solo lectura (no hay setter)."""
        return self._password_hash

    def set_password(self, plain: str) -> None:
        if not plain:
            raise ValueError("La contraseña no puede ser vacía.")
        # Hash simple (ejemplo didáctico); en producción usa salt+KDF.
        self._password_hash = hashlib.sha256(plain.encode("utf-8")).hexdigest()

    def check_password(self, plain: str) -> bool:
        return hashlib.sha256(plain.encode("utf-8")).hexdigest() == self._password_hash

    def __repr__(self) -> str:
        oculto = self._password_hash[:8] + "..." if self._password_hash else "(no-set)"
        return f"Usuario(nombre={self.nombre!r}, email={self.email!r}, password_hash={oculto})"

def demo() -> None:
    u = Usuario("Alejandro", "alejandro@example.com")
    print(u)
    u.set_password("secreto123")
    print("Password seteado. Hash:", u.password_hash[:12], "...")
    print("check_password('secreto123'):", u.check_password("secreto123"))
    print("check_password('otro')      :", u.check_password("otro"))

def interactivo() -> None:
    try:
        u = Usuario(input("Nombre: ").strip() or "Usuario", input("Email: ").strip())
    except ValueError as e:
        print("Error creando usuario:", e)
        return

    while True:
        print("\n1) Setear contraseña  2) Ver hash  3) Verificar contraseña  4) Cambiar email  5) Ver usuario  6) Salir")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                u.set_password(input("Nueva contraseña: "))
                print("OK")
            elif op == "2":
                print("Hash:", u.password_hash or "(sin configurar)")
            elif op == "3":
                print("¿Coincide?:", u.check_password(input("Contraseña a verificar: ")))
            elif op == "4":
                u.email = input("Nuevo email: ").strip()
                print("Email actualizado:", u.email)
            elif op == "5":
                print(u)
            elif op == "6":
                break
            else:
                print("Opción no válida.")
        except ValueError as e:
            print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
