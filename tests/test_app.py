# test_app.py
from app import app

def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert "¡Hola desde Flask con CI/CD!" in response.data.decode("utf-8")