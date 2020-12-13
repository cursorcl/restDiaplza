FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Se crea el Directorio de Data
RUN mkdir -p /app

# Se setea Nombre del Modulo Python a ejecutar
ENV MODULE_NAME="main"

# Se copia el contenido del proyecto dentro del docker
COPY . /app

# Se instalan los paquetes que son requerimientos para el modulo de software
RUN cd /app && pip install -r requirements.txt
