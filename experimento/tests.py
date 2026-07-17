from django.test import TestCase, Client
from django.urls import reverse
from .models import Participante, Cliente

class CadastroFuncionariosTestCase(TestCase):
    def setUp(self):
        # Criação do cliente de teste do Django (Client) e participante do experimento
        self.client = Client()
        self.participante = Participante.objects.create(identificador="ParticipanteTeste")
        
        # Define a sessão do participante simulando o login
        session = self.client.session
        session['participante_id'] = self.participante.id
        session.save()

    def test_cadastros_interface_a_10_vezes(self):
        """Testa a criação de 10 funcionários a partir da Interface A"""
        print("\nIniciando 10 testes de cadastro para Interface A...")
        
        for i in range(1, 11):
            nome = f"Funcionario A {i}"
            email = f"func_a_{i}@empresa.com"
            cargo = f"Cargo A {i}"
            registro = f"MAT-A00{i}"
            
            # Executa o POST para criar o cliente vindo da interface-a
            response = self.client.post(reverse('criar_cliente'), {
                'origem': 'interface-a',
                'nome': nome,
                'email': email,
                'cargo_ou_funcao': cargo,
                'codigo_registro': registro
            })
            
            # Verifica se redirecionou com sucesso de volta para a interface A
            self.assertRedirects(response, reverse('interface_a'))
            
            # Verifica se o registro foi salvo corretamente no banco
            self.assertTrue(Cliente.objects.filter(
                participante=self.participante,
                nome=nome,
                email=email,
                cargo_ou_funcao=cargo,
                codigo_registro=registro,
                interface='interface-a'
            ).exists())
            
            print(f"Teste A {i}/10: Cadastro concluído com sucesso ({nome})")

    def test_cadastros_interface_b_10_vezes(self):
        """Testa a criação de 10 funcionários a partir da Interface B"""
        print("\nIniciando 10 testes de cadastro para Interface B...")
        
        for i in range(1, 11):
            nome = f"Funcionario B {i}"
            email = f"func_b_{i}@empresa.com"
            cargo = f"Cargo B {i}"
            registro = f"REG-B00{i}"
            
            # Executa o POST para criar o cliente vindo da interface-b
            response = self.client.post(reverse('criar_cliente'), {
                'origem': 'interface-b',
                'nome': nome,
                'email': email,
                'cargo_ou_funcao': cargo,
                'codigo_registro': registro
            })
            
            # Verifica se redirecionou com sucesso de volta para a interface B
            self.assertRedirects(response, reverse('interface_b'))
            
            # Verifica se o registro foi salvo corretamente no banco
            self.assertTrue(Cliente.objects.filter(
                participante=self.participante,
                nome=nome,
                email=email,
                cargo_ou_funcao=cargo,
                codigo_registro=registro,
                interface='interface-b'
            ).exists())
            
            print(f"Teste B {i}/10: Cadastro concluído com sucesso ({nome})")
