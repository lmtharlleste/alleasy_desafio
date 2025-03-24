# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do diretório local para o container
COPY . /app

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Garante que o arquivo de regras seja copiado para o local correto
COPY regras/regras_linguagem_natural.txt /app/

# Executa os testes automatizados
RUN pytest --maxfail=1 --disable-warnings -q
