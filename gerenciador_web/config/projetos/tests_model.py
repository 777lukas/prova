# projetos/test_models.py
from django.test import TestCase
from .models import Projeto

class ProjetoModelTest(TestCase):
    def test_criacao_projeto(self):
        projeto = Projeto.objects.create(titulo='Novo Website', descricao='Descrição do projeto.')
        self.assertEqual(projeto.titulo, 'Novo Website')

    def test_str_representation(self):
        projeto = Projeto.objects.create(titulo='Nome para Teste Str')
        self.assertEqual(str(projeto), 'Nome para Teste Str')