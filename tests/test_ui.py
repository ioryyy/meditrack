# tests/e2e/test_ui.py
def test_registro_paciente_ui(browser):
    browser.visit('/pacientes/registro')
    browser.fill('nombre', 'Ana Torres')
    browser.find_by_text('Registrar').click()
    assert browser.is_text_present('éxito')