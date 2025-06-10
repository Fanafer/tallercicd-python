# test_app.py
from app import determinar_resultado

def test_empate():
    assert determinar_resultado("piedra", "piedra") == "Empate"
    assert determinar_resultado("papel", "papel") == "Empate"
    assert determinar_resultado("tijeras", "tijeras") == "Empate"

def test_ganar():
    assert determinar_resultado("piedra", "tijeras") == "Perdiste!"
    assert determinar_resultado("papel", "piedra") == "Ganaste!"
    assert determinar_resultado("tijeras", "papel") == "Ganaste!"

def test_perder():
    assert determinar_resultado("tijeras", "piedra") == "Perdiste"
    assert determinar_resultado("piedra", "papel") == "Perdiste"
    assert determinar_resultado("papel", "tijeras") == "Perdiste"