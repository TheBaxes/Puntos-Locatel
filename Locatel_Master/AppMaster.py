from flask import Flask
from flask import render_template
from flask import request
app= Flask(__name__)

@app.route("/")
def MasterLogin():
    return render_template('MasterLogin.html')

@app.route("/master")
def MasterVista():
    return render_template('MasterVista.html')    



if __name__ == "__main__":
    app.run(debug = True, port= 5001)    
