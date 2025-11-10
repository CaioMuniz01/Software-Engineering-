import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gerenciador import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa

tarefas = []

def test_criar_tarefa():
    criar_tarefa("Tarefa de teste")
    lista = listar_tarefas()
    assert len(lista) == 1
    assert lista[0]["nome"] == "Tarefa de teste"
    assert lista[0]["status"] == "A Fazer"

def test_atualizar_tarefa():
    criar_tarefa("Estudar Python")
    atualizar_tarefa(0, "Concluído")
    lista = listar_tarefas()
    assert lista[0]["status"] == "Concluído"

def test_excluir_tarefa():
    criar_tarefa("Excluir depois")
    excluir_tarefa(0)
    lista = listar_tarefas()
    assert len(lista) == 0
