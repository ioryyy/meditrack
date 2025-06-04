# database/models.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date)
    historial = Column(String)
    tipo = Column(String(20))  # 'general', 'urgente', 'pediatrico'

class PacienteUrgente(Paciente):
    __mapper_args__ = {'polymorphic_identity': 'urgente'}
    nivel_urgencia = Column(String(20))
    sintomas_agudos = Column(String)
    
class PacientePediatrico(Paciente):
    __mapper_args__ = {'polymorphic_identity': 'pediatrico'}
    peso = Column(Float)
    talla = Column(Float)