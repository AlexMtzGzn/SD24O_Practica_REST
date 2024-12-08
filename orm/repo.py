import orm.modelos as modelos #accedemos a modelos.py
from sqlalchemy.orm import Session
from sqlalchemy import and_

def regresa_Alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()