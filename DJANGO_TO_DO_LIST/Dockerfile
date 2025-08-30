# 1. Imagem base do Python
FROM python:3.13.3-slim

# 2. Configs para não gerar pyc e mostrar logs no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Diretório de trabalho no container
WORKDIR /app

# 4. Instala dependências do sistema (gcc pode ser útil p/ libs C)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 6. Copia o restante do código
COPY . .

# 7. Expõe a porta que vamos usar no Django
EXPOSE 8000

# 8. Comando para rodar as migrações e iniciar o servidor
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"] 

