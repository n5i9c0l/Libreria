import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from thepibbles.Audio.normalizador import Normalizador
from thepibbles.Gramatica.lexer import Tokenizador
from thepibbles.Gramatica.parser import Parser
from thepibbles.IA.promptBuilder import PromptBuilder
from thepibbles.IA.ia import Ia
from thepibbles.Audio.tts import Voz
def reproducir_audio(audio):
    try:
        import tempfile
        import subprocess
        audio.seek(0)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            f.write(audio.read())
            ruta = f.name
        subprocess.Popen(["start", ruta], shell=True)
        print("    Audio guardado y abriendo con el reproductor de Windows...")
    except Exception as e:
        print(f"    Error al reproducir audio: {e}")
def demo_pipeline(entrada: str):
    print(f"\nENTRADA:  {entrada}\n")
    # Normalizar
    print("[1] NORMALIZADOR")
    norm = Normalizador()
    try:
        normalizado = norm.normalizar(entrada)
        print(f"    Resultado: {normalizado}")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # Tokenizar
    print("\n[2] TOKENIZADOR")
    tok = Tokenizador()
    try:
        tokens = tok.tokenizar(normalizado)
        for token in tokens:
            print(f"    {token[0]:<22} -> '{token[1]}'")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # Parsear
    print("\n[3] PARSER")
    try:
        consulta = Parser(tokens).parsear()
        print(f"    Accion:     {consulta['accion']}")
        print(f"    Tema:       {consulta['tema']}")
        print(f"    Parametros: {consulta['parametros']}")
    except Exception as e:
        print(f"    ERROR: {e}")
        return
    # Construir prompt
    print("\n[4] PROMPT BUILDER")
    builder = PromptBuilder()
    prompt = builder.construir(consulta)
    lineas = prompt.strip().splitlines()
    for linea in lineas[:10]:
        print(f"    {linea}")
    if len(lineas) > 10:
        print(f"    ... ({len(lineas) - 10} líneas más)")
    # Generar respuesta IA
    print("\n[5] RESPUESTA DE LA IA")
    ia = Ia()
    respuesta = ia.generar(prompt)
    tipo = consulta["parametros"]["tipo"]
    if tipo == "audio":
        print(f"    Tipo: AUDIO")
        print(f"    Texto generado por IA: {respuesta[:200]}{'...' if len(respuesta) > 200 else ''}")
        try:
            voz = Voz()
            audio = voz.volver_audio(respuesta)
            bytes_leidos = len(audio.read())
            print(f"    Audio generado: {bytes_leidos} bytes")
            print("    Reproduciendo...")
            reproducir_audio(audio)
        except Exception as e:
            print(f"    Audio: ERROR al generar ({e})")
    else:
        print(f"    Tipo: TEXTO")
        print(f"    {respuesta[:600]}{'...' if len(respuesta) > 600 else respuesta[600:]}")
def demo_error(descripcion: str, entrada: str):
    print(f"\nCASO DE ERROR: {descripcion}")
    print(f"ENTRADA: {entrada}\n")
    norm = Normalizador()
    try:
        normalizado = norm.normalizar(entrada)
        tok = Tokenizador()
        tokens = tok.tokenizar(normalizado)
        Parser(tokens).parsear()
        print("    (no se produjo error)")
    except Exception as e:
        print(f"    ERROR capturado correctamente: {e}")
def demo_input():
    print("\nMODO TEXTO - Escribí tu consulta")
    print("Formato: <accion> <tema> tipo <texto|audio> [idioma <idioma>] [tono <tono>]")
    print("Ejemplo: explicar la fotosintesis tipo texto idioma español\n")
    entrada = input(">>> ").strip()
    if entrada == "":
        print("    No escribiste nada.")
        return
    demo_pipeline(entrada)
def demo_microfono():
    print("\nMODO MICRÓFONO - Hablá cuando estés listo")
    print("Formato al hablar: <accion> <tema> tipo <texto|audio> [idioma <idioma>]")
    print("Ejemplo: explicar la fotosintesis tipo texto idioma español\n")
    from thepibbles.Audio.stt import Audio
    listener = Audio()
    print("Escuchando...")
    texto = listener.escuchar()
    if texto is None:
        print("    No se entendió el audio, intentá de nuevo.")
        return
    print(f"    Escuché: {texto}")
    demo_pipeline(texto)
if __name__ == "__main__":
    print("\n        LIBRERÍA MONTOYA\n")
    # Casos hardcodeados
    demo_pipeline("explicar la fotosintesis tipo texto idioma español")
    demo_pipeline("resumir la revolucion francesa tipo audio idioma español tono formal")
    demo_pipeline("traducir hola mundo tipo texto idioma ingles")
    # Casos de error
    print("\n        CASOS DE ERROR ESPERADOS\n")
    demo_error("Sin parámetro tipo",  "explicar la fotosintesis idioma español")
    demo_error("Texto vacío",         "   ")
    demo_error("Tipo inválido",       "resumir algo tipo video")
    # Modo interactivo
    print("\n        MODO INTERACTIVO\n")
    print("¿Cómo querés ingresar tu consulta?")
    print("  1. Texto (teclado)")
    print("  2. Audio (micrófono)")
    print("  3. Salir")
    opcion = input("\nElegí una opción (1/2/3): ").strip()
    if opcion == "1":
        demo_input()
    elif opcion == "2":
        demo_microfono()
    elif opcion == "3":
        print("Saliendo...")
    else:
        print("Opción no válida.")