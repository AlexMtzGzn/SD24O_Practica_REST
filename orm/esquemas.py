from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str


class calificacioneBase(BaseModel):
    id_alumno:int
    uea:str
    calificacion:str