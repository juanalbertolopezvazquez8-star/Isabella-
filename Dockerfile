FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    nmap \
    sqlmap \
    hydra \
    hashcat \
    john \
    curl \
    wget \
    git \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Crear directorios necesarios
RUN mkdir -p data logs uploads downloads extractions reports

# Exponer puerto
EXPOSE 5000

# Comando de inicio
CMD ["python", "app.py"]
