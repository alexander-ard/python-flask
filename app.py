
from flask import Flask, request, render_template, redirect, url_for
from models import registros
from models import persona

app = Flask(__name__)
registros.Registros()

@app.route("/")
def index(): 
    return render_template("lista.html", lista=registros.Registros.getPersonas()) 

@app.route("/crear/",  methods =["GET", "POST"])
def crear(): 
    if request.method == "POST": 
       nombre = request.form.get("nombre")  
       apellido = request.form.get("apellido")  
       edad = request.form.get("edad")  
       ciudad = request.form.get("ciudad")

       registros.Registros.crearPersona(persona.Persona(0, nombre, apellido, edad, ciudad));
       return redirect(url_for('index'))
    
    return render_template("persona.html") 
