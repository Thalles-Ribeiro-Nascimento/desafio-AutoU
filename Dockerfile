# 1. Define a imagem base (Python oficial)
FROM python:3.12-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /desafio-autou

# 3. Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# 5. Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o código da aplicação para o container
COPY . .

# 7. Expõe a porta onde a aplicação Flask vai rodar
EXPOSE 5000

# 8. Comando para rodar a aplicação quando o container iniciar
CMD ["python3", "./project/app.py"]

