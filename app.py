from flask import Flask, render_template, url_for
app = Flask("__name__", static_folder="./static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contato")
def contato(): 
    return render_template("contato.html")

@app.route("/quem_somos")
def quem_somos():  
    return render_template("quem_somos.html")