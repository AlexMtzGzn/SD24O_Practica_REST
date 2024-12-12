from pydantic import BaseModel

class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    carrera:str
    trimestre:str
    email:str
    password:str