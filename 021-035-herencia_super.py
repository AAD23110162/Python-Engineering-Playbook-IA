
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
       # Constructor base: inicializa el nombre del animal
       if not nombre.strip():
          raise ValueError("El nombre no puede estar vacío.")
       self.nombre = nombre.strip()

    def hablar(self) -> str:
       # Método que puede ser sobreescrito por subclases
       return "..."

    def __repr__(self) -> str:
       # Representación legible del animal
       return f"{self.__class__.__name__}(nombre={self.nombre!r})"

class Perro(Animal):
    def __init__(self, nombre: str, raza: str = "mestizo") -> None:
       # Constructor: llama al constructor de Animal y agrega raza
       super().__init__(nombre)
       self.raza = raza

    def hablar(self) -> str:
       # Sobreescribe el método hablar para Perro
       return "Guau!"

class Gato(Animal):
    def hablar(self) -> str:
        # Sobreescribe el método hablar para Gato
        return "Miau"

class MascotaDeServicio(Perro):
    def __init__(self, nombre: str, servicio: str, raza: str = "labrador") -> None:
        # Constructor: llama al constructor de Perro y agrega servicio
        super().__init__(nombre, raza=raza)
        if not servicio.strip():
            raise ValueError("El servicio no puede estar vacío.")
        self.servicio = servicio.strip()

    def hablar(self) -> str:
        # Uso de super() para extender comportamiento: añade información de servicio
        return f"{super().hablar()} (servicio: {self.servicio})"

def demo() -> None:
    # Modo demostración: crea instancias de cada clase y muestra su comportamiento
    animales: list[Animal] = [
        Animal("Bicho"),
        Perro("Rocky", "pastor alemán"),
        Gato("Misha"),
        MascotaDeServicio("Luna", servicio="asistencia emocional"),
    ]
    for a in animales:
        # Muestra la representación y el resultado de hablar()
        print(f"{a!r} dice: {a.hablar()}")

def interactivo() -> None:
    # Modo interactivo: permite al usuario crear animales y probar hablar()
    print("1) Animal  2) Perro  3) Gato  4) MascotaDeServicio")
    op = input("Elige tipo: ").strip()
    try:
        if op == "1":
            # Crea un Animal genérico
            a = Animal(input("Nombre: "))
        elif op == "2":
            # Crea un Perro con nombre y raza
            a = Perro(input("Nombre: "), input("Raza (opcional): ") or "mestizo")
        elif op == "3":
            # Crea un Gato con nombre
            a = Gato(input("Nombre: "))
        elif op == "4":
            # Crea una MascotaDeServicio con nombre, servicio y raza
            a = MascotaDeServicio(
                input("Nombre: "),
                servicio=input("Servicio (p.ej. guía/asistencia): "),
                raza=input("Raza (opcional): ") or "labrador",
            )
        else:
            # Opción no reconocida
            print("Opción no válida."); return
        # Muestra la representación y el resultado de hablar()
        print(f"{a!r} dice: {a.hablar()}")
    except ValueError as e:
        # Muestra el error si ocurre una excepción en la validación
        print("Error:", e)

def main() -> None:
    # Solicita al usuario el modo de ejecución y llama al flujo correspondiente
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    # Si el modo empieza con 'i', activa el modo interactivo; si no, ejecuta demo
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
