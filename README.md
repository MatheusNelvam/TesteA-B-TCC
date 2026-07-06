# Teste A/B TCC

Este é o projeto base Django desenvolvido para o TCC de Testes A/B.

## Pré-requisitos

Certifique-se de ter instalado em sua máquina:
* Python 3.10 ou superior
* Pip (gerenciador de pacotes do Python)

## Instalação e Execução Local

Siga os passos abaixo para configurar e rodar o projeto localmente:

### 1. Clonar ou Acessar a Pasta do Projeto
Abra o seu terminal na raiz do projeto:
```bash
cd TesteA-B-TCC
```

### 2. Criar e Ativar o Ambiente Virtual (Virtual Environment)
Recomenda-se utilizar um ambiente virtual para isolar as dependências do projeto.

No **Windows (PowerShell)**:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No **Linux/macOS**:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativo, instale os pacotes necessários a partir do arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Executar as Migrações do Banco de Dados
Prepare o banco de dados SQLite local executando:
```bash
python manage.py migrate
```

### 5. Criar um Superusuário (Opcional - para acessar o painel de administração)
Caso queira acessar a área administrativa (`/admin`), crie um usuário administrador:
```bash
python manage.py createsuperuser
```

### 6. Iniciar o Servidor de Desenvolvimento
Inicie o servidor local do Django:
```bash
python manage.py runserver
```

Após iniciar, o projeto estará acessível no seu navegador no endereço:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Para acessar o painel de administração:
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
