#!/bin/python3
from flask import Flask, request, url_for, render_template
from utils import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("inicio.html",autor1 = {"nombre":"Walter","apellido":"Mendoza"},autor2 = {"nombre":"Byron","apellido":"Lopez"})

@app.route('/analizar', methods=['POST'])
def analizar():
    f = request.files['file']
    rec = './temporales/'+f.filename
    f.save(rec)

    params = request.form
    #Vamos a inicializar con los datos del form las variables que usa el algortirmo(variables en utils.py)
    #Tenemos que seleccionar el valor segun el criterio de finalizacion seleccionado
    valCriterioFinalizacion = params['valcriterio1'] if params['criterio'] == '1'else ''
    valCriterioFinalizacion = params['valcriterio2'] if params['criterio'] == '2'else valCriterioFinalizacion
    valCriterioFinalizacion = params['valcriterio3'] if params['criterio'] == '3'else valCriterioFinalizacion

    init(f.filename,params['criterio'],valCriterioFinalizacion,params['criteriop'])
    load_file()
    escribir_en_bitacora()
    print("-----------------")
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
