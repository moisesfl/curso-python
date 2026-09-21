from pathlib import Path

import markdown

# Tu contenido original en Markdown (asegúrate de que tenga líneas en blanco antes de las tablas)
contenido_markdown = """
# UD02-Condicionales

## 2.1. Lógica en tests

### Tabla resumen

| Operador | Descripción | Ejemplo |
| :--- | :--- | :--- |
| == | Igual a | a == b |
| != | Diferente de | a != b |

```python
# Bloque de código de ejemplo
if edad >= 18:
    print("Mayor de edad")
```
"""
file_path = "Z:/Workspace/curso-python/ESCO/ud2/ud2_condicionales"
file_name = Path(file_path).stem  # Extrae el nombre del archivo sin extensión

# Lee tu archivo Markdown
with open(f"{file_path}.md", "r", encoding="utf-8") as f:
  texto_md = f.read()

# 1. Convertimos usando explícitamente las extensiones necesarias
html_puro = markdown.markdown(
    texto_md, extensions=["fenced_code", "tables", "toc"]
)

# 2. Creamos una plantilla con estilos CSS para que las tablas y códigos se VEAN bien
html_con_estilos = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>UD02 - Condicionales</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        
        /* Estilos esenciales para que la TABLA sea visible */
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #cbcbcb; padding: 10px; text-align: left; }}
        th {{ background-color: #f2f2f2; font-weight: bold; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        
        /* Estilos para bloques de CÓDIGO */
        pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; border-left: 5px solid #007acc; }}
        code {{ font-family: 'Courier New', Courier, monospace; color: #d14; }}
        pre code {{ color: inherit; }}
    </style>
</head>
<body>
    {html_puro}
</body>
</html>
"""

# 3. Guardamos el archivo final listo para abrir en el navegador
with open(f"{file_name}.html", "w", encoding="utf-8") as f:
    f.write(html_con_estilos)

print("¡Archivo 'unidad2.html' generado con éxito!")

