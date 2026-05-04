import pytest
from Libreria.Audio.normalizador import Normalizador
from Libreria.Audio.tts import Voz

def test_normalizador_caso_normal():
    norm = Normalizador()
    resultado = norm.normalizar("traducir hola mundo tipo texto idioma ingles")
    assert "traducir" in resultado
    assert "hola mundo" in resultado

def test_normalizador_sin_tipo():
    norm = Normalizador()
    with pytest.raises(Exception):
        norm.normalizar("traducir hola mundo")

def test_normalizador_texto_vacio():
    norm = Normalizador()
    with pytest.raises(Exception):
        norm.normalizar("   ")

def test_tts_genera_audio():
    voz = Voz()
    audio = voz.volver_audio("Hola esto es una prueba")
    assert audio is not None
    assert audio.read(1) != b""