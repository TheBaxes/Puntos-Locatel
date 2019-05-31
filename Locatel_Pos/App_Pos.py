from flask import Flask
from flask import render_template
from flask import request
app= Flask(__name__)

@app.route("/")

def Consulta_venta_pos():
    return  render_template('VistaPos.html')


if __name__ == "__main__":
    app.run(debug = True ,port= 5000)    
