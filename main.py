from flask import Flask, render_template, request, redirect, flash

app_isma = Flask(__name__)
app_isma.config["SECRET_KEY"] = "key"

@app_isma.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get("password")
    
    if verificar_login(usuario, senha):
        return render_template("homepage.html", nome=usuario)
    else:
        flash("Dados inválidos", "danger")
        flash("Login ou senha incorretos. Acesso negado!", "danger")
        flash("Tente usuario: ismael01 senha: 123@Aavb")
        return redirect("/login")

@app_isma.route("/cadastrar", methods=["POST"])
def cadastrar():
    usuario = request.form.get('usuario')
    senha = request.form.get("password")
    
    if usuario and senha:
        return redirect("/login")
    else:
        flash("Dados inválidos", "danger")
        return redirect("/cadastro")
    
tabelaUsuario = {
    "ismael01": "123@Aavb",
    "ismael05": "1a2Aq932",
    "ismael97": "34ACa39@"
}

def verificar_login(login, senha):
    if login in tabelaUsuario and tabelaUsuario[login] == senha:
        return True
    else:
        return False

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

@app_isma.route("/contatos")
def contatos():
    return render_template("contatos.html")

if __name__ == "__main__":
    app_isma.run(debug=True)
