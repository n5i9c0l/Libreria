from thepibbles.Audio.normalizador import Normalizador
from thepibbles.Gramatica.lexer import Tokenizador
from thepibbles.Gramatica.parser import Parser
from thepibbles.IA.promptBuilder import PromptBuilder
from thepibbles.IA.ia import Ia
from thepibbles.Audio.tts import Voz
from thepibbles.libreria import Libreria


def texto_corto(texto, limite=300):
    texto = str(texto).strip().replace("\n", " ")
    return texto[:limite] + "..." if len(texto) > limite else texto


def reproducir_audio(audio):
    try:
        import tempfile
        import subprocess

        audio.seek(0)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            f.write(audio.read())
            ruta = f.name

        subprocess.Popen(["start", ruta], shell=True)
        print("Audio generado y abierto con el reproductor de Windows.")

    except Exception as e:
        print(f"Error al reproducir audio: {e}")


def demo_pipeline(entrada):
    print("\n" + "=" * 60)
    print(f"ENTRADA: {entrada}")
    print("=" * 60)

    try:
        normalizador = Normalizador()
        consulta_normalizada = normalizador.normalizar(entrada)

        print("\n[1] Normalizador")
        print(texto_corto(consulta_normalizada, 180))

        tokenizador = Tokenizador()
        tokens = tokenizador.tokenizar(consulta_normalizada)

        print("\n[2] Tokenizador")
        print(f"Tokens generados: {len(tokens)}")
        print(tokens[:8], "..." if len(tokens) > 8 else "")

        consulta_parseada = Parser(tokens).parsear()

        print("\n[3] Parser")
        print(consulta_parseada)

        prompt = PromptBuilder().construir(consulta_parseada)

        print("\n[4] PromptBuilder")
        print(texto_corto(prompt, 350))

        respuesta = Ia().generar(prompt)

        tipo = consulta_parseada["parametros"]["tipo"]

        print("\n[5] IA")
        print(f"Tipo: {tipo}")
        print(texto_corto(respuesta, 350))

        if tipo == "audio":
            audio = Voz().volver_audio(respuesta)
            print(f"Audio generado: {len(audio.getvalue())} bytes")
            reproducir_audio(audio)

    except Exception as e:
        print(f"\nERROR: {e}")


def demo_error(descripcion, entrada):
    print("\n" + "-" * 60)
    print(f"ERROR ESPERADO: {descripcion}")
    print(f"ENTRADA: {entrada}")

    try:
        consulta = Normalizador().normalizar(entrada)
        tokens = Tokenizador().tokenizar(consulta)
        Parser(tokens).parsear()

        print("No se produjo error.")

    except Exception as e:
        print(f"Error capturado correctamente: {e}")


def mostrar_resultado(resultado):
    if hasattr(resultado, "read"):
        print("Resultado: audio BytesIO")
        print(f"Tamaño: {len(resultado.getvalue())} bytes")
        reproducir_audio(resultado)

    else:
        print(texto_corto(resultado, 500))


def loop_libreria():
    lib = Libreria()

    print("\n" + "=" * 60)
    print("MODO INTERACTIVO")
    print("=" * 60)

    print("Opciones:")
    print("  1. Escribir consulta")
    print("  2. Escuchar consulta por micrófono")
    print("  3. Salir")
    print()

    while True:
        opcion = input("Elige una opción (1/2/3): ").strip()

        if opcion == "3":
            print("Saliendo...")
            break

        try:
            if opcion == "1":
                entrada = input("Consulta >>> ").strip()

                if entrada == "":
                    print("Consulta vacía.")
                    continue
                resultado = lib.procesarConsulta(entrada)
                mostrar_resultado(resultado)

            elif opcion == "2":
                print("Escuchando consulta...")
                resultado = lib.escucharConsulta()
                mostrar_resultado(resultado)

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"ERROR: {e}")

        print()


print("\nLIBRERÍA MONTOYA - DEMO\n")

print("PRUEBAS RÁPIDAS")

demo_pipeline(
    "explicar la fotosintesis tipo texto idioma español tono amigable longitud corta"
)

demo_pipeline(
    "resumir la revolucion francesa tipo audio idioma español tono formal longitud corta"
)

demo_pipeline(
    "traducir hola mundo tipo texto idioma ingles longitud corta"
)

print("\nCASOS DE ERROR ESPERADOS")

demo_error(
    "Sin parámetro tipo",
    "explicar la fotosintesis idioma español"
)

demo_error(
    "Texto vacío",
    "   "
)

demo_error(
    "Tipo inválido",
    "resumir algo tipo video"
)

loop_libreria()