## Tarea entregable – UD04

## Sistema Inteligente de Gestión “Streamify Pro”

[Tarea entregable – UD04](#page-0)

[Sistema Inteligente de Gestión “Streamify Pro”](#page-0)

[ Contexto general](#page-0)

[ Datos de partida](#page-0)

[ Requisitos funcionales (QUÉ debe hacer el programa)](#page-0)

[1. Menú de Control (while + match-case)](#page-0)

[2. Saneamiento de datos (filter + lambda)](#page-0)

[3. Auditoría de Ingresos y Servicios (reduce + recursividad)](#page-0)

[4. Clasificación (sorted + tuplas)](#page-0)

[5. Enviar facturas (recursividad)](#page-0)

[6. Salir](#page-0)

[ Requisitos técnicos (CÓMO debe hacerse)](#page-0)

[ Criterios de evaluación cubiertos](#page-0)

##  Contexto general

La empresa "Streamify" te ha pedido un sistema para procesar las facturas mensuales. El programa debe limpiar los datos corruptos, calcular los precios finales con descuentos, ordenar a los clientes por prioridad y, finalmente, enviar las notificaciones de cobro de forma recursiva. El objetivo es hacer uso de lo aprendido en esta unidad sobre funciones (map, filter, reduce,..), lambdas y recursividad.



## Datos de partida
Copia este bloque al inicio de tu programa:

```
usuarios = [
{"email": "juan@gmail.com", "plan": "estándar", "precio": 9.99, "meses": 12},
{"email": "marta@yahoo.es", "plan": "premium", "precio": 15.99, "meses": 5},
{"email": "pedro_sin_arroba", "plan": "estándar", "precio": 9.99, "meses": 2},
{"email": "ana@gmail.com", "plan": "premium", "precio": 15.99, "meses": 24},
{"email": "info@empresa.com", "plan": "básico", "precio": 5.99, "meses": 1}
]
DESCUENTO_FIDELIDAD = 0.20
servicios_adicionales = ["Cloud", ["Juegos", "Música"], "4K", ["Soporte 24/7"]]
```

##  Requisitos funcionales (QUÉ debe hacer el programa)

## 1. Menú de Control (while + match-case)

El programa debe tener un menú que permita:

- 1. Saneamiento de datos: Ejecuta el filtrado de emails.

- 2. Auditoría de Ingresos y Servicios: Muestra el total de ingresos y servicios activos.

- 3. Clasificación: Ordenación jerárquica por plan y meses.

- 4. Enviar Facturas: Ejecuta el envío de notificaciones con el resumen de gastos.

- 5. Salir.

## 2. Saneamiento de datos (filter + lambda)

En esta opción deben analizarse los usuarios almacenados y limpiar aquellos que tengan datos inválidos. Para ello debes crear una función que devuelva únicamente los usuarios con un email válido (que contenga "@"), mostrando por pantalla como resultado el número de usuarios eliminados y la lista de emails de los que quedan.

Por ejemplo, para los datos iniciales, el resultado sería similar a:

```
[EJECUTANDO FILTRADO...]
- Registro eliminado: 'pedro_sin_arroba' (Email inválido)
Saneamiento completado:
- Usuarios originales: 5
- Usuarios válidos: 4

Lista de emails listos:
1. juan@gmail.com
2. marta@yahoo.es
3. ana@gmail.com
4. info@empresa.com
```

## 3. Auditoría de Ingresos y Servicios (reduce + recursividad)

Para esta opción, el programa debe calcular el total de ingresos, teniendo en cuenta que cada usuario tiene un plan con un precio distinto, y que si el usuario lleva más de 10 meses como socio, se le aplica el descuento de fidelidad (20%).

Además de los ingresos, el sistema debe realizar un Análisis Técnico de Servicios. Para ello, debes crear una función recursiva que recorra la lista servicios_activos y cuente cuántos servicios individuales hay en total (teniendo en cuenta que algunos servicios son 'packs' que contienen otros servicios dentro).

Así, como resultado de esta opción debe mostrarse por pantalla el total de los ingresos mensuales y anuales esperados, y el número total de servicios junto con la lista aplanada de los mismos. El resultado de esta opción será algo similar a:

```
[GENERANDO INFORME DE AUDITORÍA...]

RESUMEN FINANCIERO (Precios con Dto.):

- Ingresos Mensuales Reales: 38.36€
- Proyección Ingresos Anuales: 460.32€

ANÁLISIS TÉCNICO DE SERVICIOS:
- Se han detectado 6 servicios individuales en los packs activos.
(Desglose: Cloud-Storage, Music-Pass, Video-4K, Gaming-Hub, VPN, Secure-Login)

Estado de la auditoría: COMPLETA
```


## 4. Clasificación (sorted + tuplas)

Al seleccionar esta opción, el programa deberá mostrar la lista de usuarios ordenada, de modo que pueda conocerse quiénes son los clientes con más antigüedad y sus tipos de plan, por medio de los criterios de prioridad:

- 1. Primero: Por tipo de plan (de la A a la Z).

- 2. Segundo (desempate): Por antigüedad (meses) de mayor a menor.

Como resultado se obtendría algo similar a:

```
[GENERANDO CLASIFICACIÓN POR PRIORIDAD...]

LISTA DE CLIENTES ORDENADA:
1. [Básico] - info@empresa.com (1 meses)
2. [Estándar] - juan@gmail.com (12 meses)
3. [Premium] - ana@gmail.com (24 meses)
4. [Premium] - marta@yahoo.es (5 meses)

Lista clasificada por Plan y Antigüedad (Descendente).
```

## 5. Enviar facturas (recursividad)

Para esta opción, debes implementar una función recursiva llamada:

`enviar_avisos(lista_clientes_procesados)`.



Donde como resultado el usuario obtendrá una lista de facturas enviadas a cada usuario donde especificará el precio final y el ahorro proporcionado por el descuento. De este modo el resultado sería algo similar a:

```
[INICIANDO ENVÍO RECURSIVO DE FACTURAS...]

>> Factura enviada a: juan@gmail.com Cobrado: 7.99€ | (Ahorro: 2.00€ por fidelidad)
>> Factura enviada a: marta@yahoo.es Cobrado: 15.99€ | (Sin descuento aplicado)
>> Factura enviada a: ana@gmail.com Cobrado: 12.79€ | (Ahorro: 3.20€ por fidelidad)
>> Factura enviada a: info@empresa.com Cobrado: 5.99€ | (Sin descuento aplicado)

Proceso de envío finalizado con éxito. ------------------------------------------
```

## 6. Salir

El programa se cerrará al seleccionar esta opción, mostrando por pantalla un mensaje similar a:

`Cerrando sistema... ¡Gracias por usar Streamify Pro!`

##  Requisitos técnicos (CÓMO debe hacerse)

- Modularidad obligatoria: A diferencia de las UDs anteriores, está prohibido hacer todo en un bloque. Cada requisito debe ser una función def independiente.

- Uso de herramientas del Tema 4: Es obligatorio el uso de map, filter, reduce y lambdas.

- Recursividad: Al menos dos funciones deben ser recursivas.

- Documentación: Cada función debe llevar un breve comentario explicando qué recibe, qué devuelve y cómo funciona.

- Aplicar correctamente:

    - El sangrado

    - El control del flujo de ejecución

    - La gestión de variables

- El código debe ser legible, ordenado y comentado.
