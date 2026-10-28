# Boletín de Ejercicios — UD2: Programación Orientada a Objetos (Python)

- - -

## 1️. Ejercicio A — Zoológico (Animales)

### Enunciado

Implemente un paquete `zoo` para gestionar animales de un pequeño zoológico. Debe modelar la jerarquía de **animales** con una **clase base abstracta** y varias subclases. Añada una **interfaz estructural** (Protocol) para animales que pueden ser **alimentados** y otra para animales que pueden **emitir sonido**.

### Estructura del proyecto (propuesta)

```
mi_proyecto_zoo/
│
├─ zoo/
│  ├─ __init__.py            # Re-exporta la API pública
│  ├─ base.py                # ABC: Animal
│  ├─ clases.py              # Subclases concretas (Perro, Aguila, Serpiente...)
│  ├─ interfaces.py          # Protocol: Sonoro, Alimentable (runtime_checkable)
│  ├─ utils.py               # Utilidades (estáticas) y factorías (classmethod)
│  └─ excepciones.py         # Excepciones específicas del dominio
│
└─ main.py                   # Demostración (punto de entrada con __main__)
```

### Requisitos funcionales y técnicos

*   **Clase abstracta `Animal`** en el fichero `base.py` con:
    
    *   Atributos protegidos:
        *   `nombre`, `_especie: str`, `_peso_kg: float`, `_edad: int` .
        *   Hacer comprobación de validez (peso y edad deben tener valores positivos). Verificar utilizando los setters de la clase.
    *   Métodos abstractos:
        *   `moverse() -> None`,
        *   `getTipo() -> str`: devuelve la raza dentro de la especie del animal.
    *   `__str__()` sobrescrito indicando:
        *   clase a la que pertenece el objeto, especie, peso y edad.
    *   Método de generación de animales `parir()` (nacimientos) abstracto y estático que cuando se implemente:
        *   El peso se genere aleatoreamente dentro de un rango según el animal.
        *   La raza (tipo) se genere aleatoriamente dentro de una lista.
*   **Subclases** de _Animal_ en `clases.py` (al menos 3): `Perro`, `Aguila`, `Serpiente`.
    
    *   Implementan atributos específicos.
        *   Por ejemplo raza, patas, ojos, tipocola, etc.
    *   Sobrescriben `moverse()` y `tipo()`.
    *   Implementan (si procede) métodos específicos (p. ej., `volar()` en `Aguila`).
*   **Interfaces (Protocol)** en `interfaces.py` con `@runtime_checkable`:
    
    *   `Sonoro` con `hacerSonido() -> None`.
    *   `Alimentable` con `alimentar(kg: float) -> None`
        *   valida `kg > 0`.
*   **`utils.py`**:
    
    *   Clase con métodos estáticos para diferentes funcionalidades como por ejemplo el comentado a continuación.
    *   `es_peso_saludable` indica si un peso determinado para un tipo de animal con una edad determinada es sano, devolviendo si está por debajo o por arriba del valor adecuado.
*   **Excepciones** en `excepciones.py` (p. ej., `PesoInvalido`, `EdadInvalida`).
    
*   **`__init__.py`**: permite el acceso a `Animal`, subclases e interfaces vía `__all__`.
    
*   **`main.py`**:
    
    *   Usa `if __name__ == "__main__":`.
    *   Crea una lista heterogénea de animales, recorre e imprime `__str__`, llama polimórficamente a `moverse()` y, si `isinstance(x, Sonoro)`, muestra `x.sonido()`; si `isinstance(x, Alimentable)`, `x.alimentar(kg)`.

### UML (ASCII)

**Clase base "Animal":**

```
+----------------------------------------------------+
|                    <<abstract>>                    |
|                       Animal                       |
+----------------------------------------------------+
| # total_animales: int {static}                     |
| - _nombre: str                                     |
| - _especie: str                                    |
| - _peso: float                                     |
| - _edad: int                                       |
+----------------------------------------------------+
| + __init__(nombre: str, especie: str,              |
|            peso: float, edad: int)                 |
| + getNombre() : str                                |
| + setNombre(nombre: str) : None                    |
| + getEspecie() : str                               |
| + setEspecie(especie: str) : None                  |
| + getPeso() : float                                |
| + setPeso(peso: float) : None                      |
| + getEdad() : int                                  |
| + setEdad(edad: int) : None                        |
| + __str__() : str                                  |
| # moverse() : None {abstract}                      |
| # getTipo() : str {abstract}                       |
| # parirAnimal() : None {abstract, static}          |
+----------------------------------------------------+
```

### Ejemplo de salida

```
#### Fénix    ####
Envergadura: 60.5 cm
Clase <class 'zoo.clases.Aguila'>: nombre Fénix, especie Aguila, peso 15.0 kg, edad 5 años, envergadura 60.5 cm
Este animal es de la subespecie Imperial
 ...batir alas...   ...ascendiendo...   ...planeando alto...
 IIIIIII-III!! (grito fuerte al lanzarse en picado)
 ¡IIIIIIIIHHHHH! (ruge triunfante, saciada y poderosa)
Peso: 15.0
¿Cómo está de peso este animal?: alto

#### Águila recién nacida    ####
Envergadura: 15 cm
Clase <class 'zoo.clases.Aguila'>: nombre Águila recién nacida, especie Aguila, peso 2 kg, edad 0 años, envergadura 15 cm
Este animal es de la subespecie Calva
 ...batir alas...   ...ascendiendo...   ...planeando alto...
IIIIIII-III!! (grito fuerte al lanzarse en picado)
¡IIIIIIIIHHHHH! (ruge triunfante, saciada y poderosa)
Peso: 2
¿Cómo está de peso este animal?: bajo

#### Calcetines    ####
La raza del perro es: Pastor Alemán
Clase <class 'zoo.clases.Perro'>: nombre Calcetines, especie Perro, peso 20.3 kg, edad 8 años, raza Pastor Alemán
Este animal es de la subespecie Pastor Alemán
...corre...  ...salta...  ...mueve la cola...  ¡Guau guau!
¡GUAU GUAU GUAU! (ladrido fuerte de alerta)
¡BURP! (come demasiado y se tumba satisfecho)
Peso: 20.3
¿Cómo está de peso este animal?: bajo

#### Perro recién nacido    ####
La raza del perro es: Bichón Maltés
Clase <class 'zoo.clases.Perro'>: nombre Perro recién nacido, especie Perro, peso 2 kg, edad 0 años, raza Bichón Maltés
Este animal es de la subespecie Bichón Maltés
...corre...  ...salta...  ...mueve la cola...  ¡Guau guau!
¡GUAU GUAU GUAU! (ladrido fuerte de alerta)
¡BURP! (come demasiado y se tumba satisfecho)
Peso: 2
¿Cómo está de peso este animal?: bajo

#### Sisosa    ####
¿Es venenosa esta serpiente? False
Clase <class 'zoo.clases.Serpiente'>: nombre Sisosa, especie Serpiente, peso 5.8 kg, edad 3 años, venenosaa False 
Este animal es de la subespecie Culebra
...se desliza...  ...repta entre las rocas...  ...saca la lengua...  sss...
SSSSSSS! (siseo fuerte, en actitud defensiva)
¡sssssss~! (come demasiado y se queda inmóvil digiriendo)
Peso: 5.8
¿Cómo está de peso este animal?: alto

#### Serpiente recién nacida    ####
¿Es venenosa esta serpiente? True
Clase <class 'zoo.clases.Serpiente'>: nombre Serpiente recién nacida, especie Serpiente, peso 2 kg, edad 4 años, venenosaa True 
Este animal es de la subespecie Anaconda
...se desliza...  ...repta entre las rocas...  ...saca la lengua...  sss...
SSSSSSS! (siseo fuerte, en actitud defensiva)
¡sssssss~! (come demasiado y se queda inmóvil digiriendo)
Peso: 2
¿Cómo está de peso este animal?: bajo


```

- - -

## 2️⃣ Ejercicio B — Vivero (Plantas)

### 🎯 Enunciado

Cree un paquete `botanica` para gestionar diferentes **plantas** en un vivero. Modele una jerarquía con una **clase abstracta** `Planta` y subclases concretas. Añada un **Protocol** para objetos **regables** y utilidades estáticas para validar **estacionalidad** y **riego**.

### 📁 Estructura del proyecto (propuesta)

```
mi_proyecto_botanica/
│
├─ botanica/
│  ├─ __init__.py
│  ├─ base.py                # ABC: Planta
│  ├─ clases.py              # Arbol, Arbusto, Hierba (Olivo, Rosal, Cesped)
│  ├─ interfaces.py          # Protocol: Regable (runtime_checkable)
│  ├─ utils.py               # Validaciones estáticas y factorías de clase
│  └─ excepciones.py
│
└─ main.py
```

### 🧩 Requisitos funcionales y técnicos

*   **Clase abstracta `Planta`** con:
    *   Atributos: `_especie: str`, `_altura_cm: float`, `_perenne: bool` (validación: `altura_cm >= 0`).
    *   Métodos abstractos: `crecer(cm: float) -> None`, `tipo() -> str`.
    *   `__str__()` descriptivo.
    *   Método de clase estático `crearPlantaAleatoria()`.
*   **Subclases**: `Arbol`, `Planta Herbácea`, `Hierba`.
*   **Protocol `Regable`** con `regar(litros: float) -> None` (validar `litros > 0`).
    *   **Implementación**: todas las plantas implementan `Regable`.
*   **`utils.py`**:
    *   **@staticmethod** `es_epoca_riego(mes: int) -> bool`.
    *   **@staticmethod** `calcular_riego_recomendado(altura_cm: float) -> float`.
*   **Excepciones**: `AlturaInvalida`, `RiegoInvalido`.
*   **`__init__.py`**: re-exporta API pública con `__all__`.
*   **`main.py`**: patrón `__main__`; crea varias plantas de distintos tipos; aplica `regar()` y `crecer()` polimórficamente y muestra resultados; captura excepciones.

- - -

## 3️⃣ Ejercicio C — Aeronáutica (Aeronaves)

### 🎯 Enunciado

Desarrolle un paquete `aeronaves` para gestionar diferentes **aeronaves**. Modele una **clase abstracta** `Aeronave` y subclases concretas con capacidades de **despegue/aterrizaje**. Añada protocolos de **repostaje** y **mantenimiento** y utilidades para cálculo de **autonomía**.

### 📁 Estructura del proyecto (propuesta)

```
mi_proyecto_aeronautica/
│
├─ aeronaves/
│  ├─ __init__.py
│  ├─ base.py                # ABC: Aeronave
│  ├─ clases.py              # Avion, Helicoptero, Dron
│  ├─ interfaces.py          # Protocol: Volable, Repostable, Mantenible (runtime_checkable)
│  ├─ utils.py               # Cálculos estáticos (autonomía, consumo)
│  └─ excepciones.py
│
└─ main.py
```

### 🧩 Requisitos funcionales y técnicos

*   **ABC `Aeronave`** con:
    *   Atributos: `_matricula: str`, `_capacidad_combustible_l: float`, `_consumo_l_h: float` (validación: valores > 0).
    *   Métodos abstractos: `despegar() -> None`, `aterrizar() -> None`, `tipo() -> str`.
    *   `__str__()` informativo.
    *   Método de clase estático `generarAeronaaveAleatoria() -> "Aeronave"`.
*   **Subclases**: `Avion`, `Helicoptero`, `Dron` (cada una implementa despegue/aterrizaje).
*   **Protocols** en `interfaces.py` con `@runtime_checkable`:
    *   `Volable` (`volar(horas: float) -> None`),
    *   `Repostable` (`repostar_en_vuelo(litros: float) -> None`),
    *   `Mantenible` (`realizar_mantenimiento(desc: str) -> None`).
*   **Implementación**:
    *   todas implementan `Volable` y `Mantenible`.
    *   Solo `Avion`implementa `repostar_en_vuelo()`.
*   **`utils.py`**:
    *   **@staticmethod** `autonomia_horas(capacidad_l: float, consumo_l_h: float) -> float`.
    *   **@staticmethod** `consumo_mision(horas: float, consumo_l_h: float) -> float`.
*   **Excepciones**: `CombustibleInvalido`, `ConsumoInvalido`.
*   **`__init__.py`**: re-exporta API pública con `__all__`.
*   **`main.py`**:
    *   Patrón `__main__`.
    *   Demostración: crea varias aeronaves, calcula autonomía, simula `repostar()` y `volar()` con control de consumo, prueba manejo de errores.

- - -