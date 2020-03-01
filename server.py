#!/bin/python3
from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("inicio.html")

@app.route('/analizar', methods=['POST'])
def analizar():
    f = request.files['file']
    rec = './temporales/'+f.filename
    f.save(rec)
    print(request.files)
    print(f.filename)
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
