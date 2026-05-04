print("TEST: Normalizador")
from Libreria.Audio.normalizador import Normalizador
norm = Normalizador()
resultado = norm.normalizar("traducir hola mundo tipo texto idioma ingles")
print("Normalización OK:", resultado)
try:
    norm.normalizar("traducir hola mundo")
    print("Debería haber lanzado excepción por falta de 'tipo'")
except Exception as e:
    print("Excepción esperada por falta de tipo:", e)
try:
    norm.normalizar("   ")
    print("Debería haber lanzado excepción por texto vacío")
except Exception as e:
    print("Excepción esperada por texto vacío:", e)


print()
print("TEST: Voz (TTS)")
from Libreria.Audio.tts import Voz
voz = Voz()
audio = voz.volver_audio("Hola, esto es una prueba")
if audio and audio.read(1):
    print("Audio generado correctamente")
else:
    print("Falló la generación de audio")


print()
print("TEST: Audio (STT) - Requiere micrófono")
from Libreria.Audio.stt import Audio
mic = Audio()
print("Habla algo en los próximos 5 segundos...")
texto = mic.escuchar()
if texto:
    print("Texto reconocido:", texto)
else:
    print("No se escuchó nada (puede ser normal si no hay micrófono)")
#Todo funciona al aperfección :D