
"""
021-035-herencia_super.py
-------------------------
Demuestra herencia con super():
- Animal (base)
- Perro, Gato (subclases que sobreescriben hablar)
- MascotaDeServicio (extiende Perro con atributo 'servicio')

Modos:
  DEMO: crea varias instancias y llama hablar().
  INTERACTIVO: permite crear animales y probar hablar().

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations

class Animal:
    def __init__(self, nombre: str) -> None:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = nombre.strip()

    def hablar(self) -> str:
        return "..."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(nombre={self.nombre!r})"

class Perro(Animal):
    def __init__(self, nombre: str, raza: str = "mestizo") -> None:
        super().__init__(nombre)
        self.raza = raza

    def hablar(self) -> str:
        return "Guau!"

class Gato(Animal):
    def hablar(self) -> str:
        return "Miau"

class MascotaDeServicio(Perro):
    def __init__(self, nombre: str, servicio: str, raza: str = "labrador") -> None:
        super().__init__(nombre, raza=raza)
        if not servicio.strip():
            raise ValueError("El servicio no puede estar vacío.")
        self.servicio = servicio.strip()

    def hablar(self) -> str:
        # Uso de super() para extender comportamiento (ejemplo simple)
        return f"{super().hablar()} (servicio: {self.servicio})"

def demo() -> None:
    animales: list[Animal] = [
        Animal("Bicho"),
        Perro("Rocky", "pastor alemán"),
        Gato("Misha"),
        MascotaDeServicio("Luna", servicio="asistencia emocional"),
    ]
    for a in animales:
        print(f"{a!r} dice: {a.hablar()}")

def interactivo() -> None:
    print("1) Animal  2) Perro  3) Gato  4) MascotaDeServicio")
    op = input("Elige tipo: ").strip()
    try:
        if op == "1":
            a = Animal(input("Nombre: "))
        elif op == "2":
            a = Perro(input("Nombre: "), input("Raza (opcional): ") or "mestizo")
        elif op == "3":
            a = Gato(input("Nombre: "))
        elif op == "4":
            a = MascotaDeServicio(
                input("Nombre: "),
                servicio=input("Servicio (p.ej. guía/asistencia): "),
                raza=input("Raza (opcional): ") or "labrador",
            )
        else:
            print("Opción no válida."); return
        print(f"{a!r} dice: {a.hablar()}")
    except ValueError as e:
        print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
