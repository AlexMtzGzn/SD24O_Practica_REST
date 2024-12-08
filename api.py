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

@app.get("/alumnos/{id}")
def leer_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando a alumno.")
    alumno = repo.regresa_Alumno_ID(sesion, id_alumno=id)
    if not alumno:
        return {"error": "Alumno no encontrado"}
    return alumno


@app.get("/alumnos/{id}/calificaciones")
def leer_calificaciones(id: int, sesion: Session = Depends(generador_sesion)):
    return get_calificaciones_by_alumno(sesion, id)

@app.get("/alumnos/{id}/fotos")
def read_fotos(id: int, sesion: Session = Depends(generador_sesion)):
    return get_fotos_by_alumno(sesion, id)

@app.delete("/alumnos/{id}")
def delete_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    delete_alumno_by_id(sesion, id)
    return {"message": "Alumno eliminado"}

@app.delete("/fotos/{id}")
def delete_foto(id: int, sesion: Session = Depends(generador_sesion)):
    delete_foto_by_id(sesion, id)
    return {"message": "Foto eliminada"}

@app.delete("/calificaciones/{id}")
def delete_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    delete_calificacion_by_id(sesion, id)
    return {"message": "Calificación eliminada"}
