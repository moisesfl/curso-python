# Solución Zoológico

## Estructura

```text
solucion_zoologico/
├── zoo/
│   ├── __init__.py
│   ├── base.py
│   ├── clases.py
│   ├── interfaces.py
│   ├── utils.py
│   └── excepciones.py
└── main.py
```

## Ejecución

Ejecuta el fichero `main.py` para probar el funcionamiento del paquete `zoo`.


## Decisiones de implementación

- La edad admite el valor `0` porque el enunciado incluye animales recién nacidos.
- El peso debe ser estrictamente mayor que cero.
- `Animal` implementa `Alimentable`, por lo que todas sus subclases cumplen ese protocolo.
- Las tres subclases implementan `Sonoro`.
- `parir()` es estático y cada subclase devuelve una instancia de su propio tipo.
- Los rangos de peso de `ZooUtils` son valores orientativos.
