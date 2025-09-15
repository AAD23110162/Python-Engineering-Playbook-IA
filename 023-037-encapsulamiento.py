
"""
023-037-encapsulamiento.py
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
        # Inicializa el nombre, usando un valor por defecto si está vacío
        self.nombre = nombre.strip() or "Usuario"
        # Inicializa el email privado y lo valida usando el setter
        self._email = ""
        self.email = email  # usa setter para validar
        # Inicializa el hash de la contraseña como atributo privado
        self._password_hash = ""  # encapsulado

    @property
    def email(self) -> str:
        # Permite acceder al email de forma controlada
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        # Valida el formato del email antes de asignarlo
        v = value.strip()
        if not EMAIL_RE.match(v):
            raise ValueError("Email inválido.")
        self._email = v

    @property
    def password_hash(self) -> str:
        """Exposición de solo lectura (no hay setter)."""
        # Permite consultar el hash de la contraseña, pero no modificarlo directamente
        return self._password_hash

    def set_password(self, plain: str) -> None:
        # Permite establecer la contraseña, guardando solo el hash
        if not plain:
            raise ValueError("La contraseña no puede ser vacía.")
        # Hash simple (ejemplo didáctico); en producción usa salt+KDF.
        self._password_hash = hashlib.sha256(plain.encode("utf-8")).hexdigest()

    def check_password(self, plain: str) -> bool:
        # Verifica si el hash de la contraseña ingresada coincide con el almacenado
        return hashlib.sha256(plain.encode("utf-8")).hexdigest() == self._password_hash

    def __repr__(self) -> str:
        # Representación legible del usuario, mostrando solo parte del hash
        oculto = self._password_hash[:8] + "..." if self._password_hash else "(no-set)"
        return f"Usuario(nombre={self.nombre!r}, email={self.email!r}, password_hash={oculto})"

def demo() -> None:
    # Modo demostración: crea un usuario, asigna contraseña y verifica
    u = Usuario("Alejandro", "alejandro@example.com")
    print(u)
    u.set_password("secreto123")
    print("Password seteado. Hash:", u.password_hash[:12], "...")
    print("check_password('secreto123'):", u.check_password("secreto123"))
    print("check_password('otro')      :", u.check_password("otro"))

def interactivo() -> None:
    # Modo interactivo: permite al usuario crear y gestionar un usuario por teclado
    try:
        u = Usuario(input("Nombre: ").strip() or "Usuario", input("Email: ").strip())
    except ValueError as e:
        print("Error creando usuario:", e)
        return

    while True:
        # Menú de opciones para interactuar con el usuario
        print("\n1) Setear contraseña  2) Ver hash  3) Verificar contraseña  4) Cambiar email  5) Ver usuario  6) Salir")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                # Permite establecer una nueva contraseña
                u.set_password(input("Nueva contraseña: "))
                print("OK")
            elif op == "2":
                # Muestra el hash actual de la contraseña
                print("Hash:", u.password_hash or "(sin configurar)")
            elif op == "3":
                # Verifica si la contraseña ingresada coincide
                print("¿Coincide?:", u.check_password(input("Contraseña a verificar: ")))
            elif op == "4":
                # Permite cambiar el email, validando el formato
                u.email = input("Nuevo email: ").strip()
                print("Email actualizado:", u.email)
            elif op == "5":
                # Muestra la representación del usuario
                print(u)
            elif op == "6":
                # Sale del menú interactivo
                break
            else:
                print("Opción no válida.")
        except ValueError as e:
            # Muestra errores de validación en las operaciones
            print("Error:", e)

def main() -> None:
    # Punto de entrada: permite elegir entre modo demo o interactivo
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    # Ejecuta el programa solo si se llama directamente
    main()
