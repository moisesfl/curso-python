# UD02-Tarea entregable
<div id="top"></div>


## Índice de contenidos

*   
    *   [Gestión de acceso y evaluación de usuarios en un sistema](#gestion-de-acceso-y-evaluacion-de-usuarios-en-un-sistema)
        *   [ Contexto general](#contexto-general)
    *   [ Datos de partida](#datos-de-partida)
    *   [ Requisitos funcionales (QUÉ debe hacer el programa)](#requisitos-funcionales-que-debe-hacer-el-programa)
        *   [1. Validación general del usuario (condicional simple)](#1-validacion-general-del-usuario-condicional-simple)
        *   [2. Identificación del tipo de usuario (match – case)](#2-identificacion-del-tipo-de-usuario-match-case)
        *   [3. Evaluación académica del alumno (condicionales anidados)](#3-evaluacion-academica-del-alumno-condicionales-anidados)
        *   [4. Control de edad del alumno (anidación + ejecución condicional)](#4-control-de-edad-del-alumno-anidacion-ejecucion-condicional)
        *   [5.Uso de estructura compacta (operador ternario)](#5-uso-de-estructura-compacta-operador-ternario)
    *   [ Requisitos técnicos (CÓMO debe hacerse)](#requisitos-tecnicos-como-debe-hacerse)
    *   [ Representación mediante diagrama de flujo](#representacion-diagrama-de-flujo)
    * [Entrega](#entrega)

- - -


- - -

## Gestión de acceso y evaluación de usuarios en un sistema[](#gestion-de-acceso-y-evaluacion-de-usuarios-en-un-sistema "Permanent link")

###  Contexto general[](#contexto-general "Permanent link")

Vas a desarrollar un **programa en Python** que simule el comportamiento de un **sistema de acceso y evaluación de usuarios** en una aplicación educativa.

El sistema deberá tomar decisiones en función de:

*   El tipo de usuario
*   La edad
*   La nota obtenida
*   El estado del usuario

Para ello, deberás utilizar **todas las estructuras condicionales estudiadas en el tema**, aplicando correctamente la sintaxis, el sangrado y la lógica de control.

- - -

##  Datos de partida[](#datos-de-partida "Permanent link")

El programa debe trabajar con el siguiente diccionario, cuyos valores serán modificado para realizar las pruebas:

```
usuario = {
    "nombre": "Ana",
    "edad": 17,
    "rol": "alumno",      # Puede ser: "alumno", "profesor", "invitado"
    "nota": 6.5,          # Número entre 0 y 10 (puede ser inválido). Indiferente para profesor.
    "activo": True        # Indica si el usuario está activo en el sistema
}
```

- - -

##  Requisitos funcionales (QUÉ debe hacer el programa)[](#requisitos-funcionales-que-debe-hacer-el-programa "Permanent link")

El programa arranccará, analizará el diccionario "usuario" y llevará a cabo los siguientes pasos:

- - -

### 1. Validación general del usuario (condicional simple)[](#1-validacion-general-del-usuario-condicional-simple "Permanent link")

*   Comprueba si el usuario está **activo**.
*   Si el usuario **NO está activo**, muestra el mensaje:

> `"Usuario inactivo. Acceso denegado."` \* En ese caso, **no se debe ejecutar ninguna otra parte del programa**.

- - -

### 2. Identificación del tipo de usuario (`match – case`)[](#2-identificacion-del-tipo-de-usuario-match-case "Permanent link")

Si el usuario está activo:

*   Utiliza una estructura `match – case` para analizar el valor de la clave `"rol"`.
*   El comportamiento debe ser el siguiente:
    
*   `"alumno"` → continuar con la evaluación académica.
    
*   `"profesor"` → mostrar: `"Acceso como profesor. No se requiere evaluación."`
    
*   \* `"invitado"` → mostrar: `"Acceso limitado como invitado."`
    
*   \* Cualquier otro valor → mostrar: `"Rol no reconocido."`
    

- - -

### 3. Evaluación académica del alumno (condicionales anidados)[](#3-evaluacion-academica-del-alumno-condicionales-anidados "Permanent link")

 **Este apartado solo se ejecuta si el rol es `"alumno"`**.

Debes realizar las siguientes comprobaciones, utilizando **estructuras condicionales anidadas**:

#### a) Validación de la nota[](#a-validacion-de-la-nota "Permanent link")

*   Comprueba si la nota está entre 0 y 10.
*   Si la nota **no es válida**, muestra:

> `"Nota no válida."`

#### b) Clasificación de la nota (if – elif – else)[](#b-clasificacion-de-la-nota-if-elif-else "Permanent link")

Si la nota es válida:

*   Menor que 5 → `"Suspenso"`
*   Entre 5 y 6.9 → `"Aprobado"`
*   Entre 7 y 8.9 → `"Notable"`
*   9 o más → `"Sobresaliente"`

- - -

### 4. Control de edad del alumno (anidación + ejecución condicional)[](#4-control-de-edad-del-alumno-anidacion-ejecucion-condicional "Permanent link")

*   Comprueba la edad del alumno.
*   Si es **menor de 18**, muestra:

> `"Alumno menor de edad."` \* Si es **mayor o igual que 18**, muestra:
> 
> `"Alumno mayor de edad."`

Esta comprobación debe estar **correctamente anidada** dentro del bloque del alumno.

- - -

### 5. Uso de estructura compacta (operador ternario)[](#5-uso-de-estructura-compacta-operador-ternario "Permanent link")

*   Utiliza un **operador ternario** para asignar una variable llamada `estado_academico`:
    
*   `"Promociona"` si la nota es mayor o igual que 5.
    
*   `"No promociona"` en caso contrario.

Después, muestra el valor de esa variable.

- - -

##  Requisitos técnicos (CÓMO debe hacerse)[](#requisitos-tecnicos-como-debe-hacerse "Permanent link")

El programa **debe cumplir obligatoriamente** lo siguiente:

*   Usar:
    
*   `if`
    
*   `if – else`
*   `if – elif – else`
*   condicionales **anidados**
*   operador **ternario**
*   estructura `match – case`
*   Aplicar correctamente:
    
*   El **sangrado**
    
*   El **control del flujo de ejecución**
*   La **gestión de variables**
*   No usar funciones (todo en un único bloque principal).
*   El código debe ser **legible, ordenado y comentado**.

- - -

##  Representación mediante diagrama de flujo[](#representacion-diagrama-de-flujo "Permanent link")

Para finalizar, deberás representar gráficamente el funcionamiento del programa mediante un diagrama de flujo.

El diagrama debe mostrar de forma clara todas las decisiones y caminos posibles que puede seguir el programa dependiendo de los datos del usuario.

El diagrama deberá utilizar correctamente los símbolos habituales (vistos en la UD1).

- - -

## Entrega[](#entrega "Permanent link")

- La entrega de esta tarea consistirá en un fichero .py (`apellido1_apellido2_nombre_EC_T02.py`) con el código del programa, qué deberá llevar comentarios explicativos de cada bloque. 
- La entrega del diagrama de flujo será un un fichero .png o .pdf con el nombre `apellido1_apellido2_nombre_EC_T02`. Se podrá utilizar cualquie herramienta, incluso hacerlo a mano y fotografiarlo, siempre que se lea.


[⬆ Ir arriba](#top)
