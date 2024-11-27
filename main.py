# Código da aula 01
from flask import Flask

app_isma = Flask (__name__)

@app_isma.route('/')
def raiz():
    return 'Olá, turma!'

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

# Feature código aula 02
if __name__ == "__main__":
    app_isma.run()