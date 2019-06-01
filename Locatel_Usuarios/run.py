from flask import Flask
from flask import render_template
from flask import request
app= Flask(__name__)

@app.route("/")

def _Login_():
    return render_template('LoginUsuario.html')

@app.route("/puntos")
def PuntosLocatel():
    return  render_template('VistaCliente.html')

@app.route("/catalogo")
def CatalogoUsuario():
    return render_template('CatalogoProductos.html')

@app.route("/historial")
def HistorialCompras():
    return render_template('HistorialCompras.html')





if __name__ == "__main__":
    app.run(debug = True ,port= 5002)    