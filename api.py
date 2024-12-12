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


@app.get("/alumnos") 
def leer_alumnos(sesion: Session = Depends(generador_sesion)):
    print("API consultando a los alumnos.")
    alumnos = repo.regresa_Alumnos(sesion)
    return alumnos

@app.get("/alumnos/{id}")
def leer_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando a alumno.")
    alumno = repo.regresa_Alumno_ID(sesion, id_alumno=id)
    return alumno


@app.get("/fotos")
def leer_Fotos(sesion: Session = Depends(generador_sesion)):
    print("API consultando fotos.")
    fotos = repo.regresa_Fotos(sesion)
    return fotos

@app.get("/fotos/{id}")
def leer_fotos_id(id: int, sesion: Session = Depends(generador_sesion)):
    print("API consultando fotos por id.")
    foto = repo.regresa_Foto_ID(sesion, id_foto=id)
    return foto

@app.get("/fotos/{id}/{alumno}")
def leer_foto_id_alumno(id: int, alumno: int, sesion: Session = Depends(generador_sesion)):
    print(f"API consultando foto {id} del alumno {alumno}")
    foto = repo.regresa_Foto_ID_Alumno(sesion, id_foto=id, id_alumno=alumno)
    if not foto:
        raise HTTPException(status_code=404, detail="Foto no encontrada")
    return foto

@app.get("/calificaciones")
def leer_alumnos(sesion: Session = Depends(generador_sesion)):
    print("API consultando a las calificaciones.")
    calificaciones = repo.regresa_Calificaciones(sesion)
    return calificaciones

@app.delete("/calificaciones/{id}")
def eliminar_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API eliminando calificación {id}")
    calificacion = repo.regresa_Calificaciones_ID(sesion, id_calificacion=id)
    if not calificacion:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    repo.elimina_Calificacion_ID(sesion, id_calificacion=id)
    return {"message": "Calificación eliminada"}


@app.get("/alumnos/{id}/calificaciones")
def leer_calificaciones(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API consultando calificaciones del alumno {id}.")
    calificaciones = repo.regresa_Calificaciones_ID_Alumno(sesion, id_alumno=id)
    return calificaciones

@app.get("/alumnos/{id}/fotos")
def leer_fotos_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API consultando fotos del alumno {id}")
    fotos = repo.regresa_Foto_ID_Alumno(sesion, id_alumno=id)
    return fotos


@app.delete("/alumnos/{id}")
def eliminar_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    alumno = repo.regresa_Alumno_ID(sesion, id_alumno=id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    repo.elimina_Alumno_ID(sesion, id_alumno=id)
    return {"message": "Alumno eliminado"}

@app.delete("/fotos/{id}")
def eliminar_foto(id: int, sesion: Session = Depends(generador_sesion)):
    foto = repo.regresa_Foto_ID(sesion, id_foto=id)
    if not foto:
        raise HTTPException(status_code=404, detail="Foto no encontrada")
    repo.elimina_Foto_ID(sesion, id=id)
    return {"message": "Foto eliminada"}

@app.delete("/calificaciones/{id}")
def eliminar_calificacion(id: int, sesion: Session = Depends(generador_sesion)):
    calificacion = repo.regresa_Calificaciones_ID(sesion, id_calificacion=id)
    if not calificacion:
        raise HTTPException(status_code=404, detail="Calificación no encontrada")
    repo.elimina_Calificacion_ID(sesion, id_alumno=id)
    return {"message": "Calificación eliminada"}

"""Atiende las siguientes peticiones del tipo PUT y POST:

o post("/alumnos”)
o put("/alumnos/{id})
o post("/alumnos/{id}/calificaciones")
o put("/calificaciones/{id}")
o post("/alumnos/{id}/fotos")
o put("/fotos/{id}")"""

