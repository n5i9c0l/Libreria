from IA.promptBuilder import PromptBuilder
from Gramatica.lexer import Tokenizador
from Gramatica.parser import Parser
from IA.ia import Ia
from Audio.tts import Voz
from Audio.stt import Audio
from Audio.normalizar import Normalizador

class Libreria:

    def __init__(self):
        self.tokenizador = Tokenizador()
        self.parser = Parser([])
        self.promptBuilder = PromptBuilder()
        self.ia = Ia()
        self.audio = Voz()
        self.listener = Audio()
        self.normalizador = Normalizador()
    
    def procesarConsulta(self, consulta):
        tokens = self.tokenizador.tokenizar(consulta)
        self.parser.tokens = tokens
        consultaParseada = self.parser.parsear()
        prompt = self.promptBuilder.construir(consultaParseada)
        respuesta = self.ia.generar(prompt)

        tipo = consultaParseada["parametros"]["tipo"]
        if tipo == "audio":
            return self.audio.volver_audio(respuesta)
        else:
            return respuesta

    def escucharConsulta(self):
        texto_hablado = self.listener.escuchar()

        if texto_hablado is None:
            self.listener.hablar("No pude entender el audio.")
        else:
            consulta = self.normalizador.normalizar(texto_hablado)
        return self.procesarConsulta(consulta)
