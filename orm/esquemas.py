from pydantic import BaseModel

class alumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str


class calificacionBase(BaseModel):
    id_alumno:int
    uea:str
    calificacion:str

class fotoBase(BaseModel):
    id_alumno:int
    titulo:str
    descripcion:str
    ruta:str