# Índice

- [1. Programación web - Flask I](#seccion-01)
  - [1.1. Instalación e preparación do contorno](#seccion-02)
    - [1.1.1. Creación do contorno virtual](#seccion-03)
    - [1.1.2. Instalación de Flask](#seccion-04)
    - [1.1.3. Creación dunha aplicación web](#seccion-05)
    - [1.1.4. Estrutura](#seccion-06)
    - [1.1.5. Depuración dunha aplicación Flask en VS Code](#seccion-07)
  - [1.2. Rutas](#seccion-08)
    - [1.2.1. Rutas dinámicas](#seccion-09)
  - [1.3. Métodos HTTP](#seccion-10)
    - [1.3.1. Métodos](#seccion-11)
    - [1.3.2. Códigos de resposta máis típicos](#seccion-12)
    - [1.3.3. Request](#seccion-13)
    - [1.3.4. Response](#seccion-14)
  - [1.4. Plantillas - Jinja I](#seccion-15)
    - [1.4.1. Organización de ficheiros](#seccion-16)
    - [1.4.2. Renderizar unha plantilla](#seccion-17)
    - [1.4.3. Variables](#seccion-18)
  - [1.5. Repaso HTML + CSS + JS](#seccion-19)
- [2. Programacion web - Flask II](#seccion-20)
  - [2.1. Recursos estáticos](#seccion-21)
    - [2.1.1. CSS, Bootstrap e máis](#seccion-22)
  - [2.2. Uso de url\_for](#seccion-23)
  - [2.3. Carga inicial de datos](#seccion-24)
  - [2.4. Plantillas - Jinja II](#seccion-25)
    - [2.4.1. Herdanza](#seccion-26)
    - [2.4.2. Condicionais](#seccion-27)
    - [2.4.3. Bucles](#seccion-28)
    - [2.4.4. Comentarios](#seccion-29)
  - [2.5. Formularios](#seccion-30)
    - [2.5.1. Formularios en Flask](#seccion-31)
    - [2.5.2. Validación no servidor](#seccion-32)
    - [2.5.3. Erros nas plantillas](#seccion-33)
    - [2.5.4. Seguridade](#seccion-34)
    - [2.5.5. Subida de ficheiros](#seccion-35)

---

<a id="seccion-01"></a>

# Programación web - Flask I

<figure class="my-6">
![Imaxe 25](https://python-poo-edu.rdpzi.com/docs/python-poo/gl/.gitbook/assets/image%20%2825%29.png)
</figure>

Para realizar aplicacións con Python e algunhas outras linguas é necesario utilizar frameworks como por exemplo **Flask**. Estes utilizan un concepto coñecido como **WSGI** (Web Server Gateway Interfaz).

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">WSGI</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Un servidor web non sabe ou non ten forma de executar aplicacións en Python. Por iso se creou **WSGI**. Esta é unha especificación de como se comunica un servidor web cunha aplicación web escrita en Python. Este estándar está descrito en detalle na especificación **PEP 3333**.

</div>

</div>

**Flask** é un “micro” **framework**. Céntrase en proporcionar o mínimo necesario para que poidas poñer a funcionar unha aplicación básica en uns minutos. Se necesitamos máis funcionalidades podemos estendelo coas **Flask extensions**. Xeralmente se utiliza como *framework* para **backend** aínda que é posible realizar aplicacións web **full-stack**.

Inclúe un servidor web de desenvolvemento para que poidas probar as túas aplicacións sen ter que instalar nun servidor web. Tamén trae un depurador e soporte integrado para probas unitarias. É 100% compatible co estándar **WSGI**. Algunhas características:

- Bo manejo de rutas. Co uso dun decorator Python podemos facer que a nosa aplicación utiliza URL simples e limpas.
- Soporta o uso de cookies seguras e o uso de sesiones.
- Utiliza o motor de plantillas Jinja, que nos permite renderizar vistas.
- Ideal para construír servizos web (como APIs REST), aplicacións estáticas ou pequenas aplicacións.
- É de código aberto baixo licenza BSD.

A súa documentación oficial: <a href="https://flask.palletsprojects.com/en/2.2.x/" rel="noopener noreferrer" target="_blank">https://flask.palletsprojects.com/en/2.2.x/</a>

<a id="seccion-02"></a>

## Instalación e preparación do entorno

<a id="seccion-03"></a>

### Creación do contorno virtual

Vamos a realizar a instalación de **Flask** utilizando a ferramenta **pip** nun contorno virtual creado con **venv**. (<a href="https://docs.python.org/3/library/venv.html#creating-virtual-environments" rel="noopener noreferrer" target="_blank">https://docs.python.org/3/library/venv.html#creating-virtual-environments</a>)

Un contorno virtual de Python é un ambiente creado co obxectivo de illar recursos como librerías e contorno de execución, do sistema principal e de outros contornos virtuais. Isto significa que nun mesmo sistema é posible ter instaladas múltiples versións dunha mesma librería sen crear ningún tipo de conflito.

<figure class="my-6">
![Imaxe 26](https://python-poo-edu.rdpzi.com/docs/python-poo/gl/.gitbook/assets/image%20%2826%29.png)
</figure>

Para crear un contorno virtual executamos o seguinte comando:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
python -m venv venv
```

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-amber-50/60 dark:bg-amber-950/20 border-amber-200 dark:border-amber-900/60" hint="warning">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-amber-200 dark:border-amber-900/60 bg-amber-100/60 dark:bg-amber-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Nome do contorno virtual**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Podemos chamar como queiramos á carpeta do contorno virtual, pero os nomes máis comúns son:

- venv → É o nome máis habitual e recomendado, porque coincide co módulo que a crea (python -m venv venv).
- .venv → Igual que o anterior pero con punto ao inicio, para que quede “oculto”.
- env ou .env → Tamén se usa moito, sobre todo en proxectos antigos ou por costume. (Non se recomenda para non confundir co ficheiro de variables de contorno)

</div>

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-red-50/60 dark:bg-red-950/20 border-red-200 dark:border-red-900/60" hint="danger">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-red-200 dark:border-red-900/60 bg-red-100/60 dark:bg-red-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Importante**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Nun repositorio GIT, este contorno virtual debe engadirse ao .gitignore e non incluirse no control de versións.

</div>

</div>

Unha vez creado, para empezar a utilizalo, debemos activalo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
1$ source venv/bin/activate
2(venv)$ 
3
4# Windows
5$ .\venv\Scripts\activate
6(venv)$ 
```

</div>

Unha vez activado, todas as librerías que se instalar faranse só neste contorno virtual (Entre paréntesis podemos ver o nome do contorno virtual activado).

Se queremos desactivalo, tan só temos que executar o seguinte comando:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ deactivate
```

</div>

<a id="seccion-04"></a>

### Instalación de Flask

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-red-50/60 dark:bg-red-950/20 border-red-200 dark:border-red-900/60" hint="danger">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-red-200 dark:border-red-900/60 bg-red-100/60 dark:bg-red-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">IMPORTANTE</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Se o non temos permisos da máquina para executar o "activate". Os comandos de **python** e **pip** que queiramos executar no noso proxecto deberán ser empregando os executables que están dentro do `venv` . Exemplo:

- `.\venv\Scripts\pip install Flask` en vez de `pip install Flask`
- `.\venv\Scripts\pip freeze` en vez de `pip freeze`
- `.\venv\Scripts\pip install -r requirements` en vez de `pip install -r requirements`
- `.\venv\Scripts\flask --version` en vez de `flask --version`

</div>

</div>

Unha vez creado o noso entorno de virtual, podemos realizar a instalación de Flask mediante **pip**. Para iso executaremos o seguinte comando:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ pip install Flask
```

</div>

Podemos comprobar a versión de **Flask** instalada con o seguinte comando:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ flask --version
```

</div>

<a id="detalle-04-01"></a>

#### Ficheiro de dependencias [](#ficheiro-de-dependencias)

Se queremos comprobar todos os paquetes instalados de Python no noso entorno virtual podemos executar o seguinte:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ pip freeze
```

</div>

Se queremos gardar esa lista de paquetes, xerando o arquivo de dependencias da nosa aplicación, utilizamos:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ pip freeze > requirements.txt
```

</div>

O arquivo **requirements.txt** é moi útil porque mantén un rexistro exacto das bibliotecas necesarias para o proxecto.

Grazas a el, podemos recrear o mesmo entorno en outra máquina ou tras unha reinstalación simplemente executando:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ pip install -r requirements.txt
```

</div>

Deste modo garantimos que todos os membros do equipo ou futuros despregues traballen coas mesmas versións das dependencias, evitando incompatibilidades.

<a id="seccion-05"></a>

### Creación dunha aplicación web

Podemos gardar a primeira aplicación nun único ficheiro chamado `main.py`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask
2
3app = Flask(__name__)
4
5@app.route('/')
6def hello_world():
7    return 'Ola, Mundo!'
8
9if __name__ == '__main__':
10    app.run('0.0.0.0', 8080)
```

</div>

<a id="detalle-05-01"></a>

#### Explicación do código

<div class="my-6" stepper="">

<div class="flex gap-4">

<div class="flex flex-col items-center shrink-0">

<div class="mt-3.5 w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shadow-sm ring-4 ring-white dark:ring-neutral-800" style="background-color: var(--color-book);">

1

</div>

<div class="w-0.5 flex-1 rounded-full" style="background-color: var(--color-book-bg-strong);">

</div>

</div>

<div class="min-w-0 flex-1 mb-4 rounded-xl border px-5 py-4 bg-gray-50 dark:bg-white/3 border-gray-200 dark:border-neutral-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 transition-colors" data-step="1">

**Importación da clase Flask**

Na primeira liña relevante importamos a clase Flask desde a librería do mesmo nome.

</div>

</div>

<div class="flex gap-4">

<div class="flex flex-col items-center shrink-0">

<div class="mt-3.5 w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shadow-sm ring-4 ring-white dark:ring-neutral-800" style="background-color: var(--color-book);">

2

</div>

<div class="w-0.5 flex-1 rounded-full" style="background-color: var(--color-book-bg-strong);">

</div>

</div>

<div class="min-w-0 flex-1 mb-4 rounded-xl border px-5 py-4 bg-gray-50 dark:bg-white/3 border-gray-200 dark:border-neutral-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 transition-colors" data-step="2">

**Creación da aplicación**

A continuación creamos o obxecto app da clase **Flask**. Este obxecto é a aplicación **WSGI**, que nos permitirá despregar e probar o noso proxecto.

Lle pasamos como argumento `__name__`, que indica o módulo actual.

</div>

</div>

<div class="flex gap-4">

<div class="flex flex-col items-center shrink-0">

<div class="mt-3.5 w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shadow-sm ring-4 ring-white dark:ring-neutral-800" style="background-color: var(--color-book);">

3

</div>

<div class="w-0.5 flex-1 rounded-full" style="background-color: var(--color-book-bg-strong);">

</div>

</div>

<div class="min-w-0 flex-1 mb-4 rounded-xl border px-5 py-4 bg-gray-50 dark:bg-white/3 border-gray-200 dark:border-neutral-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 transition-colors" data-step="3">

**Decorador @app.route('/')**

O decorador da función `hello_world()` define a ruta de acceso.

Neste caso, cando o navegador solicita a URL raíz (/), se executará esa función.

</div>

</div>

<div class="flex gap-4">

<div class="flex flex-col items-center shrink-0">

<div class="mt-3.5 w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shadow-sm ring-4 ring-white dark:ring-neutral-800" style="background-color: var(--color-book);">

4

</div>

<div class="w-0.5 flex-1 rounded-full" style="background-color: var(--color-book-bg-strong);">

</div>

</div>

<div class="min-w-0 flex-1 mb-4 rounded-xl border px-5 py-4 bg-gray-50 dark:bg-white/3 border-gray-200 dark:border-neutral-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 transition-colors" data-step="4">

**Función `hello_world` (función vista)**

A función `hello_world()` devolve unha **respuesta HTTP**, neste exemplo unha simple cadea de texto: "Ola, Mundo!".

</div>

</div>

<div class="flex gap-4">

<div class="flex flex-col items-center shrink-0">

<div class="mt-3.5 w-9 h-9 rounded-full flex items-center justify-center text-sm font-bold text-white shadow-sm ring-4 ring-white dark:ring-neutral-800" style="background-color: var(--color-book);">

5

</div>

</div>

<div class="min-w-0 flex-1 rounded-xl border px-5 py-4 bg-gray-50 dark:bg-white/3 border-gray-200 dark:border-neutral-700 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 transition-colors" data-step="5">

**Ejecución do servidor de desenvolvemento**

A sección `if __name__ == '__main__':` indica que, se executamos este ficheiro directamente, se iniciará o servidor de desenvolvemento de Flask con:

- Host 0.0.0.0: accesible desde calquera IP da rede.
- Porto 8080: porto no que escuchará a aplicación.

</div>

</div>

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Decorador**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Un **decorador** non é máis que unha función (función a) que toma como parámetro unha función (función b) e devolve outra función (función c).

Ao **decorar** unha función, estamos indicando que queremos modificar o comportamento dunha función xa existente, pero sen ter que modificar o seu código. Isto é moi útil cando queremos estender novas funcionalidades a dita función. Para decorar unha función só é necesario indicar o decorador co prefixo “@” na liña anterior á función a decorar.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="@decorador
def función_decorada():
    print('Ola mundo!!')">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@decorador
def función_decorada():
    print('Ola mundo!!')
```

</div>

</div>

</div>

Para poder executar a nosa aplicación web, invocamos o seguinte:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
(venv)$ python main.py
```

</div>

Agora, podemos acceder á nosa aplicación desde o navegador coa URL: http://{{ IP }}:8080

<a id="detalle-05-02"></a>

### Modo debug

Durante o desenvolvemento é recomendable activar o modo *debug* para:

- Recibir mensaxes detallados de erros.
- Habilitar o auto-reload, que reinicia o servidor cando detecta cambios no código.

Para ello, modificamos a chamada a run:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="app.run('0.0.0.0', 8080, debug=True)">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
app.run('0.0.0.0', 8080, debug=True)
```

</div>

<a id="detalle-05-03"></a>

#### Habilitar a saída por consola

Para facer que os `print` se vexan na consola do servidor, no ficheiro `main.py` é necesario engadir as seguintes liñas.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="import logging
logging.basicConfig(level=logging.DEBUG)">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

</div>

<a id="seccion-06"></a>

### Estrutura

Unha organización sinxela e recomendable para un proxecto **Flask** pode ser a seguinte:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
mi_proxecto/
├─ requirements.txt
├─ venv/
└─ app/
   └─ main.py
```

</div>

------------------------------------------------------------------------

- **requirements.txt**

  - Cal é:

  Un arquivo de texto que recolle todas as dependencias de Python necesarias para a aplicación, normalmente coas versións exactas.

  - Para que serve:

  Permite instalar de unha vez todas as librerías requiridas en calquera entorno novo con:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
pip install -r requirements.txt
```

</div>

------------------------------------------------------------------------

- **Directorio app/**

  - Función:

  Contén o código fonte da aplicación.

  - Ventaxe:

  Manter o código separado da raíz facilita a orde e escalabilidade.

  - Exemplo actual de contido:
    - **main.py:** Arquivo principal de arranque de Flask.
      - Define a aplicación (Flask(**name**)).
      - Configura as rutas.
      - Inicia o servidor de desenvolvemento.

  
A medida que o proxecto creza, aquí poderíamos engadir:

- routes/: para dividir as distintas rutas da aplicación.
- templates/: para as plantillas HTML de Flask.
- static/: para arquivos estáticos como CSS, JavaScript ou imaxes.
- models.py ou unha carpeta models/: para a lóxica de datos e as clases que representen entidades de base de datos.

<a id="seccion-07"></a>

### Depuración dunha aplicación Flask en VS Code

Cando desenvolvemos con Flask é moi útil poder poñer puntos de ruptura (breakpoints) e executar a aplicación en modo depuración.

Con Visual Studio Code isto faise creando un arquivo de configuración chamado **launch.json**.

<a id="detalle-07-01"></a>

### Crear a carpeta `.vscode`

Na raíz do teu proxecto (a carpeta onde está `requirements.txt` ou o `venv`) crea unha carpeta:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
.vscode/
```

</div>

Dentro desta carpeta crea un ficheiro `launch.json` co seguinte contido.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="json">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="flex items-center gap-2 min-w-0"><span class="text-xs font-mono font-semibold truncate" code-title="" style="color: var(--color-book);">launch.json</span><span class="shrink-0 text-[0.65rem] font-mono uppercase tracking-wide text-gray-400 dark:text-gray-500">json</span></span>

<div class="flex items-center gap-3">

</div>

</div>

```json
1{
2  "version": "0.2.0",
3  "configurations": [
4    {
5      "name": "Python: Flask",
6      "type": "debugpy",
7      "request": "launch",
8      "module": "flask",
9      "env": {
10        "FLASK_APP": "app.main",        // módulo onde está a variable 'app'
11        "FLASK_ENV": "development"      // activa o modo debug de Flask
12      },
13      "args": ["run", "--no-debugger", "--no-reload"],
14      "jinja": true,
15      "justMyCode": true
16    }
17  ]
18}
```

</div>

<a id="detalle-07-02"></a>

### Iniciar a depuración

1.  Abre VS Code na carpeta do proxecto.
2.  Activa o entorno virtual na terminal integrada.
3.  Preme F5 ou o botón verde de “Run and Debug”.
4.  Elige a configuración Python: Flask.

  

A aplicación executará e poderás:

- Colocar breakpoints en calquera arquivo .py.
- Inspeccionar variables na pestaña Debug.
- Ver a consola de Flask na terminal de depuración.

<a id="detalle-07-03"></a>

#### Engadir a Git

Dependendo do tipo de proxecto e do uso que se quiera dar ao repositorio, ten sentido ter esta carpeta incluída no control de versión.

- Se todo o equipo usa VS Code e queredes compartir unha configuración de depuración común para facilitar a vida a todos.
- Nese caso pódese manter o ficheiro `launch.json` no control de versión

<a id="detalle-07-04"></a>

#### Non Engadir a Git

Posto que os arquivos de .vscode suelen incluir configuracións de depuración, extensións ou preferencias que varían dun equipo a outro, pode que teña sentido engadir a carpeta no `.gitignore`

- Evitar conflictos: rutas ou entornos distintos que poidan provocar conflictos de merge innecesarios.
- Manter o repo limpo: o código e a documentación do proxecto non dependen destas configuracións.

<a id="seccion-08"></a>

## Rutas

O obxecto app de Flask nos proporciona o decorador @app.route, que permite asociar unha **función vista** a **unha ruta concreta**.

Cando o servidor recibe unha petición HTTP, Flask analiza a URL solicitada e o método HTTP (GET, POST, etc.) para decidir qué función executar.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route('/')
2def inicio():
3    return 'Página principal'   
4
5@app.route('/articulos/')
6def articulos():
7    return 'Lista de artículos'
8
9@app.route('/acerca-de')
10def acercade():
11    return 'Página acerca de...'
```

</div>

- Se o navegador accede a /, Flask executa inicio().
- Se a URL é /articulos/, executa articulos().
- Se é /acerca-de, executa acercade().

A función asociada debe devolver sempre unha resposta HTTP (texto, HTML, JSON, etc.).

> Se ningunha ruta coincide, Flask responde automaticamente con código de estado 404, indicando que o recurso non se encontrou.

------------------------------------------------------------------------

<a id="detalle-08-01"></a>

#### Consideracións sobre as barras finais

- Ruta terminada en /

  Intérprease como un directorio.

  Se o usuario omite a barra final (por exemplo visita /articulos en vez de /articulos/), Flask redirixe automaticamente á ruta correcta.

- Ruta sen / final

  Intérprease como un arquivo.

  Se o usuario engade a barra final (por exemplo /acercade/), Flask devolve un 404.

<a id="seccion-09"></a>

### Rutas dinámicas

Podemos crear rutas que acepten parámetros variables na URL, capturándoos como argumentos da función:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route("/artigos/<int:id>")
def amosar_artigo(id):
    return f"Amosando o artigo con id: {id}"
```

</div>

URL de exemplo: <a href="http://IP:8080/artigos/6" rel="noopener noreferrer" target="_blank">http://IP:8080/artigos/6</a>

> Resposta: *“Amosando o artigo con id: 6”*.

<a id="detalle-09-01"></a>

#### Varios patróns na mesma función

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route("/ola/")
2@app.route("/ola/<string:nome>/")
3@app.route("/ola/<string:nome>/<int:idade>/")
4def ola(nome=None, idade=None):
5    se nome e idade:
6        return f"Ola, {nome}, tes {idade} anos."
7    elif nome:
8        return f"Ola, {nome}"
9    else:
10        return "Ola mundo"
```

</div>

> <a href="http://IP:8080/ola/" rel="noopener noreferrer" target="_blank">http://IP:8080/ola/</a> → *Ola mundo*

> <a href="http://IP:8080/ola/pepe/" rel="noopener noreferrer" target="_blank">http://IP:8080/ola/pepe/</a> → *Ola, pepe*

> <a href="http://IP:8080/ola/pepe/16/" rel="noopener noreferrer" target="_blank">http://IP:8080/ola/pepe/16/</a> → *Ola, pepe, tes 16 anos.*

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Unha mesma función pode atender varias rutas.**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Nos parámetros podemos especificar o tipo de variable (opcional):

- string: texto sen barras (valor por defecto).
- int: números enteros.
- float: números decimais.
- path: texto que pode conter barras.

</div>

</div>

<a id="seccion-10"></a>

## Métodos HTTP

<a id="detalle-10-01"></a>

### O que é HTTP?

HTTP (Protocolo de Transferencia de HiperTexto) é o protocolo que utilizan os navegadores e servidores web para comunicarse.

Cada vez que un usuario abre unha páxina, o seu navegador envía unha petición HTTP ao servidor, e este responde cunha resposta HTTP que inclúe:

- Unha cabeceira de estado → o famoso “código de resposta”.
- Opcionalmente datos → como HTML, JSON, imaxes, etc.

Exemplo de petición e resposta:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="bash">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">bash</span>

<div class="flex items-center gap-3">

</div>

</div>

```bash
1> Petición (cliente → servidor)
2GET /index.html HTTP/1.1
3Host: www.ejemplo.com
4
5< Respuesta (servidor → cliente)
6HTTP/1.1 200 OK
7Content-Type: text/html
8
9<html>...</html>
```

</div>

<a id="detalle-10-02"></a>

### Códigos de resposta HTTP

Os códigos están divididos en grupos segundo a primeira cifra:

- 1xx → Informativos (pouco usados en desenvolvemento web básico).
- 2xx → Éxito (a petición se procesou correctamente).
- 3xx → Redireccións (indican que o recurso está en outra ubicación).
- 4xx → Erros do cliente (cando a petición está mal feita).
- 5xx → Erros do servidor (fallos internos do servidor).

En codigos-de-respuesta-mas-tipicos.md veremos os códigos máis empregados no desenvolvemento web.

<a id="seccion-11"></a>

### Métodos

Flask admite distintos **métodos** de petición **HTTP**.

Os máis habituais en aplicacións web son:

- **GET**: solicita un recurso do servidor (o método por defecto). Pódense enviar datos na propia URL mediante parámetros de consulta.
- **POST**: envía información ao servidor, por exemplo ao enviar un formulario HTML.

Por defecto, unha ruta en Flask só acepta **GET**.

Para permitir outros métodos, indícase co argumento `methods`.

<a id="detalle-11-01"></a>

#### Exemplo só POST

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/artigos/novo', methods=['POST'])
def artigos_novo():
    return 'Esta URL recibe información dun formulario con POST'
```

</div>

<a id="detalle-11-02"></a>

#### Exemplo GET e POST na mesma ruta

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import request
2
3@app.route('/login', methods=['GET', 'POST'])
4def login():
5    if request.method == 'POST':
6        return 'Accedemos con POST'
7    else:
8        return 'Accedemos con GET'
```

</div>

> Se o usuario abre a páxina no navegador (GET), execútase a parte do else.
>
> Se envía un formulario a esta mesma URL (POST), execútase o bloque de if.

Con estas ferramentas, Flask permite manexar rutas simples, dinámicas e múltiples métodos HTTP, facilitando a construción de aplicacións web flexibles e ben organizadas.

<a id="detalle-11-03"></a>

#### Outros métodos HTTP

<div class="my-5 rounded-xl border border-gray-200 dark:border-neutral-700 overflow-hidden" tabs="">

<div class="flex flex-wrap gap-1 px-2 pt-1.5 border-b border-gray-200 dark:border-neutral-700 bg-gray-50 dark:bg-white/3" role="tablist">

</div>

<div class="px-5 py-4 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0" tab-content="">

- Obxectivo: Solicitar datos ao servidor.
- Exemplo: cargar unha páxina ou pedir información dun usuario.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="http">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">http</span>

<div class="flex items-center gap-3">

</div>

</div>

```http
GET /usuarios?id=5 HTTP/1.1
```

</div>

</div>

<div class="px-5 py-4 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0" tab-content="" style="display: none;">

- Obxectivo: Enviar datos ao servidor para crear ou procesar algo novo.
- Exemplo: rexistrar un usuario, enviar un formulario.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="http">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">http</span>

<div class="flex items-center gap-3">

</div>

</div>

```http
POST /usuarios HTTP/1.1
Content-Type: application/json

{ "nome": "Ana", "idade": 22 }
```

</div>

</div>

<div class="px-5 py-4 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0" tab-content="" style="display: none;">

- Obxectivo: Reemplazar completamente un recurso existente.
- Exemplo: actualizar todos os datos dun usuario.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="http">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">http</span>

<div class="flex items-center gap-3">

</div>

</div>

```http
PUT /usuarios/1 HTTP/1.1
Content-Type: application/json

{ "nome": "Ana", "idade": 23 }
```

</div>

</div>

<div class="px-5 py-4 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0" tab-content="" style="display: none;">

- Obxectivo: Actualizar parcialmente un recurso.
- Exemplo: cambiar só a idade dun usuario.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="http">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">http</span>

<div class="flex items-center gap-3">

</div>

</div>

```http
PATCH /usuarios/1 HTTP/1.1
Content-Type: application/json

{ "idade": 24 }
```

</div>

</div>

<div class="px-5 py-4 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0" tab-content="" style="display: none;">

- Obxectivo: Eliminar un recurso.
- Exemplo: borra un usuario da base de datos.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="http">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">http</span>

<div class="flex items-center gap-3">

</div>

</div>

```http
DELETE /usuarios/1 HTTP/1.1
```

</div>

</div>

</div>

<a id="seccion-12"></a>

### Códigos de resposta máis típicos

<a id="detalle-12-01"></a>

### 2xx: Éxito

- 200 OK
  - Todo foi ben. É a resposta típica cando cargamos unha páxina ou un recurso.
- 201 Created
  - Úsase cando se crea un recurso novo, por exemplo, ao rexistrar un usuario nunha API.
- 204 No Content
  - A petición foi correcta, pero non hai contido que devolver (típico en peticiones DELETE).

------------------------------------------------------------------------

<a id="detalle-12-02"></a>

### 3xx: Redireccións

- 301 Moved Permanently
  - O recurso mudouse de forma definitiva a outra URL. O navegador lembralo.
- 302 Found
  - Redirección temporal, úsase moito para enviar ao usuario a outra páxina.
- 304 Not Modified
  - O navegador pide un recurso e o servidor di que xa o ten en caché, así que non o envía de novo.

------------------------------------------------------------------------

<a id="detalle-12-03"></a>

### 4xx: Erros do cliente

- 400 Bad Request
  - A petición está mal formada (falta un dato, formato incorrecto…).
- 401 Unauthorized
  - O usuario non está autenticado (necesita login/token).
- 403 Forbidden
  - O usuario está autenticado, pero non ten permisos para acceder.
- 404 Not Found
  - Recurso non encontrado, o clásico “páxina non existe”.
- 405 Method Not Allowed
  - O recurso existe, pero o método usado (GET, POST, etc.) non está permitido.

------------------------------------------------------------------------

<a id="detalle-12-04"></a>

### 5xx: Erros do servidor

- 500 Internal Server Error
  - Algo fallou dentro do servidor, pero non se especifica qué.
- 502 Bad Gateway
  - O servidor actúa como “porta de enlace” (proxy) e recibe unha resposta inválida de outro servidor.
- 503 Service Unavailable
  - O servidor non está dispoñible (sobrecarga ou mantemento).

<a id="seccion-13"></a>

### Petición

Cando a nosa aplicación **Flask** recibe unha petición HTTP, Flask compara a URL e o método coas rutas definidas mediante o decorador @app.route. Se atopa unha coincidencia, executa a función vista correspondente.

Dentro dese función podemos acceder ao obxecto `request`, que contén toda a información da petición, incluídas cabeceras, parámetros e datos enviados.

Para utilizalo, primeiro debemos importalo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
from flask import Flask, request
```

</div>

<a id="detalle-13-01"></a>

#### Atributos principais de request

- `request.url`
  - URL completa á que se fixo a petición, incluídos parámetros de consulta.
- `request.path`
  - Só a ruta da URL, sen o dominio nin os parámetros.
- `request.method`
  - Método HTTP utilizado (GET, POST, etc.).
- `request.headers`
  - Todas as cabeceras da petición.
    - Exemplo útil: request.user_agent (información do navegador e sistema operativo).
- `request.form`
  - Datos enviados no corpo da petición **POST**, normalmente desde un formulario HTML.

    Acceso: request.form\['nome_campo'\].
- `request.args`
  - Parámetros enviados na URL mediante **GET**.

    Acceso: request.args.get('clave').

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-amber-50/60 dark:bg-amber-950/20 border-amber-200 dark:border-amber-900/60" hint="warning">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-amber-200 dark:border-amber-900/60 bg-amber-100/60 dark:bg-amber-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Parámetros GET**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Os parámetros GET úsanse para enviar información na propia URL.

Características principais:

- A URL e os parámetros sepáranse con ?.
- Cada parámetro defínese como clave=valor.
- Os pares clave-valor sepáranse con &.

Exemplo: <a href="https://www.exemplo.com/index.html?nome1=valor1&amp;nome2=valor2" rel="noopener noreferrer" target="_blank">https://www.exemplo.com/index.html?nome1=valor1&amp;nome2=valor2</a>

En Python podemos capturalo -\> `nome1 = request.args.get('nome1')`

</div>

</div>

- `request.files`
  - Ficheiros subidos ao servidor en peticións **POST** ou **PUT**.
- `request.remote_addr`
  - Dirección IP do cliente que realiza a petición.
- `request.user_agent`
  - Detalles do navegador, versión, sistema operativo e dispositivo do cliente.

    Conviene convertilo a cadea: str(request.user_agent).

<a id="detalle-13-02"></a>

#### Exemplo práctico

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/peticiones/')
def return_string():
    url = request.url
    return f"A URL solicitada é: {url}"
```

</div>

Se accedemos a <a href="http://localhost:8080/peticiones/?dato=123" rel="noopener noreferrer" target="_blank">http://localhost:8080/peticiones/?dato=123</a>, a resposta será:

> A URL solicitada é: <a href="http://localhost:8080/peticiones/?dato=123" rel="noopener noreferrer" target="_blank">http://localhost:8080/peticiones/?dato=123</a>

<a id="seccion-14"></a>

### Resposta

<a id="detalle-14-01"></a>

### O obxecto Response en Flask

Cando **Flask** recibe unha petición HTTP e atopa unha ruta coincidente, o decorador **`@app.route`** executa a función vista e xera un obxecto **Response** que inclúe:

- Código de estado (por exemplo 200, 404, 500…).
- Cabeceras HTTP.
- Datos da resposta (texto, HTML, JSON, etc.).

O contido dese obxecto constrúese a partir do que devolva a función vista. Flask permite devolver a resposta de tres formas principais:

<a id="detalle-14-02"></a>

#### 1. Cadena de texto (string)

A forma máis sinxela.

- Código de estado por defecto: 200 (OK).
- Cabeceras: as que Flask asigna automaticamente (por exemplo, Content-Type: text/html).

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/string/')
def return_string():
    return '¡Hola, mundo!'
```

</div>

<a id="detalle-14-03"></a>

#### 2. Obxecto Response

Permite controlar datos, código de estado e cabeceras manualmente.

Para crealo se usa a función **make_response**:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import make_response
2
3@app.route('/object/')
4def return_object():
5    headers = {'Content-Type': 'text/plain'}
6    return make_response('¡Hola, mundo!', 200, headers)
```

</div>

<a id="detalle-14-04"></a>

#### 3. Tupla

Podemos devolver unha tupla en dúas variantes:

- Dous valores: (datos, código_de_estado)

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/tuple/')
def return_tuple():
    return '¡Hola, mundo!', 200
```

</div>

- Tres valores: (datos, código_de_estado, cabeceras)

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/tuple/')
def return_tuple_full():
    return '¡Hola, mundo!', 200, {'Content-Type': 'text/plain'}
```

</div>

<a id="detalle-14-05"></a>

### Respostas de erro

Para interromper a execución e enviar un erro HTTP en calquera momento se usa a función abort (hai que importala):

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import abort
2
3@app.route('/login')
4def login():
5    abort(401)  # Non autorizado
6    # O código posterior non se executa
```

</div>

<a id="detalle-14-06"></a>

#### Páxinas de erro personalizadas

Podemos definir unha resposta personalizada para un erro concreto usando o decorador `@app.errorhandler`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.errorhandler(404)
def page_not_found(error):
    return 'Página non encontrada...', 404
```

</div>

Así, cada vez que se produza un 404, Flask devolverá esa mensaxe e o código de estado correspondente.

<a id="detalle-14-07"></a>

### Redireccións

Para redirixir ao usuario a outra URL utilizamos redirect xunto con `url_for`.

O argumento de `url_for` é o nome da función vista á que queremos enviar ao usuario.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
from flask import redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('nome_funcion_vista'))
```

</div>

- `url_for('nome_funcion_vista')` constrúe a URL asociada á función indicada.
- `redirect()` envía a cabecera HTTP Location e o código de estado 302 por defecto.

<a id="seccion-15"></a>

## Plantillas - Jinja I

<a id="detalle-15-01"></a>

### O que é Jinja2?

**Jinja2** é o motor de plantillas que utiliza **Flask** para xerar **HTML dinámico**.

> Cando instalamos Flask, Jinja2 instálase automaticamente como dependencia.

Documentación oficial: <a href="https://jinja.palletsprojects.com" rel="noopener noreferrer" target="_blank">https://jinja.palletsprojects.com</a>

Idea clave: Unha plantilla Jinja é un arquivo HTML cunha sintaxe especial que permite:

- Insertar variables.
- Executar bucles e condicionais.
- Reutilizar estruturas mediante herdanza.

<a id="seccion-16"></a>

### Organización de ficheiros

O habitual é ter unha carpeta templates dentro do proxecto:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
mi_proxecto/
├─ app.py
└─ templates/
   ├─ base.html
   ├─ pagina1.html
   └─ ...
```

</div>

- `templates/`: Aquí gardamos todos os ficheiros de plantillas HTML.
- Cada plantilla é un ficheiro HTML (extensión .html) con marcado Jinja.  

Ao crear a aplicación Flask, podemos indicar a ruta da carpeta de plantillas (**aunque por defecto xa é templates**):

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
from flask import Flask
app = Flask(__name__, template_folder='templates')
```

</div>

<a id="seccion-17"></a>

### Renderizar unha plantilla

Para enviar HTML como resposta HTTP usamos `render_template`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
from flask import Flask, render_template

@app.route('/hola/')
def saludo():
    return render_template('template1.html')
```

</div>

Se `template1.html` está na carpeta **templates**, Flask búscalo e devolve o seu contido.

------------------------------------------------------------------------

<a id="detalle-17-01"></a>

#### Exemplo de plantilla básica (template1.html)

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<!DOCTYPE html>
2<html lang="gl">
3<head>
4  <meta charset="utf-8">
5  <title>Ola, como estás?</title>
6</head>
7<body>
8  <h1>Meu sitio web</h1>
9  <p>Benvido á miña primeira páxina con Flask e Jinja2.</p>
10</body>
11</html>
```

</div>

<a id="seccion-18"></a>

### Variables

As variábeis permiten que o HTML sexa dinámico. Podemos enviar datos desde Flask á plantilla e amosalos ou procesalos directamente no arquivo HTML.

<a id="detalle-18-01"></a>

#### Paso de variables desde Flask

Podemos pasar datos desde a función vista á plantilla e amosalos con `{{ variable }}`.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask, render_template
2app = Flask(__name__)
3
4@app.route('/usuario/<nombre>/')
5def usuario(nombre):
6    # Pasamos unha variable "nombre" á plantilla
7    return render_template('saludo.html', nombre=nombre)
```

</div>

En *saludo.html*:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<h1>Ola, {{ nombre }}!</h1>
```

</div>

Cando o usuario visite */usuario/Ana*, a resposta será:

> Ola, Ana!

<a id="detalle-18-02"></a>

#### Tipos de datos que se pueden pasar

Podemos enviar case calquera obxecto de Python:

| Tipo de dato en Flask    | Cómo acceder na plantilla                           |
|--------------------------|-----------------------------------------------------|
| Texto (`str`)            | `{{ nombre }}`                                      |
| Números (`int`, `float`) | `{{ precio }}`                                      |
| Booleanos (`bool`)       | `{{ activo }}` ou en `{% if activo %}`              |
| Listas ou tuplas         | `{{ lista[0] }}` ou en bucle `{% for x in lista %}` |
| Diccionarios             | `{{ usuario['email'] }}` ou `{{ usuario.email }}`   |
| Obxectos personalizados  | Atributos e métodos públicos: `{{ obxecto.campo }}` |

Exemplo con varios tipos:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route('/datos/')
2def datos():
3    return render_template(
4        'datos.html',
5        nombre='Laura',
6        idade=25,
7        cores=['vermello', 'verde', 'azul'],
8        usuario={'email': 'laura@example.com', 'activo': True}
9    )
```

</div>

En `datos.html`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<p>Nome: {{ nombre }} ({{ idade }} anos)</p>
2<p>Email: {{ usuario.email }}</p>
3<ul>
4  {% for cor in cores %}
5    <li>{{ loop.index }} - {{ cor }}</li>
6  {% endfor %}
7</ul>
```

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">Condicionais, bucles e mais</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

No exemplo anterior se emprega a sintaxe para utilizar estruturas iterativas dentro das plantillas. Por agora non profundizaremos mais. Vémo-lo na seguinte unidade.

</div>

</div>

<a id="detalle-18-03"></a>

#### Encadenar atributos e métodos

Jinja2 permite acceder a atributos, índices e incluso métodos seguros (sen paréntesis se non requiren argumentos):

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<p>{{ usuario.email.upper() }}</p>
<p>{{ cores|length }} cores na lista</p>
```

</div>

Os filtros permiten transformar valores na plantilla, usando o operador `|`.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<p>{{ nombre|capitalize }}</p>
```

</div>

- capitalize pon a primeira letra en maiúscula.
- Poden encadearse filtros: {{ texto\|striptags\|upper }}.

Doc:

<a id="detalle-18-04"></a>

#### Valores por defecto e control de variables

Se unha variable non existe ou é None, non amosará nada.

Podemos usar o filtro default para asignar un valor:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<p>Pais: {{ pais | default("Non especificado") }}</p>
```

</div>

<a id="detalle-18-05"></a>

#### Escapado automático

Jinja2 escapa o HTML das variables por defecto para evitar ataques XSS:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
comentario = "<script>alert('hack');</script>"
```

</div>

Plantilla:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<p>{{ comentario }}</p>
```

</div>

Resultado seguro no navegador:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<script>alert('hack');</script>
```

</div>

> Amósase como texto, non se executa

<a id="detalle-18-06"></a>

#### Variábeis especiais de Flask

Ademais das que pasamos manualmente, algunhas variables **globais** de Flask están dispoñibles nas plantillas:

- config – configuración da aplicación.
- request – obxecto da petición actual.
- session – datos de sesión do usuario.
- g – espazo de almacenamento temporal para a petición.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<p>Método HTTP: {{ request.method }}</p>
<p>Ruta solicitada: {{ request.path }}</p>
```

</div>

<a id="seccion-19"></a>

## Revisión HTML + CSS + JS

<a id="detalle-19-01"></a>

#### HTML

<a href="https://www.w3schools.com/html/default.asp" class="not-prose my-4 flex items-center gap-3 px-4 py-3 rounded-xl border no-underline transition-all group" rel="noopener noreferrer" style="border-color: var(--color-book-bg-strong);" target="_blank"><span class="shrink-0 flex items-center justify-center w-10 h-10 rounded-lg" style="background-color: var(--color-book-bg); color: var(--color-book);"></span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium text-gray-800 dark:text-gray-200">w3schools.com</span><span class="block truncate text-xs text-gray-400 dark:text-gray-500">https://www.w3schools.com/html/default.asp</span></span></a>

<a id="detalle-19-02"></a>

#### CSS

<a href="https://www.w3schools.com/css/default.asp" class="not-prose my-4 flex items-center gap-3 px-4 py-3 rounded-xl border no-underline transition-all group" rel="noopener noreferrer" style="border-color: var(--color-book-bg-strong);" target="_blank"><span class="shrink-0 flex items-center justify-center w-10 h-10 rounded-lg" style="background-color: var(--color-book-bg); color: var(--color-book);"></span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium text-gray-800 dark:text-gray-200">w3schools.com</span><span class="block truncate text-xs text-gray-400 dark:text-gray-500">https://www.w3schools.com/css/default.asp</span></span></a>

<a id="detalle-19-03"></a>

#### JavaScript

<a href="https://www.w3schools.com/js/default.asp" class="not-prose my-4 flex items-center gap-3 px-4 py-3 rounded-xl border no-underline transition-all group" rel="noopener noreferrer" style="border-color: var(--color-book-bg-strong);" target="_blank"><span class="shrink-0 flex items-center justify-center w-10 h-10 rounded-lg" style="background-color: var(--color-book-bg); color: var(--color-book);"></span><span class="min-w-0 flex-1"><span class="block truncate text-sm font-medium text-gray-800 dark:text-gray-200">w3schools.com</span><span class="block truncate text-xs text-gray-400 dark:text-gray-500">https://www.w3schools.com/js/default.asp</span></span></a>

<a id="seccion-20"></a>

# Programación web - Flask II

<a id="seccion-21"></a>

## Recursos estáticos

En unha aplicación web chamamos **recursos estáticos** aos ficheiros que o servidor envía sen modificacións cada vez que o navegador os solicita.

Son, por exemplo:

- Follas de estilo CSS
- Ficheiros JavaScript
- Imaxes (logo, iconos, banners)
- Fontes, vídeos ou outros ficheiros de medios

Estes ficheiros **non cambian dinámicamente** con cada petición (a diferenza do HTML xerado por Jinja2).

<a id="detalle-21-01"></a>

### Carpeta static/

Flask busca por defecto os ficheiros estáticos nun directorio chamado static na raíz do proxecto:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
mi_proyecto/
├─ app.py
├─ templates/
│   └─ index.html
└─ static/
    ├─ css/
    │   └─ estilo.css
    ├─ js/
    │   └─ app.js
    └─ img/
        └─ logo.png
```

</div>

> Podes crear subcarpetas dentro de static para manter o proxecto ordenado (css, js, img, etc.).

Se se quere cambiar o nome ou a ubicación desta carpeta, ao crear a aplicación se pode usar:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="app = Flask(__name__, static_folder='mi_static')">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
app = Flask(__name__, static_folder='mi_static')
```

</div>

<a id="seccion-22"></a>

### CSS, Bootstrap e máis

Cando desenvolvemos unha **aplicación web** con Flask, non só precisamos lóxica no servidor: tamén queremos que a interface sexa atractiva, responsiva e fácil de usar.

Para iso recurrimos a estilos **CSS** propios e a **librerías** de frontend como Bootstrap, Tailwind, Bulma ou outras.

Neste post veremos como organizar e usar estes recursos estáticos en Flask, e como integrar librerías externas para dar estilo ás nosas plantillas.

<a id="detalle-22-01"></a>

### Estilos propios (CSS)

1.  Crea a túa folla de estilos en `static/css/style.css`.
2.  Inclúyela na plantilla base:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

</div>

> Agora podes escribir as túas propias regras CSS e aplicalas a todas as páxinas.

<a id="detalle-22-02"></a>

### Librerías de estilos

<a id="detalle-22-03"></a>

#### Bootstrap

<a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/" rel="noopener noreferrer" target="_blank">Bootstrap</a> é a librería máis popular para crear sitios responsive rapidamente.

<sub>***Opción 1 – CDN***</sub> <sub></sub> <sub>**(recomendada)**</sub>

En `base.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
```

</div>

<sub>***Opción 2 – Local***</sub>

1.  Descarga Bootstrap e gárdalo en `static/bootstrap/`.
2.  Enlaza con `url_for('static', filename='bootstrap/css/bootstrap.min.css')`.

<a id="detalle-22-04"></a>

#### Bulma (CDN)

<a href="https://bulma.io/" rel="noopener noreferrer" target="_blank">Bulma</a> é un framework CSS ligero e baseado en Flexbox.

En `base.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bulma@1.0.4/css/bulma.min.css"
>
```

</div>

<a id="detalle-22-05"></a>

#### Tailwind CSS (CDN para desenvolvemento)

<a href="https://tailwindcss.com/" rel="noopener noreferrer" target="_blank">Tailwind</a> é “utility-first”, baseado en clases utilitarias.

En base.html:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
```

</div>

<a id="detalle-22-06"></a>

#### Materialize (CDN)

<a href="https://materializecss.com/" rel="noopener noreferrer" target="_blank">Materialize</a> implementa Material Design de Google.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
```

</div>

<a id="detalle-22-07"></a>

### Librerías de iconos

<a id="detalle-22-08"></a>

#### Bootstrap Icons

Conxunto oficial de iconos en SVG do equipo de Bootstrap.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link 
    rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" 
    integrity="sha384-tViUnnbYAV00FLIhhi3v/dWt3Jxw4gZQcNoSCxCIFNJVCx7/D55/wXsrNIRANwdD" 
    crossorigin="anonymous">
```

</div>

<a id="detalle-22-09"></a>

#### Font Awesome (CDN)

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css"
  integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw=="
  crossorigin="anonymous">
```

</div>

<a id="detalle-22-10"></a>

#### Material Icons (Google)

Iconos de Material Design de Google, en formato fonte ou SVG.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/material-icons@1.13.14/iconfont/material-icons.min.css">
```

</div>

<a id="detalle-22-11"></a>

#### Feather Icons

Iconos minimalistas en SVG.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.29.2/feather.min.js" integrity="sha512-zMm7+ZQ8AZr1r3W8Z8lDATkH05QG5Gm2xc6MlsCdBz9l6oE8Y7IXByMgSm/rdRQrhuHt99HAYfMljBOEZ68q5A==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-blue-50/60 dark:bg-blue-950/20 border-blue-200 dark:border-blue-900/60" hint="info">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-blue-200 dark:border-blue-900/60 bg-blue-100/60 dark:bg-blue-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">Como utilizalos nas plantillas</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<!-- Bootstrap Icons -->
2<button class="btn btn-primary">
3  <i class="bi bi-cloud-download"></i> Descargar
4</button>
5
6<!-- Font Awesome -->
7<button class="btn btn-danger">
8  <i class="fa-solid fa-trash"></i> Eliminar
9</button>
```

</div>

</div>

</div>

<a id="detalle-22-12"></a>

### Google Fonts

Para engadir tipografías:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">
```

</div>

En o teu CSS propio:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="css">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">css</span>

<div class="flex items-center gap-3">

</div>

</div>

```css
body {
    font-family: 'Roboto', sans-serif;
}
```

</div>

<a id="seccion-23"></a>

## Uso de url_for

En unha aplicación Flask, **`url_for`** é a forma recomendada de xerar **ligazóns internas** de maneira dinámica.

En vez de escribir a URL «a man», indica o **nome da función vista** e Flask constrúe a ruta correcta.

<a id="detalle-23-01"></a>

#### Ventajas de usar `url_for`

- Evita ligazóns rotas: se cambía a ruta en @app.route, as plantillas non precisan cambios.
- Admite parámetros dinámicos: permite pasar argumentos para crear URLs con variables.
- Funciona igual en Python e en plantillas Jinja2.

<a id="detalle-23-02"></a>

### Uso de url_for en as plantillas

<a id="detalle-23-03"></a>

#### En as vistas

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask, url_for
2app = Flask(__name__)
3
4@app.route('/')
5def index():
6    return 'Inicio'
7
8@app.route('/usuario/<nombre>/')
9def usuario(nombre):
10    return f"Hola {nombre}!"
11
12with app.test_request_context():
13    print(url_for('index'))              #  /
14    print(url_for('usuario', nombre='Ana'))  # /usuario/Ana/
```

</div>

<a id="detalle-23-04"></a>

#### En as plantillas

Dentro dunha plantilla Jinja2, a sintaxe é idéntica:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<a href="{{ url_for('index') }}">Inicio</a>
<a href="{{ url_for('usuario', nombre='Ana') }}">Saludar a Ana</a>
```

</div>

- `index` e `usuario` son **nomes das funcións vista**, non as rutas.
- Flask xerarará automaticamente as URLs correctas.

<a id="detalle-23-05"></a>

#### Parámetros dinámicos

Se a ruta definida na vista inclúe variables, pasa como argumentos con nome:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/producto/<int:id>/')
def producto(id):
    # ...
    pass
```

</div>

En a plantilla:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<a href="{{ url_for('producto', id=42) }}">Ver producto 42</a>
```

</div>

Resultado en o HTML:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<a href="/producto/42/">Ver producto 42</a>
```

</div>

<a id="detalle-23-06"></a>

#### Con query strings

A diferenza dos parámetros de *path* anteriores que identifican recursos específicos de forma obrigatoria, **formando parte integral da URL** para localizar un recurso. Os parámetros de *query* son información adicional, opcional e separada da ruta, usados para filtrar, ordenar ou paginar os resultados e non son parte do nome do recurso.

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">Path vs Query</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

Flask sabe distinguir entre meter un parámetro no *path* en vez de na *query* porque os *path params* están definidos explícitamente no decorador da ruta, polo que o resto convertese automaticamente en *query params*.

</div>

</div>

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<a href="{{ url_for('buscar', q='flask', page=2) }}">Buscar Flask</a>
```

</div>

Genera:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
/buscar?q=flask&page=2
```

</div>

E no código python podemos facer o seguinte:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/buscar/')
def buscar():
    q = request.args.get(q')
    page = request.args.get('page')
    ...
```

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-amber-50/60 dark:bg-amber-950/20 border-amber-200 dark:border-amber-900/60" hint="warning">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-amber-200 dark:border-amber-900/60 bg-amber-100/60 dark:bg-amber-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">Cando usar cada un...</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

- Usa parámetros de path cando o parámetro é esencial para identificar o recurso, como en `/usuarios/un_id`.
- Usa parámetros de query para información adicional que non é parte da identidade do recurso, como filtros (`?ciudad=Madrid`) ou paginación (`?pagina=2`).

</div>

</div>

Cando usar cada un

- Usa parámetros de path cando o parámetro é esencial para identificar o recurso, como en `/usuarios/un_id`.
- Usa parámetros de query para información adicional que non é parte da identidade do recurso, como filtros (`?ciudad=Madrid`) ou paginación (`?pagina=2`).

<a id="detalle-23-07"></a>

### Uso en recursos estáticos

`url_for` é moi útil para acceder a ficheiros da carpeta `static/`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/estilo.css') }}">
<script src="{{ url_for('static', filename='js/app.js') }}"></script>
<img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo">
```

</div>

- filename é a ruta relativa dentro de static.

<a id="detalle-23-08"></a>

### Exemplo completo

Vista:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route('/')
2def inicio():
3    return render_template('inicio.html')
4
5@app.route('/usuario')
6def usuario():
7    name = request.args.get('nombre')
8    return render_template('usuario.html', name=name)
```

</div>

Plantilla `inicio.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<!DOCTYPE html>
2<html lang="es">
3<head>
4  <meta charset="UTF-8">
5  <title>Ejemplo url_for</title>
6  <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
7</head>
8<body>
9  <nav>
10    <a href="{{ url_for('inicio') }}">Inicio</a>
11    <a href="{{ url_for('usuario', nombre='Carlos') }}">Usuario</a>
12  </nav>
13</body>
14</html>
```

</div>

<a id="seccion-24"></a>

## Cargar inicial de datos

En moitas **aplicacións web** necesitamos manexar datos que non cambian con cada petición: unha lista de produtos, unha configuración, etc... (Sempre e cando non sexa necesario empregar unha BBDD)

Se gardamos esa información nun arquivo JSON, a forma máis eficiente de traballar con ela é **ler** o arquivo **unha soa vez**, ao arrancar a aplicación, e manter os datos en memoria. Así non teremos que abrir e procesar o arquivo en cada visita do usuario, o que aforra tempo e recursos.

<a id="detalle-24-01"></a>

#### Estructura de proxecto

Normalmente, este tipo de datos estáticos incluímos nunha carpeta denominada *data.* Quedando de la seguinte forma unha posible estrutura da aplicación.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
├─ venv
├─ requirements.txt
├─ app
    └─ main.py
    └─ templates/  
├─ data/
    └─ data.json
```

</div>

<a id="detalle-24-02"></a>

#### Cargar os datos ao inicio

A idea é **ler** o arquivo **unha soa** vez cando Flask **arranca**.

Podemos facelo ao comezo de `main.py`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="flex items-center gap-2 min-w-0"><span class="text-xs font-mono font-semibold truncate" code-title="" style="color: var(--color-book);">main.py</span><span class="shrink-0 text-[0.65rem] font-mono uppercase tracking-wide text-gray-400 dark:text-gray-500">python</span></span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask
2import json
3from pathlib import Path
4
5app = Flask(__name__)
6
7# Leemos o JSON unha soa vez ao iniciar a aplicación
8with open(Path("data/data.json"), "r", encoding="utf-8") as f:
9    DATA = json.load(f)
```

</div>

Neste momento:

- DATA é unha variable global formada de estruturas de datos en Python (list, dicts...).
- A lectura execútase cando se importa `main.py`, é dicir, unha vez ao arrancar o servidor.
- Cada petición que chegue poderá acceder a esta variable directamente, sen volver a abrir o arquivo.

<a id="detalle-24-03"></a>

#### Uso dos datos nas vistas

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="flex items-center gap-2 min-w-0"><span class="text-xs font-mono font-semibold truncate" code-title="" style="color: var(--color-book);">main.py</span><span class="shrink-0 text-[0.65rem] font-mono uppercase tracking-wide text-gray-400 dark:text-gray-500">python</span></span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import jsonify
2
3# Carga de datos do ficheiro
4...
5
6@app.route("/")
7def home():
8    return jsonify(DATA)
```

</div>

<a id="detalle-24-04"></a>

#### Gardar en app.config

En vez de declarar unha variable global onde almacenamos o que haxa no noso ficheiro json de datos, podemos manter os datos dentro da configuración da aplicación da seguinte forma:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
with open("data/data.json", encoding="utf-8") as f:
    app.config["data"] = json.load(f)
```

</div>

E nas vistas podemos acceder a eses datos tal que así:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import current_app
2
3# Carga de datos do ficheiro
4...
5
6@app.route("/")
7def home():
8    datos = current_app.config["data"]
9    ...
```

</div>

Nota: Non se traduciron os nomes de variables, funcións e similares, así como as URLs e a estrutura Markdown, como se solicitou.

<a id="seccion-25"></a>

## Plantillas - Jinja II

<a id="detalle-25-01"></a>

### Que é Jinja2?

**Jinja2** é o motor de plantillas que utiliza **Flask** para xerar **HTML dinámico**.

> Cando instalamos Flask, Jinja2 se instala automaticamente como dependencia.

Documentación oficial: <a href="https://jinja.palletsprojects.com" rel="noopener noreferrer" target="_blank">https://jinja.palletsprojects.com</a>

Idea clave: Unha plantilla Jinja é un arquivo HTML cunha sintaxe especial que permite:

- Inserir variables.
- Executar bucles e condicións.
- Reutilizar estruturas mediante herdanza.

<a id="seccion-26"></a>

### Herencia

A **herencia** **de** **plantillas** é unha das características máis potentes de Jinja2.

Permite definir unha estrutura base común (cabeceira, menús, pé de páxina, etc.) e que as demais plantillas “hereden” dela, **sobrescribindo** só as partes que cambian.

<a id="detalle-26-01"></a>

#### Ventajas principais

- Reutilización: evitas repetir o mesmo HTML (header, footer, scripts).
- Mantenimiento: actualizas o deseño nun só ficheiro e se reflicte en todas as páxinas.
- Consistencia: todas as páxinas comparten o mesmo estilo e estrutura.

<a id="detalle-26-02"></a>

### Estructura de carpetas

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
mi_proyecto/
├─ app.py
└─ templates/
   ├─ base.html
   ├─ index.html
   ├─ contacto.html
   └─ ...
```

</div>

- `base.html` → Plantilla madre con o esqueleto xeral do sitio.
- As demais (index, contacto, etc.) → Plantillas fillas que herdan de `base.html`.

<a id="detalle-26-03"></a>

### Creación da plantilla base

Exemplo de `base.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<!DOCTYPE html>
2<html lang="es">
3<head>
4  <meta charset="utf-8">
5  <title>{% block title %}Mi sitio{% endblock %}</title>
6  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
7</head>
8<body>
9  <header>
10    <h1>Mi sitio web</h1>
11    <nav>
12      <a href="{{ url_for('index') }}">Inicio</a>
13      <a href="{{ url_for('contacto') }}">Contacto</a>
14    </nav>
15  </header>
16
17  <main>
18    {% block content %}{% endblock %}
19  </main>
20
21  <footer>
22    &copy; 2025 – Mi sitio
23  </footer>
24</body>
25</html>
```

</div>

- `{% block nombre %}{% endblock %}`

  Define un bloque que as plantillas fillas poden sobrescribir.

- Aquí creamos os bloques `title` e `content`.

<a id="detalle-26-04"></a>

#### Plantillas fillas

Unha plantilla filla estende da base con `{% extends "base.html" %}` e define o seu contido nos bloques:

Plantilla: `index.html`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1{% extends "base.html" %}
2
3{% block title %}Inicio{% endblock %}
4
5{% block content %}
6  <h2>Página principal</h2>
7  <p>Bienvenido a mi web con Flask y Jinja2.</p>
8{% endblock %}
```

</div>

Plantilla: `contacto.html`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1{% extends "base.html" %}
2
3{% block title %}Contacto{% endblock %}
4
5{% block content %}
6  <h2>Contáctanos</h2>
7  <form>
8    <!-- formulario -->
9  </form>
10{% endblock %}
```

</div>

<a id="detalle-26-05"></a>

#### Vista en Flask

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask, render_template
2app = Flask(__name__)
3
4@app.route('/')
5def index():
6    return render_template('index.html')
7
8@app.route('/contacto/')
9def contacto():
10    return render_template('contacto.html')
```

</div>

Cando o usuario visita `/`, Flask:

1.  Carga `index.html`.
2.  Inserta o contido dos seus bloques en `base.html`.
3.  Devuelve o HTML final ao navegador.

<a id="detalle-26-06"></a>

### Bloques anidados e extra

Pódense ter varios bloques: scripts, estilos, sidebar, etc.

Na filla podes:

- Sobrescribir completamente o bloque.
- Extenderlo coa variable `{{ super() }}` para manter o contido orixinal e engadir máis.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% block scripts %}
  {{ super() }}
  <script src="{{ url_for('static', filename='js/pagina.js') }}"></script>
{% endblock %}
```

</div>

<a id="detalle-26-07"></a>

### Herencia múltiple e anidada

Unha plantilla filla pode ser a súa vez base de outras, creando varios niveis de herencia:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
base.html
└─ dashboard_base.html
    ├─ usuarios.html
    └─ productos.html
```

</div>

<a id="seccion-27"></a>

### Condiciones

As condicións permiten que unha plantilla muestre ou oculte contido segundo o valor dunha variable ou o resultado dunha **expresión lóxica**.

A sintaxe é moi semellante á de Python, pero usando as etiquetas de **Jinja2**:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1{% if condicion %}
2    <!-- contido se a condición é verdadeira -->
3{% elif outra_condicion %}
4    <!-- contido alternativo -->
5{% else %}
6    <!-- contido se nada anterior se cumpra -->
7{% endif %}
```

</div>

<a id="detalle-27-01"></a>

### Uso básico

Exemplo na vista Flask:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/usuario/<nome>/')
def usuario(nome):
    return render_template('condicional.html', nome=nome)
```

</div>

Plantilla `condicional.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% if nome %}
    <h1>Ola, {{ nome }}!</h1>
{% else %}
    <h1>Ola, visitante anónimo</h1>
{% endif %}
```

</div>

> Se a URL é /usuario/Ana → Ola, Ana!
>
> Se non se pasa nome (ou é unha cadea baleira) → Ola, visitante anónimo.

<a id="detalle-27-02"></a>

### Comparacións e operadores lóxicos

| Operador  | Significado                     | Exemplo                        |
|-----------|---------------------------------|--------------------------------|
| `==`      | Igual a                         | `{% if idade == 18 %}`         |
| `!=`      | Diferente de                    | `{% if cor != 'vermello' %}`   |
| `>` `<`   | Maior / menor que               | `{% if prezo > 100 %}`         |
| `>=` `<=` | Maior ou igual / Menor ou igual | `{% if cantidade >= 10 %}`     |
| `and`     | E lóxico                        | `{% if activo and premium %}`  |
| `or`      | Ou lóxico                       | `{% if admin or editor %}`     |
| `not`     | Negación                        | `{% if not usuario %}`         |
| `in`      | Pertence a colección            | `{% if 'vermello' in cores %}` |

<a id="detalle-27-03"></a>

### Verificar existencia de variables

Se a variable non existe ou é **None**, a condición considérase falsa:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% if pais %}
   País: {{ pais }}
{% else %}
   País non especificado
{% endif %}
```

</div>

Podemos combinalo co filtro `default`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<p>País: {{ pais | default('Descoñecido') }}</p>
```

</div>

<a id="detalle-27-04"></a>

### Probas (tests) de Jinja2

| Proba                   | Uso                                |
|-------------------------|------------------------------------|
| `defined` / `undefined` | `{% if variable is defined %}`     |
| `none`                  | `{% if variable is none %}`        |
| `odd` / `even`          | `{% if numero is even %}`          |
| `divisibleby(n)`        | `{% if numero is divisibleby 3 %}` |
| `string` / `number`     | `{% if dato is string %}`          |
| `sequence`              | `{% if lista is sequence %}`       |

Exemplo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% if idade is divisibleby 2 %}
    <p>A idade é par</p>
{% else %}
    <p>A idade é impar</p>
{% endif %}
```

</div>

<a id="detalle-27-05"></a>

### Exemplo completo

Vista:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route('/produtos/')
2def produtos():
3    items = [
4        {"nome": "Portátil", "prezo": 800},
5        {"nome": "Ratón", "prezo": 20},
6        {"nome": "Teclado", "prezo": 35}
7    ]
8    return render_template('produtos.html', produtos=items, oferta=True)
```

</div>

Plantilla `produtos.html`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<h1>Lista de produtos</h1>
2<ul>
3  {% for p in produtos %}
4    <li>
5      {{ p.nome }} - {{ p.prezo }} €
6      {% if p.prezo > 100 %}
7          <strong>(Caro)</strong>
8      {% else %}
9          (Económico)
10      {% endif %}
11    </li>
12  {% endfor %}
13</ul>
14
15{% if oferta %}
16    <p>¡Hoxe todos os produtos teñen un 10% de descuento!</p>
17{% endif %}
```

</div>

<a id="seccion-28"></a>

### Bucles

En Jinja2 podemos recorrer **listas**, **tuplas**, **diccionarios** e **outros iterables** utilizando a sentencia de control `{% for ... %}`.

Isto permite xerar HTML repetitivo de forma dinámica: táboas, listas de elementos, menús, etc.

<a id="detalle-28-01"></a>

### Sintaxe básica

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% for elemento in coleccion %}
   {{ elemento }}
{% endfor %}
```

</div>

- ***elemento*** é a variable de iteración.
- ***colección*** é unha lista, tupla, conxunto, diccionario ou obxecto iterable que tes pasado á plantilla.

Ejemplo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/colores/')
def colores():
    lista = ["rojo", "verde", "azul"]
    return render_template("colores.html", colores=lista)
```

</div>

Plantilla `colores.html`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<ul>
  {% for color in colores %}
    <li>{{ color }}</li>
  {% endfor %}
</ul>
```

</div>

Saída:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<ul>
  <li>rojo</li>
  <li>verde</li>
  <li>azul</li>
</ul>
```

</div>

<a id="detalle-28-02"></a>

### Variables especiais do bucle

Dentro de un bucle Jinja, a variable implícita loop proporciona información útil:

| Variable          | Significado                                           |
|-------------------|-------------------------------------------------------|
| `loop.index`      | Iteración actual (comeza en 1).                       |
| `loop.index0`     | Iteración actual (comeza en 0).                       |
| `loop.first`      | True na primeira iteración.                           |
| `loop.last`       | True na última iteración.                             |
| `loop.length`     | Número total de elementos da colección.               |
| `loop.revindex`   | Nº de elementos restantes (comeza en 1 ao final).     |
| `loop.revindex0`  | Igual ao anterior pero comezando en 0.                |
| `loop.cycle(a,b)` | Alterna valores en cada iteración (ideal para filas). |

Ejemplo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<ul>
2  {% for color in colores %}
3    <li>{{ loop.index }} - {{ color }}
4        {% if loop.first %}(primer elemento){% endif %}
5    </li>
6  {% endfor %}
7</ul>
```

</div>

<a id="detalle-28-03"></a>

### Control de espazos e saltos de liña

Para evitar que se xeren liñas en branco indeseadas, se pode engadir un guión `(-)`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{% for elem in lista -%}
   <li>{{ elem }}</li>
{%- endfor %}
```

</div>

> O guión suprime o salto de liña que normalmente engade Jinja2.

<a id="detalle-28-04"></a>

### Bucles anidados

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<ul>
2  {% for fila in matriz %}
3    <li>
4      {% for celda in fila %}
5        [{{ celda }}]
6      {% endfor %}
7    </li>
8  {% endfor %}
9</ul>
```

</div>

<a id="detalle-28-05"></a>

### Recorrer diccionarios

Cando a colección é un diccionario, podes acceder a **chaves** e **valores**:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route('/usuarios/')
def usuarios():
    data = {"Ana": 25, "Luis": 30}
    return render_template("usuarios.html", usuarios=data)
```

</div>

Plantilla:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<ul>
  {% for nombre, edad in usuarios.items() %}
    <li>{{ nombre }}: {{ edad }} anos</li>
  {% endfor %}
</ul>
```

</div>

<a id="detalle-28-06"></a>

### Uso de filtros dentro do bucle

Podes aplicar filtros mentres iteras:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<ul>
  {% for nombre in nombres|sort %}
    <li>{{ nombre|capitalize }}</li>
  {% endfor %}
</ul>
```

</div>

<a id="detalle-28-07"></a>

### Romper ou continuar o bucle

Jinja2 ofrece break e continue (desde versións recentes):

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1{% for n in numeros %}
2    {% if n == 0 %}
3        {% continue %}
4    {% endif %}
5    {% if n > 10 %}
6        {% break %}
7    {% endif %}
8    <p>{{ n }}</p>
9{% endfor %}
```

</div>

<a id="detalle-28-08"></a>

### Condicionais dentro de bucles

Pódese combinar if con for para filtrar datos:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<ul>
2  {% for n in numeros %}
3    {% if n > 5 %}
4       <li>{{ n }}</li>
5    {% endif %}
6  {% endfor %}
7</ul>
```

</div>

<a id="detalle-28-09"></a>

### Exemplo completo

Vista:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route('/productos/')
2def productos():
3    items = [
4        {"nombre": "Portátil", "precio": 800},
5        {"nombre": "Ratón", "precio": 20},
6        {"nombre": "Teclado", "precio": 35}
7    ]
8    return render_template("productos.html", productos=items)
```

</div>

Plantilla `productos.html`

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1<table border="1">
2  <tr><th>#</th><th>Producto</th><th>Precio</th></tr>
3  {% for p in productos %}
4    <tr class="{{ loop.cycle('fila-par','fila-impar') }}">
5      <td>{{ loop.index }}</td>
6      <td>{{ p.nombre }}</td>
7      <td>{{ p.precio }} €</td>
8    </tr>
9  {% endfor %}
10</table>
```

</div>

<a id="seccion-29"></a>

### Comentarios

Os comentarios serven para **anotar** ou **explicar o código** da plantilla sen que esas notas aparezan no HTML final que recibe o navegador.

Son moi útiles para:

- Documentar partes complexas da plantilla.
- Deixar recordatorios ou instrucións para outros desenvolvedores.
- Desactivar temporalmente fragmentos de código sen borralos.

<a id="detalle-29-01"></a>

### Sintaxe

A sintaxe de comentario en Jinja2 é:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{#  Este es un comentario  #}
```

</div>

- Todo o que estea entre {# e \#} ignórase completamente ao renderizar a plantilla.
- O comentario non se envía ao cliente nin aparece no HTML final.

Exemplo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{# Aquí mostramos el nombre del usuario #}
<p>Bienvenido, {{ usuario }}</p>
```

</div>

No navegador só verás:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<div class="flex items-center gap-3">

</div>

</div>

```text
<p>Bienvenido, Ana</p>
```

</div>

<a id="detalle-29-02"></a>

### Comentarios de varias liñas

Pódense escribir comentarios longos en varias liñas:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
1{#
2  Este bloque de HTML muestra
3  la lista de productos disponibles.
4  Se actualiza automáticamente.
5#}
6<ul>
7  {% for p in productos %}
8    <li>{{ p }}</li>
9  {% endfor %}
10</ul>
```

</div>

<a id="detalle-29-03"></a>

### Desactivar temporalmente código

Pódense comentar fragmentos de código Jinja2 para probas:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
{#
{% if usuario %}
  <p>Hola, {{ usuario }}</p>
{% endif %}
#}
```

</div>

<a id="seccion-30"></a>

## Formularios

Un formulario HTML é a forma máis común de recoller información do usuario nunha páxina web: nome, contrasinal, comentarios, arquivos…

A estrutura básica é:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<form method="POST" action="/procesar">
2  <label for="nome">Nome:</label>
3  <input id="nome" name="nome" type="text">
4
5  <label for="idade">Idade:</label>
6  <input id="idade" name="idade" type="number">
7
8  <button type="submit">Enviar</button>
9</form>
```

</div>

<a id="detalle-30-01"></a>

#### Elementos clave

- \<form\>: o contedor principal.
  - method → determina como se envían os datos:
    - GET: engade os datos á URL. Útil en búsquedas.
    - POST: manda os datos no corpo da petición. Máis usado en formularios de login, rexistro, etc.
  - action → a ruta do servidor que recibirá a información (en Flask será unha función).
- Campos:
  - \<input\>: para datos de texto, números, contrasinais, emails, etc.
  - \<textarea\>: para textos largos (comentarios).
  - \<select\>: listas desplegables.
  - \<button type="submit"\>: botón que envía o formulario.
- Atributos importantes:
  - name: a clave coa que o servidor recibirá o valor.
  - required: fai que o campo sexa obrigatorio.
  - type: define o tipo de dato (text, password, number, email, etc.).

<a id="detalle-30-02"></a>

#### Exemplo con validación simple en HTML5

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<form method="POST" action="/rexistro">
2  <label for="email">Correo:</label>
3  <input id="email" name="email" type="email" required>
4
5  <label for="contrasinal">Contrasinal:</label>
6  <input id="contrasinal" name="contrasinal" type="password" required minlength="6">
7
8  <button type="submit">Rexistrarse</button>
9</form>
```

</div>

Neste caso:

- O navegador pedirá que o campo email teña un formato válido.
- O contrasinal debe ter mínimo 6 caracteres.

<a id="seccion-31"></a>

### Formularios en Flask

Flask nos permite recibir os datos que o usuario introduce nun formulario. Para ello usamos o obxecto request.

<a id="detalle-31-01"></a>

#### Flujo básico

1.  Creamos unha ruta que mostra o formulario (cunha plantilla HTML).
2.  Creamos outra ruta que recibe os datos cando o usuario pulsa “Enviar”.

Ejemplo en `main.py`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1from flask import Flask, render_template, request
2
3app = Flask(__name__)
4
5@app.route("/formulario")
6def formulario():
7    return render_template("formulario.html")
8
9@app.route("/procesar", methods=["POST"])
10def procesar():
11    nome = request.form["nome"]
12    idade = request.form["idade"]
13    return f"Hola {nome}, tes {idade} anos"
```

</div>

- `@app.route("/formulario")`: mostra a páxina co formulario.
- `@app.route("/procesar", methods=["POST"])`: define a ruta que recibirá a información.
- `request.form["nome"]`: accede ao valor do campo name="nome" do formulario.
- `request.form` é como un diccionario con todos os datos enviados mediante POST.

<a id="detalle-31-02"></a>

#### Plantilla templates/formulario.html

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<!DOCTYPE html>
2<html lang="gl">
3<head>
4  <meta charset="UTF-8">
5  <title>Formulario</title>
6</head>
7<body>
8  <h1>Introduce os teus datos</h1>
9  <form method="POST" action="/procesar">
10    <label for="nome">Nome:</label>
11    <input id="nome" name="nome" type="text" required>
12
13    <label for="idade">Idade:</label>
14    <input id="idade" name="idade" type="number" required>
15
16    <button type="submit">Enviar</button>
17  </form>
18</body>
19</html>
```

</div>

<a id="detalle-31-03"></a>

#### Listas de valores (checkboxes)

Cando hai varias casillas co mesmo nome, Flask devuelve unha lista:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<form method="POST" action="/procesar">
2  <p>Linguas favoritas:</p>
3  <label><input type="checkbox" name="linguas" value="Python"> Python</label>
4  <label><input type="checkbox" name="linguas" value="Java"> Java</label>
5  <label><input type="checkbox" name="linguas" value="C#"> C#</label>
6  <button type="submit">Enviar</button>
7</form>
```

</div>

En Flask:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route("/procesar", methods=["POST"])
def procesar():
    linguas = request.form.getlist("linguas")
    return f"Os teus linguas favoritos son: {', '.join(linguas)}"
```

</div>

<a id="detalle-31-04"></a>

#### Datos con GET

Se o formulario usa method="GET", os valores chegan na URL:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="/procesar?nome=Ana&amp;idade=20">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
/procesar?nome=Ana&idade=20
```

</div>

E accedemos con `request.args`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
@app.route("/procesar", methods=["GET"])
def procesar_get():
    nome = request.args.get("nome")
    idade = request.args.get("idade")
    return f"Hola {nome}, tes {idade} anos"
```

</div>

<a id="seccion-32"></a>

### Validación no servidor

Aunque o navegador pode facer validacións básicas con **HTML5** (ex. required, type="email", min, max…), non basta con iso.

O usuario **pode desactivar** **JavaScript** ou enviar peticións falsas. Por iso sempre **debemos comprobar os datos no servidor**.

<a id="detalle-32-01"></a>

#### Comprobar campos baleiros

Exemplo: un formulario de rexistro pide nome e idade.

En Flask, comprobamos antes de usalos:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route("/procesar", methods=["POST"])
2def procesar():
3    nome = request.form.get("nome", "").strip()
4    idade = request.form.get("idade", "")
5
6    if not nome:
7        return "O nome é obrigatorio", 400
8    if not idade:
9        return "A idade é obrigatoria", 400
10
11    return f"Rexistro correcto: {nome} ({idade} anos)"
```

</div>

<a id="detalle-32-02"></a>

#### Validar tipo de dato

Por exemplo, asegurarnos de que idade sexa un número enteiro:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="if not idade.isdigit():
    return &quot;A idade debe ser un número&quot;, 400

idade = int(idade)
if idade &lt; 0 or idade &gt; 120:
    return &quot;A idade non é válida&quot;, 400">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1if not idade.isdigit():
2    return "A idade debe ser un número", 400
3
4idade = int(idade)
5if idade < 0 or idade > 120:
6    return "A idade non é válida", 400
```

</div>

<a id="detalle-32-03"></a>

#### Validar con regras propias

Outros casos comúns:

- Emails: que contengan @.
- Contraseñas: mínimo de caracteres.
- Seleccións: que o valor enviado esté nunha lista permitida.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="rol = request.form.get(&quot;rol&quot;, &quot;&quot;)
if rol not in roles_permitidos:
    return &quot;O rol non é válido&quot;, 400">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
rol = request.form.get("rol", "")
if rol not in roles_permitidos:
    return "O rol non é válido", 400
```

</div>

<a id="detalle-32-04"></a>

#### Devolver mensaxes claros

En lugar de mostrar un simple “erro”, convén indicar cal é o campo que fallou para que o usuario poida corrixilo.

Exemplo de resposta con varios erros:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="erros = []
if not nome:
    erros.append(&quot;O nome é obrigatorio&quot;)
if not idade.isdigit():
    erros.append(&quot;A idade debe ser un número&quot;)

if erros:
    return &quot;&lt;br&gt;&quot;.join(erros), 400">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1erros = []
2if not nome:
3    erros.append("O nome é obrigatorio")
4if not idade.isdigit():
5    erros.append("A idade debe ser un número")
6
7if erros:
8    return "<br>".join(erros), 400
```

</div>

<a id="seccion-33"></a>

### Erros nas plantillas

Cando traballamos con formularios en Flask, o habitual é que o usuario poida cometer erros ao enviar datos: campos baleiros, formatos incorrectos, valores fóra de rango, etc.

En lugar de mostrar un mensaje xenérico, é máis útil **manter a mesma vista** e **amosar os erros** xusto debaixo do formulario ou de cada campo.

Por defecto, se devolvemos unha cadea cun erro, o navegador só mostrará ese texto plano:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python" runnable="" source="return &quot;O nome é obrigatorio&quot;, 400">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
return "O nome é obrigatorio", 400
```

</div>

<a id="detalle-33-01"></a>

### Volver a renderizar a plantilla

O fluxo sería:

- Validamos os datos no servidor.
- Se hai erros, volvemos a renderizar a mesma plantilla pasando a mensaxe de erro como unha variable (ao igual que calquera outra).
- Así, a plantilla pode amosar o erro sen perder os datos introducidos.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1@app.route("/login", methods=["POST"])
2def login():
3    error = None
4    name = ""
5    password = ""
6
7    if request.method == "POST":
8        name = request.form.get("name", "").strip()
9        password = request.form.get("password", "")
10
11        if not name:
12            error = "O nome é obrigatorio"
13        elif password != 1234: # Para este exemplo, só consideramos válida a password: 1234 
14            error = "Credenciais incorrectas"
15
16        if error:
17            # Volvemos ao formulario co erro
18            return render_template("login.html", error=error, name=name, password=password)
19
20        # Se todo vai ben → rediriximos a outra ruta
21        return redirect(url_for("pagina_principal", name=name))
22
23    return render_template("login.html")
```

</div>

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
1<form method="POST">
2  <label>Nome:</label><br>
3  <input type="text" name="name" value="{{ nome or '' }}"><br>
4  
5  <label>Contraseña:</label><br>
6  <input type="password" name="password" value="{{ password or '' }}"><br>
7  
8  {% if error %}
9    <p class="error">{{ error }}</p>
10  {% endif %}
11  
12  <button type="submit">Enviar</button>
13</form>
```

</div>

<a id="seccion-34"></a>

### Seguridade

Cando traballamos con formularios en aplicacións web non basta que funcionen: tamén hai que **pensar na seguridade**.

<a id="detalle-34-01"></a>

#### Escape de datos

Todo o que o usuario escribe nun formulario podería conter código malicioso (exemplo: `<script>alert("hola")</script>`).

Para evitar que eso se execute na nosa páxina, Flask/Jinja escapan automaticamente o contido das variables para evitar calquera posible ataque.

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="django">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">django</span>

<div class="flex items-center gap-3">

</div>

</div>

```django
<p>{{ comentario }}</p>
```

</div>

Na páxina verase tal cual como texto, **non se execute**.

------------------------------------------------------------------------

<a id="detalle-34-02"></a>

#### CSRF (Cross-Site Request Forgery)

É un ataque no que outra web tenta enganar ao usuario para que envíe un formulario á nosa aplicación sen darse conta.

A defensa básica é usar un **token oculto** no formulario que só o noso servidor coñece.

En proxectos reais se usa a librería **Flask-WTF**, que engade automaticamente ese token de seguridade.

------------------------------------------------------------------------

<a id="detalle-34-03"></a>

#### Validar sempre no servidor

Non confiar só nas validacións de HTML ou JavaScript. O navegador pode saltarlas, pero o **servidor sempre debe comprobar que os datos son correctos**.

------------------------------------------------------------------------

<a id="detalle-34-04"></a>

#### Subida de arquivos

Se o formulario permite subir ficheiros (`<input type="file">`):

- Comprobar a extensión (exemplo: só .jpg, .png, .pdf).
- Poner un límite de tamaño para evitar abusos.
- Gardalos nunha carpeta controlada, nunca en calquera parte do proxecto.

<a id="seccion-35"></a>

### Subida de arquivos

Moitas veces un formulario non só recolle texto, senón tamén arquivos (exemplo: foto de perfil, documento PDF…). Flask permite facelo de forma sinxela.

<a id="detalle-35-01"></a>

#### Formulario en HTML

Para subir arquivos hai que engadir un atributo especial en `<form>`:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="html">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">html</span>

<div class="flex items-center gap-3">

</div>

</div>

```html
<form method="POST" action="/subir" enctype="multipart/form-data">
  <label for="arquivo">Selecciona un arquivo:</label>
  <input id="arquivo" type="file" name="arquivo" required>
  <button type="submit">Subir</button>
</form>
```

</div>

- enctype="multipart/form-data" → obrigatorio para que o navegador envíe o arquivo.
- type="file" → mostra o selector de ficheiros.
- name="arquivo" → será a clave que usaremos en Flask.

<a id="detalle-35-02"></a>

#### Recibir arquivo en Flask

Na ruta usamos `request.files` para acceder ao arquivo:

<div class="not-prose group relative my-4 rounded-lg overflow-hidden border border-gray-200 dark:border-gray-700 text-sm" code-block="" data-language="python">

<div class="flex items-center justify-between px-4 py-2 border-b border-black/10 dark:border-white/10" style="background-color: var(--color-book-bg);">

<span class="text-xs font-mono font-semibold" style="color: var(--color-book);">python</span>

<div class="flex items-center gap-3">

</div>

</div>

```python
1import os
2from flask import Flask, request
3
4app = Flask(__name__)
5
6@app.route("/subir", methods=["POST"])
7def subir():
8    arquivo = request.files["arquivo"]
9    if arquivo.filename == "":
10        return "Non seleccionaches ningún arquivo", 400
11
12    ruta = os.path.join("uploads", arquivo.filename)
13    arquivo.save(ruta)
14
15    return f"Arquivo {arquivo.filename} subido con éxito"
```

</div>

<div class="not-prose my-5 rounded-xl border overflow-hidden bg-green-50/60 dark:bg-green-950/20 border-green-200 dark:border-green-900/60" hint="success">

<div class="flex items-center gap-2.5 px-4 py-2.5 border-b border-green-200 dark:border-green-900/60 bg-green-100/60 dark:bg-green-900/20">

<span class="shrink-0 w-5 h-5"></span><span class="text-[0.95rem] font-semibold text-gray-800 dark:text-gray-100 leading-snug" hint-title="">**Limitar o tamaño dos arquivos**</span>

</div>

<div class="px-5 py-4 text-[0.95rem] leading-relaxed text-gray-700 dark:text-gray-300 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0 [&_p]:my-2 [&_ul]:my-2 [&_ul]:list-disc [&_ul]:pl-5 [&_ol]:my-2 [&_ol]:list-decimal [&_ol]:pl-5 [&_ul_ul]:list-[circle] [&_ul_ul]:my-1 [&_ol_ol]:my-1 [&_ul_ol]:my-1 [&_ol_ul]:my-1 [&_li]:my-1 [&_li]:pl-1 [&_li]:marker:text-gray-400 dark:[&_li]:marker:text-gray-500 [&_strong]:font-semibold [&_strong]:text-gray-900 dark:[&_strong]:text-gray-100 [&_em]:italic [&_a]:font-medium [&_a]:underline [&_a.not-prose]:no-underline [&_code]:bg-black/[0.07] dark:[&_code]:bg-white/10 [&_code]:px-1 [&_code]:py-0.5 [&_code]:rounded [&_code]:text-[0.85em] [&_code]:font-mono [&_code]:text-gray-800 dark:[&_code]:text-gray-200" hint-body="">

En Flask podemos limitar o tamaño máximo da seguinte forma

`app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024 # 5 MB`

</div>

</div>
