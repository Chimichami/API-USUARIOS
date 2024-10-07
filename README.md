# API de Usuarios

## Descripción
La API de Usuarios permite gestionar usuarios en el sistema, proporcionando funcionalidades para crear, obtener y eliminar usuarios. La API está construida con FastAPI y utiliza PostgreSQL como base de datos.

## Tecnologías
- **Lenguaje**: Python
- **Framework**: FastAPI
- **Base de datos**: PostgreSQL
- **Docker**: Para la creación de contenedores

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Chimichami/API-USUARIOS.git
   cd api-usuarios
2. **Crea un entorno virtual (opcional pero recomendado)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
4. **Configura la base de datos**:
   Asegúrate de tener PostgreSQL instalado y en funcionamiento.
   Crea una base de datos para la API y actualiza el archivo de configuración con la URL de conexión.
5. **Ejecuta las migraciones (si utilizas Alembic o similar)**:
   ```bash
   alembic upgrade head
## Uso
1. **Ejecuta la API**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
2. **Realiza peticiones a la API**:

   Crear un usuario (POST):

   ```bash
   POST http://localhost:8000/usuarios/
   Content-Type: application/json

   {
     "nickname": "nuevo_usuario"
   }
   ```
   Obtener usuarios (GET):
   ```bash
   GET http://localhost:8000/usuarios/



