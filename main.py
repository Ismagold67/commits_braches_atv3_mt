# Código da aula 01 e aula 04
from flask import Flask, render_template

app_isma = Flask (__name__, template_folder='templates')

# Feature código aula 02
def saudacoes(nome):
    return f'Olá, {nome}'

# Feature código aula 03
@app_isma.route('/rota1')
def rota1():
    return 'Olá Usuário!!'

@app_isma.route('/rota2')
def rota2():
    resposta = "<h3> Essa é outra página da rota 2 </h3>"
    return resposta

# Feature código aula 04
@app_isma.route("/")
def homepage():
    return render_template("homepage.html")

@app_isma.route("/contato")
def contato():
    return render_template("contato.html")

# Feature código aula 02
if __name__ == "__main__":
    app_isma.run()