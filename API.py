# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
#Page ou endpoint racine de l'API 
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')