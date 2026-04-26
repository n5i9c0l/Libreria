import speech_recognition as sr
import pyttsx3

class MiAudio:
    def __init__(self):
        self.reconocedor = sr.Recognizer()
        self.motor = pyttsx3.init()

    def escuchar(self):
        with sr.Microphone() as fuente:
            print("Empiece a realizar el dictado:")
            audio = self.reconocedor.listen(fuente)
        try:
            texto = self.reconocedor.recognize_google(audio, language="es-ES")
            print("Dijiste: " + texto)
            return texto
        except:
            print("No puedo entender el audio.")
            return None

    def hablar(self, texto):
        self.motor.say(texto)
        self.motor.runAndWait()