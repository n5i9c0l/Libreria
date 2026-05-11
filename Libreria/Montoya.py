import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), "..")))
from Libreria.Audio.normalizador import Normalizador
from Libreria.Gramatica.lexer import Tokenizador
from Libreria.Gramatica.parser import Parser
from Libreria.IA.promptBuilder import PromptBuilder
from Libreria.IA.ia import Ia
from Libreria.Audio.tts import Voz
SEPARADOR = '='*50
def demo_pipeline(entrada: str):
    print(SEPARADOR)
    print(f"ENTRADA:  {entrada}")
    print(SEPARADOR)
    # --- Paso 1: Normalizar ---
    print("\n[1] NORMALIZADOR")
    norm = Normalizador()
    try:
        normalizado = norm.normalizar(entrada)
        print(f"    Resultado: {normalizado}")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # --- Paso 2: Tokenizar ---
    print("\n[2] TOKENIZADOR")
    tok = Tokenizador()
    try:
        tokens = tok.tokenizar(normalizado)
        for token in tokens:
            print(f"    {token[0]:<22} -> '{token[1]}'")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # --- Paso 3: Parsear ---
    print("\n[3] PARSER")
    try:
        consulta = Parser(tokens).parsear()
        print(f"    Accion:     {consulta['accion']}")
        print(f"    Tema:       {consulta['tema']}")
        print(f"    Parametros: {consulta['parametros']}")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # --- Paso 4: Construir prompt ---
    print("\n[4] PROMPT BUILDER")
    builder = PromptBuilder()
    prompt = builder.construir(consulta)
    # Mostrar solo las primeras líneas para no saturar la salida
    lineas = prompt.strip().splitlines()
    for linea in lineas[:10]:
        print(f"    {linea}")
    if len(lineas) > 10:
        print(f"    ... ({len(lineas) - 10} líneas más)")
    # --- Paso 5: Generar respuesta IA ---
    print("\n[5] RESPUESTA DE LA IA")
    ia = Ia()
    respuesta = ia.generar(prompt)
    tipo = consulta["parametros"]["tipo"]
    if tipo == "audio":
        voz = Voz()
        audio = voz.volver_audio(respuesta)
        bytes_leidos = len(audio.read())
        print(f"    Tipo: AUDIO")
        print(f"    Texto generado por IA: {respuesta[:200]}{'...' if len(respuesta) > 200 else ''}")
        print(f"    Audio generado: {bytes_leidos} bytes")
    else:
        print(f"    Tipo: TEXTO")
        print(f"    {respuesta[:600]}{'...' if len(respuesta) > 600 else respuesta[600:]}")

    print()
def demo_error(descripcion: str, entrada: str):
    print(SEPARADOR)
    print(f"CASO DE ERROR: {descripcion}")
    print(f"ENTRADA: {entrada}")
    print(SEPARADOR)
    norm = Normalizador()
    try:
        normalizado = norm.normalizar(entrada)
        tok = Tokenizador()
        tokens = tok.tokenizar(normalizado)
        Parser(tokens).parsear()
        print("    (no se produjo error)")
    except Exception as e:
        print(f"    ERROR capturado correctamente: {e}")
    print()
if __name__ == "__main__":
    print("\n" + SEPARADOR)
    print("        DEMO DE LA LIBRERÍA - PIPELINE COMPLETO")
    print(SEPARADOR + "\n")
    # Casos normales
    demo_pipeline("explicar la fotosintesis tipo texto idioma español")
    demo_pipeline("resumir la revolucion francesa tipo audio idioma español tono formal")
    demo_pipeline("traducir hola mundo tipo texto idioma ingles")
    # Casos de error
    print("\n" + SEPARADOR)
    print("               CASOS DE ERROR ESPERADOS")
    print(SEPARADOR + "\n")
    demo_error("Sin parámetro tipo",         "explicar la fotosintesis idioma español")
    demo_error("Texto vacío",                "   ")
    demo_error("Tipo inválido",              "resumir algo tipo video")