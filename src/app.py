from flask import Flask, render_template
import os
from database import conectar, cerrar

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'template')

app = Flask(__name__, template_folder=template_dir)

# Rutas de la aplicación
@app.route('/')
def home():
    conexion = conectar()
        #hacer algo con la coneccion
    
    cerrar(conexion)

    return render_template("index.html")
    
    
if __name__ == '__main__':
    app.run(debug=True, port=4000)
