from flask import Flask, jsonify, request
# classe aluno
class Aluno:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
# classe professor
class Professor:
    def __init__(self, id, nome):
        self.id = id
        self.name = nome
# database
database = dict()
database['ALUNOS'] = []
database['PROFESSORES'] = []
# flask - rotas
app = Flask(__name__)
# todos - raiz (show)
@app.route('/')
# listagem geral
def all():
    return jsonify(database)

# alunos (view)
@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def retrieve_aluno(id_aluno):
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return {'message': 'Não encontrado'}, 404
# alunos (show)
@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNOS'])
# alunos (create)
@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database['ALUNOS'].append(novo_aluno)
    return jsonify(database['ALUNOS'])
@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    novo_dado_aluno = request.get_json()
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            aluno['id'] = novo_dado_aluno['id']
            aluno['nome'] = novo_dado_aluno['nome']
            return jsonify(database)
    return {'message': 'Não encontrado'}, 404
# alunos (alter)
@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    exists = 0
    for aluno in database['ALUNOS']:
        if aluno['id'] == id_aluno:
            exists = 1
    if not exists:
        return {'message': 'Não encontrado'}, 404
    new_database = []
    for aluno in database['ALUNOS']:
        if aluno['id'] != id_aluno:
            new_database.append(aluno)
    database['ALUNOS'] = new_database
    return database

# professores (view)
@app.route('/professores/<int:id_professor>', methods=['GET'])
def retrieve_professor(id_professor):
    for professor in database['PROFESSORES']:
        if professor['id'] == id_professor:
            return jsonify(professor)
    return {'message': 'Não encontrado'}, 404
# professores (show)
@app.route('/professores')
def professores():
    return jsonify(database['PROFESSORES'])
# professores (create)
@app.route('/professores', methods=['POST'])
def novo_professor():
    novo_professor = request.get_json()
    database['PROFESSORES'].append(novo_professor)
    return jsonify(database['PROFESSORES'])
# professores (alter)
@app.route('/professores/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    novo_dado_professor = request.get_json()
    for professor in database['PROFESSORES']:
        if professor['id'] == id_professor:
            professor['id'] = novo_dado_professor['id']
            professor['nome'] = novo_dado_professor['nome']
            return jsonify(database)
    return {'message': 'Não encontrado'}, 404
@app.route('/professores/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    exists = 0
    for professor in database['PROFESSORES']:
        if professor['id'] == id_professor:
            exists = 1
    if not exists:
        return {'message': 'Não encontrado'}, 404
    new_database = []
    for professor in database['PROFESSORES']:
        if professor['id'] != id_professor:
            new_database.append(professor)
    database['PROFESSORES'] = new_database
    return database

# executa o servidor
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)