import orm.esquemas as esquemas
import orm.modelos as modelos #accedemos a modelos.py
from sqlalchemy.orm import Session
from sqlalchemy import and_

def regresa_Alumnos(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

def regresa_Alumno_ID(sesion: Session, id_alumno: int):
    print("SELECT * FROM app.alumnos WHERE id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

def regresa_Fotos(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

def regresa_Foto_ID(sesion:Session, id_foto:int):
    print("SELECT * FROM app.fotos WHERE id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

def regresa_Foto_ID_Alumno(sesion: Session, id_foto: int, id_alumno: int):
    print(f"SELECT * FROM app.fotos WHERE id = {id_foto} AND id_alumnos = {id_alumno}")
    return sesion.query(modelos.Foto).filter(and_(modelos.Foto.id == id_foto, modelos.Foto.id_alumno == id_alumno)).first()
def regresa_Calificaciones(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

def regresa_Calificaciones_ID(sesion:Session, id_calificacion:int):
    print("SELECT * FROM app.calificaciones WHERE id = ", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

def regresa_Calificaciones_ID_Alumno(sesion: Session, id_alumno: int):
    print("SELECT * FROM app.calificaciones WHERE id_alumnos = ", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()

def elimina_Alumno_ID(sesion: Session, id_alumno: int):
    print("DELETE FROM app.alumnos WHERE id = ", id_alumno)
    alumno = sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()
    if alumno:
        sesion.delete(alumno)
        sesion.commit()
    else:
        respuesta = {"mensaje" : "Alumno no encontrado"}
        return respuesta

def elimina_Calificacion_ID(sesion: Session, id_calificacion: int):
    print("DELETE FROM app.calificaciones WHERE id = ", id_calificacion)
    sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).delete()
    sesion.commit() 

def elimina_Foto_ID(sesion: Session, id: int):
    print("DELETE FROM app.fotos WHERE id = ", id)
    sesion.query(modelos.Foto).filter(modelos.Foto.id == id).delete()
    sesion.commit()

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

# Guardamos al alumno

def inserta_Alumno(session:Session, alumno_nuevo:esquemas.alumnoBase): 
    alumno_bd = modelos.Alumno()
    alumno_bd.nombre = alumno_nuevo.nombre
    alumno_bd.edad = alumno_nuevo.edad
    alumno_bd.domicilio = alumno_nuevo.domicilio
    alumno_bd.carrera = alumno_nuevo.carrera
    alumno_bd.trimestre = alumno_nuevo.trimestre
    alumno_bd.email = alumno_nuevo.email
    alumno_bd.password = alumno_nuevo.password

    session.add(alumno_bd)
    session.commit()
    session.refresh(alumno_bd)
    return alumno_bd

def actualiza_Alumno(sesion:Session, id_alumno:int, alumno_esquema:esquemas.alumnoBase): 
    alumno_db = regresa_Alumno_ID(sesion, id_alumno)
    if alumno_db is not None:
        alumno_db.nombre = alumno_esquema.nombre
        alumno_db.edad = alumno_esquema.edad
        alumno_db.domicilio = alumno_esquema.domicilio
        alumno_db.carrera = alumno_esquema.carrera
        alumno_db.trimestre = alumno_esquema.trimestre
        alumno_db.email = alumno_esquema.email
        alumno_db.password = alumno_esquema.password
        sesion.commit()
        sesion.refresh(alumno_db)
        print(alumno_esquema)
        return alumno_esquema 
    else:
        respuesta = {"mensaje" : "Alumno no encontrado"}
        return respuesta
    
def guarda_Calificacion_ID_Alumno(sesion:Session, id_alumno:int, calificacion_nueva:esquemas.calificacionBase):
    alumno = regresa_Alumno_ID(sesion, id_alumno)
    calificacion_bd = modelos.Calificacion()
    if alumno is not None:
        calificacion_bd.id_alumno = id_alumno
        calificacion_bd.uea = calificacion_nueva.uea
        calificacion_bd.calificacion = calificacion_nueva.calificacion
        sesion.add(calificacion_bd)
        sesion.commit()
        sesion.refresh(calificacion_bd)
        return calificacion_bd
    else:
        respuesta = {"mensaje" : "Alumno no encontrado"}
        return respuesta

def actualiza_Calificacion_ID(sesion:Session, id_calificacion:int, calificacion_esquema:esquemas.calificacionBase):
    calificacion_bd = regresa_Calificaciones_ID(sesion, id_calificacion)
    if calificacion_bd is not None:
        calificacion_bd.id_alumno = calificacion_esquema.id_alumno
        calificacion_bd.uea = calificacion_esquema.uea
        calificacion_bd.calificacion = calificacion_esquema.calificacion
        sesion.commit()
        sesion.refresh(calificacion_bd)
        print(calificacion_esquema)
        return calificacion_esquema
    else:
        respuesta = {"mensaje" : "Calificación no encontrada"}
        return respuesta

def guarda_Foto_ID_Alumno(sesion:Session, id_alumno:int, foto_nueva:esquemas.fotoBase):
    foto = regresa_Alumno_ID(sesion, id_alumno)
    foto_bd = modelos.Foto()
    if foto is not None:
        foto_bd.id_alumno = id_alumno
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        foto_bd.ruta = foto_nueva.ruta
        sesion.add(foto_bd)
        sesion.commit()
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje" : "Alumno no encontrado"}
        return respuesta

def actualiza_Foto_ID(sesion:Session, id_foto, foto_esquema:esquemas.fotoBase):
    foto_bd = regresa_Foto_ID(sesion, id_foto)
    if foto_bd is not None:
        foto_bd.id_alumno = foto_esquema.id_alumno
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        foto_bd.ruta = foto_esquema.ruta
        sesion.commit()
        sesion.refresh(foto_bd)
        print(foto_esquema)
        return foto_esquema
    else:
        respuesta = {"mensaje" : "Foto no encontrada"}
        return respuesta
    