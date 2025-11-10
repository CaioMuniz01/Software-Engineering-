import unittest
import sys
import os

# Adiciona o caminho da pasta src ao sistema
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gerenciador import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa

class TestGerenciador(unittest.TestCase):

    def setUp(self):
        # Garante que a lista de tarefas começa vazia antes de cada teste
        global tarefas
        from gerenciador import tarefas
        tarefas.clear()

    def test_criar_tarefa(self):
        criar_tarefa("Estudar GitHub Actions")
        self.assertEqual(len(listar_tarefas()), 1)
        self.assertEqual(listar_tarefas()[0]["nome"], "Estudar GitHub Actions")

    def test_atualizar_tarefa(self):
        criar_tarefa("Fazer commit")
        atualizar_tarefa(0, "Concluído")
        self.assertEqual(listar_tarefas()[0]["status"], "Concluído")

    def test_excluir_tarefa(self):
        criar_tarefa("Excluir teste")
        excluir_tarefa(0)
        self.assertEqual(len(listar_tarefas()), 0)

if __name__ == "__main__":
    unittest.main()
