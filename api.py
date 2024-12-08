from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo # Función para hacer las consultas a la BD
from sqlalchemy.orm import Session
from sqlalchemy import and_
from orm.config import generador_sesion # Generador de sesiones

# Se crea el servidor
app = FastAPI()

# GET ALUMNOS

# get("/alumnos”)
@app.get("/alumnos")
def lista_alumnos(session:Session=Depends(generador_sesion)):
    print("API consultando a los alumnos.")
    return repo.devuelve_alumnos(session)

