from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma/valor1=<int:n1>/valor2=<int:n2>")
def soma(n1,n2):
    return f'Soma dos valores {n1} e {n2} = {n1 + n2}'

@app.route("/subtrair/valor1=<int:n1>/valor2=<int:n2>")
def subtrair(n1,n2):
    return f'Subtracao dos valores {n1} e {n2} = {n1 - n2}'

@app.route("/multiplicar/valor1=<int:n1>/valor2=<int:n2>")
def multiplicar(n1,n2):
    return f'Resultado da multiplicacao {n1} e {n2} = {n1 * n2}'

@app.route("/divisao/valor1=<int:n1>/valor2=<int:n2>")
def divisao(n1,n2):

    if n1 == 0:
        return f'Esta invalido'
    elif n2 == 0:
        return f'Esta invalido'
    else:
        return f'Resultado divisao {n1} e {n2} = {n1 / n2}'
    






if __name__ == "__main__":
    app.run(debug=True)
