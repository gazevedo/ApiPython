import pandas as pd
from flask import Flask, jsonify, request

tabela = pd.read_csv('Folha.csv')

app = Flask(__name__)


@app.route('/')
def homepage():
  return 'A API está no ar'


@app.route('/listafuncionario')
def getlistafuncionario():
  lista_funcionarios = tabela['Funcionario'].tolist()
  return jsonify(lista_funcionarios)


@app.route('/totalfolha')
def gettotalfolha():
  total_folha = tabela['Salario'].sum()
  return jsonify(total_folha)


@app.route('/folha')
def getfolha():
  tabela_dict = tabela.to_dict(orient='records')
  return jsonify(tabela_dict)


@app.route('/funcionario/<codigo>', methods=['GET'])
def get_funcionario(codigo):
  funcionario = tabela[tabela['codigo'] == int(codigo)]
  if not funcionario.empty:
    funcionario_dict = funcionario.iloc[0].to_dict()
    return jsonify(funcionario_dict)
  else:
    return jsonify({'error': 'Funcionário não encontrado'}), 404


@app.route('/atualizarSalario', methods=['POST'])
def atualizar_salario():
  if not request.json:
    return jsonify({'error': 'Solicitação deve ser JSON'}), 400

  dados = request.json
  codigo = dados.get('codigo')
  novo_salario = dados.get('salario')

  if codigo is None or novo_salario is None:
    return jsonify({'error': 'Código e salário são obrigatórios'}), 400

  index = tabela.index[tabela['codigo'] == int(codigo)].tolist()
  if index:
    tabela.at[index[0], 'Salario'] = novo_salario
    tabela.to_csv('Folha.csv', index=False)  # Salvar as mudanças no CSV
    return jsonify({'success': True})
  else:
    return jsonify({'error': 'Funcionário não encontrado'}), 404


# Rota para excluir um funcionário
@app.route('/excluirFuncionario/<codigo>', methods=['DELETE'])
def excluir_funcionario(codigo):
  index = tabela.index[tabela['codigo'] == int(codigo)].tolist()
  if index:
    tabela.drop(index[0], inplace=True)
    tabela.to_csv('Folha.csv', index=False)  # Salvar as mudanças no CSV
    return jsonify({'success': True})
  else:
    return jsonify({'error': 'Funcionário não encontrado'}), 404


app.run(host='0.0.0.0')
