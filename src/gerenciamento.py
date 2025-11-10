# src/gerenciador.py
tarefas = []

def criar_tarefa(nome):
    tarefas.append({"nome": nome, "status": "A Fazer"})

def listar_tarefas():
    return tarefas

def atualizar_tarefa(indice, novo_status):
    tarefas[indice]["status"] = novo_status

def excluir_tarefa(indice):
    tarefas.pop(indice)
