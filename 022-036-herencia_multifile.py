
"""
022-036-herencia_multifile.py
-----------------------------
En un proyecto real, estas clases estarían en archivos separados:
vehiculo.py, auto.py, moto.py, camion.py, main.py
Para efectos practicos, aquí se muestran juntas.

Jerarquía:
- Vehiculo (base)
- Auto, Moto, Camion (heredan y usan super())

Modos:
  DEMO: crea distintas subclases y muestra informacion.
  INTERACTIVO: permite elegir tipo y capturar datos.

Autor: Alejandro Aguirre Díaz
"""
from __future__ import annotations

class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int) -> None:
        if not (marca.strip() and modelo.strip()):
            raise ValueError("Marca y modelo no pueden estar vacíos.")
        if anio < 1886:
            raise ValueError("El año es inválido (antes de 1886).")
        self.marca = marca.strip()
        self.modelo = modelo.strip()
        self.anio = int(anio)

    def info(self) -> str:
        return f"{self.marca} {self.modelo} ({self.anio})"

class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, puertas: int = 4) -> None:
        super().__init__(marca, modelo, anio)
        if puertas not in (2, 3, 4, 5):
            raise ValueError("Número de puertas no usual.")
        self.puertas = puertas

    def info(self) -> str:
        return f"Auto: {super().info()} | puertas={self.puertas}"

class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, cilindraje_cc: int) -> None:
        super().__init__(marca, modelo, anio)
        if cilindraje_cc <= 0:
            raise ValueError("Cilindraje debe ser > 0.")
        self.cilindraje_cc = cilindraje_cc

    def info(self) -> str:
        return f"Moto: {super().info()} | {self.cilindraje_cc} cc"

class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, carga_max_t: float) -> None:
        super().__init__(marca, modelo, anio)
        if carga_max_t <= 0:
            raise ValueError("La carga máxima debe ser > 0.")
        self.carga_max_t = float(carga_max_t)

    def info(self) -> str:
        return f"Camión: {super().info()} | carga_max={self.carga_max_t} t"

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
            print("⚠️ Ingresa un número válido (float).")

def demo() -> None:
    v: list[Vehiculo] = [
        Auto("Toyota", "Yaris", 2020, puertas=4),
        Moto("Yamaha", "MT-07", 2022, cilindraje_cc=689),
        Camion("Volvo", "FH", 2019, carga_max_t=18.0),
    ]
    for obj in v:
        print(obj.info())

def interactivo() -> None:
    print("1) Auto  2) Moto  3) Camión")
    op = input("Elige tipo: ").strip()
    marca = input("Marca: ").strip()
    modelo = input("Modelo: ").strip()
    anio = leer_int("Año: ", minimo=1886)

    try:
        if op == "1":
            puertas = leer_int("Puertas [2/3/4/5]: ")
            veh = Auto(marca, modelo, anio, puertas)
        elif op == "2":
            cc = leer_int("Cilindraje (cc): ", minimo=1)
            veh = Moto(marca, modelo, anio, cc)
        elif op == "3":
            carga = leer_float("Carga máx (ton): ", minimo=0.1)
            veh = Camion(marca, modelo, anio, carga)
        else:
            print("Opción no válida."); return
        print(veh.info())
    except ValueError as e:
        print("Error:", e)

def main() -> None:
    modo = input("Selecciona modo [demo/interactivo]: ").strip().lower()
    interactivo() if modo.startswith("i") else demo()

if __name__ == "__main__":
    main()
