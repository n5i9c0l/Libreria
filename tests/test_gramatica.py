# ============================================================
#  TEST DEL MÓDULO GRAMATICA
# ============================================================

from Libreria.Gramatica.lexer import Tokenizador
from Libreria.Gramatica.parser import Parser

# ---- 1. LEXER ----
print("=" * 40)
print("TEST: Tokenizador (Lexer)")
print("=" * 40)

tok = Tokenizador()

# Caso normal
tokens = tok.tokenizar('traducir : "hola mundo" (tipo = "texto", idioma = "ingles")')
print("✅ Tokens generados:", tokens)

# Verifica que los tipos de tokens sean correctos
tipos = [t[0] for t in tokens]
assert "ACCION" in tipos, "❌ Falta ACCION"
assert "DOS_PUNTOS" in tipos, "❌ Falta DOS_PUNTOS"
assert "VALOR" in tipos, "❌ Falta VALOR"
assert "PARAMETRO" in tipos, "❌ Falta PARAMETRO"
print("✅ Tipos de tokens correctos")

# Palabra no permitida → debe lanzar excepción
try:
    tok.tokenizar('traducir : "hola" (tipo = "texto", 123)')
    print("❌ Debería haber lanzado excepción")
except Exception as e:
    print("✅ Excepción esperada por token inválido:", e)


# ---- 2. PARSER ----
print()
print("=" * 40)
print("TEST: Parser")
print("=" * 40)

# Caso normal completo
tokens = tok.tokenizar('explicar : "la fotosíntesis" (tipo = "texto", idioma = "español", tono = "formal")')
parser = Parser(tokens)
resultado = parser.parsear()

assert resultado["accion"] == "explicar", "❌ Acción incorrecta"
assert resultado["tema"] == "la fotosíntesis", "❌ Tema incorrecto"
assert resultado["parametros"]["tipo"] == "texto", "❌ Tipo incorrecto"
assert resultado["parametros"]["idioma"] == "español", "❌ Idioma incorrecto"
print("✅ Parseo correcto:", resultado)

# Solo parámetro obligatorio
tokens = tok.tokenizar('resumir : "la revolución" (tipo = "audio")')
parser = Parser(tokens)
resultado = parser.parsear()
assert resultado["parametros"]["tipo"] == "audio"
print("✅ Parseo con solo tipo obligatorio:", resultado)

# Tipo inválido → debe lanzar excepción
try:
    tokens = tok.tokenizar('resumir : "algo" (tipo = "video")')
    parser = Parser(tokens)
    parser.parsear()
    print("❌ Debería haber lanzado excepción por tipo inválido")
except Exception as e:
    print("✅ Excepción esperada por tipo inválido:", e)

# Primer parámetro no es tipo → debe lanzar excepción
try:
    tokens = tok.tokenizar('resumir : "algo" (idioma = "español")')
    parser = Parser(tokens)
    parser.parsear()
    print("❌ Debería haber lanzado excepción")
except Exception as e:
    print("✅ Excepción esperada por falta de tipo primero:", e)


print()
print("=" * 40)
print("FIN DE TESTS DE GRAMATICA")
print("=" * 40)