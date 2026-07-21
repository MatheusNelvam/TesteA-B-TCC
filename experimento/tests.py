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

    def test_presenca_nudges_interface_b(self):
        """Valida a renderização dos 5 nudges na Interface B"""
        print("\nValidando a presença dos 5 Nudges na Interface B...")
        response = self.client.get(reverse('interface_b'))
        self.assertEqual(response.status_code, 200)
        
        # Nudge 1: Barra de Progresso de Meta
        self.assertContains(response, 'id="goalProgressBar"')
        self.assertContains(response, 'id="goalCounter"')
        
        # Nudge 2: Reforço Positivo
        self.assertContains(response, 'id="reinforcementBox"')
        self.assertContains(response, 'Reforço Positivo & Conquista')
        
        # Nudge 3: Fila de Sugestões / Default (Autopreenchimento)
        self.assertContains(response, 'id="suggestedProfilesContainer"')
        self.assertContains(response, 'Fila de Contratações Sugeridas')
        
        # Nudge 4: Micro-marcos de Conquista
        self.assertContains(response, 'id="milestoneModal"')
        self.assertContains(response, 'Excelente Progresso!')
        
        # Nudge 5: Enquadramento de Bem-Estar / Recuperação Biológica
        self.assertContains(response, 'id="recoveryCard"')
        self.assertContains(response, 'Janela de Recuperação Biológica')
        
        print("[SUCESSO] Todos os 5 Nudges estao presentes e corretamente renderizados na Interface B!")

