from flask import Flask, render_template

app_isma = Flask(__name__)

@app_isma.route("/cadastro")
def homepage():
    return render_template("cadastro.html")

@app_isma.route("/login")
def indice():
    return render_template("login.html")

if __name__ == "__main__":
    app_isma.run(debug=True)
