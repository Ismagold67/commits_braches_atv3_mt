from flask import Flask, render_template

app_isma = Flask(__name__)

@app_isma.route("/index")
def indice():
    return render_template("index.html")

@app_isma.route("/contato")
def contato():
    return render_template("contato.html")

@app_isma.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})
def usuarios(nome_usuario, nome_profissao):
    dados_usu = {"profissao":nome_profissao, "disciplina":"Desenvolvimento WEB III"}
    return render_template("usuario.html", nome=nome_usuario, dados = dados_usu)

if __name__ == "__main__":
    app_isma.run()