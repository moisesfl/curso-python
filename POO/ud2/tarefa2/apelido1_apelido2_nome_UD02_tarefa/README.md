# Sistema de Domótica — UD2

Aplicación modular en Python que simula dispositivos domóticos administrados por un Hub central.

## Contenido
- `domotica/base.py`: clase abstracta `Dispositivo` y propiedades validadas.
- `domotica/dispositivos.py`: sensor, bombilla y cerradura inteligentes.
- `domotica/interfaces.py`: capacidades mediante `Protocol` (`Medible`, `Conmutable`, `Actualizable`).
- `domotica/hub.py`: registro, consulta, listado, operaciones polimórficas y estadísticas.
- `domotica/common.py`: validaciones, creación de ID y excepciones de dominio.
- `main.py`: demostración integral y pruebas de errores.

## Requisitos
Python 3.10 o posterior (se utilizan anotaciones de tipos modernas y `match` no es necesario).

## Ejecución
Desde la carpeta raíz del proyecto:

```bash
python main.py
```

## Decisiones de implementación
- Los ID admiten letras, números y guiones; deben comenzar por una letra.
- `Conmutable` define `encender()`/`apagar()`. En la cerradura se interpretan como bloquear/desbloquear para permitir la operación polimórfica común.
- La actualización de firmware está implementada en las bombillas; por ello son los dispositivos que satisfacen `Actualizable`.
- Se añade `calibrar(offset)` al sensor para cubrir la acción de calibración del ejemplo del enunciado.
- `Hub.obtener(id)` permite consultar y lanza `NoEncontrado` cuando no existe.

## Entrega
Antes de entregar:
1. Revisa el código y personaliza los datos/nombres si corresponde.
2. Crea un repositorio público en GitHub y sube el contenido.
3. Sustituye el enlace de `enlace_github.txt` por la URL real del repositorio.
4. Genera el ZIP con el nombre solicitado para tu caso.
