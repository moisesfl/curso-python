
import email

from click import Path
import data_base
from flask import Flask, json, render_template, request, flash, redirect, url_for
import os, json
import data_base
from importlib.metadata import version

#Constantes
path_cofig_file = ("../data/config.json")
path_app = os.path.dirname(os.path.abspath(__file__))



def read_json(path_file):
    try:
        with open((path_file), "r", encoding="utf-8") as f:
            DATA = json.load(f)
            return DATA
    except FileNotFoundError:
        print(f"File not found: {path_file}")
    except json.JSONDecodeError:
        print(f"Invalid JSON in file: {path_file}")
    return None


config_data = read_json(os.path.join(path_app, path_cofig_file))

print (config_data)



print (f"Versión paquete data_base: {version("data_base")}")
#template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#template_dir = os.path.join (template_dir, 'src', 'templates')

#Init database
mysql_db = data_base.MySQLDatabase("root", "", "clase")
mysql_db.connect()

#'templates' es el nombre por defecto
app = Flask(__name__)
TITLE = "FLASK PROJECT"

@app.route('/config/')
def return_string():
    return json.dumps(config_data)

@app.route('/')
def home():
    return render_template('home.html', main_title = TITLE)
    #return 'Hello, World!'

@app.route("/post/<string:slug>/")
def show_post(slug):
    return f"mostrar el post {slug}"

@app.route("/subir", methods=["GET", "POST"])
def subir():

    if request.method == "POST":

        arquivo = request.files.get("arquivo")

        if arquivo is None or arquivo.filename == "":
            return render_template(
                "subir.html",
                error="Non seleccionaches ningún arquivo"
            ), 400

        return "Arquivo recibido correctamente", 200

    return render_template("subir.html")


@app.route("/admin/crear_alumno/", methods = ['POST','GET'])
def post_form( ):
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        lenguas = request.form.getlist('lenguas')

        if not nombre:
            error = "Debes cubrir el campo del nombre."  
        else:
            #guardar datos
            alumno = data_base.Alumno(nombre, email)
            mysql_db.create(alumno)
        
            return f"Usuario {nombre} registrado correctamente."   



    return render_template("new_post_form.html", error = error)


@app.route("/admin/alumno_id/<int:slug_id>/")
def obtener_info_alumnos(slug_id):
    assert isinstance(slug_id, int), 'La variable debe ser un entero'

    # Consulta
    info_alumno = mysql_db.read(slug_id)
    
    mesaje = (
        f"Para el id {slug_id} la información es: {info_alumno}" 
        if info_alumno != None else f"No existe el alumno con el id {slug_id}" 
    )

    return mesaje


@app.route("/admin/eliminar_alumno/<int:slug_id>/")
def eliminar_alumno(slug_id):
    assert isinstance(slug_id, int), 'La variable debe ser un entero'

    #Consulta
    res = mysql_db.delete(slug_id)

    mesaje = (
        f"Eliminado alumnos con id {slug_id}" 
        if res != 0 else f"No existe el alumno con el id {slug_id}" 
    )

    return mesaje


# @app.route("/admin/post/")
# @app.route("/admin/post/<int:post_id>/")
# def post_form(post_id=None):
#     return render_template("new_post_form.html", post_id=post_id)

if __name__ ==  "__main__":
    app.run (debug=True, port = 4000)
    