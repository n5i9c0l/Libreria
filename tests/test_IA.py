print("TEST: PromptBuilder")
from Libreria.IA.promptBuilder import PromptBuilder
builder = PromptBuilder()
consulta = {
    "accion": "explicar",
    "tema": "la fotosíntesis",
    "parametros": {
        "tipo": "texto",
        "idioma": "español",
        "tono": "formal"
    }
}
prompt = builder.construir(consulta)
if "fotosíntesis" in prompt and "explicar" in prompt:
    print("Prompt construido correctamente")
    print("--- Prompt generado ---")
    print(prompt)
else:
    print("El prompt no tiene el contenido esperado")
consulta_minima = {
    "accion": "resumir",
    "tema": "la revolución francesa",
    "parametros": {
        "tipo": "audio"
    }
}
prompt_minimo = builder.construir(consulta_minima)
if "español" in prompt_minimo and "neutral" in prompt_minimo:
    print("Defaults aplicados correctamente")
else:
    print("Los defaults no se aplicaron bien")


print()
print("TEST: Gemini")
from Libreria.IA.gemini import Gemini
try:
    gemini = Gemini()
    respuesta = gemini.generar("Decí solo 'hola' y nada más")
    if respuesta and len(respuesta) > 0:
        print("Gemini respondió:", respuesta.strip())
    else:
        print("Gemini no devolvió respuesta")
except Exception as e:
    print("Error en Gemini:", e)


print()
print("TEST: OpenRouter")
from Libreria.IA.openRouter import OpenRouter
try:
    openrouter = OpenRouter()
    respuesta = openrouter.generar("Decí solo 'hola' y nada más")
    if respuesta and len(respuesta) > 0:
        print("OpenRouter respondió:", respuesta.strip())
    else:
        print("OpenRouter no devolvió respuesta")
except Exception as e:
    print("Error en OpenRouter:", e)

print()
print("TEST: IA (orquestador)")
from Libreria.IA.ia import Ia
try:
    ia = Ia()
    respuesta = ia.generar("Decí solo 'hola' y nada más")

    if respuesta and len(respuesta) > 0:
        print("IA respondió:", respuesta.strip())
    else:
        print("IA no devolvió respuesta")
except Exception as e:
    print("Error en IA:", e)
#Todo esta super top