import numpy as np
import pandas as pd
import os
from flask import Flask, request, render_template, make_response
from flask_cors import CORS
import joblib

app = Flask(__name__, static_url_path='/static')
CORS(app, origins=["http://localhost:5173"])
model = joblib.load('model/pipeline_logistica.pkl')

@app.route('/')
def display_gui():
  return render_template('template.html')

@app.route('/verificar', methods=['POST'])
def verificar():
  data = request.get_json()
  print(data)

  colunas = [
    'idade', 'genero_estado_civil', 'pessoas_responsaveis', 'trabalhador_estrangeiro',
    'emprego', 'tempo_trabalho_atual', 'patrimonio', 'tempo_residencia_atual',
    'posse_moradia', 'situacao_conta_corrente', 'poupanca_titulos', 'valor_credito',
    'parcelamento_sobre_renda(%)', 'duracao_emprestimo(meses)', 'proposito_credito',
    'historico_de_credito', 'outros_parcelamentos', 'creditos_existentes', 'parceiros_fiadores'
]

  teste = pd.DataFrame([data], columns=colunas)
  classe = model.predict(teste)[0]

  print(":::::: Dados do Teste ::::::")
  print(teste)
  print("Classe Predita: {}".format(str(classe)))

  return {"classe": str(classe)}

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='localhost', port=port)
