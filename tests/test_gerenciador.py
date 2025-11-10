# tests/test_gerenciador.py

import unittest
from src.gerenciador import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa, tarefas

class TestGerenciador(unittest.TestCase):

    def setUp(self):
        tarefas.clear()  # Limpa a lista antes de cada teste

    def test_criar_tarefa(self):
        criar_tarefa("Estudar GitHub Actions")
        self.assertEqual(len(listar_tarefas()), 1)
        self.assertEqual(listar_tarefas()[0]["nome"], "Estudar GitHub Actions")
        self.assertEqual(listar_tarefas()[0]["status"], "A Fazer")

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
