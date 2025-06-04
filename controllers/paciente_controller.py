# controllers/paciente_controller.py
from flask import Blueprint, request, jsonify
from database import Session
from database.models import Paciente

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/pacientes', methods=['POST'])
def crear_paciente():
    data = request.json
    session = Session()
    nuevo_paciente = Paciente(
        nombre=data['nombre'],
        fecha_nacimiento=data['fecha_nacimiento']
    )
    session.add(nuevo_paciente)
    session.commit()
    return jsonify({"id": nuevo_paciente.id}), 201
# controllers/paciente_controller.py (ampliación)
@paciente_bp.route('/pacientes/urgentes', methods=['POST'])
def crear_urgente():
    data = request.json
    paciente = PacienteUrgente(
        nombre=data['nombre'],
        nivel_urgencia=data['urgencia']
    )
    # ... persistencia
    return jsonify({"nivel": paciente.nivel_urgencia})

