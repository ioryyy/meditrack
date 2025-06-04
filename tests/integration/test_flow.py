# tests/integration/test_flow.py
def test_flujo_completo_creacion():
    # Simular solicitud POST
    response = client.post('/pacientes', data={'nombre': 'Carlos R.'})
    assert response.status_code == 201
    assert b"id" in response.data