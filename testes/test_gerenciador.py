# tests/test_gerenciador.py
import unittest
from src.gerenciador import criar_tarefa, listar_tarefas

class TestGerenciador(unittest.TestCase):
    def test_criar_tarefa(self):
        criar_tarefa("Estudar GitHub Actions")
        self.assertEqual(len(listar_tarefas()), 1)

if __name__ == '__main__':
    unittest.main()
