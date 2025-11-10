# src/gerenciador.py

tarefas = []

def criar_tarefa(nome):
    """Cria uma nova tarefa"""
    tarefas.append({"nome": nome, "status": "A Fazer"})

def listar_tarefas():
    """Lista todas as tarefas"""
    return tarefas.copy()  # Evita alteração externa

def atualizar_tarefa(indice, novo_status):
    """Atualiza o status de uma tarefa"""
    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = novo_status
    else:
        raise IndexError("Índice inválido.")

def excluir_tarefa(indice):
    """Exclui uma tarefa"""
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
    else:
        raise IndexError("Índice inválido.")
