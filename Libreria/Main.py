from Libreria.IA.gemini import Ia
from Libreria.Audio.audio import Audio
audiouwu = Audio()
iaunu = Ia()
try:
    texto = audiouwu.escuchar()
    if texto:
        respuesta = iaunu.generar(texto)
        print("IA respondió: " + respuesta)
        audiouwu.hablar(respuesta)
except Exception as e:
    print("Ocurrió un error")
