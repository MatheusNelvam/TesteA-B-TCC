# Usa uma imagem oficial do Python leve
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Define variáveis de ambiente para o Python não gerar arquivos .pyc e não reter buffers
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema (necessárias para compilar alguns pacotes Python)
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Instala o Gunicorn e as dependências do projeto
RUN pip install --upgrade pip
RUN pip install gunicorn

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia todo o código do projeto para o container
COPY . /app/

# Expõe a porta que o Gunicorn vai rodar internamente
EXPOSE 8000

# Comando para rodar as migrações, coletar estáticos e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 core.wsgi:application"]