from marshmallow import Schema, fields, validate

class FormSchema(Schema):
  # Step 1
  idade = fields.Integer(
    required=True,
    validate=[validate.Range(min=18, error="A idade mínima é 18 anos")]
  )
  genero_estado_civil = fields.String(
    required=True,
    validate=validate.OneOf(['A91', 'A92', 'A93', 'A93', 'A94', 'A95'], error="Selecione uma opção válida")
  )
  pessoas_responsaveis = fields.Integer(
    required=True,
    validate=[validate.Range(min=1, error="Deve ser um número positivo")]
  )
  trabalhador_estrangeiro = fields.String(
    required=True,
    validate=validate.OneOf(['A201', 'A202'], error="Selecione uma opção válida")
  )

  # Step 2
  emprego = fields.String(
    required=True,
    validate=validate.OneOf(['0', '1', '2', '3'], error="Selecione uma opção válida")
  )
  tempo_trabalho_atual = fields.String(
    required=True,
    validate=validate.OneOf(['0', '1', '2', '3', '4'], error="Selecione uma opção válida")
  )
  patrimonio = fields.String(
    required=True,
    validate=validate.OneOf(['A121', 'A122', 'A123', 'A124'], error="Selecione uma opção válida")
  )
  tempo_residencia_atual = fields.Integer(
    required=True,
    validate=[validate.Range(min=1, error="O tempo residência atual deve ser positivo")]
  )
  posse_moradia = fields.String(
    required=True,
    validate=validate.OneOf(['A151', 'A152', 'A153'], error="Selecione uma opção válida")
  )

  # Step 3
  situacao_conta_corrente = fields.String(
    required=True,
    validate=validate.OneOf(['0', '1', '2', '3'], error="Selecione uma opção válida")
  )
  poupanca_titulos = fields.String(
    required=True,
    validate=validate.OneOf(['0', '1', '2', '3', '4'], error="Selecione uma opção válida")
  )
  valor_credito = fields.Integer(
    required=True,
    validate=[validate.Range(min=1, error="O valor do crédito deve ser positivo")]
  )
  parcelamento_sobre_renda = fields.Integer(
    required=True,
    data_key="parcelamento_sobre_renda(%)",  # aceita a chave com parêntese
    validate=[validate.Range(min=1, error="O percentual deve ser positivo")]
  )

  # Step 4
  duracao_emprestimo = fields.Integer(
    required=True,
    data_key="duracao_emprestimo(meses)",  # aceita a chave com parêntese
    validate=[validate.Range(min=1, error="A duração deve ser positiva")]
  )
  proposito_credito = fields.String(
    required=True,
    validate=validate.OneOf(['A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50'], error="Selecione uma opção válida")
  )
  historico_de_credito = fields.String(
    required=True,
    validate=validate.OneOf(['A30','A31','A32','A33','A34'], error="Selecione uma opção válida")
  )
  outros_parcelamentos = fields.String(
    required=True,
    validate=validate.OneOf(['A141','A142','A143'], error="Selecione uma opção válida")
  )
  creditos_existentes = fields.Integer(
    required=True,
    validate=[validate.Range(min=1, error="Créditos existentes deve ser positivo")]
  )

  # Step 5
  parceiros_fiadores = fields.String(
    required=True,
    validate=validate.OneOf(['A101','A102','A103'], error="Selecione uma opção válida")
  )
