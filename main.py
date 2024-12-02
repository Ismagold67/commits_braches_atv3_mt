from flask import Flask, render_template

app_isma = Flask(__name__)

@app_isma.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app_isma.route("/login")
def indice():
    return render_template("login.html")

@app_isma.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app_isma.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app_isma.run(debug=True)
