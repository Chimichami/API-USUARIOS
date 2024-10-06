# Imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la app
EXPOSE 8000

# Comando para correr la app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
