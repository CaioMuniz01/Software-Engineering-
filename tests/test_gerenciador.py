import unittest
from src import gerenciador  # Importa o módulo inteiro

class TestGerenciador(unittest.TestCase):

    def setUp(self):
        # Limpa a lista de tarefas antes de cada teste
        gerenciador.tarefas.clear()

    def test_criar_tarefa(self):
        gerenciador.criar_tarefa("Estudar GitHub Actions")
        tarefas = gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]["nome"], "Estudar GitHub Actions")
        self.assertEqual(tarefas[0]["status"], "A Fazer")

    def test_atualizar_tarefa(self):
        gerenciador.criar_tarefa("Fazer commit")
        gerenciador.atualizar_tarefa(0, "Concluído")
        tarefas = gerenciador.listar_tarefas()
        self.assertEqual(tarefas[0]["status"], "Concluído")

    def test_excluir_tarefa(self):
        gerenciador.criar_tarefa("Excluir teste")
        gerenciador.excluir_tarefa(0)
        tarefas = gerenciador.listar_tarefas()
        self.assertEqual(len(tarefas), 0)

if __name__ == "__main__":
    unittest.main()
