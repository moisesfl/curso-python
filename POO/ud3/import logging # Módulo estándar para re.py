import logging           # Módulo estándar para registro de eventos
from pathlib import Path # Manejo de rutas

# Configuramos el logger para escribir en un archivo .log
ruta_log = Path("logs/errores.log")
ruta_log.parent.mkdir(parents=True, exist_ok=True)  # Creamos la carpeta 'logs' si no existe

logging.basicConfig(
    filename=ruta_log,                     # Archivo donde se guardarán los logs
    level=logging.ERROR,                   # Nivel mínimo: solo errores o más graves
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato con fecha y nivel
)

ruta = Path("datos/inexistente.txt")  # Archivo que no existe (forzará FileNotFoundError)

try:
    with ruta.open("r", encoding="utf-8") as f:
        contenido = f.read()  # Intentamos leer (no llegaremos aquí si falla)
except FileNotFoundError as e:
    # Registramos el error en el fichero .log con el detalle de la excepción
    logging.error("Archivo no encontrado: %s", e)
    print("Se ha registrado el error en el log:", ruta_log)
except Exception as e:
    # Registramos cualquier otro error no esperado
    logging.exception("Error inesperado accediendo al archivo")  # incluye traceback
    print("Error inesperado registrado en el log.")