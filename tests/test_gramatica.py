import pytest
from Libreria.Gramatica.lexer import Tokenizador
from Libreria.Gramatica.parser import Parser

def test_tokenizador_tipos_correctos():
    tok = Tokenizador()
    tokens = tok.tokenizar('traducir : "hola mundo" (tipo = "texto")')
    tipos = [t[0] for t in tokens]
    assert "ACCION" in tipos
    assert "DOS_PUNTOS" in tipos
    assert "VALOR" in tipos
    assert "PARAMETRO" in tipos

def test_tokenizador_token_invalido():
    tok = Tokenizador()
    with pytest.raises(Exception):
        tok.tokenizar('traducir : "hola" (tipo = "texto", 123)')

def test_parser_caso_normal():
    tok = Tokenizador()
    tokens = tok.tokenizar('explicar : "la fotosíntesis" (tipo = "texto", idioma = "español")')
    resultado = Parser(tokens).parsear()
    assert resultado["accion"] == "explicar"
    assert resultado["tema"] == "la fotosíntesis"
    assert resultado["parametros"]["tipo"] == "texto"
    assert resultado["parametros"]["idioma"] == "español"

def test_parser_solo_tipo():
    tok = Tokenizador()
    tokens = tok.tokenizar('resumir : "la revolución" (tipo = "audio")')
    resultado = Parser(tokens).parsear()
    assert resultado["parametros"]["tipo"] == "audio"

def test_parser_tipo_invalido():
    tok = Tokenizador()
    tokens = tok.tokenizar('resumir : "algo" (tipo = "video")')
    with pytest.raises(Exception):
        Parser(tokens).parsear()

def test_parser_sin_tipo():
    tok = Tokenizador()
    tokens = tok.tokenizar('resumir : "algo" (idioma = "español")')
    with pytest.raises(Exception):
        Parser(tokens).parsear()