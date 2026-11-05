from flask import Flask, render_template, request
import os


#template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# template_dir = os.path.join (template_dir, 'src', 'templates')


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


@app.route("/admin/post/", methods = ['POST'])
def post_form( ):
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contraseña = request.form.get('contraseña')
    return render_template("new_post_form.html")

# @app.route("/admin/post/")
# @app.route("/admin/post/<int:post_id>/")
# def post_form(post_id=None):
#     return render_template("new_post_form.html", post_id=post_id)


if __name__ ==  "__main__":
    app.run (debug=True, port = 4000)