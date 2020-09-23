from flask import Flask

app = Flask(__name__)

@app.route("/")
def index(): 
    return "Index."

@app.route("/world/")
def world(): 
    return "Hello world."

@app.route("/hello/<name>")
def hello(name): 
    return f"Hola, {name}"