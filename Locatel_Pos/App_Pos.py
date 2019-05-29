from flask import Flask
from flask import render_template
from flask import request
app= Flask(__name__)

@app.route("/")


@app.route("/puntos")
def Consulta_venta_pos():
    return  'hola pos'


if __name__ == "__main__":
    app.run(debug = True ,port= 5000)    
