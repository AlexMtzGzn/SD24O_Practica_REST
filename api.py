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
    alumno = repo.regresa_Alumno_ID(sesion, id)
    return alumno

@app.get("/alumnos/{id}/calificaciones")
def read_calificaciones(id: int, db: Session = Depends(get_db)):
    return get_calificaciones_by_alumno(db, id)

@app.get("/alumnos/{id}/fotos")
def read_fotos(id: int, db: Session = Depends(get_db)):
    return get_fotos_by_alumno(db, id)

@app.delete("/alumnos/{id}")
def delete_alumno(id: int, db: Session = Depends(get_db)):
    delete_alumno_by_id(db, id)
    return {"message": "Alumno eliminado"}

@app.delete("/fotos/{id}")
def delete_foto(id: int, db: Session = Depends(get_db)):
    delete_foto_by_id(db, id)
    return {"message": "Foto eliminada"}

@app.delete("/calificaciones/{id}")
def delete_calificacion(id: int, db: Session = Depends(get_db)):
    delete_calificacion_by_id(db, id)
    return {"message": "Calificación eliminada"}
