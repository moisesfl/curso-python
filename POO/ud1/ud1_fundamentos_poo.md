# Unidad 1: Fundamentos de la Programación Orientada a Objetos (POO) en Python
 
>  _Unidad teórica orientada a la comprensión de los fundamentos de la POO mediante ejemplos del mundo real y analogías con Python._

- - -

##  1. Introducción a la Programación Orientada a Objetos

La **Programación Orientada a Objetos (POO)** surge como respuesta a la necesidad de **modelar sistemas complejos** de una forma más intuitiva.  
A diferencia de la programación estructurada (centrada en funciones y datos), la POO organiza el código en **entidades llamadas objetos**, que combinan **datos (atributos)** y **comportamientos (métodos)**.

### Ejemplo comparativo del mundo real

**Ejemplo 1: Una receta de cocina**

*   En programación estructurada, tendríamos funciones como `mezclar()`, `hornear()`, `servir()`, y variables sueltas con los ingredientes.
*   En POO, el objeto sería una **Receta**, con atributos (`ingredientes`, `tiempo`, `temperatura`) y métodos (`preparar()`, `hornear()`, `servir()`).

**Ejemplo 2: Fábrica de coches**

*   Cada coche es un objeto que tiene atributos (`color`, `modelo`, `potencia`) y métodos (`acelerar()`, `frenar()`, `girar()`).
*   La **clase Coche** es el molde general del que se fabrican todos los coches.

### Ventajas de la POO

*   **Organización:** El código se agrupa en clases y objetos, facilitando su comprensión.
    
    > Ejemplo: En un videojuego, todos los personajes heredan de una clase base `Personaje`, lo que evita duplicar código.
    
*   **Claridad:** Cada clase tiene responsabilidades claras y separadas.
    
    > Ejemplo: La clase `Inventario` gestiona los objetos del jugador, y la clase `Mapa` gestiona el entorno.
    
*   **Reutilización:** Las clases pueden heredarse, extenderse y usarse en nuevos proyectos.
    
    > Ejemplo: una clase `Vehículo` puede reutilizarse para crear `Coche`, `Moto`, o `Camión`.
    

### Esquema básico UML (ASCII)

```
+--------------------------+
|        Clase             |
+--------------------------+
| - atributos              |
| - propiedades            |
+--------------------------+
| + métodos                |
| + comportamientos        |
+--------------------------+
            │
            ▼
+--------------------------+
|       Objeto             |
+--------------------------+
| instancia de la clase    |
+--------------------------+
```

- - -

## 2. Concepto de Objeto 

Un **objeto** es una entidad que tiene:

*   **Identidad:** lo diferencia de otros objetos.
*   **Estado** → describe el objeto y su estado mediante los atributos.
*   **Comportamiento** → lo que puede hacer, que se implementa mediante métodos.

### Ejemplos con UML

**Ejemplo 1: Usuario de red social**

```
+----------------------------+
| Usuario                   |
+----------------------------+
| - nombre                   |
| - foto                     |
| - lista_amigos             |
+----------------------------+
| + publicar()               |
| + enviar_mensaje()         |
+----------------------------+
```

**Ejemplo 2: Archivo del sistema**

```
+----------------------------+
| Archivo                   |
+----------------------------+
| - nombre                   |
| - tamaño                   |
| - fecha_creación           |
+----------------------------+
| + abrir()                  |
| + borrar()                 |
+----------------------------+
```

**Ejemplo 3: Personaje de videojuego**

```
+----------------------------+
| Personaje                 |
+----------------------------+
| - vida                     |
| - energía                  |
| - nivel                    |
+----------------------------+
| + atacar()                 |
| + defender()               |
+----------------------------+
```

**Ejemplo 4: Cuenta Bancaria**

```
+----------------------------+
| CuentaBancaria            |
+----------------------------+
| - titular                  |
| - saldo                    |
+----------------------------+
| + ingresar()               |
| + retirar()                |
+----------------------------+
```

- - -

##  3. Atributos y Encapsulación 

Los **atributos** representan los datos que describen el estado de un objeto.

###  Tipos de atributos

*   **Públicos:** accesibles desde cualquier parte.
*   **Privados:** solo accesibles dentro de la clase.
*   **Protegidos:** accesibles desde la clase y sus subclases.

###  Ejemplos

1.  **Juego de rol:** un personaje tiene `nombre`, `nivel`, `puntos_de_vida` y `experiencia`.
2.  **Empresa:** un empleado tiene `nombre`, `sueldo`, `puesto`.
3.  **Tienda online:** un producto tiene `nombre`, `precio`, `stock`.
4.  **Red social:** un usuario tiene `nombre`, `email`, `número_de_amigos`.

###  Encapsulación

La **encapsulación** protege los datos internos del objeto, impidiendo su modificación directa desde fuera.  
Se accede a ellos mediante **métodos getters y setters**.

**Ejemplo UML:**

```
+----------------------------+
| CuentaBancaria            |
+----------------------------+
| - titular                  |
| - saldo                  |
+----------------------------+
| + depositar()              |
| + retirar()                |
| + consultar_saldo()        |
+----------------------------+
```

- - -

##  4. Métodos 

Los **métodos** son las acciones que puede realizar un objeto.

**Ejemplos:**

*   En una **bombilla**, los métodos son `encender()` y `apagar()`.
*   En una **cuenta bancaria**, `ingresar()` y `retirar()`.
*   En un **personaje de videojuego**, `saltar()`, `atacar()`, `recuperar_vida()`.
*   En un **archivo**, `abrir()`, `leer()`, `guardar()`, `cerrar()`.

Los métodos permiten **interactuar con los datos internos** de un objeto de manera controlada.

- - -

##  5. Clases e Instancias 

Una **clase** es la plantilla general que define las características y comportamientos comunes de un conjunto de objetos.  
Una **instancia** es un objeto concreto creado a partir de esa clase.

**Ejemplo:**

```
Clase Coche
 ├── Atributos: color, marca, modelo
 └── Métodos: arrancar(), frenar()

Objeto mi_coche
 ├── color = rojo
 ├── marca = Toyota
 └── modelo = Corolla
```

###  Conceptos avanzados

*   **Clases anidadas:** clases definidas dentro de otras, útiles para estructuras lógicas.
*   **Herencia:** una clase puede heredar atributos y métodos de otra.
*   **Sobreescritura de métodos:** redefinir un método heredado para adaptarlo.
*   **Sobrecarga de métodos:** permitir varios métodos con el mismo nombre pero diferentes parámetros.
*   **Polimorfismo:** capacidad de un objeto para comportarse de diferentes maneras según el contexto.
*   **Importación de clases:** posibilidad de reutilizar clases definidas en otros módulos.

###  Herencia UML

```
+-------------------+
| Animal            |
+-------------------+
| + comer()         |
| + dormir()        |
+-------------------+
       ▲
       │
+--------------+      +--------------+
| Perro        |      | Gato         |
+--------------+      +--------------+
| + ladrar()   |      | + maullar()  |
| + comer()    |      | + comer()    |
+--------------+      +--------------+
```

### Ejemplo de sobrescritura

```python
class Animal:
    def sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def sonido(self):
        print("Guau guau")
```

### Ejemplo de sobrecarga (simulada)

```python
class Calculadora:
    def sumar(self, a, b, c=None):
        return a + b if c is None else a + b + c
```

### Ejemplo de polimorfismo

```python
class Ave:
    def volar(self): print("El ave vuela")

class Pinguino(Ave):
    def volar(self): print("El pingüino no vuela")

for animal in [Ave(), Pinguino()]:
    animal.volar()
```

- - -

##  6. Constructores 

El **constructor** es un tipo especial de método que **se ejecuta automáticamente al crear un objeto**.

###  Ejemplo

Cuando creamos un nuevo usuario en una aplicación, el constructor define su nombre, correo y estado inicial.

###  Otros ejemplos

*   Crear una **cuenta bancaria** con saldo inicial.
*   Crear un **producto** con su nombre y precio definidos.
*   Crear un **pedido** con fecha y cliente asignados.

- - -

##  7. Destructores 


El **destructor** (`__del__()`) se ejecuta cuando un objeto deja de existir.  
Python incluye un **recolector de basura (Garbage Collector)** que destruye automáticamente los objetos no referenciados.

```python
class Archivo:
    def __init__(self, nombre):
        self.archivo = open(nombre, "w")
    def __del__(self):
        self.archivo.close()
        print("Archivo cerrado correctamente.")
```

- - -

##  8. Ortogonalidad de los Métodos 

La **ortogonalidad** implica que cada método cumpla una sola función y no dependa innecesariamente de otros.

###  Buen diseño

```
Clase Calculadora
 ├── sumar()
 ├── restar()
 ├── multiplicar()
 └── dividir()
```

###  Mal diseño

```
Clase Calculadora
 └── operar()  # hace todo, difícil de mantener
```

**Ejemplo adicional (web):**  
`GestorUsuarios` con métodos separados `registrar()`, `autenticar()`, `cambiar_contraseña()`.

**Ejemplo adicional (científico):**  
`Simulacion` con `inicializar()`, `ejecutar()`, `guardar_resultados()`.

###  Relación con los patrones de diseño

Los **patrones de diseño** se basan en la ortogonalidad y la reutilización.  
Se clasifican en:

*   **Creacionales:** Estos patrones proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código existente.
    *   _[Singleton](https://refactoring.guru/es/design-patterns/singleton)_
    *   _[Factory](https://refactoring.guru/es/design-patterns/factory-method)_
*   **Estructurales:** Estos patrones explican cómo ensamblar objetos y clases en estructuras más grandes, mientras se mantiene la flexibilidad y eficiencia de la estructura.
    *   _[Adapter](https://refactoring.guru/es/design-patterns/adapter)_
    *   _[Decorator](https://refactoring.guru/es/design-patterns/decorator)_.
*   **De comportamiento:** cómo colaboran los objetos.
    *   _[Observer](https://refactoring.guru/es/design-patterns/observer)_
    *   _[Strategy](https://refactoring.guru/es/design-patterns/strategy)_

Para consultar más información: [https://refactoring.guru/es/design-patterns](url)

#### Patrones de diseño en Python

#####  Más utilizados en Python

*   **Strategy** — “muy común” en Python; usado para cambiar el comportamiento sin herencia \* **Factory Method** — “ampliamente usado”; aporta flexibilidad al crear objetos.
*   **Abstract Factory** — “bastante común”; frecuente en frameworks para extender/customizar componentes.
*   **Builder** — “bien conocido” en el mundo Python; útil cuando hay muchas opciones de configuración.
*   **Iterator** — “muy común”; estándar para recorrer colecciones.
*   **Observer** — “bastante común”, especialmente en GUIs y sistemas basados en eventos.
*   **Command** — “bastante común”; alternativa a callbacks, colas de tareas, histórico de operaciones.
*   **Chain of Responsibility** — “bastante común” cuando encadenas manejadores/filtros.
*   **Composite** — “bastante común”; muy útil para jerarquías (UI, árboles, grafos).
*   **Adapter** — “bastante común”, sobre todo para integrar **código legado** con clases modernas.
*   **Template Method** — “bastante común” en frameworks para esqueleto de algoritmos con pasos sobreescribibles.

#####  Poco usados / desaconsejados en Python

*   **Singleton** — muchos desarrolladores lo consideran **antipatrón**; su uso **va a la baja** en Python.
*   **Visitor** — **no es muy común** por su complejidad y aplicabilidad limitada.
*   **Proxy** — **no es un invitado frecuente** en la mayoría de apps Python (aunque útil en casos especiales).
*   **Flyweight** — su único fin es minimizar memoria; **si no tienes problemas de RAM, puedes ignorarlo** por ahora.

- - -

##  9. Tipos de Métodos 

###  Clasificación

| Tipo de método | Descripción | Ejemplo real |
| --- | --- | --- |
| **Instancia** | Actúan sobre un objeto concreto. | Un coche arranca. |
| **Clase** | Actúan sobre la clase completa. | Contar coches creados. |
| **Estáticos** | No dependen de ningún objeto, es decir, no hace falta crear un objeto para utilizarlos | Calcular impuestos. |

###  Setters y Getters

Permiten **leer y modificar** atributos de forma controlada.

*   **Getter:** devuelve el valor de un atributo.
*   **Setter:** cambia el valor de un atributo.

###  Mutadores y No Mutadores

*   **Mutadores:** modifican el estado del objeto (por ejemplo, `depositar_dinero()`).
*   **No mutadores:** no modifican el estado (por ejemplo, `consultar_saldo()`).

- - -

###  Conclusión

La **Programación Orientada a Objetos** es una forma estructurada de pensar el software como un conjunto de **entidades interconectadas**.  
Cada clase representa un concepto del mundo real, y los objetos son sus manifestaciones concretas.  
Python simplifica la aplicación de estos principios gracias a su sintaxis clara, favoreciendo el desarrollo de programas **modulares, mantenibles y reutilizables**.

Dominar la POO es el primer paso para comprender **patrones de diseño**, **arquitecturas modernas** y **frameworks avanzados** como Django o Flask.  
Su comprensión es esencial para el desarrollo profesional en Python.

- - -

 **Bibliografía y recursos recomendados:**

*   [Refactoring Guru – Patrones de Diseño](https://refactoring.guru/es/design-patterns)
*   Booch, G. (2007). _Object-Oriented Analysis and Design with Applications._
*   Lutz, M. (2013). _Learning Python._ O’Reilly Media.
*   Documentación oficial de Python: [https://docs.python.org/es/3/](https://docs.python.org/es/3/)
