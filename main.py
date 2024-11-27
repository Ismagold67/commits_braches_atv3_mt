# ódigo da aula 01
from flask import Flask

app_isma = Flask (__name__)

@app_isma.route('/')
def raiz():
    return 'Olá, turma!'

app_isma.run()