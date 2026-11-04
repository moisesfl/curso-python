# UD3 — Tarea entregable - Gestión de estudiantes y docentes de un instituto

## Entrega

### Cómo entregar

*   Proyecto en Github.
    *   El proyecto deberá tener un README.MD con una breve explicación del mismo.
    *   Se deberá crear en modo público para que pueda acceder.
    *   Crear un fichero de texto .txt con el enlace al proyecto de GitHub y subirlo a la plataforma.
*   Fichero zip con el proyecto.
    *   Subir a la plataforma el fichero .zip con el siguiente formato: `apelido1_apelido2_nome_UD03_tarefa.zip`.

- - -

##  Enunciado general

**Descripción:** Aplicación con interfaz por consola que permite gestionar los estudiantes y profesores de un centro de formación profesional de informática mediante el almacenamiento de datos en un fichero json básico para estudiantes y otro para profesores.

*   Más información: [Wikipedia JSON](https://es.wikipedia.org/wiki/JSON)

**Requisitos:**

*   **Menú de usuario**:
    
    1.  Listar estudiantes.
    2.  Listar profesores.
    3.  Crear estudiante.
    4.  Eliminar estudiante.
    5.  Crear profesor.
    6.  Eliminar profesor.
    7.  Modificar datos estudiante.
    8.  Modificar datos de profesor.
    9.  Buscar datos de estudiantee.
    10.  Buscar datos de profesor.
    11.  Salir.
    
*   **Datos de estudiantes**:
    
    *   DNI -> clave que identifica cada registro. str.
    *   Nombre -> str.
    *   Apellidos -> str.
    *   Ciclo -> siglas (ASIR, DAM, etc). str.
    *   Curso -> int.

*   **Datos profesores**:
    
    *   DNI -> clave que identificaa cada registro. str.
    *   Nombre -> str.
    *   Apellidos -> str.
    *   Especialidad. -> _Informática, Sistemas y Aplicaciones informáticas, Formación y Orientación Laboral_
    *   Ciclos -> siglas (ASIR, DAM, etc). str.
    *   Módulos -> siglas (SRI, PSP, SAD, AD, PAR, ...). str.

*   **Gestión de errores**:
    
    *   Gestionar los posibles errores que pueda dar el programa si el fichero no existe, etc.
    *   En caso de que haya un error, el programa mostrará cual es el error y volverá al menú principal.
*   Generar un **log** en la carpeta en que se ejecuta el programa. Se almacenara en cada línea la fecha y hora, la tarea ejecutada y el usuario que la ejecutó. También se mostrarán los errores.
    

**Estructura:**

*   `main.py`
*   app
    *   `__init__.py`
        
    *   `interfaz_usuario.py` -> clase con el menú y banners.
        
    *   `ficheros.py` -> clase con las funcionalidades para trabajar con ficheros.
        
    *   `gestion_instituto.py` -> clase con las funcionalidades para gestionar estudiantes y profesores que usa las clases respectivas.
        
    *   `estudiante.py` -> clase con funcionalidades específicas para gestionar a los estudiantes y que usa las funcionalidades de "ficheros.py".
        
    *   `docente.py` -> clase con funcionalidades específicas para gestionar a los docentes y que usa las funcionalidades de "ficheros.py".
        
    *   `registrar.py` -> clase con las funciones para generar logs.
        
*   datos
    *   `docentes.json`
    *   `estudiantes.json`

- - -

## Pistas

### Fichero main.py

```python
# Importaciones
from app import cargarInterfaz 

# Función principal
def main():
    """ Ejecuta la interfaz de usuario """
    cargarInterfaz()

if __name__ == "__main__":
    main()

```

### Estructura fichero interfaz\_usuario.py

```python

from .gestion_instituto import GestorInstituto

# FUNCIONALIDADES DE LA INTERFAZ

def cargarInterfaz() -> None:
    """ Renderizado de la Interfaz """
    mostrarBannerInicio()
    mostrarMenuPrincipal()
    mostrarBannerFin()
 
def mostrarBannerInicio() -> None:
    """ BANNER DE INICIO """

def mostrarBannerFin() -> None:
    """ BANNER DE FIN """

def mostrarMenuPrincipal() -> None:
    """ Menú principal """
          
def pedirDatosEstudiante() -> dict:
    
def pedirModificacionEstudiante(dni) -> dict:
    
```

### Fichero ficheros.py

Este fichero tiene las funciones para leer y escribir JSON. Ejemplo:

```Python
class GestorFicheros():
    # ATRIBUTOS DE CLASE
    ficheros_abiertos = 0
    operaciones_ficheros = 0

    # CONSTRUCTOR
    """ Clase para leer, escribir, ... ficheros """
    def __init__(self, ruta: str):
        """ Inicialización para un fichero concreto.
            Mantenemos el objeto creado para tratar con
            un fichero determinado

            Args:
            - ruta: ruta del fichero de estudiantes.json, profesores.json ...
        """
        self._ruta = ruta

    # MÉTODOS DE INSTANCIA JSON
    # leer fichero json
    def leerJSON(self) -> json:
        """
        Lectura de ficheros JSON (no formatea)
        
        :param ruta: objeto Path con la ruta del fichero
        :type ruta: Path
        :return: Devuelve un objeto con el contenido del fichero
        :rtype: str
        """
       
    # Escribir fichero json
    def añadirEnJSON(self, contenido: dict) -> None:
        """ 
        Escritura de ficheros json

        :param ruta: ruta al fichero
        :param contenido: nuevo contenido que va a tener el fichero json
        """
        
```