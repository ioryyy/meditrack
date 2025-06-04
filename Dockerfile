# Use a imagem base do Python
FROM python:3.10-slim

# Configure vari?veis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Defina o diret?rio de trabalho
WORKDIR /app

# Copie e instale depend?ncias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante da aplica??o
COPY . .

# Exponha a porta 5000
EXPOSE 5000

# Comando para rodar a aplica??o
CMD ["python", "app.py"]
