# Usa la imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias definidas en el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al directorio de trabajo
COPY src .

# Expone el puerto en el que se ejecutará la aplicación
EXPOSE 4000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["python", "app.py"]
