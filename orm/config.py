from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_BASE_DATOS = "postgresql://usuario_ejemplo:Scanner1314@localhost:5432/bd_alumnos"

engine = create_engine(URL_BASE_DATOS,
                       connect_args={
                           "options": "-csearch_path=app"  #Para que la BD se conecte por medio del esquema
                       })

SessionClass = sessionmaker(engine) 

def generador_sesion():
    sesion = SessionClass()
    try:
        #equivalente a return sesion pero de manera segura
        yield sesion 
    finally: 
        sesion.close()

BaseClass = declarative_base()