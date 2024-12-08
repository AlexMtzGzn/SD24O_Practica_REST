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


"""▪ SELECT * FROM app.alumnos
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