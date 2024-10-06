from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# Modelo de Usuario
class Usuario(BaseModel):
    nickname: str

# Modelo de Login
class Login(BaseModel):
    fecha: str
    hora: str

# Base de datos simulada en memoria
usuarios_db = {}
logins_db = []

# Endpoint para registrar un nuevo usuario
@app.post("/usuarios/", response_model=Usuario, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: Usuario):
    usuarios_db[usuario.nickname] = usuario
    return usuario

# Endpoint para obtener todos los usuarios
@app.get("/usuarios/", response_model=List[Usuario])
def obtener_usuarios():
    return list(usuarios_db.values())

# Endpoint para registrar un login de un usuario
@app.post("/usuarios/{nickname}/login/", response_model=Login, status_code=status.HTTP_201_CREATED)
def realizar_login(nickname: str):
    if nickname not in usuarios_db:
        return {"error": "Usuario no encontrado"}

    ahora = datetime.now()
    login = Login(fecha=ahora.strftime("%Y-%m-%d"), hora=ahora.strftime("%H:%M:%S"))
    logins_db.append({"usuario": nickname, "login": login})
    return login

# Endpoint para obtener todos los logins de un usuario
@app.get("/usuarios/{nickname}/logins/", response_model=List[Login])
def obtener_logins(nickname: str):
    logins_usuario = [entry["login"] for entry in logins_db if entry["usuario"] == nickname]
    return logins_usuario
