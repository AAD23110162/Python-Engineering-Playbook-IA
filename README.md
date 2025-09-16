# Python Engineering Playbook IA

**Autor:** Alejandro Aguirre Díaz.  
**Descripción:** Portafolio de 23 prácticas progresivas para aprender Python con enfoque a IA, desde la preparación del entorno, hasta Programación Orientada a Objetos (POO).  
**Ultima modificación:** Lunes 15 de septiembre del 2025.

---

## 📑 Tabla de contenidos

### 🔧 000 – Preparación del entorno
- `001-001-diagnostico_entorno.py` → Imprime la versión de Python, la ruta del intérprete y verifica si `pip` está disponible en el sistema. Útil para validar el entorno antes de programar.
- `002-002-primer_script.py` → Solicita un nombre por consola y muestra un saludo personalizado. Ejemplo básico de entrada/salida y uso de funciones.

---

### 📘 010 – Python básico
- `003-011-variables_demo.py` → Demuestra la declaración y uso de variables de distintos tipos (int, float, str, bool, lista, tupla, dict). Imprime su valor y tipo.
- `004-012-comentarios_y_keywords.py` → Ejemplos de comentarios de una y varias líneas. Muestra el uso de 5 palabras reservadas (`if`, `else`, `for`, `def`, `return`) con ejemplos prácticos.
- `005-013-io_basica.py` → Solicita nombre y edad al usuario, valida que la edad sea un número entero y muestra un saludo. Ejemplo de validación básica de entrada.
- `006-014-strings_basicos.py` → Analiza un texto ingresado: cuenta caracteres, mayúsculas, minúsculas y encuentra la palabra más larga. Muestra métricas útiles de cadenas.
- `007-015-listas_tuplas_sets_dicts.py` → Convierte una entrada separada por comas en lista, tupla, conjunto y diccionario de frecuencias. Demuestra transformaciones y conteo de elementos.
- `008-016-conversiones_y_booleanos.py` → Realiza conversiones seguras de string a int, float y bool. Demuestra operadores lógicos y el concepto de "truthiness" en Python.
- `009-017-condicionales_y_bucles.py` → Juego interactivo donde el usuario debe adivinar un número entre 1 y 100 en 7 intentos. Incluye validación y pistas.
- `010-018-funciones_intro.py` → Calculadora con dos modos: CLI (argumentos) e interactivo. Permite sumar, restar, multiplicar y dividir, validando errores como división por cero.

---

### 📗 020 – Python avanzado
- `011-021-oop_intro_resumen.py` → Introducción a POO con clases `Usuario`, `ItemPedido` y `Pedido`. Permite crear pedidos, agregar ítems, calcular totales y marcar como pagado. Incluye validaciones y resumen de pedido.
- `012-022-pilares_oop.py` → Demuestra los pilares de la POO: herencia, abstracción (clase Figura), polimorfismo y encapsulamiento. Permite calcular área y perímetro de figuras.
- `013-023-modulos_y_paquetes.py` → Crea un paquete temporal con funciones (`es_par`, `fibonacci`) y lo importa dinámicamente. Ejemplo de modularidad y uso de importlib.
- `014-024-fechas_y_math.py` → Calcula días entre dos fechas y realiza operaciones matemáticas (raíz, seno, coseno, factorial). Incluye modo interactivo y validación de entrada.
- `015-026-funciones_avanzadas.py` → Incluye decoradores personalizados (`@timeit`, `@retry`), generador de Fibonacci y ejemplos de funciones de orden superior. Demuestra patrones avanzados de funciones.
- `016-027-programacion_defensiva.py` → Buenas prácticas de validación de entradas, manejo de excepciones personalizadas y logging de errores. Incluye utilidades para dividir y validar emails.

---

### 📙 030 – POO en Python
- `017-031-intro_poo.py` → Clase `Punto2D` con métodos para mover el punto y calcular la distancia a otro punto. Incluye modo interactivo y validaciones.
- `018-032-atributos_y_metodos.py` → Clase `CuentaBancaria` con métodos para depositar, retirar, transferir y consultar saldo. Demuestra encapsulamiento y manejo de errores.
- `019-033-init_y_self.py` → Clase `Producto` con atributos definidos en el constructor. Calcula el precio final aplicando IVA y descuento. Incluye validaciones.
- `020-034-args_en_clases.py` → Clase `Paquete` que recibe múltiples ítems por `*args` y calcula el peso y volumen total. Permite agregar ítems dinámicamente.
- `021-035-herencia_super.py` → Demuestra herencia y uso de `super()` con clases `Animal`, `Perro`, `Gato` y `MascotaDeServicio`. Permite sobreescribir métodos y extender funcionalidad.
- `022-036-herencia_multifile.py` → Ejemplo de jerarquía de clases (`Vehiculo`, `Auto`, `Moto`, `Camion`) en un solo archivo, simulando estructura multifile. Incluye validaciones y modos de uso.
- `023-037-encapsulamiento.py` → Clase `Usuario` con atributos privados, validación de email y manejo seguro de contraseñas usando hash. Demuestra encapsulamiento y propiedades.

---

## ⚡ Modos DEMO e INTERACTIVO (scripts del 011 al 023)

A partir del script `011-021-oop_intro_resumen.py` hasta `023-037-encapsulamiento.py`, cada práctica implementa dos modos de ejecución:

- **Modo DEMO:**
	- Ejecuta automáticamente ejemplos predefinidos, mostrando el flujo típico de uso del código sin requerir interacción del usuario.
	- Permite observar rápidamente el funcionamiento, validaciones y resultados esperados de cada clase o función.

- **Modo INTERACTIVO:**
	- Permite al usuario ingresar datos por teclado y manipular los objetos o funciones del script en tiempo real.
	- Facilita la experimentación, deteccion de errores y la validación de casos personalizados para el programa.


Cada script a partir del 011 hasta el 023 inicia preguntando al usuario desde la consola y/o terminal el modo deseado de ejecucion para que lo seleccione escribiendo la letra "d" para demo o "i" para interactivo.

---

## 📚 Glosario técnico

**Abstracción:** Principio de POO que permite definir la estructura y comportamiento esencial de un objeto, ocultando detalles internos.

**Argumento:** Valor que se pasa a una función o método al llamarlo.

**Atributo:** Variable asociada a una clase o instancia de clase.

**Booleano:** Tipo de dato que solo puede tomar los valores `True` o `False`.

**Clase:** Plantilla para crear objetos que agrupa atributos y métodos relacionados.

**CLI (Command Line Interface):** Interfaz de línea de comandos, permite interactuar con el programa mediante texto en la terminal.

**Constructor (`__init__`):** Método especial que se ejecuta al crear una nueva instancia de una clase.

**Decorador:** Función que modifica el comportamiento de otra función o método, aplicándose con el símbolo `@`.

**Diccionario:** Estructura de datos que almacena pares clave-valor.

**Docstring:** Cadena de texto (generalmente multilínea) que se coloca al inicio de módulos, clases o funciones para documentar su propósito, uso y detalles relevantes. Se accede con `.__doc__`.

**Encapsulamiento:** Principio de POO que restringe el acceso directo a los atributos de un objeto, usando métodos o propiedades para controlarlo.

**Excepción:** Error detectado durante la ejecución de un programa, que puede ser gestionado con bloques `try`/`except`.

**Float:** Tipo de dato numérico de punto flotante (números decimales).

**Función:** Bloque de código reutilizable que realiza una tarea específica y puede recibir argumentos y devolver valores.

**Generador:** Función especial que utiliza `yield` para devolver una secuencia de valores, uno a la vez.

**Hash:** Valor numérico generado a partir de datos, usado para comparar, almacenar o proteger información (por ejemplo, contraseñas).

**Herencia:** Principio de POO que permite crear nuevas clases basadas en otras existentes, heredando sus atributos y métodos.

**Input:** Entrada de datos proporcionada por el usuario al programa.

**Instancia:** Objeto concreto creado a partir de una clase.

**Int:** Tipo de dato numérico entero.

**Iterador:** Objeto que permite recorrer una secuencia de elementos, como listas o generadores.

**Keyword (palabra reservada):** Palabra que tiene un significado especial en Python y no puede usarse como identificador.

**Lista:** Estructura de datos que almacena una secuencia ordenada de elementos.

**Método:** Función definida dentro de una clase y asociada a sus instancias.

**Módulo:** Archivo de Python que puede contener funciones, clases y variables reutilizables en otros scripts.

**Objeto:** Instancia de una clase, con atributos y métodos propios.

**POO (Programación Orientada a Objetos):** Paradigma de programación basado en el uso de clases y objetos.

**Polimorfismo:** Principio de POO que permite que diferentes clases implementen métodos con el mismo nombre pero comportamientos distintos.

**Propiedad (`@property`):** Decorador que permite definir métodos que se acceden como atributos, útil para encapsular lógica de acceso.

**Set:** Estructura de datos que almacena elementos únicos, sin orden específico.

**String:** Tipo de dato que representa texto.

**Tupla:** Estructura de datos inmutable que almacena una secuencia de elementos.

**Type hint:** Anotación opcional en Python que indica el tipo esperado de variables, argumentos o valores de retorno en funciones y métodos. Facilita la legibilidad y el análisis del código.

**Validación:** Proceso de comprobar que los datos cumplen ciertos requisitos antes de ser procesados.

