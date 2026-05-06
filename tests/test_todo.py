import pytest

from Libreria.Audio.normalizador import Normalizador
from Libreria.Gramatica.lexer import Tokenizador
from Libreria.Gramatica.parser import Parser
from Libreria.IA.promptBuilder import PromptBuilder
from Libreria.IA.ia import Ia

def test_pipeline_completo_texto():
    entrada = "explicar la fotosintesis tipo texto idioma español"
    norm = Normalizador()
    texto_normalizado = norm.normalizar(entrada)
    assert "explicar" in texto_normalizado
    assert "fotosintesis" in texto_normalizado
    tok = Tokenizador()
    tokens = tok.tokenizar(texto_normalizado)
    assert len(tokens) > 0
    parser = Parser(tokens)
    consulta = parser.parsear()
    assert consulta["accion"] == "explicar"
    assert "tema" in consulta
    assert consulta["parametros"]["tipo"] == "texto"
    builder = PromptBuilder()
    prompt = builder.construir(consulta)
    assert "explicar" in prompt
    assert consulta["tema"] in prompt
    ia = Ia()
    respuesta = ia.generar(prompt)
    assert respuesta is not None
    assert len(respuesta) > 0

def test_pipeline_falla_sin_tipo():
    entrada = "explicar la fotosintesis idioma español"
    norm = Normalizador()
    with pytest.raises(Exception):
        texto_normalizado = norm.normalizar(entrada)
        tok = Tokenizador()
        tokens = tok.tokenizar(texto_normalizado)
        Parser(tokens).parsear()

def test_pipeline_audio_output():
    entrada = "resumir la revolucion francesa tipo audio idioma español"
    norm = Normalizador()
    texto = norm.normalizar(entrada)
    tok = Tokenizador()
    tokens = tok.tokenizar(texto)
    consulta = Parser(tokens).parsear()
    assert consulta["parametros"]["tipo"] == "audio"
    builder = PromptBuilder()
    prompt = builder.construir(consulta)
    ia = Ia()
    respuesta = ia.generar(prompt)
    assert respuesta is not None