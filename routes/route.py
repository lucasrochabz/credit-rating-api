from flask import  Blueprint, request, jsonify
from marshmallow import ValidationError
from schemas import FormSchema
import pandas as pd
import joblib

route_bp = Blueprint("route", __name__)
schema = FormSchema()
model = joblib.load('models/pipeline_logistica.pkl')

@route_bp.route('/verificar', methods=['POST'])
def verificar():
  try:
    data = schema.load(request.json)

    # Cria DataFrame com mapeamento correto
    teste = pd.DataFrame([{
      'idade': data['idade'],
      'genero_estado_civil': data['genero_estado_civil'],
      'pessoas_responsaveis': data['pessoas_responsaveis'],
      'trabalhador_estrangeiro': data['trabalhador_estrangeiro'],
      'emprego': data['emprego'],
      'tempo_trabalho_atual': data['tempo_trabalho_atual'],
      'patrimonio': data['patrimonio'],
      'tempo_residencia_atual': data['tempo_residencia_atual'],
      'posse_moradia': data['posse_moradia'],
      'situacao_conta_corrente': data['situacao_conta_corrente'],
      'poupanca_titulos': data['poupanca_titulos'],
      'valor_credito': data['valor_credito'],
      'parcelamento_sobre_renda(%)': data['parcelamento_sobre_renda'],
      'duracao_emprestimo(meses)': data['duracao_emprestimo'],
      'proposito_credito': data['proposito_credito'],
      'historico_de_credito': data['historico_de_credito'],
      'outros_parcelamentos': data['outros_parcelamentos'],
      'creditos_existentes': data['creditos_existentes'],
      'parceiros_fiadores': data['parceiros_fiadores']
    }])

    classe = int(model.predict(teste)[0])

    return jsonify({'status': 'ok', "data": classe}), 200
  except ValidationError as err:
    return jsonify({'status': 'error', 'errors': err.messages}), 400
