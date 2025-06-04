# tests/unit/test_paciente_model.py
def test_creacion_paciente_urgente():
    from database.models import PacienteUrgente
    paciente = PacienteUrgente(
        nombre="María Gómez",
        nivel_urgencia="Alta",
        sintomas_agudos="Dolor torácico"
    )
    assert paciente.tipo == 'urgente'
    assert "Dolor torácico" in paciente.sintomas_agudos