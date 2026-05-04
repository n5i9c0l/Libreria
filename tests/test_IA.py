import pytest
from Libreria.IA.promptBuilder import PromptBuilder
from Libreria.IA.gemini import Gemini
from Libreria.IA.openRouter import OpenRouter
from Libreria.IA.ia import Ia

def test_prompt_builder_caso_normal():
    builder = PromptBuilder()
    consulta = {
        "accion": "explicar",
        "tema": "la fotosíntesis",
        "parametros": {"tipo": "texto", "idioma": "español", "tono": "formal"}
    }
    prompt = builder.construir(consulta)
    assert "explicar" in prompt
    assert "fotosíntesis" in prompt

def test_prompt_builder_defaults():
    builder = PromptBuilder()
    consulta = {
        "accion": "resumir",
        "tema": "la revolución francesa",
        "parametros": {"tipo": "audio"}
    }
    prompt = builder.construir(consulta)
    assert "español" in prompt
    assert "neutral" in prompt

def test_gemini_responde():
    gemini = Gemini()
    respuesta = gemini.generar("Decí solo 'hola' y nada más")
    assert respuesta is not None
    assert len(respuesta) > 0

def test_openrouter_responde():
    openrouter = OpenRouter()
    respuesta = openrouter.generar("Decí solo 'hola' y nada más")
    assert respuesta is not None
    assert len(respuesta) > 0

def test_ia_orquestador_responde():
    ia = Ia()
    respuesta = ia.generar("Decí solo 'hola' y nada más")
    assert respuesta is not None
    assert len(respuesta) > 0