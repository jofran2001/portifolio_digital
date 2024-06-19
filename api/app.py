from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/experiencias.html")
def experiencias():
  return render_template("experiencias.html")

@app.route("/projetos.html")
def projetos():
  return render_template("projetos.html")

@app.route("/index.html")
def inicio():
  return render_template("index.html")
