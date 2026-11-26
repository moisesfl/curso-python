# UD04 — Tarea evaluable: desarrollo de una aplicación web con Flask

---

## 1. Enunciado general

**Descripción:**

El alumnado deberá desarrollar una aplicación web para la gestión de tareas pendientes (TO-DO), utilizando el lenguaje de programación Python y el framework Flask.

Para el desarrollo de la aplicación se tomará como punto de partida el videotutorial disponible en la unidad:

- [Flask Tutorial – Full Course for Beginners](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=12s).

La aplicación deberá incorporar una serie de modificaciones respecto al videotutorial, poniendo en práctica los conocimientos adquiridos a lo largo de las diferentes unidades del módulo.

---

## 2. Requisitos de la aplicación

  ### 2.1. Funcionalidades

  La aplicación web deberá permitir:

  - Crear nuevas tareas.
  - Consultar y visualizar las tareas existentes.
  - Modificar tareas.
  - Eliminar tareas.
  - Almacenar las tareas de forma persistente en una base de datos.

  ### 2.2. Base de datos y programación orientada a objetos

  A diferencia del videotutorial, **no se permitirá el uso de la librería SQLAlchemy** para la gestión de la base de datos.

  El alumnado deberá implementar su propio sistema de acceso y gestión de la base de datos, utilizando MySQL o SQLite.

  Para ello, deberá:

  - Aplicar los principios de la programación orientada a objetos (POO).
  - Implementar las clases necesarias para representar y gestionar los datos de la aplicación.
  - Separar la lógica de acceso a la base de datos de la lógica de la aplicación web.
  - Crear un paquete Python independiente para la gestión de la base de datos, de forma similar a lo trabajado en los contenidos de la Unidad 2.

  ### 2.3. Diseño e interfaz web

  La aplicación deberá cumplir los siguientes requisitos:

  - La página web tendrá un aspecto personalizado. No se admitirán entregas con un diseño idéntico al del videotutorial.
  - La aplicación estará en gallego o castellano.
  - La interfaz será intuitiva, organizada y sencilla de utilizar.
  - Se utilizarán plantillas HTML (templates) y/o ficheros estáticos (CSS, imágenes, etc.), siguiendo la estructura propia de un proyecto Flask.

  ### 2.4. Calidad del código

  - El código deberá estar organizado y suficientemente comentado de forma explicativa.
  - Se utilizarán nombres significativos para las variables, funciones, métodos y clases.
  - Se deberán controlar los posibles errores y excepciones que puedan producirse durante la ejecución de la aplicación.

  ### 2.5. Despliegue de la aplicación

  Una vez finalizado el desarrollo, la aplicación deberá desplegarse en una plataforma (por ejemplo PythonAnywhere) que permita acceder a ella a través de Internet.

  El alumnado deberá comprobar que la aplicación desplegada funciona correctamente y que todas sus funcionalidades están disponibles.

---

## 3. Consideraciones importantes

- El videotutorial servirá como punto de partida, pero el alumnado deberá adaptar y modificar la aplicación de acuerdo con los requisitos establecidos en esta tarea.
- El alumnado deberá ser capaz de explicar y justificar el funcionamiento del código desarrollado.
- Los trabajos en los que se acredite que el código ha sido copiado o generado mediante inteligencia artificial, incumpliendo las normas de la tarea, serán calificados con un 0.
- El docente podrá solicitar una demostración del funcionamiento de la aplicación, una explicación de determinadas partes del código o la realización de pequeñas modificaciones sobre el mismo.

---

## 4. Entrega

  ### 4.1. Elementos que se deben entregar

  - Proyecto en un repositorio de GitHub.
  - Fichero ZIP con el proyecto completo.
  - Enlace a la aplicación web desplegada.

  El proyecto deberá incluir un fichero `README.md` en el que se describan, como mínimo, los siguientes aspectos:

  - Descripción y funcionalidades de la aplicación.
  - Tecnologías utilizadas.
  - Estructura del proyecto.
  - Instrucciones de instalación y ejecución.
  - Instrucciones para la configuración de la base de datos.

  También se deberá incluir un fichero `requirements.txt` con las dependencias necesarias para ejecutar la aplicación.

  ### 4.2. Formato de la entrega mediante fichero ZIP

  El formato del nombre del fichero ZIP será el siguiente:

  `apelido1_apelido2_nome_UD04_tarefa.zip`

  No será necesario incluir el entorno virtual (`.venv`) ni los ficheros temporales generados durante el desarrollo.

  ### 4.3. Cómo compartir el proyecto en GitHub

  El alumnado deberá asegurarse de que el docente dispone de acceso al repositorio de GitHub para su revisión y evaluación.

  1. Crear un fichero de texto que contenga el enlace al repositorio de GitHub.

  2. Nombrar el fichero de la siguiente manera:

     `apelido1_apelido2_nome_UD04_tarefa_git.txt`

  3. Adjuntar dicho fichero en la entrega.

  ### 4.4. Enlace a la aplicación desplegada

  1. Crear un fichero de texto que contenga el enlace a la aplicación web desplegada.

  2. Nombrar el fichero de la siguiente manera:

     `apelido1_apelido2_nome_UD04_tarefa_despregue.txt`

  3. Adjuntar dicho fichero en la entrega.
