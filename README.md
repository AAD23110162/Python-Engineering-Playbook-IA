

# Python Engineering Playbook IA

**Autor:** Alejandro Aguirre Díaz  
**Descripción:** Portafolio de 23 prácticas progresivas para aprender Python con enfoque a IA, desde la preparación del entorno hasta Programación Orientada a Objetos (POO).  
Cada práctica es un script numerado y documentado con `docstrings` y `type hints`.

---

## 📑 Tabla de Contenidos

### 🔧 000 – Preparación del entorno
- `001-001-diagnostico_entorno.py` → Muestra versión de Python, ruta del intérprete y disponibilidad de `pip`.  
- `002-002-primer_script.py` → Primer programa en Python: saludo personalizado desde CLI.

---

### 📘 010 – Python básico
- `003-011-variables_demo.py` → Declaración de variables de distintos tipos y uso de `type()`.  
- `004-012-comentarios_y_keywords.py` → Uso de comentarios y 5 palabras reservadas con ejemplos.  
- `005-013-io_basica.py` → Entrada de nombre/edad con `input()` y salida validada.  
- `006-014-strings_basicos.py` → Análisis de cadenas: contar caracteres, mayúsculas, palabra más larga.  
- `007-015-listas_tuplas_sets_dicts.py` → Transformar una lista en tupla, set y diccionario de frecuencias.  
- `008-016-conversiones_y_booleanos.py` → Conversión segura de `str` a otros tipos y operadores lógicos.  
- `009-017-condicionales_y_bucles.py` → Juego de adivinar un número con intentos y pistas.  
- `010-018-funciones_intro.py` → Calculadora básica (+, −, ×, ÷) con funciones y manejo de errores.

---

### 📗 020 – Python avanzado
- `011-021-oop_intro_resumen.py` → Introducción a clases simples (`Usuario`, `Pedido`).  
- `012-022-pilares_oop.py` → Ejemplos de herencia, encapsulamiento, polimorfismo y abstracción.  
- `013-023-modulos_y_paquetes.py` → Ejemplo de módulo propio y cómo importarlo.  
- `014-024-fechas_y_math.py` → CLI que calcula días transcurridos entre fechas y usa operaciones matemáticas.  
- `015-025-funciones_avanzadas.py` → Decoradores (`@timeit`), `lambda` y generadores con `yield`.  
- `016-026-programacion_defensiva.py` → Manejo de excepciones personalizadas y validaciones robustas.

---

### 📙 030 – POO básica
- `017-031-intro_poo.py` → Clase `Punto2D` con métodos `mover()` y `distancia()`.  
- `018-032-atributos_y_metodos.py` → Clase `CuentaBancaria` con operaciones y representación.  
- `019-033-init_y_self.py` → Clase `Producto` con atributos en `__init__` y cálculo de precio final. 
- `020-034-args_en_clases.py` → Clase `Paquete(*items)` que calcula peso/volumen total.  
- `021-035-herencia_super.py` → Clases `Animal` → `Perro`/`Gato` con uso de `super()`.  
- `022-036-herencia_multifile.py` → Ejemplo de herencia separando clases en varios archivos.  
- `023-037-encapsulamiento.py` → Clase `Usuario` con atributo privado y uso de `@property`.

---

## 🚀 Cómo ejecutar
```bash
python nombre_del_script.py