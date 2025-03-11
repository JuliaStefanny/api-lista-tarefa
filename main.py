from flask import Flask, request
from tarefas import Tarefa

app = Flask(__name__)

tarefas = [
    Tarefa(task_id=1,
           titulo="Estudar Javascript",
           descricao="Estudar Javascript para usar",
           status="Em andamento",
           data_inicio="Iniciou semana passada",
           data_prevista="Daqui a um mes",
           nota=8).to_jason(),
    Tarefa(task_id=2,
           titulo="Estudar Flask",
           descricao="Estudar Flask para aprender sobre web service",
           status="Não iniciado",
           data_inicio="ano passado",
           data_prevista="final do ano",
           nota=6).to_jason()
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return tarefas

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            return tarefa

    return 'Tarefa não encontrada'

@app.route('/tasks', methods=['POST'])
def creat_task():
    task = request.json
    ultimo_id = tarefas[-1].get('task_id') + 1
    task['task_id'] = ultimo_id
    tarefas.append(task)
    return task

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_search = None
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            task_search = tarefa

    task_body = request.json
    task_search['titulo'] = task_body.get('titulo')
    task_search['descricao'] = task_body.get('descricao')
    task_search['status'] = task_body.get('status')
    task_search['data nota'] = task_body.get('data nota')
    task_search['data prevista'] = task_body.get('data prevista')
    task_search['nota'] = task_body.get('nota')

    return  task_search

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('task_id') == task_id:
            tarefas.remove(tarefa)

    return 'Tarefa removida'

if __name__=='__main__':
    app.run(debug=True)