
import data_base
from flask import Flask, render_template, request
import os
import data_base
from importlib.metadata import version


print (f"Versión paquete data_base: {version("data_base")}")
#template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#template_dir = os.path.join (template_dir, 'src', 'templates')

# def main():
#     mysql_db = data_base.MySQLDatabase("root", "", "clase")
#     mysql_db.connect()

mysql_db = data_base.MySQLDatabase("root", "", "clase")
mysql_db.connect()

#'templates' es el nombre por defecto
app = Flask(__name__)
TITLE = "FLASK PROJECT"

@app.route('/')
def home():
    return render_template('home.html', main_title = TITLE)
    #return 'Hello, World!'

@app.route("/post/<string:slug>/")
def show_post(slug):
    return f"mostrar el post {slug}"


@app.route("/admin/crear_alumno/", methods = ['POST','GET'])
def post_form( ):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        #guardar datos
        alumno = data_base.Alumno(nombre, email)
        mysql_db.create(alumno)

    return render_template("new_post_form.html")


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

# @app.route("/admin/post/")
# @app.route("/admin/post/<int:post_id>/")
# def post_form(post_id=None):
#     return render_template("new_post_form.html", post_id=post_id)



if __name__ ==  "__main__":
    app.run (debug=True, port = 4000)
    