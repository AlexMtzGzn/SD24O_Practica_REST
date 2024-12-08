import orm.modelos as modelos #accedemos a modelos.py
from sqlalchemy.orm import Session
from sqlalchemy import and_

def regresa_Alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

def regresa_Alumno_ID(sesion:Session):
    print("SELECT * FROM app.alumnos WHERE id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_usuario).first()

def regresa_Fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

def regresa_Foto_ID(sesion:Session, id_foto:int):
    print("SELECT * FROM app.fotos WHERE id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

def regresa_Foto_ID_Alumno(sesion:Session, id_alumno):
    print("SELECT * FROM app.fotos WHERE id_alumnos = ", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Alumno.id == id_alumno).first()

def regresa_Calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

def regresa_Calificaciones_ID(sesion:Session, id_calificacion:int):
    print("SELECT * FROM app.calificaciones WHERE id = ", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

def regresa_calificaciones_ID_Alumno(sesion:Session, id_alumno:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos = ", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Alumno.id == id_alumno).first()

def calificaciones_por_id_alumno(session:Session, id_alumno:int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos = ", id_alumno)
    return session.query(modelos.Calificacion).filter(modelos.Alumno.id == id_alumno).first()

"""▪ SELECT * FROM app.alumnos
▪ SELECT * FROM app.alumnos
▪ SELECT * FROM app.alumnos WHERE id={id_al}
▪ SELECT * FROM app.fotos
▪ SELECT * FROM app.fotos WHERE id={id_fo}
▪ SELECT * FROM app.fotos WHERE id_alumnos={id_al}
▪ SELECT * FROM app.calificaciones
▪ SELECT * FROM app.calificaciones WHERE id={id_fo}
▪ SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
▪ DELETE FROM app.alumnos WHERE id_alumnos={id_al}
▪ DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
▪ DELETE FROM app.fotos WHERE id_alumnos={id_al}"""