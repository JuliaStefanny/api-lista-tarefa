class Tarefa:

    def __init__(self, task_id, titulo, descricao, status, data_inicio, data_prevista, nota):
        self.task_id = task_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_inicio = data_inicio
        self.data_prevista = data_prevista
        self.nota = nota

    def to_jason(self):
        return {
            "task_id": self.task_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_inicio": self.data_inicio,
            "data_prevista": self.data_prevista,
            "nota": self.nota
        }