from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [
  {
    'id': 1,
    'titulo':"Analista de Dados",
    'localidade': 'SC, Brasil',
    'salario': 'R$ 3500'
  },
  {
    'id': 2,
    'titulo': "Desenvolvedor Front-End",
    'localidade': 'PR, Brasil',
    'salario': 'R$ 3000'
  },
  {
    'id': 3,
    'titulo': "Cientista de Dados",
    'localidade': 'SP, Brasil',
    'salario': 'R$ 4000'
  },
  {
    'id': 4,
    'titulo': "Desenvolvedor Back-End",
    'localidade': 'SP, Brasil',
    'salario': 'R$ 5000'
  },
  {
    'id': 5,
    'titulo': "Estatístico",
    'localidade': 'RJ, Brasil',
    'salario': 'R$ 4000'
  },
  {
    'id': 6,
    'titulo': "Cientista de Dados",
    'localidade': 'RJ, Brasil',
    'salario': 'R$ 14000'
  }
]

@app.route("/")
def hello():
  return render_template("home.html", vagas=VAGAS)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGAS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)